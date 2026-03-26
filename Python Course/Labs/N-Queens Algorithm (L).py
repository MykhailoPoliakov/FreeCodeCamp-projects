import copy

def dfs_n_queens( n ) -> list:
    if n == 1:
        return [[0]]
    if n < 3:
        return []


    output: list = []
    stack = [[ [ '' for _ in range(n) ] for _ in range(n)],]

    while stack:
        matrix: list = stack.pop()

        for row in range(n):
            for col in range(n):

                if matrix[row][col] in [ 'Q','x' ]:
                    continue

                new_matrix = copy.deepcopy(matrix)

                for i in range(n):
                    new_matrix[row][i] = 'x'
                    new_matrix[i][col] = 'x'
                    if col + i in range(n) and row + i in range(n):
                        new_matrix[row + i][col + i] = 'x'
                    if col - i in range(n) and row - i in range(n):
                        new_matrix[row - i][col - i] = 'x'
                    if col + i in range(n) and row - i in range(n):
                        new_matrix[row - i][col + i] = 'x'
                    if col - i in range(n) and row + i in range(n):
                        new_matrix[row + i][col - i] = 'x'
                new_matrix[row][col] = 'Q'

                count: int = 0
                save = True
                for em_row in range(n):
                    if '' in new_matrix[em_row]:
                        stack.append(copy.deepcopy(new_matrix))
                        save = False
                        break
                    if 'Q' in new_matrix[em_row]:
                        count += 1

                if save and count == n:

                    output_list = []
                    for f_row in range(n):
                        for f_col in range(n):
                            if new_matrix[f_row][f_col] == 'Q':
                                output_list.append(f_col)

                    if output_list not in output:

                        print_text = ''
                        for j in range(n):
                            print_text += f"{new_matrix[j]}\n"
                        print(print_text)

                        output.append( output_list )

    return output

print(len(dfs_n_queens( 8 )))