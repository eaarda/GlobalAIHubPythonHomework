
def getValues():
    values = []
    for i in range(0, 5):
        # input methods always takes string types
        value = input('Please enter a value: ')
        values.append(value)
    return values


def printValues(list):
    for i in range(0, 5):
        print(f'{i+1}. value: {list[i]} and type: {type(list[i])} ')


def main():
    print("Hi, user!")
    list = getValues()
    printValues(list)


if __name__ == "__main__":
    main()
