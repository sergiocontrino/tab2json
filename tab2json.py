import os
import sys
import getopt
import json
from os.path import isfile, join
from isatools.convert import isatab2json
cwd= os.getcwd()

#print(cwd)

#print ("This is the name of the script: ", sys.argv[0])
#print ("Number of arguments: ", len(sys.argv))
#print ("The arguments are: " , str(sys.argv))

from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument("-i", "--indir", dest="indir",
#                    help="directory with ISA tab files")
                    help="directory with ISAtab files", metavar="ISAtab dir")
#parser.add_argument("-o", "--out", dest="outfile",
#                    help="output json ISA file, no extension", metavar="ISAjson")
#parser.add_argument("-q", "--quiet",
#                    action="store_false", dest="verbose", default=True,
#                    help="don't print status messages to stdout")

args = parser.parse_args()

print (args.indir)
#print (args.outfile)

output_file = args.indir + ".json"
output_path = "./jsondir/"
input_path = "./isatabs/" + args.indir

if not os.path.exists(output_path):
        os.makedirs(output_path)
#print(output_path)

print("ISA json built in " + output_path + output_file + "\n")

# isa_json = isatab2json.convert('./isatabs/'args.indir, use_new_parser=True)
#isa_json = isatab2json.convert(join('./isatabs/'args.indir), use_new_parser=True)
isa_json = isatab2json.convert(input_path, use_new_parser=True)

try:
     with open(join(output_path,output_file), 'w') as out_fp:
              json.dump(isa_json, out_fp, indent=4)
except IOError as e:
     print("something went wrong:", e)


