def fibonacci( n ):
    if n < 1:
        return 0

    sequence = [0, 1]
    for _ in range( n-1 ):
        sequence = [ sequence[1], sequence[0] + sequence[1] ]

    return sequence[1]

print( fibonacci( 10 ) )