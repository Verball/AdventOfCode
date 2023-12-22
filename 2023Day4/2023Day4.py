def main():
    with open("2023Day4Input.txt") as file:
        total = 0
        for line in file:
            yourNumber = set()
            amountCorrect = 0
            for num in line[line.find(":") + 2 : line.find("|") - 1].split():
                yourNumber.add(num)
            for winningNumber in line[line.find("|") + 2 : -1].split():
                if winningNumber in yourNumber:
                    if amountCorrect == 0:
                        amountCorrect = 1
                    else:
                        amountCorrect *= 2
            total += amountCorrect
        print(total)


if __name__ == "__main__":
    main()
