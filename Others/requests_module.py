# pip install requests
import requests

try:
    req = requests.get('https://xkcd.com/353',)
    print(dir(req))
except Exception :

    print(Exception)


# req = requests.get('https://httpbin.org/delay/3', timeout=2)
# print(req)

# get request

# req = requests.get('https://httpbin.org/basic-auth/Tushar/12', auth=('Tushark', 12))
# print(req.text)

# post request

# payload = {'username': 'Tushar', 'password': 'test123'}
#
# req = requests.post('https://httpbin.org/post', data=payload)
# req_dict = req.json()
# print(req_dict['headers'])
# print(req.json())


# payload = {'page': 2, 'count': 25}
# x = requests.get('https://httpbin.org/get', params=payload)
# print(req.url )
# print(req.text)

# req = requests.get('https://xkcd.com/353',)
# print(req)
# # with open('comics.png', 'wb') as file:
# #     file.write(x.content)
#
# print(x.text)
