import os

print(os.path.exists('test.txt'))
print(os.path.isfile('test.txt'))
print(os.path.isdir('test.txt'))


os.symlink('test.txt', 'symlink.txt')