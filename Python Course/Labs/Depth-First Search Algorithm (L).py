def dfs( matrix: list, label: int) -> list:

    length: int = len(matrix)
    stack: list[int] = [ label ]
    checked: list[bool] = [ False for _ in range(length) ]
    output: list[int] = []

    while stack:
        current: int = stack.pop( )

        checked[current] = True
        output.append( current )

        for i in range(length):
            if matrix[current][i] and not checked[i]:
                stack.append( i )

    return output



dfs([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]], 1)