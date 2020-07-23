f = open('test.txt','a')
f.write('Test\n')
print('I am print', file=f)
print('My', 'name', 'is', 'Mike.', sep='#', end='!', file=f)
f.close()



