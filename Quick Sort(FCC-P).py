def quick_sort( input_array: list) -> list:
    array = input_array.copy()

    if len(array) <= 1:
        return array

    pivot: int = (( len(array) - 1 ) // 2)

    low_list:  list = [ el for el in array if el <  array[pivot] ]
    mid_list:  list = [ el for el in array if el == array[pivot] ]
    high_list: list = [ el for el in array if el >  array[pivot] ]

    low_list  = quick_sort( low_list  )
    high_list = quick_sort( high_list )

    array: list = low_list + mid_list + high_list

    return array



lst = [4, 42, 16, 23, 15, 8]
print(quick_sort( lst ))
