import sys


def max_path_sum(tri):
    # Using dynamic programming method and calculate
    # from "bottom row to top row" calculation
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
    inputfile = sys.argv[1]
    inputlist = []

    with open(inputfile, "r") as f:
        inputlist = f.read().splitlines()

    triangle = [input.split() for input in inputlist]
    triangle = [list(map(int, row)) for row in triangle]

    print(max_path_sum(triangle))
