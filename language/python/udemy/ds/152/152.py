j = {
  "employee":
          [
            {"id":  111, "name":  "Mike"},
            {"id":  222, "name":  "Nancy"}
          ]
}

import json
print(j)
print("###########")
print(json.dumps(j))

a = json.dumps(j)
print("###########")

print(json.loads(a))
print("###########")

with open('test.json','w') as f:
    json.dump(j, f)


with open('test.json','r') as f:
    print(json.load(f))
