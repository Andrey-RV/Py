n, j, m=[int(x) for x in (input("Enter three positive numbers separated by spaces: ").split())]
if n<=0 or j<=0 or m<=0:
    print("Invalid input")
    exit()

count=0
i=1
sequence = []

while count<n:
    if i%m==j%m:
        sequence.append(i)
        count+=1
    i+=1
    
print("The fist {} 'i' numbers such that i%{}={}%{} are {}".format(n, m, j, m, sequence))
