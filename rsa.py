# CSCI 663 Project RSA
# Alex Danielle Basden

print("Simple RSA Encrypt and Decrypt Program!")
print("Remember these Prime Numbers for When you wish to decrypt / encrypt")

# Input Prime Numbers
print("Please enter the 'p' & 'q' values.")
print("Current the prime numbers: 2, 3, and 5 are giving errors: Use at own risk")
p = int(input("Enter a prime number for p: "))
q = int(input("Enter a prime number for q: "))


# Check if the numbers are prime
# Is rough could do better (Prime Numbers, 2, 3, 5 are messing up).
def primecheck(i):
    if i == 2:
        return True
    elif ((i < 2) or ((i % 2) == 0)):
        return False
    elif i > 2:
        for j in range(2, i):
            if not (i % j):
                return False
    return True


checkP = primecheck(p)
checkQ = primecheck(q)
while (((checkP == False) or (checkQ == False))):
    p = int(input("Try again and enter a prime number for p: "))
    q = int(input("Try again and enter a prime number for q: "))
    checkP = primecheck(p)
    checkQ = primecheck(q)

# The RSA mod
n = p * q
#  The Eulers Toitent
r = (p - 1) * (q - 1)
print(" The Eulers Toitent value of (r) is:", r)

# Algorithms
# GCD (Greatest Common Divisor


def egcd(e, r):
    while r != 0:
        e, r = r, e % r
    return e


# def egcd(a, b):
#     x,y, u,v = 0,1, 1,0
#     while a != 0:
#         q, r = b//a, b%a
#         m, n = x-u*q, y-v*q
#         b,a, x,y, u,v = a,r, u,v, m,n
#     gcd = b
#     return gcd, x, y


# Euclid's Algorithm
def euclidalgorithm(e, r):
    for i in range(1, r):
        while (e != 0):
            a, b = r // e, r % e
            if b != 0:
                print("%d = %d*(%d) + %d" % (r, a, e, b))
            r = e
            e = b


# Extended Euclidean Algorithm
def exteuclidalgorithm(a, b):
    if a % b == 0:
        return b, 0, 1
    else:
        gcd, s, t = exteuclidalgorithm(b, a % b)
        s = s - ((a // b) * t)
        print("%d = %d*(%d) + (%d)*(%d)" % (gcd, a, t, s, b))
        return gcd, t, s


# Multiplicative Inverse
def multiinverse(e, r):
    gcd, s, _ = exteuclidalgorithm(e, r)
    if gcd != 1:
        return None
    else:
        if s < 0:
            print("s = %d. Because %d is < (less than) 0, s = s(modular) s = %d." % (s, s, s % r))
        elif s > 0:
            print("s = %d." % s)
        return s % r


# e Value Calculation (coprime e,r)
for i in range(1, 70000):  # can change
    if egcd(i, r) == 1:
        e = i
print("E =: ", e)


print("Euclid's Algorithm Test:")
euclidalgorithm(e, r)
d = multiinverse(e, r)

print("D =: ", d)
public = (e, n)
private = (d, n)
print("---------------------")
print("The *Private* Key =: ", private)
print("The *Public* Key =: ", public)
print("--------------------_")


# Encryption


def encrypt(publickey, numbertext):
    e, n = publickey
    x = []
    m = 0
    for j in numbertext:
        if j.isupper():
            m = ord(j) - 65
            c = (m ** e) % n
            x.append(c)
        elif j.islower():
            m = ord(j) - 97
            c = (m ** e) % n
            x.append(c)
        elif j.isspace():
            x.append(400)
    return x


# Decryption

def decrypt(privatekey, cryptotext):
    d, n = privatekey
    splitText = cryptotext.split(',')  # split text
    x = ''
    m = 0
    for j in splitText:
        if j == '400':  # '400' is space
            x += ' '
        else:
            m = (int(j) ** d) % n
            m += 65
            c = chr(m)
            x += c
    return x


# User Input for Message to Encrypt
print("******IMPORTANT******")
print("For decryption: please separate numbers with an ',' ie: 3, 4, 12")
userMessage = input("Please enter the message you wish to encrypt or decrypt: ")
print("The message you have entered is: ", userMessage)  # remove in future

# Choose to Encrypt or Decrypt and Print
choice = input("Enter '1' for DECRYPTION || Enter '2' for ENCRYPTION || Entering anything else will exit the program: ")
#  while choose != 0:
if choice == '2':
    encryptMessage = encrypt(public, userMessage)
    print("Encrypted message is the following:", encryptMessage)
    print("Please restart if wish to encrypt or decrypt another message.")

elif choice == '1':
    print("Your decrypted message is:", decrypt(private, userMessage))
    print("Please restart if wish to encrypt or decrypt another message.")

else:
    print("Thank you for trying the RSA Simple Program")
