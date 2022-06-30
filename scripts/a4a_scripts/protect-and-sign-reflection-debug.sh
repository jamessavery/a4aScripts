#!/bin/sh

# Clean up old binary
rm -rf output-reflection-debug
rm -rf output

# Secure binary application
secure-dex -i ${A4A_APK}.apk -o output -b blueprint-reflection-debug.json 

if [ $? -eq 0 ]; then

# Sign the application
	./sign.sh
	cp -r output output-reflection-debug
	rm -f output-reflection-debug/${A4A_APK}-protected.apk.*
	rm -f output-reflection-debug/${A4A_APK}-unaligned*
else
    echo PROTECTION ERROR
fi

echo Done!
