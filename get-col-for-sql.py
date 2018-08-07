import pandas as pd 
filePath = "C:/Users/1568925/Documents/Projects/Nostro Remediation/SIT/ebbs/SampleData/"
inputFile = "ebbsprd_zm_account.dat"
outputFile = 'ebbs_masternos.txt' # output1.txt, output2.txt, etc.

df = pd.read_csv(filePath + inputFile, sep="|",usecols=['masterno'], index_col=None,  dtype=str)

outputFile = open(filePath+outputFile,'w')

#df1 = df.to_string(header=False,index=False,index_names=False).split('\n')
#
#
#vals = [",".join(ele.split()) for ele in df1]
#print(vals)

for ele in df['masterno'].unique():
#    print(ele, end=",")
    
    outputFile.write("'%s'," % ele)
outputFile.close()

print(inputFile, df['masterno'].unique().size)
