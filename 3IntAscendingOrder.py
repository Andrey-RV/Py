#Reads 3 integers and print them in ascending order

string=input("Enter three number: ")
sequence=string.split()
if len(sequence)>3:
    print("You entered more than three numbers")
    exit()
for i in range(0, 3):
    if sequence[i]!=min(sequence) and sequence[i]!=max(sequence):
        mean=sequence[i]
print(min(sequence), mean, max(sequence))
