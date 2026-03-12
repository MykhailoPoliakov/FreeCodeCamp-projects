def square_root_bisection(number, tolerance=1, max_iter=10) -> None:
    if number < 0:
        raise ValueError('Square root of negative number is not defined in real numbers')
    elif number in [0, 1]:
        print(f'The square root of {number} is {number}')
        return number

    low = 0
    high = number
    amount_iter = 1

    tolerance = tolerance / 2

    while low <= high and amount_iter <= max_iter:
        mid = (low + high) / 2

        if number - tolerance <= mid * mid <= number + tolerance:
            print(f"The square root of {number} is approximately {abs(mid)}")
            return abs(mid)
        elif mid * mid > number + tolerance:
            print(mid, '-')
            high = mid + 1
        else:
            print(mid, '+')
            low = mid - 1

        print()
        amount_iter += 1

    print(f"Failed to converge within {max_iter} iterations")
    return None


square_root_bisection(0.001, 1e-7, 50)