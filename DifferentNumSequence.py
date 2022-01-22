#Prints from a sequence of integers how many different numbers it contains.

string=input("Enter a sequence of numbers separeted by spaces: ")
sequence=string.split()
unique=0
for i in range(len(sequence)):
    for j in range(i+1, len(sequence)):
        if sequence[i] == sequence[j]:
            repeated=True
            break
        else:
            repeated=False
    if repeated==False:
        unique+=1
print("There are {} unique numbers in the sequence.".format(unique))