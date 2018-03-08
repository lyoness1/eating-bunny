# This is a very elegent solution
# - well named
# - has comments
# - has tests
# - avoids repetition by using extraction and abstraction
# - is a working solution

# This is a "yes" candidate

def eat(garden):
    """Returns the total number of carrots eaten by Mr. Bunny

        >>> garden1 = [[5, 7, 8, 6, 3], [0, 0, 7, 0, 4], [4, 6, 3, 4, 9], [3, 1, 0, 5, 8]]
        >>> garden2 = [[5, 7, 8, 6, 3], [0, 0, 7, 0, 4], [4, 6, 3, 4, 9]]
        >>> garden3 = [[7, 0, 6, 3], [0, 2, 0, 4], [6, 3, 4, 9], [1, 1, 5, 0]]
        >>> eat(garden1)
        27
        >>> eat(garden2)
        27
        >>> eat(garden3)
        26

    """
    # Find the dimensions of the garden
    N = len(garden)  # rows
    M = len(garden[0])  # cols

    # Find starting indecies, carrot count
    possible_start_cells = [(N/2, M/2),
                            ((N-1)/2, M/2),
                            (N/2, (M-1)/2),
                            ((N-1)/2, (M-1)/2)]

    count, curr_row, curr_col = find_max_carrot_count(garden, possible_start_cells)

    # Look all directions, move, eat, update
    while True:
        options_to_look = [(curr_row - 1, curr_col),
                           (curr_row, curr_col - 1),
                           (curr_row + 1, curr_col),
                           (curr_row, curr_col + 1)]

        amount, new_row, new_col = find_max_carrot_count(garden, options_to_look)

        # No more carrots to eat
        if amount == 0:
            return count

        # eat current carrots, update position, total count
        else:
            garden[curr_row][curr_col] = 0
            curr_row, curr_col = new_row, new_col
            count += amount


def find_max_carrot_count(garden, idx_list):
    """finds the cell in garden with max num carrots from idx_list"""
    count = 0
    row, col = idx_list[0]
    for x, y in idx_list:
        if x < 0 or x >= len(garden) or y < 0 or y >= len(garden[0]):
            continue
        elif garden[x][y] > count:
            count, row, col = garden[x][y], x, y

    return count, row, col


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n ALL TESTS PASSED!! \n"

