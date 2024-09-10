#Activity2
with open("coding.txt") as fp:
    data1=fp.read()
with open("technology.txt") as fp:
    data2=fp.read()

data1+="\n"
data1+=data2
print("Merging")
with open("mergedfile.txt","w") as fp:
    fp.write(data1)
fp.close()