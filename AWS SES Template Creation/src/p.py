import json
import os
add='admin_add_user'
json_source ='src/SubjectBody/'
# json_source +=add
# print(json_source)
add+='.json'
path = os.path.join(json_source, add)

print(path)

# with open ('src/SubjectBody/admin_add_user.json','r') as f:
with open (path,'r') as f:
    data = json.load(f,strict=False)
print(data['admin_add_user']['subject'])
