#!/bin/sh

# Clean up old binary
rm -rf output-debug
rm -rf output

# Secure binary application
secure-dex -i $A4A_APK.apk -o output -b blueprint-debug.json 

if [ $? -eq 0 ]; then

# Sign the application
	./sign.sh
	cp -r output output-debug
	rm -f output-debug/${A4A_APK}-protected.apk.*
	rm -f output-debug/${A4A_APK}-unaligned*
else
    echo PROTECTION ERROR
fi

echo Done!
