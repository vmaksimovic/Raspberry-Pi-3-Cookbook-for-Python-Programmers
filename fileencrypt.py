

import sys #imorted to obtain comand line arguments
import encryptdecrypt as ENC

#Define expected inputs

ARG_INFILE = 1
ARG_OUTFILE = 2
ARG_KEY = 3
ARG_LENGTH = 4

def convertFile(infile, outfile, key):
	#convert key yext to an integer
	try:
		enc_key = int(key)
	except ValueError:
		print("Error! The key %s should be an integer valiue!" %(key))
	#code put on two lines
	else:
		try:
			#open file
			with open(infile) as f_in:
				infile_content = f_in.readlines()
		except IOError:
			print("Unable to open %s "%(infile))
		try:
			with open(outfile,'w') as f_out:
				for line in infile_content:
					out_line=ENC.encryptText(line, enc_key)
					f_out.writelines(out_line)
		except IOError:
			print("Unable to open %s" %(outfile))
		print("Conversion complite: %s" %(outfile))
	finally:
		print("FINISH")
		
#chech arguments
if len(sys.argv) == ARG_LENGTH:
	print("Command %s" %(sys.argv))
	convertFile(sys.argv[ARG_INFILE], sys.argv[ARG_OUTFILE], sys.argv[ARG_KEY])
else:
	print("Ussage: filencetypt.py infile outfile key")
	
