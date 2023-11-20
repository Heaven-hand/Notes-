# OpenSSL Handbook 

#### written by: SONG CHANGLIN

### 一、安装OpenSSL

```
git clone https://github.com/openssl/openssl.git
```

##### 1.完成初始的默认参数设置（如果失败或自行设置参数请参考OpenSSL文档）

```
$./Configure          #在OpenSSL的对应目录下
```

##### 2.开始编译源码，并完成测试检验

```
$make
$make test
$sudo make install
```

### 二、OpenSSL使用

##### 1.使用帮助命令查看其基础的命令

```
$openssl help
```

##### 标准命令：

```
Standard commands
asn1parse         ca                ciphers           cmp               
cms               crl               crl2pkcs7         dgst              
dhparam           dsa               dsaparam          ec                
ecparam           enc               engine            errstr            
fipsinstall       gendsa            genpkey           genrsa            
help              info              kdf               list              
mac               nseq              ocsp              passwd            
pkcs12            pkcs7             pkcs8             pkey              
pkeyparam         pkeyutl           prime             rand              
rehash            req               rsa               rsautl            
s_client          s_server          s_time            sess_id           
smime             speed             spkac             srp               
storeutl          ts                verify            version           
x509              
```

##### 信息哈希获得digest的命令（hash）

```
Message Digest commands (see the `dgst' command for more details)
blake2b512        blake2s256        md4               md5               
rmd160            sha1              sha224            sha256            
sha3-224          sha3-256          sha3-384          sha3-512          
sha384            sha512            sha512-224        sha512-256        
shake128          shake256          sm3               
```

##### 加密算法命令

```
Cipher commands (see the `enc' command for more details)
aes-128-cbc       aes-128-ecb       aes-192-cbc       aes-192-ecb       
aes-256-cbc       aes-256-ecb       aria-128-cbc      aria-128-cfb      
aria-128-cfb1     aria-128-cfb8     aria-128-ctr      aria-128-ecb      
aria-128-ofb      aria-192-cbc      aria-192-cfb      aria-192-cfb1     
aria-192-cfb8     aria-192-ctr      aria-192-ecb      aria-192-ofb      
aria-256-cbc      aria-256-cfb      aria-256-cfb1     aria-256-cfb8     
aria-256-ctr      aria-256-ecb      aria-256-ofb      base64            
bf                bf-cbc            bf-cfb            bf-ecb            
bf-ofb            camellia-128-cbc  camellia-128-ecb  camellia-192-cbc  
camellia-192-ecb  camellia-256-cbc  camellia-256-ecb  cast              
cast-cbc          cast5-cbc         cast5-cfb         cast5-ecb         
cast5-ofb         des               des-cbc           des-cfb           
des-ecb           des-ede           des-ede-cbc       des-ede-cfb       
des-ede-ofb       des-ede3          des-ede3-cbc      des-ede3-cfb      
des-ede3-ofb      des-ofb           des3              desx              
rc2               rc2-40-cbc        rc2-64-cbc        rc2-cbc           
rc2-cfb           rc2-ecb           rc2-ofb           rc4               
rc4-40            seed              seed-cbc          seed-cfb          
seed-ecb          seed-ofb          sm4-cbc           sm4-cfb           
sm4-ctr           sm4-ecb           sm4-ofb
```

```
$man <具体命令>         #可以打开对应的详细文档进行查阅（press q to quit or press h for more）
```

##### 2.进行基础的密码学操作

##### 1）Hash the file using SHA-512

```
$openssl dgst -sha512 <filename>
$openssl dgst -sha512 -hex plaintext_file.jpg > plaintext_file.hex  #保存为16进制的文件
```

##### 2）Generate RSA-4096 key pairs

```
$openssl genrsa -out RSA_private_key.pem 4096 #生成私钥
$openssl rsa -pubout -in RSA_private_key.pem -out RSA_public_key.pem #利用私钥生成公钥
$openssl pkey -in RSA_private_key.pem -pubout -out RSA_public_key.pem #利用私钥生成公钥
```

```
$cat RSA_private_key.pem   #查看私钥具体内容
-----BEGIN PRIVATE KEY-----
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
WI1ZTRUauTJObKqoMRmx6tLTKSg=
-----END PRIVATE KEY-----

```

```
#查看秘钥的详细信息
$openssl pkey -in RSA_private_key.pem -text -noout #公钥不能被读取（在OpenSSL中默认的e为65,537） 
Private-Key: (4096 bit, 2 primes)
modulus:
    00:8d:c2:2d:bd:15:bf:98:89:97:90:44:76:08:0b:
    b7:4d:37:97:d9:75:b3:fb:bd:08:77:17:66:7f:54:
    87:13:16:dd:b4:49:ba:1d:5b:03:e0:dd:75:73:28:
    b0:54:6d:87:bb:7f:1f:c5:fc:fa:93:23:e1:c9:71:
    b3:4b:57:f8:d0:f4:00:f2:1c:4c:2b:4a:50:c0:db:
    0b:e0:a7:33:9e:98:cd:86:f4:60:fc:c2:cb:bb:fb:
    aa:7e:d4:ff:8c:91:85:8c:a6:b7:46:b1:90:e2:a3:
    c6:a7:b0:70:ca:91:e6:1d:77:9b:cb:8c:b8:d9:79:
    cc:c6:b4:87:79:6e:6d:32:b7:cd:10:d3:5a:70:91:
    aa:96:4b:79:83:cf:45:1a:5b:e1:d9:38:c9:86:c9:
    43:65:cd:9d:c8:12:66:e6:d9:02:14:14:7a:dd:e2:
    87:76:16:6b:44:55:32:bc:5c:4b:7a:c5:7a:0c:5e:
    3d:7a:dc:cf:4a:26:b8:a0:fc:c8:e1:be:f3:e1:86:
    20:8e:a7:72:f3:1b:97:ae:33:fe:55:ff:e3:f5:1d:
    92:9a:d4:fe:07:5d:0e:cd:b8:fe:26:f0:1f:5a:ae:
    a4:00:9b:ed:b8:9f:a9:ea:8c:11:39:a5:ba:65:b8:
    f4:18:fa:d5:23:65:54:3f:ff:cc:d8:e7:9e:08:9b:
    84:7c:59:cd:25:8e:d5:ab:20:bf:42:9b:63:fa:f8:
    97:59:eb:90:db:43:a4:db:0c:cc:62:34:ec:c5:1d:
    bd:fc:f3:4b:bc:6a:1e:61:f9:de:6f:ee:9b:a9:a9:
    49:ed:a8:ec:0c:a0:d0:82:ae:41:2c:cb:a0:20:18:
    ee:4b:63:1f:bb:0b:7a:82:97:2e:45:6c:a4:ba:f0:
    fc:58:9c:69:63:18:5c:c8:22:b2:4d:3e:e0:d0:1e:
    3f:a3:95:24:31:53:37:e1:9a:34:24:2b:0f:bc:38:
    f8:23:71:f6:32:ed:76:ca:21:41:12:69:cb:c0:34:
    6d:c9:97:85:36:d3:57:7d:d5:dd:1c:ed:f5:0d:e3:
    20:d5:84:42:26:52:35:e1:ef:54:74:40:09:97:92:
    b4:3e:c3:31:62:ff:52:51:0d:9e:c4:c7:45:fa:08:
    34:b9:44:f6:18:0c:04:8e:c4:3f:57:7f:80:d3:bc:
    ca:25:51:44:2f:c5:06:40:29:d9:64:4e:4d:59:4d:
    1a:42:20:26:b2:9d:44:d6:e7:91:39:1c:4a:d4:54:
    08:9b:9a:37:68:42:f9:db:ae:57:95:93:e7:80:35:
    fb:8e:ff:06:25:d2:45:80:e0:ec:20:49:12:c1:79:
    cd:35:39:14:77:d4:a6:7b:ff:b4:77:6e:69:82:95:
    1e:2c:19
publicExponent: 65537 (0x10001)
privateExponent:
    3a:1f:b0:f6:ab:fc:b8:86:18:74:5b:9d:c5:7b:90:
    d7:a9:73:c4:58:64:f3:db:b8:fa:b5:3f:af:6d:34:
    e4:0d:c8:ea:d6:83:3d:97:2d:90:fd:3c:cd:36:c8:
    27:09:28:62:7c:c5:d7:2c:96:5e:35:e9:44:96:0d:
    5c:ce:ac:c7:cd:22:51:de:f3:18:00:24:e9:10:a3:
    3d:0a:eb:27:f1:90:53:f0:12:e5:6e:71:1a:de:95:
    ab:e2:ee:18:68:1b:0d:54:e7:e2:0c:0e:97:cd:f5:
    9d:aa:07:84:3a:c5:c1:c6:c9:23:0a:a9:af:4e:d2:
    b0:62:77:4b:f5:14:c0:03:bf:19:da:39:dd:10:43:
    72:c2:e5:f6:83:85:eb:95:af:eb:47:88:26:d5:81:
    3b:ef:e8:41:e4:e3:4c:5d:9d:2f:c0:ad:6d:08:d2:
    d7:6d:c0:38:5e:0b:ef:84:f9:6d:dd:79:8b:65:7f:
    14:1d:20:36:b6:21:30:f2:30:c1:09:b5:4a:fe:ef:
    9e:c1:81:46:c6:89:84:75:11:64:cb:4b:70:e8:b7:
    c4:f7:a1:30:ec:43:d8:d1:e7:a7:dc:55:87:59:14:
    18:e7:92:22:4b:dd:9b:67:9f:ca:94:54:03:d8:eb:
    b4:a7:ac:ef:f0:0b:2c:76:e0:b1:ec:f0:d6:c9:dc:
    4c:61:e6:fd:32:58:95:65:99:be:23:4b:fa:51:f2:
    5c:9c:b2:67:eb:28:2c:ae:65:6e:9a:ce:67:7b:1c:
    c2:e2:66:de:f5:7d:53:9a:40:77:45:be:3c:dc:6b:
    d3:68:96:0e:0a:d5:66:68:8b:1c:ea:0d:dc:8d:d6:
    70:16:14:a6:e0:f5:25:20:d1:e7:90:cd:6e:47:78:
    64:60:2f:58:3a:bd:10:e1:59:44:73:a7:6b:40:bb:
    db:5f:a3:f6:f6:f0:01:4a:a7:34:5a:24:4e:3f:b7:
    7c:ec:4d:a3:7b:ee:d8:a1:4d:04:f2:43:59:1b:a7:
    b7:a3:3b:f4:da:2c:5d:f9:5c:db:89:3e:c5:63:a7:
    f6:fd:9b:06:b0:49:24:ea:54:97:78:93:e6:66:87:
    ae:c5:77:91:13:8d:40:2c:da:40:6a:09:24:6b:fd:
    c5:30:c8:09:05:a7:0a:00:5a:9c:eb:15:71:a1:82:
    4e:ee:db:84:f6:be:3c:35:0e:01:60:67:ab:3b:13:
    f4:5f:2f:97:59:fa:d3:c4:4f:2b:e3:fd:de:d0:dd:
    9d:5b:57:a9:d6:cb:e6:a6:3b:f1:da:bc:b6:7c:78:
    d5:cb:de:7c:af:65:ff:64:a9:fb:9f:06:11:57:12:
    47:c3:49:d3:d3:c2:ec:85:26:f5:7c:05:fe:26:a1:
    d7
prime1:
    00:b6:c6:f5:29:1f:90:c9:e2:ca:d4:e7:fd:2c:5e:
    33:7e:e7:f1:16:0a:86:d5:1f:ef:76:e9:60:7a:81:
    eb:74:28:c9:e9:54:81:22:23:26:83:80:70:62:db:
    21:46:c6:90:d6:bf:69:20:e4:1a:38:bd:f3:db:78:
    1f:ce:04:62:66:11:c6:5d:5b:00:bb:84:d6:96:39:
    6e:06:3c:7e:27:70:8e:58:88:50:0a:69:e3:ea:ff:
    aa:a4:dc:54:34:ab:1a:5f:f0:8e:30:48:69:fe:9b:
    56:f9:a3:fe:57:41:1d:c4:65:27:95:8a:7f:56:21:
    4c:3b:72:0d:53:6a:d5:29:ed:6d:ee:b0:b6:34:c2:
    7a:dc:34:e5:8a:ca:d7:49:14:9e:7a:27:bc:73:c8:
    bc:48:0a:c3:75:d6:0d:2b:50:26:cb:6d:11:46:8b:
    21:f0:c6:ca:d3:1f:eb:ca:7f:8d:59:af:2d:ab:ba:
    e2:a1:c6:39:80:8c:7b:6e:77:2d:80:f9:fd:f7:a0:
    e1:74:89:37:68:00:52:42:74:bd:fb:de:e3:6f:51:
    20:9a:71:22:0d:d4:30:f5:93:1b:36:7f:1b:f5:04:
    4a:ce:ae:72:cc:94:ee:20:8b:b5:00:88:85:78:02:
    d7:3f:0a:1b:5a:22:91:e7:c1:d0:33:1d:c1:7d:b7:
    c3:b3
prime2:
    00:c6:8c:7a:4c:2e:24:b8:c7:a4:11:aa:f1:27:dd:
    69:59:93:2a:33:8b:f4:d8:8c:39:05:22:81:ef:73:
    15:7c:f3:41:21:5c:d0:9a:53:24:88:44:fc:21:76:
    4f:47:35:58:1c:c5:cc:4c:df:17:f6:10:29:f1:9d:
    5f:e0:e9:18:08:a5:e4:95:49:79:3e:7b:08:7e:9c:
    35:59:04:08:c1:e4:c1:fe:ce:d2:5c:68:ee:0d:a4:
    d6:20:40:5f:57:b2:01:1e:ce:87:93:d3:9e:57:e6:
    42:d2:17:c4:1a:b5:a3:d5:df:f1:61:58:84:7e:d9:
    8e:9c:a9:15:f0:c5:82:2f:3c:c1:89:0e:6d:0f:20:
    1c:c1:f9:dd:1f:eb:92:3f:78:e3:2e:e8:d6:36:fd:
    d7:98:22:23:f1:6a:e2:19:d2:fb:79:3c:70:9f:ae:
    29:b4:8e:84:69:dc:ed:4f:9d:49:09:5f:9a:14:96:
    c4:16:40:74:b6:23:1c:15:52:3f:d4:b2:c4:af:ec:
    5d:8a:82:a9:9e:35:b1:68:0c:f1:01:74:e5:bc:cb:
    3d:f8:f8:0f:22:62:60:df:f2:96:46:ee:da:66:8f:
    b9:93:59:b0:db:88:5f:b7:da:56:ea:0e:ef:98:94:
    6b:10:25:dc:e3:40:50:7d:61:c1:13:57:6f:5e:e1:
    1b:03
exponent1:
    01:15:bb:3c:cc:40:2a:c2:9a:db:9a:a8:e9:0b:82:
    18:bd:bd:b3:98:ca:66:17:73:6f:6c:41:33:58:f4:
    11:d3:70:27:5f:66:08:d2:d6:96:af:3b:7b:8a:bb:
    6e:d5:1c:e4:f9:6b:e1:53:19:48:be:ef:e4:9c:98:
    eb:bb:20:ee:64:2a:9e:41:3d:06:df:e9:fa:28:4b:
    1b:e4:5e:07:53:e6:b4:65:d2:bb:cd:17:1a:3c:fc:
    41:50:41:7b:b2:8c:4c:87:7c:00:93:5d:75:b2:6c:
    58:bc:fd:74:7d:21:75:19:f8:9b:2d:a0:45:dd:9a:
    bb:3b:99:12:a6:ae:af:3a:06:8e:05:24:7f:b9:ab:
    cb:04:d1:5b:fa:8a:3e:97:cd:bd:01:e1:5f:7a:90:
    8b:88:ec:d2:15:3c:2c:c6:a4:04:4f:18:6c:27:c5:
    42:cd:9b:44:97:8a:e9:bf:ca:11:ff:35:31:30:c1:
    c9:9e:08:97:57:be:1f:d0:bb:47:69:b4:75:34:d2:
    41:c3:d2:bd:5e:4b:1e:b3:dc:b0:d3:08:dc:8f:49:
    b7:40:f6:a7:c8:5b:a6:09:82:7e:d7:50:4e:2b:01:
    5a:aa:b4:69:bc:74:91:62:e2:e7:26:e8:4b:e7:10:
    6a:02:60:59:2f:9d:58:17:d1:69:8c:42:aa:c1:5d:
    7b
exponent2:
    4a:20:a0:78:58:b1:f5:1a:f4:32:74:73:dc:c2:59:
    56:cc:0e:f1:77:cb:4e:1d:ec:1b:f2:aa:38:4f:eb:
    31:df:4f:ed:b8:cd:59:10:b9:8e:f6:d2:7b:5b:c4:
    75:7d:81:0c:1c:fd:0d:a6:2d:37:fd:08:eb:e0:29:
    af:ba:d6:f2:43:9d:77:ef:1a:89:2d:3e:1a:a7:0f:
    73:d0:81:c4:82:37:bb:7e:54:23:94:39:6c:76:a2:
    4b:20:3d:78:6c:48:e6:cb:8c:ea:b0:13:6a:15:d9:
    d4:be:72:c4:d6:13:f9:01:c7:08:e5:17:72:94:9f:
    1d:f6:32:ee:d5:8e:a9:3c:31:b5:8d:e1:41:c8:67:
    74:34:69:4e:45:91:30:89:5d:a8:61:dd:b8:62:45:
    5f:d3:3f:40:1e:fb:93:50:a5:fa:b9:8a:02:d3:ef:
    56:2d:ef:59:e6:d5:e2:e7:82:21:31:c4:40:f3:98:
    fa:05:ce:8d:41:c6:76:5f:62:dd:72:70:e4:8d:86:
    ce:f3:c1:88:03:db:dc:51:18:99:c6:9f:0f:41:82:
    3d:b5:bf:50:c3:12:10:0a:6d:f8:c5:ac:5c:a6:44:
    4e:b3:29:c8:8c:bd:cf:d2:80:a8:9a:32:f1:f0:57:
    98:8b:ca:50:3d:ee:cf:20:f4:08:d8:98:08:00:5b:
    29
coefficient:
    50:dc:73:37:4c:6b:e3:cc:d1:ae:94:b0:58:20:fc:
    33:9d:e6:a2:36:8a:4e:b9:51:14:a1:3b:31:2f:0f:
    c0:2e:db:29:63:5e:42:70:34:85:5c:2b:58:68:35:
    e7:05:c9:09:d4:c3:be:ec:ca:0b:dc:38:b0:3e:c3:
    8b:5b:d2:38:80:84:f0:fd:d2:64:dd:59:70:4c:f0:
    0a:d2:a8:d1:5a:b7:b3:b4:a8:a7:bd:b5:c4:b3:93:
    20:f8:b3:b1:02:5a:3d:4b:a8:4d:8e:a0:17:9a:b7:
    ad:2d:7c:e1:b8:c0:dd:c7:5d:83:93:ff:be:76:d6:
    fc:02:f4:ba:3e:8c:32:2b:f0:50:77:54:85:e9:79:
    44:d7:4c:25:52:20:18:72:92:7b:3f:70:77:d3:20:
    54:52:14:1e:ac:78:bf:b5:aa:ff:56:51:cd:d6:0b:
    ac:8f:08:3b:11:86:03:ba:24:c1:42:9d:49:55:f3:
    e1:ce:86:f1:b2:87:7e:b8:ff:e0:8f:31:a5:8d:69:
    2d:1a:a6:09:57:a3:8f:25:1f:f8:99:30:f4:3b:a9:
    4d:57:96:39:9e:b2:05:e6:61:54:f4:82:03:5c:9f:
    b3:4c:8a:f2:cf:15:e1:fd:cc:98:3c:58:8d:59:4d:
    15:1a:b9:32:4e:6c:aa:a8:31:19:b1:ea:d2:d3:29:
    28
```

##### 3）对文件进行签名

数字签名分为摘要和加密两部分，但是在openssl提供的指令中，并没有区分两者。需要注意的是，签名是指对明文的摘要进行加密，得到的密文就称为签名，而非对明文数据进行加密。

**签名：**

```
$openssl dgst -sha256 -sign RSA_private_key.pem -out signed_file.hex plaintext_file.jpg
```

**验签：**

```
$openssl dgst -verify RSA_public_key.pem -sha256 -signature signed_file.hex plaintext_file.jpg
```

![image-20231018115849445](C:\Users\scl\AppData\Roaming\Typora\typora-user-images\image-20231018115849445.png)

##### 4）生成AES-256密钥

```
$openssl rand -out AES_key.txt -base64 32   #32字节对应256bits
$hexdump -C AES_key.txt  #查看二进制内容
```

##### 5）利用密钥加解密文件

公钥加密，私钥解密

**加密：**

```
$openssl pkeyutl -encrypt -in AES_key.txt -inkey RSA_public_key.pem -pubin -out encrypted_AES_key.txt
```

**解密：**

```
$openssl pkeyutl -decrypt -in encrypted_AES_key.txt -inkey RSA_private_key.pem -out decrypted_AES_key.txt
```

##### 6）利用AES key加密文件（利用不同的模式mode）

##### Galois Counter Mode (GCM)

```
$openssl rand -out IV.hex -hex 16   #生成随机的IV向量（16进制）128bits
```

```
$openssl enc -aes-256-gcm -in plaintext_file.jpg -out ciphertext_file.enc -K AES_key.txt -iv IV.txt
```

```
$openssl enc -aes-256-gcm -nosalt -p -in plaintext_file.jpg -out ciphertext_file.enc
```

```
#失败
enc: AEAD ciphers not supported
```



##### CBC（Cipher Block Chaining）

```
$openssl enc -aes-256-cbc -in plaintext_file.jpg -out ciphertext_file.enc -K AES_key.txt -iv IV.txt
```

```
$openssl rand -out IV.hex -hex 16   #生成随机的IV向量（16进制）128bits
```

```
$openssl enc -e -aes-256-cbc -in plaintext_file.jpg -out ciphertext_file.en -K 9d92831fa647675b000b47989224b5e3ef9d358509a14abc81a32009cb94d543 -iv 667b02a85c61c786def4521b060265e8
```

```
$openssl enc -d -aes-256-cbc -in ciphertext_file.en -out decrypted_file.de -K 9d92831fa647675b000b47989224b5e3ef9d358509a14abc81a32009cb94d543 -iv 667b02a85c61c786def4521b060265e8
```

##### 7）解密文件并检查hash

```
$openssl dgst -sha512 -hex decrypted_file.de > digest_decrypted_file.hex
```



##### 过程中出现的问题&解决办法

##### Q1

对应的库损坏，可以从官网下载源码将库文件进行替换

https://blog.csdn.net/qq_41765969/article/details/127565952



