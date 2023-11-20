## Key Agreement

- [x] Find a generator of of $Z_{11}$*
- [x] What Discrete Logarithm Problem 

- [x] Public key based key agreement 

  For secret key cryptography the main problems are key management and key distribution.–Keys need to be distributed via secure channels.

  In public key (PK) systems, we have the problem of **key authentication**. Which key (really) belongs to who?

  Keys need to be distributed via **authentic channels.**

  ​	Two users use a supplementary secure channel

  ​	Key exchange via a trusted authority

  ​	Key exchange using public channels

  To use a public key algorithm, Alice must have Bob's public key.

  Authentication

  Integrity

  Validity is an important consideration. Keys are usually valid for certain period of time, their lifetime. Key updates : send in real time, periodic checks

  tp will not know the secret component 

- [x] Describe Diffie-Hellman Key Exchange protocol

  Certificates?



## Secret Sharing Scheme

- [x] $(t, n)$ secret sharing scheme 

  Threshold secret sharing

  t-out-of-n secret sharing scheme

  Shamir’s Secret Sharing Scheme

  it takes t points to define a polynomial of degree t-1

  **Perfect Security**

  **Ideal**: Each share is exactly the same size as the secret. 

  **Extendable**–More shares can be created New users joining the system 

  **Flexible**–can support different levels of trust • Given more share to more trusted people

  Homomorphic property

- [x] $(t, t)$ secret sharing scheme 

  The simplest threshold secret sharing 

  The secret can be reconstructed only when all the shares are combined together 

  **Unconditionally secure** 

  With less than n shares, no information of S can be recovered

- [x] Shamir secret sharing scheme

- [x] Lagrange interpolation 

- [x] Construct a $(t, t)$ secret sharing scheme to share secrets from $Z_m$, where $m$ is not necessarily a prime. 

- [x] General access structure 

- [ ] Cumulative arrays 

- [ ] Secret sharing for general access structures using cumulative arrays. 



## Digital Signature

- [x] Basic concept of digital signature, Public key based signatures 

  A digital signature is generally represented as a string of bits attached to a message.

  Easy to generate. –Easy to verify by a receiver. –Hard to forge.

- [ ] Describe the following digital signature schemes: RSA, ElGamal and DSA (three algorithms: key generations, signing, verification) 

- [x] Show that in the ElGamal Signature Scheme, if the random per-message value $k$ is known then one can forge signature at will. Also the same $k$ should not be used in signing two different messages. 

- [x] Explain: Blind signatures, Undeniable signatures, Fail-stop signature schemes, Threshold signature schemes

  **Blind signature** The requester wants to obtain the signer’s signature of message m.–The requester doesn’t want to reveal m to anyone, including the signer.

  **undeniable signature** These are non-transferable signatures. That is, the signature can be verified only with the collaboration of the signer.

  **Fail-stop signature schemes** (with high probability) subsequently be able to prove that Oscar's signature is a forgery. A Fail-Stop Signature Scheme provides enhanced security against the possibility that a very powerful adversary might be able to forge a signature.

  **Threshold signature schemes** same like t-out-of n secret sharing



## Public-key cryptography

- [x] The concept of PKC (how does it work?) 

  The encryption and decryption keys are different.

  The decryption key cannot be deduced from the encryption key.

  A PK cryptosystem can provide confidentiality

- [x] The Merkle-Hellman cryptosystem (security based on the difficulty of the subset sum problem) 

- [x] The RSA cryptosystem (security based on the difficulty of factoring large integers) 

- [x] The ElGamal cryptosystem (Security based on Discrete Logarithm Problem)

- [ ] Draw a diagram of public-key cryptosystem, name its main components, and specify its security requirements. 

- [ ] Define encryption, decryption and key generation function used in the RSA/ElGamal/Merkle-Hellman cryptosystems.

- [x] Show that in RSA if one knows $\phi(N)$ can factor $N$ easily. 

- [x] Discuss the security issues for multiplicative properties in RSA. 

  the plaintext and ciphertext are the same not all the messages are concealed

  A prime is safe if p=2q+1, where q is a prime itself

  It is important to note that the security of RSA is not provably equivalent to the difficulty of factoring. That is, **it might be possible to break RSA without factoring n.**

- [x] Discuss various attacks on RSA.

  **Common modulus attack**

  **Low exponent attack** encryption exponent is small，not dependent

  **Low decryption exponent**  If the decryption exponent is **less that N/4 and e<N** then d can be found.

