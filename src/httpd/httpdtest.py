'''
Created on 2017Äê9ÔÂ11ÈÕ

@author: YCH
'''
from wsgiref.simple_server import make_server
httpd = make_server("127.0.0.1",33003)
httpd.serve_forever