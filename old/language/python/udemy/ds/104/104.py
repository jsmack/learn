import string
import csv
import operator
import os

RECOMMEND_FILE = 'recommend.csv'
FIELD_NAMES = ['Restaurant', 'Count']
NAME_ROBO = "hogehoge"

csv_exists = os.path.isfile(RECOMMEND_FILE)

with open(RECOMMEND_FILE, 'a') as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=FIELD_NAMES)
    if not csv_exists:
        writer.writeheader()

    reader = csv.DictReader(csv_file)
    csv_sorted = sorted(reader, key=operator.itemgetter(1))
    print(csv_sorted)
    welcome_str = """
    -----------------------------------------------------------------
    Hello. I am $name_robo. Who are you?
    -----------------------------------------------------------------
    """
    welcome_template = string.Template(welcome_str)
    welcome = welcome_template.substitute(name_robo=NAME_ROBO)

    restaurant_str = """
    -----------------------------------------------------------------
    Hi $name_input. which restaurants  do you like?
    -----------------------------------------------------------------
    """

    goodbye_str = """
    -----------------------------------------------------------------
    $name_robo: $name_input. thank you so much.
    $name_robo: Have a nice day!
    -----------------------------------------------------------------
    """

    print(welcome)

    name_input = input()
    print(name_input)

    restaurant_template = string.Template(restaurant_str)
    restaurant = restaurant_template.substitute(name_input=name_input)
    print(restaurant)

    restaurant_input = input()
    print(restaurant_input)


    goodbye_template = string.Template(goodbye_str)
    goodbye = goodbye_template.substitute(name_robo=NAME_ROBO, name_input=name_input)
    print(goodbye)

    writer.writerow({'Restaurant': restaurant_input, 'Count': 1})
