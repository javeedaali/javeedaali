hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    for index in hexNum:
        if index not in hexNumbers:
            print("Number is not a valid hexadecimal.")
            return None
    if len(hexNum) > 3:
        print("Number must be no more than 3 characters long.")
        return None
    elif len(hexNum) == 3: 
        return 256*hexNumbers[hexNum[0]] + 16*hexNumbers[hexNum[1]] + hexNumbers[hexNum[2]]
    elif len(hexNum) == 2:
        return 16*hexNumbers[hexNum[0]] + hexNumbers[hexNum[1]]
    elif len(hexNum) == 1:
        return hexNumbers[hexNum]

def main():
    num_to_test = input("Enter hexidecimal number to convert: ")
    print(f"'{num_to_test}' converted to decimal = {hexToDec(num_to_test)}")

if __name__ == "__main__":
    return_code = main()