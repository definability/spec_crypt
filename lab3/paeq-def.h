extern void Init();

extern void FPerm(const unsigned char* input, unsigned char* output);
extern int crypto_aead_encrypt(
	char *c, unsigned long long *clen,
	const char *m, unsigned long long mlen,
	const char *ad, unsigned long long adlen,
	const char *nsec,
	const char *npub,
	const char *k
	);
#ifdef EXTRANONCE 
extern int crypto_aead_encrypt_no_nonce(
	unsigned char *c, unsigned long long *clen,
	const unsigned char *m, unsigned long long mlen,
	const unsigned char *ad, unsigned long long adlen,
	const unsigned char *nsec,
	unsigned char *npub,
	const unsigned char *k
	);
#endif

extern
int crypto_aead_decrypt(
char *m, unsigned long long *mlen,
char *nsec,
const char *c, unsigned long long clen,
const char *ad, unsigned long long adlen,
const char *npub,
const char *k
);

extern  int key_bytes;
extern  int nonce_bytes;
extern  int tag_bytes;
