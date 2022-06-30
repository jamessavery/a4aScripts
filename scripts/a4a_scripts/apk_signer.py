import os
import os.path
import sys
import argparse
import subprocess

""" This module is designed to ease up manual signign of .APK files.
    for detailed usage information see "APK_Signer.py -h"
    Note:
    In order to use this application machine must have android SDK installed and
    ANDROID_SDK_HOME set in environmental variables.
"""


def get_sdk_build_tools_path():
    if os.environ.get('ANDROID_HOME') is None:
        sys.exit("ANDROID_HOME variable not set")

    skd_versions = os.listdir(os.path.join(os.environ.get('ANDROID_HOME'), 'build-tools'))
    return os.path.join(os.environ.get('ANDROID_HOME'), 'build-tools', max(skd_versions))


def set_arguments(parser):
    parser.add_argument("--sign",
                        help="Sign the APK",
                        action="store_true")
    parser.add_argument("--verify",
                        help="Verify signed APK",
                        action="store_true")
    parser.add_argument("-ks", "--keyStore",
                        help="Path to keyStore file")
    parser.add_argument("-pw", "--keyStore_password",
                        help="password of keyStore")
    parser.add_argument("-in", "--unsigned_apk",
                        help="APK to Sign")
    parser.add_argument("-out", "--signed_apk",
                        help="Output for signed APK. APK for verification")


def get_arguments(parser):
    return parser.parse_args()


class SigningConfig:
    def __init__(self, ks, ks_pass):
        self.keyStore = ks
        self.keyStorePass = ks_pass
        self.alias = 'build'
        self.aliasPass = ks_pass


class ApkSigner:
    def __init__(self, toolsDir, config, unsigned_apk, signed_apk):
        self._toolsDir = toolsDir
        self._config = config

        self._unsigned_apk = unsigned_apk
        self._aligned_apk = None
        self._signed_apk = signed_apk

        if self._signed_apk is None:
            self._signed_apk = os.path.splitext(self._unsigned_apk)[0] + '-signed.apk'

    @staticmethod
    def _get_align_tool(toolsDir):
        align_tool = os.path.join(toolsDir, 'zipalign')

        if os.path.exists(align_tool) is not True:
            sys.exit("zipalign not found in " + toolsDir)
        return align_tool

    def _align_apk(self):
        align_tool = self._get_align_tool(self._toolsDir)

        """unsigned_app.apk -> unsigned_app-aligned.apk"""
        self._aligned_apk = os.path.splitext(self._unsigned_apk)[0] + '-aligned.apk'

        align_cmd = [align_tool,
                     #Verbose mode is disabled by default
                     "-v",
                     "-f",
                     "-p",
                     "4",
                     self._unsigned_apk,
                     self._aligned_apk
                     ]
        return_code = subprocess.call(align_cmd)
        #if return_code != 0:
             #sys.exit("Error aligning apk file")
        #"print "---- Align successful ----""

    @staticmethod
    def _get_sign_tool(toolsDir):
        sign_tool = os.path.join(toolsDir, 'apksigner')

        if os.path.exists(sign_tool) is not True:
            sys.exit("apksigner not found in " + toolsDir)
        return sign_tool

    def sign_apk(self):
        self._align_apk()
        sign_tool = self._get_sign_tool(self._toolsDir)

        sign_cmd = [sign_tool,
                    "sign",
                    "--ks", self._config.keyStore,
                    "--ks-pass", "pass:"+self._config.keyStorePass,
                    "--out", self._signed_apk,
                    self._aligned_apk
                    ]

        return_code = subprocess.call(sign_cmd)
        if return_code != 0:
            sys.exit("Error signing apk file")
        #"print "---- Sign successful ----""

    def verify_apk(self):
        verify_tool = self._get_sign_tool(self._toolsDir)
        verify_cmd = [verify_tool, "verify", self._signed_apk]

        return_code = subprocess.call(verify_cmd)
        if return_code != 0:
            sys.exit("Error verifying apk file")
        #"print "---- Verification successful ----""

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    set_arguments(parser)
    args = get_arguments(parser)

    """ Performs a check to see if Android_SDK_HOME is set """
    toolsDir = get_sdk_build_tools_path()

    """ ZipAligns and Signs the APK """
    if args.sign is True:
        config = SigningConfig(args.keyStore, args.keyStore_password)
        signer = ApkSigner(toolsDir, config, args.unsigned_apk, args.signed_apk)
        signer.sign_apk()

        if args.verify is True:
            signer.verify_apk()

    """ Verify the provided APK """
    if args.sign is not True and args.verify is True:
        tool = ApkSigner._get_sign_tool(toolsDir)
        verify_cmd = [tool, "verify", args.signed_apk]

        return_code = subprocess.call(verify_cmd)
        if return_code != 0:
            sys.exit("Error verifying apk file")
        #"print "---- Verification successful ----""


