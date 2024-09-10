#Activity1
with open("coding.txt","w") as file:
    file.write("Computer programming or coding is the composition of sequences of instructions, called programs, that computers can follow to perform tasks. It involves designing and implementing algorithms, step-by-step specifications of procedures, by writing code in one or more programming languages.")
file.close()
with open("coding.txt","r") as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)
file.close()