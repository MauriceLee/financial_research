def three_days(data):
    info = []
    for i in range(len(data)):
        if i < 3:
            info.append(0)
        elif data[i] > data[i-1] > data[i-2] > data[i-3]:
            info.append(1)
        elif data[i] < data[i-1] < data[i-2] < data[i-3]:
            info.append(-1)
        else:
            info.append(0)
    return info
    
data = [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368]
print(three_days(data))