import copy

def print_text( output_text, matrix , n ):
    text = output_text
    for j in range( n ):
        text += f"{matrix[j]}\n"
    print(text)



def dfs_n_queens( n: int ) -> list:

    # basic solutions
    if n == 1:
        return [[0]]
    if n < 3:
        return []



    # range n for cycles
    RANGE: range = range(n)

    # list with final solutions
    output: list = []
    # main stack
    stack = [[ [[ '' for _ in RANGE ] for _ in RANGE ],0],]


    # iterate through all possible positions
    while stack:
        # output for testing
        print("new cycle")

        # pop from stack
        matrix, level = stack.pop()

        # on next free colon
        col = level
        for row in reversed(RANGE):

            # check if queen can be placed
            if matrix[row][col] in ['Q', 'x']:
                continue

            # place the queen and calculate board
            new_matrix = copy.deepcopy(matrix)
            for i in RANGE:
                # directions
                new_matrix[row][i] = 'x'
                new_matrix[i][col] = 'x'
                # diagonals
                if row + i in RANGE and col + i in RANGE:
                    new_matrix[row + i][col + i] = 'x'
                if row - i in RANGE and col - i in RANGE:
                    new_matrix[row - i][col - i] = 'x'
                if row - i in RANGE and col + i in RANGE:
                    new_matrix[row - i][col + i] = 'x'
                if row + i in RANGE and col - i in RANGE:
                    new_matrix[row + i][col - i] = 'x'
            # place the queen
            new_matrix[row][col] = 'Q'

            # append to stack
            if level < n - 1:
                stack.append([copy.deepcopy(new_matrix), level + 1])

                # output for testing
                print_text(f' append, level : {level}\n', new_matrix, n)
                continue


            # append final result
            result = [f_row for f_col in range(n) for f_row in range(n) if new_matrix[f_row][f_col] == 'Q']
            output.append(result)

            # output for testing
            print_text(f' output, level : {level}\n', new_matrix, n)
            break


    return output



print( dfs_n_queens( 8 ) )