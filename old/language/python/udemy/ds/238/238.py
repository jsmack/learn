import json
import pprint

l = ['apple', 'orange', 'banana', 'peach', 'mango']
l.insert(0, l[:])
print(l)
pp = pprint.PrettyPrinter(indent=4, width=40, compact=True)
pp.pprint(l)

d = {'a': 'A', 'b': 'B', 'c': {'x': {'y': 'Y'}}}
pp2 = pprint.PrettyPrinter(
    indent=4
)
pp2.pprint(d)

print(json.dumps(l,indent=4))
print(json.dumps(d,indent=4))


from urllib.request import urlopen

with urlopen('https://pypi.org/pypi/Twisted/json') as url:
    http_info = json.load(url)['info']
    #raw_data = url.read().decode(http_info.get_content_charset())
    #print(raw_data)

#raw_data = json.loads(http_info)
#pprint.pprint(http_info)
print(json.dumps(http_info, indent=4))