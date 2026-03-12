def selection_sort( array: list) -> list:

    i = 0
    length = len(array)

    while True:

        if i == length:
            return array

        min_index = i

        for num in range( i + 1, length ):
            if array[ num ] < array[ min_index ]:
                min_index = num

        if min_index != i:
            array[ i ] , array[ min_index ] = array[ min_index ], array[ i ]

        i += 1

print(selection_sort([1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]))