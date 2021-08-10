# input is get user input data

CASINO_AGE = 18
GAME_TEXT = """ Please input game
1: rulet
2: backjack
3: porker
"""
game_dir = {1: "rulet", 2: "blackjack", 3:"porker"}

age = int(input("How old are you?: "))
print(f'You are {age} years old.')

if age >= CASINO_AGE:
    game = int(input(GAME_TEXT))

game = int(game)

print(f'You choice {game} = {game_dir[game]}')