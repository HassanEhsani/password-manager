master_pwd = input("What is the master password? ")

def view():
    pass
def add():
    name = input('Account Name: ')
    pwd = input("password: ")
    
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd)

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