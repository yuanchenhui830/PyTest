'''
Created on 2017��9��11��

@author: YCH
'''
from wsgiref.simple_server import make_server
httpd = make_server("127.0.0.1",33003)
httpd.serve_forever