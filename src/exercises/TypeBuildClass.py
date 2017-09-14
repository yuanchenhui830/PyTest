Hello = type('Hello',(object,),dict(hello=lambda self,x,y:x * y))
h = Hello()
print(h.hello(2,3))