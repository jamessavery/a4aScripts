# This script can be used to list how many classes are visible
# in an unprotected/protected APK that's been decompiled using apktool
# Modify the list of top level packages to correspond to what exists in the 
# decompiled APK

# usage: ./count-visible-classes.sh <apktool directory that contains smali* directories>

find $1/smali* -name *.smali | grep \
-e .*smali.*/android/support/ \
-e .*smali.*/androidx/ \
-e .*smali.*/bo/app \
-e .*smali.*/com/ \
-e .*smali.*/dagger/ \
-e .*smali.*/defpackage/ \
-e .*smali.*/developers/mobile/abt/ \
-e .*smali.*/io/ \
-e .*smali.*/kotlin/ \
-e .*smali.*/kotlin/coroutines/ \
-e .*smali.*/okhttp3/ \
-e .*smali.*/okio/ \
-e .*smali.*/org/ \
-e .*smali.*/retrofit2/ \
-e .*smali.*/timber/log/ \
-e .*smali.*/zendesk/ \
| wc -l
