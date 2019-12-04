import argparse
import os
import time
import datetime
import hashlib
import logging

def is_valid_file(parser, arg):
    """
    Check if arg is a valid file that already exists on the file system.

    Parameters
    ----------
    parser : argparse object
    arg : str

    Returns
    -------
    arg
    """
    arg = os.path.abspath(arg)
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg
logging.basicConfig(filename='special.log',level=logging.INFO,format= ' [%(asctime)s]  {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%Y-%m-%d %H:%M:%S')
parser = argparse.ArgumentParser(description="Demo of setting logging verbosity using -vvvv style args")
#Define arguments
parser.add_argument('-v', "--verbose",    help="allows progress messages to be displayed", action='store_true')
logging.debug(argparse,)
parser.add_argument('-i', '--inputFile',  required=True, help="specifiy a single input file",metavar="FILE",
type=lambda x: is_valid_file(parser, x))
logging.info('input file selected {} + {}')
parser.add_argument('-o', '--outputFile', required=True, help="specifiy a single output file",metavar="FILE",
type=lambda x: is_valid_file(parser, x))
parser.add_argument('-l', '--logFile',    required=True, help="specifiy a log file to record results",metavar="FILE",
type=lambda x: is_valid_file(parser, x))
fileName = "inputtest.txt"
modified = os.path.getmtime(fileName)
size = os.path.getsize(fileName)
args = parser.parse_args()
def file_as_bytes(fileName):
    with fileName:
        return fileName.read()

logging.info("Week 7 Solution, Professor Hosmer")
with open(fileName,mode='rb') as file:
    fileContent = file.read()
    print (file)
logging.info("Read the file stats success")
logging.info("File Contents Read Success")
if args.verbose:
    print("Verbose selected")
else:
    print("Verbose not selected")

if args.inputFile:
    print("Input file ingested")
else:
    print("Error: no input file")
    exit()

if args.outputFile:
    print("Output file processed")
else:
    print("Error: no output file")
    exit()

if args.logFile:
    print("Log selected")
else:
    print("Log not selected")
print ("======================================")
#output file
f = open("Outputfile.txt","w")
logging.info(fileName +'file opened success')
print("File Name: ", fileName , file=f)
logging.info('file name is printed to outputfile' + fileName)
print("File Size: ", size, file=f)
print("Date modified:",datetime.datetime.fromtimestamp(modified),file=f)
year,month,day,hour,minute,second=time.localtime(modified)[:-3]
hashValue = hashlib.sha256(file_as_bytes(open(fileName, 'rb'))).hexdigest()
print("File Header:",hashlib.sha256(file_as_bytes(open(fileName, 'rb'))).hexdigest(),file=f)
logging.info('SHA256' + hashValue)
f.close()
logging.info(fileName +'file closed success')











