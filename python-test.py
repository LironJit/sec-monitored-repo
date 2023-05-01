# gitlab.bandit.B323 
# Python.Lang.Security.Unverified-Ssl-Context.Unverified-Ssl-Context
import ssl

context = ssl._create_unverified_context()

import ssl

context = ssl._create_unverified_context()
context = ssl._create_unverified_context()

import ssl

def create_context():
    return ssl._create_unverified_context()

context1 = create_context()
context2 = create_context()

import ssl

context = ssl._create_unverified_context()
response = requests.get("https://example.com", verify=context)
