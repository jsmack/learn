# カプセル(encapsulation)

def casino_entrance(age, min_age=21):
    if age < min_age:
        print(f"Under the age of {min_age} are not allowed to enter the casino")
        return

    def inner_casino_entrance():
        print("Welcome to casino")


    return inner_casino_entrance()


casino_entrance(28)