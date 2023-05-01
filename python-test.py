# gitlab.bandit.B411
# Python.Lang.Security.Use-Defused-Xmlrpc.Use-Defused-Xmlrpc
import xmlrpclib

# gitlab.bandit.B323 
# Python.Lang.Security.Unverified-Ssl-Context.Unverified-Ssl-Context
context = ssl._create_unverified_context()

# gitlab.bandit.B501
# Python.Requests.Security.Disabled-Cert-Validation.Disabled-Cert-Validation
import requests
response = requests.get('https://insecure-server.com', verify=False)

# gitlab.bandit.B602
# Python.Lang.Security.Audit.Subprocess-Shell-True.Subprocess-Shell-True
print('hello')
import subprocess
output = subprocess.check_output(f"nslookup2 {my_domain}", shell=True, encoding='UTF-8')

# gitlab.bandit.B313.B314.B315.B316.B318.B319.B320.B405.B406.B407.B408.B409.B410
# Python.Lang.Security.Use-Defused-Xml.Use-Defused-Xml

import xml.etree.ElementTree as ET

xml_string = "<root><user>John</user></root>"
tree = ET.fromstring(xml_string)
