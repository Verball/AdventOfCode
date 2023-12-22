def main():
    with open("2023Day6Input.txt") as file:
        times = file.readline()
        distances = file.readline()
        times = [int(x) for x in times[times.find(":") + 1 :].split()]
        distances = [int(x) for x in distances[distances.find(":") + 1 :].split()]
        res = 1

        for time, distance in zip(times, distances):
            count = 0
            for ms in range(time + 1):
                speed = ms
                msRemaining = time - ms
                distanceTraveled = speed * msRemaining
                if distanceTraveled > distance:
                    count += 1
            res *= count

        print(res)


if __name__ == "__main__":
    main()
