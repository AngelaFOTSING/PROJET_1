from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
import datetime
import uuid

one_day = datetime.timedelta(1, 0, 0)

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)

public_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
).public_key()

#public_key = private_key.public_key()

builder = x509.CertificateBuilder()
builder = builder.subject_name(x509.Name([
    x509.NameAttribute(NameOID.COUNTRY_NAME, u'FR'),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u'France'),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u'Paris'),
    x509.NameAttribute(NameOID.COMMON_NAME, u'My CA'),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u'Angela Company'),
    x509.NameAttribute(NameOID.ORGANIZATIONAL_UNIT_NAME, u'Angela'),
]))
builder = builder.issuer_name(x509.Name([
    x509.NameAttribute(NameOID.COMMON_NAME, u'My CA'),
]))
builder = builder.not_valid_before(datetime.datetime.today() - one_day)
builder = builder.not_valid_after(datetime.datetime(2022, 10, 31))
builder = builder.serial_number(int(uuid.uuid4()))
builder = builder.public_key(public_key)
builder = builder.add_extension(
    x509.BasicConstraints(ca=True, path_length=None), critical=True,
)
certificate = builder.sign(
    private_key=private_key, algorithm=hashes.SHA256(),
    backend=default_backend()
)
print(isinstance(certificate, x509.Certificate))

with open("ca.key", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"pkiANGELA.06")
    ))

with open("ca.crt", "wb") as f:
    f.write(certificate.public_bytes(
        encoding=serialization.Encoding.PEM,
    ))