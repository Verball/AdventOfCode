"""
Problem:
The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
"""


def main():
    arr = []

    with open("2023Day1Input.txt") as file:
        lines = [line.rstrip() for line in file]
    for stringEntry in lines:
        for i in stringEntry:
            if i.isdigit():
                num1 = i
                break
        for j in stringEntry[::-1]:
            if j.isdigit():
                num2 = j
                break
        arr.append(int(num1 + num2))
    print(sum(arr))


if __name__ == "__main__":
    main()
