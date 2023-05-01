
#################### gitlab.bandit.B611
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

def get_older_models(age):
    query = "SELECT * FROM myapp_mymodel WHERE age >= %d" % age
    return MyModel.objects.raw(query)


############### gitlab.bandit.B610
from django.db.models import F
from myapp.models import MyModel

MyModel.objects.filter(foo__lt=42).extra(where=["bar = %s"], params=[42])



######### gitlab.bandit.B602
print('hello')
import subprocess
output = subprocess.check_output(f"nslookup2 {my_domain}", shell=True, encoding='UTF-8')


############# gitlab.bandit.B413
import pycrypto


########### gitlab.bandit.B412
import wsgiref.handlers

def my_app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b'Hello, World!']

wsgiref.handlers.CGIHandler().run(my_app)


########## gitlab.bandit.B401
import telnetlib
telnetlib.Telnet('localhost', 23)


######## gitlab.bandit.B313.B314.B315.B316.B318.B319.B320.B405.B406.B407.B408.B409.B410
import xml.etree.ElementTree as ET

xml_string = "<root><user>John</user></root>"
tree = ET.fromstring(xml_string)


