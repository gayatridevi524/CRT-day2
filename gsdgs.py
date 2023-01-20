name=input("Name:")

userInput = input("username:")

if userInput != 0:
    password = input("enter password:")
    lower_case, upper_case, special_char, digits = 0, 0, 0, 0
    if (len(password) <= 8):
        for i in password:

            # counting lowercase alphabets
            if (i.islower()):
                lower_case += 1

            # counting uppercase alphabets
            if (i.isupper()):
                upper_case += 1

            # counting digits
            if (i.isdigit()):
                digits += 1

            # counting the mentioned special characters
            if (i == '@' or i == '$' or i == '_'):
                special_char += 1
    if (lower_case >= 1 and upper_case >= 1 and special_char >= 1 and digits >= 1 and lower_case + special_char + upper_case + digits == len(password)):
        print("Valid Password")
    else:
        print("Invalid Password")
print(userInput,"welcome!")
