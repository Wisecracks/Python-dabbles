# it only reads one line at a time. When the next line is read, the previous one will be garbage collected unless you have stored a reference to it somewhere else 

with open("log.txt") as infile:
    for line in infile:
        do_something_with(line)

# ##############		
import sys

with open(sys.argv[2], 'w') as outfile:
    with open(sys.argv[1]) as infile:
        for line in infile:
            outfile.write(line)

# ##############
		
# alternate
chunk = infile.read(chunksize)
# read lines within chunck

# ##############
# with pandas

df = pd.read_csv('matrix.txt',sep=',', header = None, skiprows= 1000, nrows=1000)