# JWT attacks
- [What Are jwt](#intro)
- [Attacks](#attacks)
	+ [simple scenario](#simple)
		+ [decode vs verify](#decodeVuln)
	+ [jwt header attacks](#)
## What Are jwt <a name="intro"></a>

jwt stands for json web token, they are a different way to store session tipically. unlike session data are stored in the jwt.

### jwt parts

jwt consists of 3 parts separated by dot: header, payload, sign. like this:

**eyJraWQiOiIuLi8uLi8uLi8uLi8uLi8uLi9kZXYvbnVsbCIsImFsZyI6IkhTMjU2In0.eyJpc3MiOiJwb3J0c3dpZ2dlciIsInN1YiI6ImFkbWluaXN0cmF0b3IiLCJleHAiOjE2OTIzNTc3NzZ9.oS2CpYpiofOhVaaisMdzLaFjW_mFqShzNVeEo-i_pY8**

The header and payload parts of a JWT are just base64url-encoded JSON objects. The header contains metadata about the token itself, while the payload contains the actual "claims" about the user.
The third part is the signature and it is used to verify the token, there many algorithm to do that.

### jws vs jwe

to be short jws is just encoded and use a signature while jwe are encrypted. but almost always when people talk about jwt they mean a jws token.


## simple vulnerable scenario
### decode vs verify <a name="decodeVuln"></a>
jwt libraries typically provide one method for verifying tokens and another that just decodes them.
If the web app use decode it means that the application doesn't verify the signature and is possible to modify jwt contents without knowing sign key.

### none algorithm

In the header jwt tokens contains an alg parameter. This tells the server which algorithm was used to sign the token. If the application is vulnerable we can set __alg__ to __none__ to bypass the sign check
(usually server reject token with no signature).

### Bruteforce secret keys
If secret keys is not safe enough is possible to bruteforce it locally with hashcat for example.
> hashcat -a 0 -m 16500 \<jwt\> \<wordlist\>

## JWT header parameter injections
in jws there are header parameter that could lead to an attack:
- jwk (json web key) emedded json object representing the key
- jku (json web key set url) url from which servers can fetch a set of keys
- kid (Key ID) an id that server use to identify the correct key

### Injecting jwk
If jku is supported by the server is possible too choose the public key used to verify the jwt.
```
{
    "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
    "typ": "JWT",
    "alg": "RS256",
    "jwk": {
        "kty": "RSA",
        "e": "AQAB",
        "kid": "ed2Nf8sb-sD6ng0-scs5390g-fFD8sfxG",
        "n": "yy1wpYmffgXBxhAUJzHHocCuJolwDqql75ZWuCQ_cb33K2vh9m"
    }
}
```
Ideally, servers should only use a limited whitelist of public keys to verify JWT signatures. However, misconfigured servers sometimes use any key that's embedded in the jwk parameter.

### Injecting jku
instead of embedding public keys directly jku reference to a jwk Set containing the key. When verifying the signature, the server fetches the revelant key from this URL.

some websites could have some protection refer to ssrf to bypass them.

### injecting kid
sometimes kid is used to access directly to the key file and this could lead to directory traversal vulnerability. The easiest way to exploit this is access to `/dev/null` this way the key used to verify will be an empty string.

>(Note use 'AA==' as key which is the base64 encode of null byte) 

## Algorithm confusion

usually verify function works like this:
``` 
function verify(token, secretOrPublicKey){
    algorithm = token.getAlgHeader();
    if(algorithm == "RS256"){
        // Use the provided key as an RSA public key
    } else if (algorithm == "HS256"){
        // Use the provided key as an HMAC secret key
    }
}
```

problems arise when website developer use verify assuming that it will exclusively handle JWTs signed using an asymmetric algorithm. This is an example:  

```
publicKey = <public-key-of-server>;
token = request.getCookie("session");
verify(token, publicKey);
```

In this case if the server receives a token signed using a symmetric algorithm like HS256 it will use the public key as the secret key. this mean that we can sign and verify token with the public key.

### Steps to exploit
- Obtain the server's public key
- Convert the public key to a suitable format
- Create a malicious JWT
- Sign the token with HS256, using the public key as the secret

#### Obtain the server's public key
Sometimes server expose their public keys as JWK via standard endpoints like `/jwk.json`.

if keys are not exposed there is an algorithm to retrieve the key by 2 signed token, is possible to run it with a really convenient docker:  
>  docker run --rm -it portswigger/sig2n \<token1\> \<token2\> 

#### Convert the public key to a suitable format
The public key can be stored in the server in many different format and it is important to use the right one and to match every single byte.
