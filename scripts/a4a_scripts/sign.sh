#!/bin/sh

# Sign the application
python3 apk_signer.py --sign --verify --keyStore $KEYSTORE --keyStore_password $KEYSTORE_PW --unsigned_apk output/${A4A_APK}-unaligned-unsigned-protected.apk --signed_apk output/${A4A_APK}-protected.apk

echo Done Signing!
