class AgeError(Exception):    
    def __init__(self, message):    
        self.message = message

def Error(age):
    try:
        if age<=18:
            raise AgeError("Your Not Eligibal to Vote!")
        else :
            print("Your Are Eligible To Vote!")
    except AgeError as ae:
        print(ae)

age = int(input("Enter your age = "))
Error(age)