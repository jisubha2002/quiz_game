import random
import string
n=int(input("put the length of password:"))
s=string.ascii_lowercase + string.ascii_uppercase +string.digits 
print(s)
passwd ="".join(random.choice(s) for i in range(n))
print("password is ", passwd)

