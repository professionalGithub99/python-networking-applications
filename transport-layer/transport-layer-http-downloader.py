import sys, socket
#The purpose fo this script is to use sockets in order to get a webpage. 
try:
    rfc_number=int(sys.argv[1])
except (IndexError,ValueError):
    print('Must supply an RFC number as first argument')
    sys.exit(2)
host = 'www.ietf.org'
port = 80
sock = socket.create_connection((host,port))
req = (
 'GET /rfc/rfc2423.txt HTTP/1.1\r\n'
 'Host: {host}\r\n'
 'User-Agent: Python/{version}\r\n'
 'Connection: close\r\n'
 '\r\n'
)
req = req.format(
 host=host,
 version=sys.version_info[0]
)
print(req)
print(type(req))
sock.sendall(req.encode('ascii'))
rfc_raw = bytearray()
while True:
    buf = sock.recv(4096)
    if not len(buf):
        break
    rfc_raw += buf
rfc = rfc_raw.decode('utf-8')
print(rfc)
