//#define EXTRANONCE

#include "paeq-def.h"

#include <stdio.h>
#include "stdint.h"
#include <cstring>
#include <stdlib.h>
#include "string.h"
//#include "wmmintrin.h"
#if defined(_MSC_VER)
#include "intrin.h"
#else
#include <x86intrin.h>
#endif
#include "emmintrin.h"
#include <openssl/sha.h>

int enc(char* filename, char* key);
int dec(char* filename, char* key);

int main(int argc, char* argv[])
{
    if (argc < 4) {
        printf("USAGE: %s FILENAME e[ncryption]|d[ecryption] KEY\n\n", argv[0]);
        return -1;
    }
    char key_hash[SHA512_DIGEST_LENGTH];
    SHA512((unsigned char*)argv[3], strlen(argv[3]), (unsigned char*)key_hash);
    if (*argv[2] == 'd') {
        if (dec(argv[1], key_hash)) {
            printf("Error: Wrong key!\n");
        }
    }
    else {
        enc(argv[1], key_hash);
    }
	return 0;
}

int enc(char* filename, char* k) {
    FILE * input = fopen(filename, "rb");

    fseek(input, 0L, SEEK_END);
    unsigned long long plaintext_length = ftell(input);
    fseek(input, 0L, SEEK_SET);
    char *plaintext = (char*)malloc((size_t)plaintext_length);
    //memset(plaintext, 0, plaintext_length);
    char s;
    int i=0;
    while (fscanf(input, "%c", &s) != EOF) {
        plaintext[i] = s;
        i++;
    }
    fclose(input);
    plaintext_length = strlen(plaintext);
    unsigned long long ciphertext_length;
    unsigned long long decrypted_length;
    char* plaintext_decrypted = (char*)malloc(plaintext_length+tag_bytes);
    char* ciphertext = (char*)malloc(plaintext_length+tag_bytes);
    char associated_data[] = "ad";
    unsigned long long ad_length = strlen(associated_data);
    char nonce[] = "nonce";
	crypto_aead_encrypt(ciphertext, &ciphertext_length, plaintext, plaintext_length, associated_data, ad_length, NULL, nonce, k);
    //printf("%s ->", plaintext);
    int filename_length = strlen(filename);
    char * enc_filename = (char*) malloc(filename_length+5);
    char * mac_filename = (char*) malloc(filename_length+5);
    strcpy(enc_filename, filename);
    strcpy(mac_filename, filename);
    strcat(enc_filename, ".enc");
    strcat(mac_filename, ".mac");
    FILE * enc_output = fopen(enc_filename, "w");
    FILE * mac_output = fopen(mac_filename, "w");
    FILE * tmp_output = fopen("tmp.txt", "w");
    for (i=0; i<plaintext_length; i++) {
        //printf(" %02X", ciphertext[i] & 0xFF);
        fprintf(enc_output, "%c", ciphertext[i] & 0xFF);
        fprintf(tmp_output, "%c", ciphertext[i] & 0xFF);
    }
    //printf(": ");
    for (; i<ciphertext_length; i++) {
        //printf("%02X ", ciphertext[i] & 0xFF);
        fprintf(mac_output, "%c", ciphertext[i] & 0xFF);
        fprintf(tmp_output, "%c", ciphertext[i] & 0xFF);
    }
    fclose(enc_output);
    fclose(mac_output);
    free(enc_filename);
    free(mac_filename);
    free(plaintext_decrypted);
    free(ciphertext);
    free(plaintext);
    return 0;
}

int dec(char* filename, char* key) {
    char* plaintext_decrypted = (char*)malloc(2048+tag_bytes);
    unsigned long long decrypted_length;
    char associated_data[] = "ad";
    unsigned long long ad_length = strlen(associated_data);
    char nonce[] = "nonce";
    int filename_length = strlen(filename);
    char * enc_filename = (char*) malloc(filename_length+5);
    char * mac_filename = (char*) malloc(filename_length+5);
    strcpy(enc_filename, filename);
    strcpy(mac_filename, filename);
    strcat(enc_filename, ".enc");
    strcat(mac_filename, ".mac");
    FILE * enc_output = fopen(enc_filename, "rb");
    FILE * mac_output = fopen(mac_filename, "rb");

    fseek(enc_output, 0L, SEEK_END);
    unsigned long long ciphertext_length = ftell(enc_output);
    char* ciphertext = (char*)malloc(ciphertext_length);
    fseek(enc_output, 0L, SEEK_SET);

    int i=0;
    char s;
    while (fscanf(enc_output, "%c", &s) != EOF) {
        ciphertext[i] = s&0xFF;
        //printf(" %02X", s&0xFF);
        i++;
    }
    //printf(": ");
    while (fscanf(mac_output, "%c", &s) != EOF) {
        ciphertext[i] = s&0xFF;
        //printf("%02X ", s&0xFF);
        i++;
    }
    //printf("\n");
    ciphertext[i] = 0;
    fclose(enc_output);
    fclose(mac_output);
    ciphertext_length = (unsigned long long)i;

    char * k = (char*) malloc(strlen(key));
    strcpy(k, key);
	int result = crypto_aead_decrypt(plaintext_decrypted, &decrypted_length, NULL, ciphertext, ciphertext_length, associated_data, ad_length, nonce, k);
    free(enc_filename);
    free(mac_filename);
    free(ciphertext);
    if (result) {
        free(plaintext_decrypted);
        return result;
    }
    printf("Your text: `%s'\n", plaintext_decrypted);
    free(plaintext_decrypted);
    return 0;
}
