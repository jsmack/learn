
try:
    from lesson import utils
except ImportError:
    print('ImportError')
    from lesson.tools import utils
utils.say_twice('word')

