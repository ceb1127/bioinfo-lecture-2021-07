Seq1 = "AGTTTATAG"

for i in range(len(Seq1)):
    #print(i, Seq1[i])
	#print(i,i+1,Seq1[i:i+2])
    if Seq1[i:i+2] == "TT":
		print(i, Seq1[i:i+2])
