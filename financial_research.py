import pandas as pd


def read_csv(file):
    df = pd.read_csv(file, converters={'Adj Close': float}) 
    df = df['Adj Close']
    return df.tolist()


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

    return result


def calc_profit(data, signal):
    pos = 0
    entry = 0
    total  = 0
    for i in range(len(data)):
        if signal[i] == 1:
            if pos == 0:
                entry = data[i]
            elif pos == -1:
                profit = entry - data[i]
                total += profit
                entry = data[i]
            pos = 1
        elif signal[i] == -1:
            if pos == 0:
                entry = data[i]
            elif pos == 1:
                profit = data[i] - entry
                total += profit
                entry = data[i]
            pos = -1

    return total * 1000


def main():
    data = read_csv('2330.csv')
    signal = three_days(data)
    total = calc_profit(data, signal)
    print(total)


main()