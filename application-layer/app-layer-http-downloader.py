import sys, urllib.request
def print_req_body(body):
    for i in body:
        print(i)
    
try: 
    #Choose the rfc number to put into url
    rfc_number=int(sys.argv[1])
    template='http://www.ietf.org/rfc/rfc{}.txt'
    url=template.format(rfc_number)
    #this urllib reads a url returns httpresponse and reads the body
    rfc_raw=urllib.request.urlopen(url).read()
    #Printing out an http header response
    rfc_header=urllib.request.urlopen(url).getheaders()
    rfc=rfc_raw.decode()
    #print_req_body(rfc)
    print(urllib.request.urlopen(url).read().decode())
    print(type(urllib.request.urlopen(url)),'type')
    print(type(rfc_raw),"type")
    print(type(rfc),"decoded type")
    #print(rfc)
    #print(rfc_header)
except(IndexError,ValueError):
    print('Please supply RFC Number as an argument')
    sys.exit(2)


