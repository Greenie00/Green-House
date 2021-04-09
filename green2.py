database = {}
import random

def init():

    isValidOptionSelected = False
    print('Welcome To Bank Green')

    while isValidOptionSelected == False:

        haveAccount = int(input('Do You Have An Account With Us 1.(Yes) 2.(No) \n'))

        if(haveAccount == 1):
           isValidOptionSelected = True
           logjn()
        elif(haveAccount == 2):
           isValidOptionSelected = True
           print(register())
        else:
           print('You Have Selected An Invalid Option')


def register():
    print("********  Start Registration  *********")
    
    email = input("What is Your Email address? \n")
    first_name = input("What is Your First Name? \n")
    last_name = input("What is Your Last Name? \n")
    password = input("Create a Password \n")

    newAccountNumber = generateAccountNumber()

    database[newAccountNumber] = [ first_name, last_name, email, password ]

    print("Your Accoubt Has Been Created")

    login()
    
def login():
    print("Login to Your Account")


def generateAccountNumber():

   return random.randrange(1111111111,9999999999)



#### Actual System ####
#print(generateAccountNumber())
init()
