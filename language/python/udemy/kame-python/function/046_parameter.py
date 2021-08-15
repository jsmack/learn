def func(first, second, third=3):
    print(f"first: {first}, second: {second}, third: {third}")

# argument -> parameter
func("1", "2", "3")
# first: 1, second: 2, third: 3

func("1", third="3", second="2")
# first: 1, second: 2, third: 3

func("1", "2")
# first: 1, second: 2, third: 3

func("1", "2", "33")
# first: 1, second: 2, third: 33

