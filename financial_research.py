def three_days(data):
    last = data[0]
    big = 0
    small = 0
    result = []

    for d in data:
        if d > last:
            small = 0
            big += 1
            if big >= 3:
                result.append(1)
            else:
                result.append(0) 
        elif d < last:
            big = 0
            small -= 1
            if small <= -3:
                result.append(-1)
            else:
                result.append(0)
        else:
            big = 0
            small = 0
            result.append(0)
        last = d

    return(result)

data = [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368] #[0, 0, 0, 1, 1, 1, 0, 0]
print(three_days(data))