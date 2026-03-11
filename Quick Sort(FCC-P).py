def quick_sort( array: list) -> list:
    low = 0
    high = len(array) - 1
    pivot = (low + high) // 2

    low_list = array[:pivot]
    high_list = array[pivot:]
    middle_list = [element for element in array if element == pivot]