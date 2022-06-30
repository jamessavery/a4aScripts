# a4a_scripts

This contains some useful scripts I use for A4A protection.

There are scripts for the following:

- debug: debug charset and all active guards have debug = true
- release: ascii charset and all active guards have debug = false
- reflection-debug: Turns the reflection debugger on

- There's also a generic blueprint template (blueprint-template.json) that can be used as a starting point with minimal edits to start with a new app. 

Modify setenvs.sh to update the APK name, path to A4A, path to the Android Keystore & password and bundleid, then "source setenvs.sh"

The memory-game.apk is included as an example. The various scripts:

- protect-and-sign-<variant>: Protects with the associated blueprint, and signs the APK (example just uses the debug keystore)
- sign-<variant>: Just signs
- load-<variant>: Uninstalls the existing APK, loads the new APK, then clears the logcat
- logcat.sh: dumps the logcat info just for the bundleid in question
- reflection-debug.sh: For use with the reflection debug APK, runs the reflection debugger and dumps the new reflections to keepsignatures-reflection.txt

