count = 0

while count < 10:
    print(count)
    count += 1

while True:
    age = int(input("Please input your age?: "))
    if not 0 <= age <= 120:
        print("The age entered is invalid.")
        continue
    else:
        print(f"You enterd age is { age }")
        break

games = {1: "rulet", 2: "blackjack", 3: "porker"}
while True:
    game = int(input("Please input game you want to play : "))
    if min(games) <= game <= max(games):
        print(f'You choie game is { games[game] }')
        break
    else:
        print(f'Please input a valied game code: { min(games) } - { max(games) }')
        continue