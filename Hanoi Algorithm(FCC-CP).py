def hanoi_solver( num: int ) -> str:

    move: list[list[int]] = [ [] , [] , [] ]
    move[0] = [digit for digit in reversed(range(1,num + 1))]

    direction: dict = {
        'right' : { 0 : 2, 1 : 0, 2 : 1 },
        'left'  : { 0 : 1, 1 : 2, 2 : 0 },}

    odd_sys  = direction['right'] if num % 2 != 0 else direction['left']
    even_sys = direction['left'] if num % 2 != 0 else direction['right']

    disks: list = [ j + 1 for j in range(num)]
    output: str = ''

    i = 1
    while True:

        output += f'{move[ 0 ]} {move[ 1 ]} {move[ 2 ]}'

        if move == [[], [], list(reversed(range(1,num + 1))) ]:
            return output
        else:
            output += '\n'

        for disk in disks:
            if ((2**disk / 2) + i) % 2**disk == 0:
                for index, row in enumerate(move):
                    if row and row[-1] == disk:

                        sys = odd_sys if disk % 2 != 0 else even_sys
                        move[ sys[ index ]].append( move[ index ].pop() )
                        break
                break

        i += 1





print(hanoi_solver( 2 ))