import pandas as pd
import matplotlib.pyplot as plt


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
    trades = []
    for i in range(len(data)):
        if signal[i] == 1:
            if pos == 0:
                entry = data[i]
            elif pos == -1:
                profit = entry - data[i]
                trades.append(profit)
                entry = data[i]
            pos = 1
        elif signal[i] == -1:
            if pos == 0:
                entry = data[i]
            elif pos == 1:
                profit = data[i] - entry
                trades.append(profit)
                entry = data[i]
            pos = -1

    return trades


def calc_equity(trades):
    equities = []
    equity = 0
    for trade in trades:
        equity += trade
        equities.append(equity)
    return equities


def graph_equity(equity):
    plt.plot(equity)
    plt.ylabel('equity')
    plt.xlabel('trades')
    plt.show()


def main():
    data = read_csv('2330.csv')
    signal = three_days(data)
    trades = calc_profit(data, signal)
    total = sum(trades) * 1000
    print('總共損益為', total)
    print('一共有', len(trades), '筆交易')
    equity = calc_equity(trades)
    graph_equity(equity)


main()