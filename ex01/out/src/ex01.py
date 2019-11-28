#!/usr/bin/env python3

'''
@author: Christian Wressnegger
'''

try:
    # For evaluating the exercises we'll provide a similar but
    # different configuration that contains alternative input
    # values than those provided in the script that was handed
    # out (nothing mean though). Develop your solution robust
    # enough to work with various kinds and variations of input.
    import ex01_testdata_lecturer as testdata  # @UnresolvedImport @UnusedImport

except:
    import ex01_testdata as testdata  # @UnusedImport


import filecmp
import os
import subprocess
import sys
import tempfile
import unittest

unittest.TestLoader.sortTestMethodsUsing = None
PYTHON = "python3"
PYERROR = "For running your solutions we call '{}'.\nThe name might be different for your installation (e.g. on Windows)\n"


class Ex01(unittest.TestCase):

    TASKS = 0
    MY_DIR = os.path.dirname(os.path.abspath(__file__))

    @staticmethod
    def call(tool, params):
        script = os.path.join(Ex01.MY_DIR, tool)
        cmd = '{} "{}" {}'.format(PYTHON, script, params)

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
        out, _ = p.communicate()

        if p.returncode != 0:
            sys.stderr.write(PYERROR.format(PYTHON))

        return out, p.returncode

    @staticmethod
    def tmpfile():
        fd, fname = tempfile.mkstemp(dir=Ex01.MY_DIR)
        os.close(fd)
        return fname

    def _check_encrypttool(self, tool, x, s=slice(0, None)):
        for alphabet, a, b in testdata.TOOL_MAP[tool][x][s]:
            fname = Ex01.tmpfile()

            with open(fname, 'wb') as f:
                f.write(a)
                f.seek(0)

            out, _ = Ex01.call(
                tool, '--{} {} "{}"'.format(x, alphabet, fname))

            os.remove(fname)
            self.assertEqual(out.strip(), b, "wrong {}ion".format(x))

    def _check_analysistool(self, tools, params=""):
        for plaintext, ciphertext in testdata.TOOL_MAP[tools[0]]:
            k, _ = Ex01.call(tools[0], '"{}" {}'.format(ciphertext, params))
            k = k.strip().decode('ascii')

            self.assertTrue(len(k) > 0, "No key extracted")

            fname1, fname2 = Ex01.tmpfile(), Ex01.tmpfile()

            Ex01.call(tools[1],
                      '--decrypt {} "{}" --out "{}"'.format(k, ciphertext, fname1))

            Ex01.call("mono/mono.py",
                      '--encrypt abcdefghijklmnopqrstuvwxyz "{}" --out "{}"'.format(plaintext, fname2))

            ok = os.path.getsize(fname1) > 0 and filecmp.cmp(fname1, fname2)
            os.remove(fname1)
            os.remove(fname2)

            self.assertTrue(ok, "Incorrect key/ decryption :(")

    def test_04_mono(self):
        TOOL = "mono/mono.py"
        self._check_encrypttool(TOOL, "encrypt", slice(0, 1))
        self._check_encrypttool(TOOL, "encrypt", slice(1, None))
        self._check_encrypttool(TOOL, "decrypt")
        Ex01.TASKS += 1

    def test_05_breakmono(self):
        TOOLS = ("mono/break_mono.py", "mono/mono.py")
        self._check_analysistool(TOOLS)
        Ex01.TASKS += 1

    def test_06_vig(self):
        TOOL = "vigenere/vig.py"
        self._check_encrypttool(TOOL, "encrypt")
        self._check_encrypttool(TOOL, "decrypt")
        Ex01.TASKS += 1

    def test_07_breakvig(self):
        TOOLS = ("vigenere/break_vig.py", "vigenere/vig.py")
        self._check_analysistool(
            TOOLS, "--keylen {}".format(testdata.BREAK_VIG_KEYLEN))
        Ex01.TASKS += 1
        pass

    def test_XX(self):
        if Ex01.TASKS > 0:
            print("[*] {} out of {} exercises work flawlessly! 👍".format(Ex01.TASKS, 4))
        else:
            print("[*] Unfortunately, non of the exercises work as expected (yet 😉)")


if __name__ == "__main__":
    unittest.main()
