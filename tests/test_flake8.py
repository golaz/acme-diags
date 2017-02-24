import unittest
import os
import subprocess
import shlex

class TestFlake8(unittest.TestCase):

    def test_flake8(self):
        flake8_pth = os.path.dirname(os.path.abspath(__file__))
        flake8_pth = os.path.join(flake8_pth, "..")
        flake8_pth = os.path.abspath(flake8_pth)
        flake8_pth = os.path.join(flake8_pth, "acme_diags")

        P = subprocess.Popen(shlex.split("flake8 --max-line-length=120 %s" % flake8_pth),
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)
        P.wait()
        out = P.stdout.read()
        if out is not "":
            print(out)
        self.assertEquals(out, "")
