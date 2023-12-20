def checkSymbol(x, y, array):
    # Checking Top Values
    try:
        if not (array[x - 1][y - 1].isalnum()) and not (array[x - 1][y - 1] == "."):
            return True
    except IndexError:
        pass
    try:
        if not (array[x - 1][y].isalnum()) and not (array[x - 1][y] == "."):
            return True
    except IndexError:
        pass
    try:
        if not (array[x - 1][y + 1].isalnum()) and not (array[x - 1][y + 1] == "."):
            return True
    except IndexError:
        pass
    # Checking Left and Right
    try:
        if not (array[x][y - 1].isalnum()) and not (array[x][y - 1] == "."):
            return True
    except IndexError:
        pass
    try:
        if not (array[x][y + 1].isalnum()) and not (array[x][y + 1] == "."):
            return True
    except IndexError:
        pass
    # Checking Bottom Values
    try:
        if not (array[x + 1][y - 1].isalnum()) and not (array[x + 1][y - 1] == "."):
            return True
    except IndexError:
        pass
    try:
        if not (array[x + 1][y].isalnum()) and not (array[x + 1][y] == "."):
            return True
    except IndexError:
        pass
    try:
        if not (array[x + 1][y + 1].isalnum()) and not (array[x + 1][y + 1] == "."):
            return True
    except IndexError:
        pass
    return False


def main():
    total = 0
    with open("2023Day3Input.txt") as file:
        lineString = [line.rstrip() for line in file]
        charMax = len(lineString[0])
        for lineCount, line in enumerate(lineString):
            currentNum = ""
            symbolFlag = False
            for charCount, char in enumerate(line):
                if char.isnumeric():
                    if currentNum:
                        currentNum += char
                    else:
                        currentNum = char
                    if not (symbolFlag):
                        symbolFlag = checkSymbol(lineCount, charCount, lineString)
                if (
                    (char == "." or charCount == charMax - 1 or not (char.isalnum()))
                    and currentNum
                    and symbolFlag
                ):
                    print(f"Adding {currentNum}")
                    total += int(currentNum)
                    currentNum = ""
                    symbolFlag = False
                elif char == "." or charCount == charMax - 1:
                    currentNum = ""
                    symbolFlag = False

    print(total)


if __name__ == "__main__":
    main()
