import requests
payload_dict={'email':'daddykjs222k@gmail.com','password':'aDK1!kdsj','day':'01','month':'91','year':'1981'}
headers={'Content-Type':'application/x-www-form-urlencode;charset=UTF-8','User-Agent':'Mozilla/5.0 (X11; Linux i686; rv:84.0) Gecko/20100101 Firefox/84.0'}
#r=requests.post('https://secure.runescape.com/m=account-creation/create_account',data=payload_dict,headers=headers)
r=requests.get('https://secure.runescape.com/m=account-creation/create_account')
print(r.content)
print(r.status_code)
print(r.headers)
print(r.url)
#print(urlunparse((netloc,"",path,"",query_dict)))
