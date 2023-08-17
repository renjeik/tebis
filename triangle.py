import sys


def max_path_sum(tri):
    # Using dynamic programming method and calculate
    # "from bottom row to top row" iteratively
    for row in range(len(tri) - 2, -1, -1):
        for col in range(len(tri[row])):
            left = tri[row + 1][col]
            right = tri[row + 1][col + 1]

            # Choose the larger adjacent value
            # Add all values dynamically
            if left > right:
                tri[row][col] += left
            else:
                tri[row][col] += right

    return tri[0][0]


if __name__ == "__main__":
    # Part 1
    triangle = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
    ]
    print("Part 1: " + str(max_path_sum(triangle)))  # Expect 1074

    # Part 2
    inputfile = sys.argv[1]
    inputlist = []

    with open(inputfile, "r") as f:
        inputlist = f.read().splitlines()

    triangle = [input.split() for input in inputlist]
    triangle = [list(map(int, row)) for row in triangle]

    print("Part 2: " + str(max_path_sum(triangle)))  # Expect 7273

    # Unit testing
    triangle = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    print("Unit testing: " + str(max_path_sum(triangle)))  # Expect 23
