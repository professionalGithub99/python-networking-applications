from urllib.request import Request,urlopen,build_opener,HTTPCookieProcessor
from urllib.parse import quote,urlencode
from  http.cookiejar import FileCookieJar,CookieJar
from FileCookieJarExt import FileCookieJarExt
import webbrowser
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
req=Request("https://www.github.com",headers=agent,method='GET')
res=urlopen(req)
print(res.status)
print(res.getheader('Set-Cookie'))
print(req.headers)
print(len(res.read()))
file_cookie_jar=FileCookieJarExt()
cookie_res=build_opener(HTTPCookieProcessor(file_cookie_jar))
cookie_res.open(req)
print(file_cookie_jar)
print(file_cookie_jar.filename)
file_cookie_jar.save('TestFile.txt')
