import subprocess

#subprocess.run(['ls', '-al'])

r = subprocess.run('ls -la', shell=True)
print(r.returncode)



p1 = subprocess.Popen(['ls', '-al'], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ['grep', '102.py'], stdin=p1.stdout, stdout=subprocess.PIPE)

p1.stdout.close()
output = p2.communicate()[0]
print(output)