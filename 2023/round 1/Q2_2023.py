strandA,strandB = input().split()

DNA_database = {'A':'T',
                'T':'A',
                'C':'G',
                'G':'C'}

corrupted = False 
for DNA in range(len(strandA)):
    if DNA_database[strandA[DNA]] != strandB[DNA]:
        corrupted = True
        break

if corrupted:
    print("CORRUPTED")
else:
    print("OK")
        


