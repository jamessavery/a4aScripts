#!/bin/sh

adb uninstall $A4A_BUNDLE_ID

adb install -t output-release/${A4A_APK}-protected.apk

adb logcat -c
