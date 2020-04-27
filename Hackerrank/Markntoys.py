'''
Mark and Jane are very happy after having their first child. Their son loves toys, so Mark wants to buy some. There are a number of different toys lying in front of him, tagged with their prices. Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money.

Given a list of prices and an amount to spend, what is the maximum number of toys Mark can buy? For example, if  and Mark has  to spend, he can buy items  for , or  for  units of currency. He would choose the first group of  items.

Function Description

#Complete the function maximumToys in the editor below. It should return an integer representing the maximum number of toys Mark can purchase.

maximumToys has the following parameter(s):

prices: an array of integers representing toy prices
k: an integer, Mark's budget

#Input Format
The first line contains two integers,  and , the number of priced toys and the amount Mark has to spend.
The next line contains  space-separated integers 

#Constraints
A toy can't be bought multiple times.

#Output Format

An integer that denotes the maximum number of toys Mark can buy for his son.
'''

def maximumToys(prices, k):
    # sort prices
    prices.sort()
    # num toys to buy
    num_toys_to_buy = 0
    # total so far
    total_so_far = 0
    # iterate over toys
    for toy in prices:
        #total so far inc by current price
        total_so_far += toy
        # check total so far exceeds > k:
        if total_so_far <= k:
            # toys to buy inc 1
            num_toys_to_buy += 1
        # else
        else:
            # return num toys to buy
            return num_toys_to_buy

if __name__ == "__main__":
    k = (50)
    prices = (1, 12, 5, 111, 200, 1000, 10)
    print(maximumToys)
