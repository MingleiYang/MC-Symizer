# -*- coding: UTF-8 -*-

#

"""
Testing module the util module
"""

import os
import unittest
import subprocess
import shlex
import urllib
import tarfile
import shutil


def call_command(command, pipe=None, echo=False):
    if echo:
        print command

    process = subprocess.Popen(shlex.split(command.encode("ascii")),
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    output = process.communicate(input=pipe)
    return output


class UtilTest(unittest.TestCase):
    def setUp(self):
        # update if needed
        self.MCSYM_DB_PATH = "/u/major/public_html/MC-Sym/DB"
        self.DATA_ON_SERVER = "http://major.iric.ca/~leongs/jenkins_tests/MC-Symizer/data.tar.gz"
        # build all the paths
        self.MCSYMIZER_PATH = os.path.abspath(os.path.join(os.curdir, "src", "mcsymizer.py"))
        self.DATA_ARCHIVE = os.path.abspath(os.path.join(os.curdir, "tests", "data.tar.gz"))
        self.DATA_DIR = os.path.abspath(os.path.join(os.curdir, "data"))

        # download and create the DATASET if needed
        if not os.path.exists(self.DATA_DIR):
            if not os.path.exists(self.DATA_ARCHIVE):
                # download the data tar file
                urllib.urlretrieve(self.DATA_ON_SERVER,
                                   filename=self.DATA_ARCHIVE)

            tar = tarfile.open(self.DATA_ARCHIVE)
            tar.extractall(path=os.curdir)

    def tearDown(self):
        # delete the data dir
        if os.path.exists(self.DATA_DIR):
            shutil.rmtree(self.DATA_DIR)

    def test_generated_script(self):
        def build_args(curr_line):
            name, s1, S1, s2, S2 = line.split("\t")
 
            dict_params = dict(name=name.strip(),
                               sequence1=s1.strip(), structure1=S1.strip(),
                               sequence2=s2.strip(), structure2=S2.strip(), 
                               db_path=self.MCSYM_DB_PATH)
 
            argument_string = " --use_relative_path "
            for k, v in dict_params.iteritems():
                if v:
                    argument_string += "--{k} ".format(k=k)
                    argument_string += '"{v}" '.format(v=v)
            return argument_string, dict_params
 
        # read the input file
        with open(os.path.join(self.DATA_DIR,
                               "seq_struct.tsv"), 'rb') as input_file:
            for line in input_file:
                if not line.startswith("#") and line.strip():
                    args, dict_params = build_args(line)
                    out, err = call_command("python {mcsymizer} {args}".format(mcsymizer=self.MCSYMIZER_PATH,
                                                                               args=args))
 
                    # open the valid file
                    valid_out = ""
                    with open(os.path.join(self.DATA_DIR,
                                           "validated_generated_scripts",
                                           dict_params["name"]+".mcc"),
                              'rb') as valid_f:
                        valid_out = valid_f.read()

                    print "testing {name}".format(name=dict_params["name"])
                    print err
                    self.assertEqual(out.strip(), valid_out.strip())

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CallCommandTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
