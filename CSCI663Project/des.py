# Using Pydes.py
# Alex Basden
# Simple Message using DES with Pydes.Py
from tkinter import *
from pydes import des

def clearAll() :
    text1_field.delete(1.0, END)
    text2_field.delete(1.0, END)


def encryption():
    input_text = text1_field.get("1.0", "end")[:-1]

    d = des()

    output_text =""

    key = "secret_K"
    output_text = d.encrypt(key, input_text, padding=True)

    text2_field.insert('end -1 chars', output_text)


def decryption():
    input_text = text1_field.get("1.0", "end")[:-1]

    d = des()

    key = "secret_K"
    output_text = d.decrypt(key, input_text, padding=True)

    text2_field.insert('end -1 chars', output_text)
# key = "secret_K"
# text = input("Please enter your message you wish to decrypt/encrypt: ")
# d = des()

#encrypted = d.encrypt(key, text, padding=True)
#decrypted = d.decrypt(key, encrypted, padding=True)
#print("Encrypted Message: %r" % encrypted)
#print("Your original Message was: ", decrypted)

# Driver code
if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background='white')

    # Set the configuration of GUI window (WidthxHeight)
    root.geometry("1200x900")

    # set the name of tkinter GUI window
    root.title("Decryption/Encryption")

    # Create Welcome to SpongeBob Mocking Text Generator label
    headlabel = Label(root, text='DES Encryption and Diffie Hellman',
                      fg='black', bg="blue")

    # Create a "Input Text " label
    label1 = Label(root, text=" Message you wish to encrypt or decrypt:",
                   fg='white', bg='black')

    # Create a "Output Text " label
    label2 = Label(root, text="Message encrypted or decrypted:",
                   fg='white', bg='black')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    headlabel.grid(row=0, column=1)

    # padx keyword argument used to set padding along x-axis .
    label1.grid(row=1, column=0, padx=5)
    label2.grid(row=3, column=0, padx=5)

    # Create a text area box
    # for filling or typing the information.
    text1_field = Text(root, height=5, width=50, font="lucida 13")
    text2_field = Text(root, height=5, width=50, font="lucida 13")

    # padx keyword argument used to set padding along x-axis .
    # pady keyword argument used to set padding along y-axis .
    text1_field.grid(row=1, column=1, padx=5, pady=10)
    text2_field.grid(row=3, column=1, padx=5, pady=10)

    # Create a Generate Button and attached
    # with generate function
    button1 = Button(root, text="Encrypt", bg="red", fg="black",
                     command=encryption)

    button1.grid(row=2, column=1)

    button2 = Button(root, text="Decrypt", bg="red", fg="black", command=decryption)
    button2.grid(row=2, column=2)

    # Create a Clear Button and attached
    # with clearAll function
    button3 = Button(root, text="Clear", bg="red",
                     fg="black", command=clearAll)

    button3.grid(row=4, column=1)

    root.mainloop()