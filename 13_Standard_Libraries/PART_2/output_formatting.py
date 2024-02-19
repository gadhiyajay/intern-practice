from urllib import request
response = request.urlopen("https://jsonplaceholder.typicode.com/users")
json_response = response.read()
import json
users = json.loads(json_response)

# print(users)
#
# print("******************")
#
# for user in users:
#     print(user)
#
# print("******************")

from pprint import pprint, pp

pprint(users[2])
print("***********************************************")
pp(users)