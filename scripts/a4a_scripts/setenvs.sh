# Path to A4A Installation
export A4A_INSTALL=/opt/arxan/tools/securedex/working

# Path to Android Keystore and Keystore passsword
export KEYSTORE=debug.keystore
export KEYSTORE_PW=android
# Replace with Bundle ID, to retrieve from the APK:
# aapt dump badging <path-to-apk> | grep package:\ name
export A4A_BUNDLE_ID=com.sanint.app

# Replace with APK name (don't include .apk extension)
export A4A_APK=International
