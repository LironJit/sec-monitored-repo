import tempfile
import ssl

# gitlab.bandit.B323
context = ssl._create_unverified_context()

# gitlab.bandit.B306
import tempfile
filename = tempfile.mktemp()

# gitlab.bandit.B611
from django.db import models
query = f"SELECT * FROM {my_table}"
result = MyModel.objects.raw(query)
raw_query = models.RawSQL('SELECT * FROM my_table WHERE id = %s', (some_id,))
results = MyModel.objects.filter(raw_query)

# gitlab.bandit.B501
import requests
response = requests.get('https://insecure-server.com', verify=False)

#gitlab.bandit.B610
from django.db import models
my_query = "SELECT * FROM my_table WHERE id = %s"
my_params = (some_id,)
MyModel.objects.filter(extra= { 'select': { 'my_field': my_query }, 'select_params': my_params })

# gitlab.bandit.B602
import subprocess
subprocess.call("rm -rf /", shell=True)

# gitlab.bandit.B506
import yaml
my_data = "---\n- foo\n- !!python/object/apply:os.system ['rm -rf /']\n"
my_obj = yaml.load(my_data)

# gitlab.bandit.B413
import Crypto
message = b"Hello, world!"
key = b"mysecretkey"
cipher = Crypto.Cipher.AES.new(key, Crypto.Cipher.AES.MODE_CBC)
encrypted_message = cipher.encrypt(message)

# gitlab.bandit.B412
import wsgiref.handlers
server = wsgiref.handlers.CGIHandler()
server.start()

# gitlab.bandit.B411
import xmlrpclib

# gitlab.bandit.B402
import ftplib
ftp = ftplib.FTP("example.com")
ftp.login("username", "password")
ftp.retrlines("LIST")
ftp.quit()

# gitlab.bandit.B401
import telnetlib
tn = telnetlib.Telnet('example.com', 23)
tn.write(b'username\n')
tn.write(b'password\n')

# gitlab.bandit.B313.B314.B315.B316.B318.B319.B320.B405.B406.B407.B408.B409.B410
import xml.etree.ElementTree as ET
tree = ET.parse('file.xml')
root = tree.getroot()

