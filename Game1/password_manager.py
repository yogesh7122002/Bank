from cryptography.fernet import Fernet


def load_Key():
    try:
        with open("key.key","rb") as f:
            key = f.read()
            return key
    except FileNotFoundError:
        print("Key file not found. Generating a new key...")
        write_key()
        return load_Key()


def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as k:
        k.write(key)

# master_pwd = input("Enter The Master Password :") 
# +master_pwd 

key = load_Key()
fer = Fernet(key)




def view():
      with open('password.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip();
            user,passw = data.rsplit("|")
            print(user ," ",fer.decrypt(passw.encode()).decode())



def add():
    name  = input("Account Name :")
    password = input("Password :")
    with open('password.txt','a') as f:
        f.write(name+" | "+ fer.encrypt(password.encode()).decode()+"\n")

while True:
    mode = input("Would you like to add a new password or view existing passwords(view/add) or (Q/q) to Quit the App :").lower()
    if mode=="q": break
    if mode =="view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode")