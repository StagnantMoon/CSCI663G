# Diffie-Hellman Example
# Alex Danielle Basden
# Calculate secret key
print("Enter a shared prime for two people 'p' and an integer for shared base 'g': ")
sharedPrime = int(input("Enter the shared prime number for p: "))
sharedBase = int(input("Enter the shared base ('g'): "))

# Verify SharedPrime is a prime


def prime(i):
    if i == 2:
        return True
    elif ((i < 2) or ((i % 2) == 0)):
        return False
    elif i > 2:
        for j in range(2, i):
            if not (i % j):
                return False
    return True

checkP = prime(sharedPrime)
while (checkP == False):
    sharedPrime = int(input("Try again and enter a prime number  for p: "))
    checkP = prime(sharedPrime)

print("Enter user A secret and user B secret")
aSecret = int(input("Enter User A Secret as an integer: "))
bSecret = int(input("Enter User B Secret as an integer: "))

# Begin the Application
print("Shared Prime: ", sharedPrime)
print("Shared Base: ", sharedBase)

# User A sends User B : a = sharedBase^aSecret mod p
a = (sharedBase**aSecret) % sharedPrime
print("User A Sends 'a': ", a)

# User B sends User A : b = sharedBase ^ bSecret mod p
b = (sharedBase**bSecret) % sharedPrime
print("User B Sends 'b': ", b)
print("********************************************")
print("Private Shared Secret:")
# s = b ^ aSecret mod p
user1SharedSecret = (b ** aSecret) % sharedPrime
# s = a ^bSecret mod p
user2SharedSecret = (a ** bSecret) % sharedPrime

print("User A shared secret: ", user1SharedSecret)
print("User B shared secret: ", user2SharedSecret)
