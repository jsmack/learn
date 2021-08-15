age = int(input("How old are you?: "))
casino_age = 18

game_dict = {1: 'roulette', 2: 'blackjack', 3: 'porker'}

if age >= casino_age:
    print('Welcome to casio!')
    while True:
        print('Select the game you want to play.')
        for num, game_name in game_dict.items():
            print(f'{num}: {game_name}')
        game = int(input(':'))

        if game in game_dict.keys():
            print(f'You choiced {game_dict[game]}')
            break
        else:
            print(f'{game} invalid numeric.')
            continue
else:
    print(f'You must be {casino_age} years old to enter the casino')