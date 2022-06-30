#!/bin/sh

adb uninstall $A4A_BUNDLE_ID

adb install -t output-original/${A4A_APK}-signed.apk

adb logcat -c
