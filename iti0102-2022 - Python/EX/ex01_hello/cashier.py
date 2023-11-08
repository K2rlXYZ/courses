"""EX01 Cashier."""

"""
4. Cashier
Example output:

Enter a sum: 64
Amount of coins needed: 6

"""
amount = int(input("Enter a sum: "))
number_of_coins = 0

coins = [50, 20, 10, 5, 1]

for coin in coins:
    number_of_coins += int(amount / coin)
    amount = amount % coin

print(f"Amount of coins needed: {number_of_coins}")
