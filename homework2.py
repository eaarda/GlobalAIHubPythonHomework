def getUser():
    firstName = input('Please enter your name: ')
    lastName = input('Please enter your last name: ')
    age = int(input('Please enter your age: '))
    dateOfBirth = int(input('Please enter your date of birth year: '))

    user = [firstName, lastName, age, dateOfBirth]
    return user


def infoUser(x):
    for info in x:
        print(info)


def userControl(x):
    if x[2] < 18:
        print("You cant go out because it's too dangerous!!")
    else:
        print("You can go out to the street..")


def main():
    print("This is user identification program")
    user = getUser()
    infoUser(user)
    userControl(user)


if __name__ == "__main__":
    main()
