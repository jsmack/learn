fruits = ['apple', 'peach', 'grapes', 'banana']

for fruit in fruits:
    print(fruit)
else:
    print("The loop has turned around.")


balance = 1000
game_price = 200

while balance >= game_price:
    choice = input(f"Would you like to participate out in the {game_price} games?(Balance{balance} yen) (y/n)?: ")
    if choice == 'y':
        balance -= game_price
    elif choice == 'n':
        print("Let's play again.")
        break
    else:
        print("Please enterd y or n.")
else:
    print(f'Your balance is {balance} yen. You are out of money.')
