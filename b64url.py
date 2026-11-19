from cryptography import x509
import base64, json

def b64url(n):
    b=n.to_bytes((n.bit_length() + 7) // 8, "big")
    return base64.urlsafe_b64encode(b).rstrip(b"=").decode()

cert= x509.load_pem_x509_certificate(open("publickey509.pem","rb").read())
nums=cert.public_key().public_numbers()

jwks={"keys":[{"kty":"RSA","use":"sig","kid":"1","n":b64url(nums.n),"e":b64url(nums.e)}]
      }
json.dump(jwks, open("jwks.json","w"), indent=2)
