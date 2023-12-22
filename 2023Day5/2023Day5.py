def main():
    with open("2023Day5Input.txt") as file:
        seeds = file.readline()
        seeds = [[int(x)] for x in seeds[seeds.find(":") + 1 :].split()]
        mapCount = 0

        for line in file:
            if ":" in line:
                mapCount += 1
                for seed in seeds:
                    if len(seed) < mapCount:
                        seed.append(seed[-1])
            elif line != "\n":
                mappedNum, inputNum, mapRange = [int(num) for num in line.split()]
                for seed in seeds:
                    if (
                        seed[-1] in range(inputNum, inputNum + mapRange)
                        and len(seed) <= mapCount
                    ):
                        seed.append(mappedNum + (seed[-1] - inputNum))
        minLoc = seeds[0][-1]

        for seed in seeds:
            print(seed)
            minLoc = min(minLoc, seed[-1])
        print(minLoc)


if __name__ == "__main__":
    main()
