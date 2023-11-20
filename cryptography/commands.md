## COMMANDS & DETAILS

##### SONG CHANGLIN (G2204828F)

1. Choose a picture as the plaintext. Name this file as ***plaintext_file.jpg***

   the size of it is ***1.05MB***

2. Hash the file using SHA-512, name the output digest as ***digest_file.hex***.

   ```
   $openssl dgst -sha512 -hex plaintext_file.jpg > digest_file.hex
   ```

3. Generate an RSA-4096 key pair, name the output as ***RSA_public_key.pem*** & ***RSA_private_key.pem***

   ```
   $openssl genrsa -out RSA_private_key.pem 4096
   $openssl pkey -in RSA_private_key.pem -pubout -out RSA_public_key.pem
   ```

4. Sign plaintext_file using RSA private key and output the result as ***signed_file***.

   ```
   $openssl dgst -sha256 -sign RSA_private_key.pem -out signed_file plaintext_file.jpg
   $openssl dgst -verify RSA_public_key.pem -sha256 -signature signed_file plaintext_file.jpg #verify
   ```

5. Generate an AES-256 key, name the output as ***AES_key.txt***.

   ```
   $openssl rand -out AES_key.txt -base64 32
   $openssl rand -out AES_key.txt -hex 32
   ```

   turn the hex into binary string using auto-tools

6. Encrypt the AES key by using the RSA public key and output as ***encrypted_AES_key.txt***.
   Decrypt encrypted_AES_key.txt by using the RSA private key and output as a binary string into a
   file named ***decrypted_AES_key.txt***.
   Ensure that the content is identical with AES_key.txt.

   ```
   $openssl pkeyutl -encrypt -in AES_key.txt -inkey RSA_public_key.pem -pubin -out encrypted_AES_key.txt # encryption
   $openssl pkeyutl -decrypt -in encrypted_AES_key.txt -inkey RSA_private_key.pem -out decrypted_AES_key.txt # decryption
   ```

7. Encrypt plaintext_file by using the AES key in ***CBC mode***.
   Output the encrypted file as ***ciphertext_file*** 

   generate IV and name as ***IV.hex*** (IV used must be hex)

   the IV is **6595c271fb4ac045d3f15a91fa594f4b**

   the AES key is **68f017b74db58bb6639419eaa72aa7afaaf11572c2e15f9de58f5a60ee083ae3**

   ```
   $openssl rand -out IV.hex -hex 16 # generate IV
   $openssl enc -e -aes-256-cbc -in plaintext_file.jpg -out ciphertext_file -K 68f017b74db58bb6639419eaa72aa7afaaf11572c2e15f9de58f5a60ee083ae3 -iv 6595c271fb4ac045d3f15a91fa594f4b
   $openssl enc -d -aes-256-cbc -in ciphertext_file -out decrypted_file -K 68f017b74db58bb6639419eaa72aa7afaaf11572c2e15f9de58f5a60ee083ae3 -iv 6595c271fb4ac045d3f15a91fa594f4b
   ```

8. Decrypt ciphertext_file and save the output as ***decrypted_file***.
   Output the SHA-512 digest of decrypted_file, in hexadecimal, as ***digest_decrypted_file.hex***.

   ```
   $openssl dgst -sha512 -hex decrypted_file > digest_decrypted_file.hex
   ```

   both digests are the same : 5b581e3397a85a01f0b2afe346e067dcc2afe971b889e2e2fc5755e9ef8d86e7356de554b6ad399aee26599d93ac3c7ce89c617200739c7a7df3aa01111bf519