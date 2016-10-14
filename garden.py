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
    
    # Find the starting indecies, carrot count
    if (N % 2) != 0 and (M % 2) != 0:
        start_row, start_col = N/2, M/2
        count = garden[start_row][start_col]
        for x in xrange(N/2, N/2 + 2):
            for y in xrange(M/2, M/2 + 2):
                if garden[x][y] > count:
                    start_row = x
                    start_col = y
                    count = garden[x][y]

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
    curr_row, curr_col = start_row, start_col
    while True:
        amount = 0
        zero_count = 0

        # Look up
        if curr_row > 0:
            if garden[curr_row - 1][curr_col] > amount:
                amount = garden[curr_row - 1][curr_col]
                new_row, new_col = curr_row - 1, curr_col

        # Look down
        if curr_row < N - 1:
            if garden[curr_row + 1][curr_col] > amount:
                amount = garden[curr_row + 1][curr_col]
                new_row, new_col = curr_row + 1, curr_col

        # Look right
        if curr_col < M - 1:
            if garden[curr_row][curr_col + 1] > amount:
                amount = garden[curr_row][curr_col + 1]
                new_row, new_col = curr_row, curr_col + 1

        # Look left
        if curr_col > 0:
            if garden[curr_row][curr_col - 1] > amount:
                amount = garden[curr_row][curr_col - 1]
                new_row, new_col = curr_row, curr_col - 1
        print amount
        # No more carrots to eat... 
        if amount == 0:
            return count

        # update position, total
        else:
            garden[curr_row][curr_col] = 0
            curr_row, curr_col = new_row, new_col
            count += amount



print eat(garden)