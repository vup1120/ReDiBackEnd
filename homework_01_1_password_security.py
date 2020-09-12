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


def main():
    key = str(input("Enter your new password: "))
    if check_length(key)+check_uppercase(key)+check_digits(key)+check_consecutive_digits(key) < 4:
        print('The password is not strong enough')
    else:
        print('The password seems good')

main()