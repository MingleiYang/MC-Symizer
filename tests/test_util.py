# -*- coding: UTF-8 -*-

#

"""
Testing module the util module
"""

import os
import unittest2 as unittest
import subprocess
import shlex


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
        self.INPUT_TSV = "tests/data/input_seq_struct.tsv"
        self.MCSYMIZER_PATH = "src/mcsymizer.py"
        self.DATA_ON_SERVER = "http://major.iric.ca/~leongs/jenkins_tests/MC-Symizer/data.tar.gz"
        self.DATA_DIR = "tests/data"
        
        print os.path.abspath(os.curdir)

    def tearDown(self):
        pass
        
#     def test_generated_script(self):
#         def build_args(curr_line):
#             name, s1, S1, s2, S2 = line.strip().split("\t")
# 
#             dict_params = dict(name=name,
#                                sequence1=s1, structure1=S1,
#                                sequence2=s2, structure2=S2,
#                                use_relative_path=True, db_path=self.MCSYM_DB_PATH)
# 
#             argument_string = ""
#             for k, v in dict_params.iteritems():
#                 if v:
#                     argument_string += "--{k} ".format(k=k)
#                     if not isinstance(k, bool):
#                         argument_string += '"{v}" '.format(v=v)
#             return argument_string, dict_params
# 
#         # read the input file
#         with open(self.INPUT_TSV, 'rb') as input_file:
#             for line in input_file:
#                 if not line.startswith("#") and line.strip():
#                     args, dict_params = build_args(line)
#                     out, err = call_command("python {mcsymizer} {args}".format(mcsymizer=self.MCSYMIZER_PATH,
#                                                                                args=args))
# 
#                     # open the valid file
#                     valid_out = ""
#                     with open(os.path.join(self.VALID_DIRECTORY, dict_params["name"]+".mcc"), 'rb') as valid_f:
#                         valid_out = valid_f.read()
# 
#                     self.assertEqual(out.strip(), valid_out.strip())

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(CallCommandTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
