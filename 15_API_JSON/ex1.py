import requests

# Sending a GET request
response_get = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print("GET Response Status Code:", response_get.status_code)
print("GET Response Body:", response_get.text)
print()

# Sending a POST request
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response_post = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)
print("POST Response Status Code:", response_post.status_code)
print("POST Response Body:", response_post.text)
print()

# Sending a PUT request
data = {'title': 'foo', 'body': 'bar', 'userId': 1}
response_put = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=data)
print("PUT Response Status Code:", response_put.status_code)
print("PUT Response Body:", response_put.text)
print()

# Sending a DELETE request
response_delete = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print("DELETE Response Status Code:", response_delete.status_code)
print("DELETE Response Body:", response_delete.text)
