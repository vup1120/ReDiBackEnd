def check_length(key):
    if len(key) >= 8:
        return True
    else:
        return False


def check_uppercase(key):
    if sum([i.isupper() for i in key]) > 0:
        return True
    else:
        return False


def check_digits(key):
    if sum([i.isdigit() for i in key]) > 1:
        return True
    else:
        return False


def check_consecutive_digits(key):
    check = [i.isdigit() for i in key]
    for i in range(len(check) - 1):
        tmp = check[i] + check[i + 1]
        while tmp > 1:
            return False
    return True

def isvalid(key):
    isLong = check_length(key)
    isUpperCase = check_uppercase(key)
    isDigits = check_digits(key)
    noConsecutive = check_consecutive_digits(key)
    return isLong, isUpperCase, isDigits, noConsecutive


def check_password():
    isLong, isUpperCase, isDigits, noConsecutive = False, False, False, False

    while isLong + isUpperCase + isDigits + noConsecutive < 4:
        key = str(input("Enter your password: "))
        isLong, isUpperCase, isDigits, noConsecutive = isvalid(key)

        if not isLong:
            if check_length(key) == True:
                isLong = True
                break
            else:
                print("Invalid Password. Must have a minimum of 8 characters")
                continue

        if not isUpperCase:
            if check_uppercase(key) == True:
                isUpperCase = True
                break
            else:
                print("Invalid Password. Must contain at least one upper-case letter")
                continue

        if not isDigits:
            if check_digits(key) == True:
                isDigits = True
                break
            else:
                print("Invalid Password. Must contain at least two digits")
                continue

        if not noConsecutive:
            if check_consecutive_digits(key) == True:
                noConsecutive = True
                break
            else:
                print("Invalid Password. Can’t contain two or more consecutive digits")
                continue

    print('The password looks fine')

check_password()