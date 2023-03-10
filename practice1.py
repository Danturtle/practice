x = int(input("Enter the height : "))
y = x - 1
z = 1
while x > 0:
    print(" " * y, "*" * z)
    x = x - 1
    y = y - 1
    z = z + 2

print("---------------------------------- \n \n \n \n \n \n \n")


a = int(input("Enter your number:"))
b = 0
for i in range(1 , a+1):
    if a%i == 0:
        b += 1

if b == 2:
    print(f"{a} , is a prime number.")
else:
    print(f"{a} , isn't a prime number.")

print("---------------------------------- \n \n \n \n \n \n \n")



for i in range(1 , 1001):
    if i > 1:
        for c in range(2, i):
            if i % c == 0:
               break
        else:
            print(i)
