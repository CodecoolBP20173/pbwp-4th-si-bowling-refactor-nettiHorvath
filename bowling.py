def score(game):
    global result
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i-1])
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            spare_or_strike(game, i)
        if game[i].lower() == 'x' or in_first_half is False:
            in_first_half = True
            frame += 1
        else:
            in_first_half = False
    return result


def spare_or_strike(game, i):
    global result
    next_value = get_value(game[i+1])
    if game[i] == '/':
        result += next_value
    elif game[i].lower() == 'x':
        result += next_value
        if game[i+2] == '/':
            result += 10 - next_value
        else:
            result += get_value(game[i+2])
    return result


def get_value(char):
    pins_down = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    if char in pins_down:
        return int(char)
    elif char.lower() == 'x':
        return 10
    elif char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()
