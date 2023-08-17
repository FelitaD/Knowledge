def avg(*list_numbers: float) -> float: # python know we can pass more than 1 argument
    total = 0
    for num in list_numbers:
        if isinstance(num, (int, float)):
            total += num
        else:
            raise TypeError("wrong input data, please put numbers.")

    return total / len(list_numbers)

