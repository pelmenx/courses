# Good morning! Here's your coding interview problem for today.
#
# This problem was asked by Facebook.
#
# Given a array of numbers representing the stock prices of a company in
# chronological order, write a function that calculates the maximum profit you
# could have made from buying and selling that stock once. You must buy before you
# can sell it.
#
# For example, given [9, 11, 8, 5, 7, 10], you should return 5, since you could
# buy the stock at 5 dollars and sell it at 10 dollars.
#
#
# --------------------------------------------------------------------------------
#
#
def maximum_profit(array):
    max_profit = 0
    min_cost = array[0]
    for i in range(1, len(array)):
        if array[i] < min_cost:
            min_cost = array[i]
        else:
            if array[i] - min_cost > max_profit:
                max_profit = array[i] - min_cost
    return max_profit


print(maximum_profit([9, 11, 8, 5, 7, 10]))
