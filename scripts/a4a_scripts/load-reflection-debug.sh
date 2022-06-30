#!/bin/sh

adb uninstall $A4A_BUNDLE_ID

adb install -t output-reflection-debug/${A4A_APK}-protected.apk

adb logcat -c
