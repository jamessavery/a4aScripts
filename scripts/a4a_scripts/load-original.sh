#!/bin/sh

adb uninstall $A4A_BUNDLE_ID

adb install -t ${A4A_APK}.apk

adb logcat -c
