import os

def input_data():
    msg = input("Ingrese su mensaje a ocultar:\n")
    filename = input("Ingrese el nombre de su archivo mp3:\n")
    return msg, filename

def open_file(filename):
    filepath = "./test/" + filename
    file = open(filepath, "rb")
    return file

def menu():
    print("-"*15 + "\n"*2)
    print("Bienvenido" + "\n"*2)
    print("-"*15 + "\n"*2)

def hide(msg, file):
    # TODO: steganography
    return True

if (__name__=='__main__'):
    menu()
    msg, filename = input_data()
    file = open_file(filename)