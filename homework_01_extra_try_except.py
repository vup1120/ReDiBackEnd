# A function that validates a password (regular string) based on the criterias below:
# Must have a minimum of 8 characters. (e.g.: “Al4e2!” fails the criteria)
# Must contain at least one upper-case letter (e.g.: “ab3cd@1efg” fails the criteria)
# Must contain at least two digits (e.g: “Uv3!xxzy” fails the criteria)
# Can’t contain two or more consecutive digits (e.g.: “UX525!pun” fails the criteria)

# It asks the user to keep inputting passwords until they input a correct one instead of only reporting whether the password is correct or not,
# also report to the user the first failed criteria.


# set up the criteria
MIN_LENGTH = 8
MIN_UPPERCASE = 1
MIN_DIGITS = 2


def check_length(key):
    if len(key) >= MIN_LENGTH:  # place numbers inside a constant so you can easily change this later without having to go through the entire code
        return True
    else:
        return False

def check_uppercase(key):
    if sum([i.isupper() for i in key]) >= MIN_UPPERCASE:
        return True
    else:
        return False

def check_digits(key):
    if sum([i.isdigit() for i in key]) >= MIN_DIGITS:
        return True
    else:
        return False

def check_consecutive_digits(key):
    check = [i.isdigit() for i in key]
    for i in range(len(check) - 1):
        tmp = check[i] + check[i + 1]  # this is genius!
        while tmp > 1:
            return False
    return True


def main():
'''
check if the user-input password fits the criteria
'''
    while True:
        try:
            key = str(input("Enter your new password: "))
            if check_length(key) == False:
                raise PassWordNotStrongLength
            elif check_uppercase(key) == False:
                raise PassWordNotStrongUpperCase
            elif check_digits(key) == False:
                raise PassWordNotStrongTwoDigits
            elif check_consecutive_digits(key) == False:
                raise PassWordNotStrongNoConsecutive
            else:
                print('The password seems good')
                break
        except PassWordNotStrongLength:
            print("Invalid Password. Must have a minimum of 8 characters")
        except PassWordNotStrongUpperCase:
            print("Invalid Password. Must contain at least one upper-case letter")
        except PassWordNotStrongTwoDigits:
            print("Invalid Password. Must contain at least two digits")
        except PassWordNotStrongNoConsecutive:
            print("Invalid Password. Can’t contain two or more consecutive digits")


class PassWordNotStrongLength(Exception):  # default for all exceptions
    pass
class PassWordNotStrongUpperCase(Exception):  # default for all exceptions
    pass
class PassWordNotStrongTwoDigits(Exception):  # default for all exceptions
    pass
class PassWordNotStrongNoConsecutive(Exception):  # default for all exceptions
    pass

main()