#!/bin/sh

rm -rf output-original
mkdir output-original
cp ${A4A_APK}.apk output-original

# Sign the application
python apk_signer.py --sign --verify --keyStore $KEYSTORE --keyStore_password $KEYSTORE_PW --unsigned_apk output-original/${A4A_APK}.apk --signed_apk output-original/${A4A_APK}-signed.apk

rm -f output-original/${A4A_APK}.apk
rm -f output-original/${A4A_APK}-signed.apk.*
rm -f output-original/${A4A_APK}-*aligned*

echo Done!
