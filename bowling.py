def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == '/':
            result += 10 - get_value(game[i-1])
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            next_score = get_value(game[i+1])
            if game[i] == '/':
                result += next_score
            elif game[i].lower() == 'x':
                result += next_score
                if game[i+2] == '/':
                    result += 10 - next_score
                else:
                    result += get_value(game[i+2])
        if in_first_half is True:
            in_first_half = False
        else:
            in_first_half = True
            frame += 1
        if game[i].lower() == 'x':
            in_first_half = True
            frame += 1
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
