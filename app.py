from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)''' 

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            # Split using '|', but limit the split to two parts
            user, passw = data.split("|", 1)  
            print("User:", user, ", Password:", passw)

        
def add():
    name = input('Account Name: ')
    pwd = input("password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()) + "\n")  

while True:
    mode = input("would you like to add a new password or view exsiting ones (view, add), prees q to quit ? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")