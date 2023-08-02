import requests

url = 'https://www.ibm.com/'
r = requests.get(url)

# print(r)
# print(r.status_code)
# print("Request Header", r.request.headers)
# print("Request Body", r.request.body)
# print(r.headers["Date"])
# print(r.headers['Content-Type'])
 
# print(r.encoding)
# print(r.text[0:1000])


url2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'

r2 = requests.get(url2)

# print(r2)
# print(r2.status_code)
# print("Request Header", r2.request.headers)
# print("Request Body", r2.request.body)
# print(r2.headers["Date"])
# print(r2.headers['Content-Type'])
# print(r2.encoding)


# ****************Get Request with URL Parameters**************

url_get='http://httpbin.org/get'
payload={"name":"Joseph","ID":"123"}
r_get=requests.get(url_get,params=payload)

# print(r_get.status_code)
# printr("GET request URL: ", r_get.url)
# print("request body:", r_get.request.body)
# print(r_get.text)
# print(r_get.headers['Content-Type'])

# print(r_get.json())
# print(r_get.json()['args'])


# *********************************Post Requests********************
url_post='http://httpbin.org/post'
payload_post={"name":"John","ID":"456"}
r_post=requests.post(url_post,data=payload_post)

# print("POST request URL:",r_post.url )
# print("POST request body:",r_post.request.body)
# print(r_post.json()['form'])