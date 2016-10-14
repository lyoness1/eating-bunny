garden = (
[[5, 7, 8, 6, 3],
 [0, 0, 7, 0, 4],
 [4, 6, 3, 4, 9],
 [3, 1, 0, 5, 8]]
)

def eat(garden):

    # Find the dimensions of the garden
    N = len(garden)  # rows
    M = len(garden[0])  # cols
    
    # Find the starting indecies
    if (N % 2) == 0 and (M % 2) == 0:
        most = 0
        for x in xrange(N/2 - 1, N/2 + 1):
            for y in xrange(M/2 - 1, M/2 + 1):
                if garden[x][y] > count:
                    start_row, start_col = x, y
                    most = garden[x][y]

    elif (N % 2) != 0 and (M % 2) == 0:
        start_row, start_col = N/2, M/2 - 1
        count = garden[start_row][start_col]
        if garden[start_row][start_col + 1] > count:
            start_col = start_col + 1
            count = garden[start_row][start_col]

    elif (N % 2) == 0 and (M % 2) != 0:
        start_row, start_col = N/2 - 1, M/2
        count = garden[start_row][start_col]
        if garden[start_row + 1][start_col] > count:
            start_row = start_row + 1
            count = garden[start_row][start_col]

    elif (N % 2) != 0 and (M % 2) != 0:
        start_row, start_col = N/2, M/2
        count = garden[start_row][start_col]

    # Look all directions, move, eat, update
    while True:
        amount = 0

        # Look up
        if start_row > 0 and garden[start_row - 1][start_col] > amount:
            amount = garden[start_row - 1][start_col]
            new_row, new_col = start_row - 1, start_col

        # Look down
        if start_row < N - 1 and garden[start_row + 1][start_col] > amount:
            amount = garden[start_row + 1][start_col]
            new_row, new_col = start_row + 1, start_col

        # Look right
        if start_col < M - 1 and garden[start_row][start_col + 1] > amount:
            amount = garden[start_row][start_col + 1]
            new_row, new_col = start_row, start_col + 1

        # Look left
        if start_col > 0 and garden[start_row][start_col - 1] > amount:
            amount = garden[start_row][start_col - 1]
            new_row, new_col = start_row, start_col - 1

        # No more carrots to eat... 
        if amount == 0:
            return count

        # update position, total
        else:
            garden[start_row][start_col] = 0
            start_row, start_col = new_row, new_col
            count += amount



print eat(garden)