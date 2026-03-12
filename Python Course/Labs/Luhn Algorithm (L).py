def verify_card_number(dirty_number: str) -> str:

    clean_number: str = ''
    for num in dirty_number:
        if num in  [ str(j) for j in range(10) ]:
            clean_number += num

    length: int = len(clean_number)

    new_number: int = 0

    for index, i in enumerate(reversed(range(length))):

        if not index % 2:
            new_number += int(clean_number[i])
            continue

        digit = f'{int(clean_number[i]) * 2}'

        if len(digit) <= 1:
            new_number += int(digit)
            continue

        new_number += int(digit[0]) + int(digit[1])

    if new_number % 10:
        return 'INVALID!'
    else:
        return 'VALID!'

