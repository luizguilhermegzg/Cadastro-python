import os
user = {
    "name": "",
    "age": "",
    "email": "",
    "password": ""
} 
def input_name(name_received):
    user["name"] = name_received
def input_age(age_received):
    user["age"] = age_received
def input_email(email_received):
    user["email"] = email_received
def input_password(password_received):
    user["password"] = password_received
def verify_data(result):
    if result == "yes":
        print("Logging...")
    elif result == "no":
        print("Try again...")
        os.system('cls' if os.name == 'nt' else 'clear')
        initialize_functios()
    else:
        print("Please type only 'yes or no'")
        os.system('cls' if os.name == 'nt' else 'clear')    
        for requiriment, data in user.items():
            print("Your ",requiriment,":",data)
        verify_data(input("If everything is ok say 'yes', otherwise say 'no' (in lower-case):  "))

def initialize_functios():
    input_name(input("ENTER YOUR NAME: "))
    input_age(int(input("ENTER YOUR AGE: ")))
    input_email(input("ENTER YOUR EMAIL: "))
    input_password(input("ENTER YOUR PASSWORD: "))
    verify_data(input("If everything is ok say 'yes', otherwise say 'no' (in lower-case): "))
initialize_functios() 
