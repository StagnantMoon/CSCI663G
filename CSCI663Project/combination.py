# Diffie-Hellman Example
# Alex Danielle Basden
# Calculate secret key
from tkinter import *
from pydes import des


def clearAll():
    text1_field.delete(1.0, END)
    text2_field.delete(1.0, END)
    text3_field.delete(1.0, END)
    text4_field.delete(1.0, END)
    text5_field.delete(1.0, END)
    text6_field.delete(1.0, END)
    text7_field.delete(1.0, END)
    text8_field.delete(1.0, END)
    text9_field.delete(1.0, END)
    text10_field.delete(1.0, END)


def encryption():
    input_text = text1_field.get("1.0", "end")[:-1]

    d = des()

    output_text = ""

    key = "secret_K"
    output_text = d.encrypt(key, input_text, padding=True)

    text2_field.insert('end -1 chars', output_text)


def decryption():
    input_text = text1_field.get("1.0", "end")[:-1]

    d = des()

    key = "secret_K"
    output_text = d.decrypt(key, input_text, padding=True)

    text2_field.insert('end -1 chars', output_text)


# def prime(i):
#     if i == 2:
#         return True
#     elif ((i < 2) or ((i % 2) == 0)):
#         return False
#     elif i > 2:
#         for j in range(2, i):
#             if not (i % j):
#                 return False
#     return True


def dhellman():
    sharedPrime = text3_field.get("1.0", "end")[:-1]
    sharedBase = text4_field.get("1.0", "end")[:-1]
    aSecret = text5_field.get("1.0", "end")[:-1]
    bSecret = text6_field.get("1.0", "end")[:-1]
    sharedPrime = int(sharedPrime)
    sharedBase = int(sharedBase)
    aSecret = int(aSecret)
    bSecret = int(bSecret)
    a = (sharedBase ** aSecret) % sharedPrime
    b = (sharedBase ** bSecret) % sharedPrime
    userAshared = (b ** aSecret) % sharedPrime
    userBshared = (a ** bSecret) % sharedPrime

    text7_field.insert('end -1 chars', a)
    text8_field.insert('end -1 chars', b)
    text9_field.insert('end -1 chars', userAshared)
    text10_field.insert('end -1 chars', userBshared)


# print("Enter a shared prime for two people 'p' and an integer for shared base 'g': ")
# sharedPrime = int(input("Enter the shared prime number for p: "))
# sharedBase = int(input("Enter the shared base ('g'): "))

# Verify SharedPrime is a prime
# checkP = prime(sharedPrime)
# while (checkP == False):
# sharedPrime = int(input("Try again and enter a prime number  for p: "))
# checkP = prime(sharedPrime)

# print("Enter user A secret and user B secret")
# aSecret = int(input("Enter User A Secret as an integer: "))
# bSecret = int(input("Enter User B Secret as an integer: "))

# Begin the Application
# print("Shared Prime: ", sharedPrime)
# print("Shared Base: ", sharedBase)

# User A sends User B : a = sharedBase^aSecret mod p
# a = (sharedBase**aSecret) % sharedPrime
# print("User A Sends 'a': ", a)

# User B sends User A : b = sharedBase ^ bSecret mod p
# b = (sharedBase**bSecret) % sharedPrime
# print("User B Sends 'b': ", b)
# print("********************************************")
# print("Private Shared Secret:")
# s = b ^ aSecret mod p
# user1SharedSecret = (b ** aSecret) % sharedPrime
# s = a ^bSecret mod p
# user2SharedSecret = (a ** bSecret) % sharedPrime
# print("User A shared secret: ", user1SharedSecret)
# print("User B shared secret: ", user2SharedSecret)
# Driver code
if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background='white')

    # Set the configuration of GUI window (Widthx Height)
    root.geometry("1200x900")

    # set the name of tkinter GUI window
    root.title("Decryption/Encryption")

    # Create Label for Head
    headlabel = Label(root, text='DES Encryption', fg='black', bg="blue")
    head2label = Label(root, text='Diffie Hellman Example', fg='red', bg="black")
    # Create Labels for DES
    label1 = Label(root, text=" Message you wish to encrypt or decrypt:", fg='white', bg='black')
    label2 = Label(root, text="Message encrypted or decrypted:", fg='white', bg='black')
    # Create Labels for DiffieHellman
    label3 = Label(root, text="Enter the shared prime number for p: ", fg='white', bg='black')
    label4 = Label(root, text="Enter the shared base ('g'): ", fg='white', bg='black')
    label5 = Label(root, text="Enter User A Secret: ", fg='white', bg='black')
    label6 = Label(root, text="Enter User B Secret: ", fg='white', bg='black')
    label7 = Label(root, text="User A sends 'a' to User B, a = :", fg='white', bg='black')
    label8 = Label(root, text="User B sends 'b' to User A, b = :", fg='white', bg='black')
    label9 = Label(root, text="User A Shared Secret  = :", fg='white', bg='black')
    label10 = Label(root, text="User B Shared Secret = :", fg='white', bg='black')
    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    headlabel.grid(row=0, column=1)
    head2label.grid(row=4, column=1)
    # padx keyword argument used to set padding along x-axis .
    label1.grid(row=1, column=0, padx=5)
    label2.grid(row=3, column=0, padx=5)
    label3.grid(row=5, column=0, padx=5)
    label4.grid(row=5, column=2, padx=5)
    label5.grid(row=7, column=0, padx=5)
    label6.grid(row=7, column=2, padx=5)
    label7.grid(row=9, column=0, padx=5)
    label8.grid(row=9, column=2, padx=5)
    label9.grid(row=10, column=0, padx=5)
    label10.grid(row=10, column=2, padx=5)

    # Create a text area box
    # for filling or typing the information.
    text1_field = Text(root, height=3, width=50, font="lucida 13")
    text2_field = Text(root, height=3, width=50, font="lucida 13")
    text3_field = Text(root, height=1, width=24, font="lucida 13")
    text4_field = Text(root, height=1, width=24, font="lucida 13")
    text5_field = Text(root, height=1, width=24, font="lucida 13")
    text6_field = Text(root, height=1, width=24, font="lucida 13")
    text7_field = Text(root, height=1, width=24, font="lucida 13")
    text8_field = Text(root, height=1, width=24, font="lucida 13")
    text9_field = Text(root, height=1, width=20, font="lucida 13")
    text10_field = Text(root, height=1, width=20, font="lucida 13")
    # padx keyword argument used to set padding along x-axis .
    # pady keyword argument used to set padding along y-axis .
    text1_field.grid(row=1, column=1, padx=5, pady=10)
    text2_field.grid(row=3, column=1, padx=5, pady=10)
    text3_field.grid(row=5, column=1, padx=5, pady=10)
    text4_field.grid(row=5, column=3, padx=5, pady=10)
    text5_field.grid(row=7, column=1, padx=5, pady=10)
    text6_field.grid(row=7, column=3, padx=5, pady=10)
    text7_field.grid(row=9, column=1, padx=5, pady=10)
    text8_field.grid(row=9, column=3, padx=5, pady=10)
    text9_field.grid(row=10, column=1, padx=5, pady=10)
    text10_field.grid(row=10, column=3, padx=5, pady=10)
    # Create a Generate Button and attached
    # with generate function
    button1 = Button(root, text="Encrypt", bg="red", fg="black", command=encryption)
    button1.grid(row=1, column=3)

    button2 = Button(root, text="Decrypt", bg="red", fg="black", command=decryption)
    button2.grid(row=3, column=3)

    # Create a Clear Button and attached
    # with clearAll function
    button3 = Button(root, text="Clear All", bg="red", fg="black", command=clearAll)
    button3.grid(row=15, column=1)

    button4 = Button(root, text="Calculate Shared Secret", bg="red", fg="black", command=dhellman)
    button4.grid(row=11, column=1, pady=25)
    root.mainloop()
