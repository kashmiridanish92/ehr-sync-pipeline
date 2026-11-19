import datetime, base64
from cryptography import x509
from  cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa

key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,)

name= x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, "ehr-sync-pipeline")])
now=datetime.datetime.now(datetime.timezone.utc)
cert= (x509.CertificateBuilder().subject_name(name).
issuer_name(name).public_key(key.public_key()).serial_number(x509.random_serial_number()).not_valid_before(now).not_valid_after(now+datetime.timedelta(days=365)).sign(key, hashes.SHA256()))

with open("private_key.pem", "wb") as f:
    f.write(key.private_bytes(serialization.Encoding.PEM,
                              serialization.PrivateFormat.PKCS8,
                              serialization.NoEncryption()))

pem=cert.public_bytes(serialization.Encoding.PEM)
with open("publickey509.pem","wb") as f:
    f.write(pem)

with open("publickey509.b64","wb") as f:
    f.write(base64.b64encode(pem))
