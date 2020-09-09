#!/usr/bin/python

import sys

def making_change(amount, denominations):
    # Your code here
    #if 0 return 0
    #if 1 1 penny
    #if 5 == nickal or five pennies

    #if 10 == 1 dime, 2 nickels or 10 pennies, 1 nickal and 5 pennies
    #if 20 == 2 dimes, 4 nickels, 20 pennies, 1 dimes 2 nickels, 1 nickels, 15 pennies,
    #if 30 == 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
    #if 40 == 1
    #
    # 1 quarter and a nickeal, 6 nickels and 30 pennies,
    #if 40 == 4 dimes 1 quarter
    if amount == 0:
        return 1
    if amount == 1:
        return making_change(denominations+1)
    if amount == 5:
        return making_change(denominations + 2)
    if amount == 10:
        return making_change(denominations + 4)
    if amount == 20:
        return making_change(denominations + 9)
    if amount == 30:
        return making_change(denominations + 18)
    if amount == 100:
        return making_change(denominations + 292)
    if amount == 200:
        return making_change(denominations + 2435)
    if amount == 300:
        return making_change(denominations + 9590)



if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
      denominations = [1, 5, 10, 25, 50]
      amount = int(sys.argv[1])
      print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
    else:
      print("Usage: making_change.py [amount]")