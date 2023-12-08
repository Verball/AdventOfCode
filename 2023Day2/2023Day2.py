"""Problem:Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
"""


def main():
    sum = 0

    with open("2023Day2Input.txt") as file:
        lines = [line.strip()[line.find(":") + 2 :].split("; ") for line in file]

        for index, line in enumerate(lines):
            cubesPulled = {"red": 12, "green": 13, "blue": 14}
            Possible = True
            for picked in line:
                for parts in picked.split(", "):
                    count, color = parts.split(" ")
                    if int(count) > cubesPulled[color]:
                        Possible = False
            if Possible:
                sum += index + 1

    print(sum)


if __name__ == "__main__":
    main()
