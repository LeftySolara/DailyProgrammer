def main():
    with open("input4.txt", 'r') as data_file:
        grid = []
        size = int(data_file.readline())
        logs = int(data_file.readline())

        for line in data_file:
            line = line.rstrip().split()
            for i in range(len(line)):
                grid.append(int(line[i]))

    smallest = min(grid)
    for i in range(logs):
        while True:
            grid[grid.index(min(grid))] += 1
            break

    # display grid
    for i in range(0, size*size, size):
        print(*grid[i:i+size])

        

if __name__ == '__main__':
    main()