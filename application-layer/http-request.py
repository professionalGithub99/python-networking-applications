from urllib.request import Request, urlopen
from http.cookiejar import CookieJar
from urllib.request import build_opener,HTTPCookieProcessor,BaseHandler
import gzip
from urllib.parse import urlparse,parse_qs,quote
cookie_jar=CookieJar()
req=Request("http://www.ietf.org/rfc/rfc2423.txt")
req.add_header('Accept-Encoding','gzip')
req.add_header('Accept','application/grjkjkjaphql')
response=urlopen(req)
print(type(gzip.decompress(response.read()).decode().splitlines()[:5]))
print(type(response))
open_url=build_opener(HTTPCookieProcessor(cookie_jar))
cookie_response=open_url.open("http://www.ietf.org/rfc/rfc2423.txt")
#print(cookie_response.getheaders())
second_cookie=list(cookie_jar)



req=Request("")
cookie_jar=CookieJar()
open_url=build_opener(HTTPCookieProcessor(cookie_jar))
open_url.open("http://www.gmail.com")
