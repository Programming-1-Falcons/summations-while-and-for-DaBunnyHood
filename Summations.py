#While

output = 0
x = 0
num = int(input("Number: "))

while x < num:
    x = x + 1
    output = x + output

print(output)

#For
num = range(1,int(input("Number: ")),1)


for output in num:
    print(output)

print(output + 1)
