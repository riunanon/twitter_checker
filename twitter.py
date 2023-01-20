import requests
def email_check(email):
    url='https://api.twitter.com/i/users/email_available.json?email='+email
    response=requests.get(url).json()
    if response['valid']:
        return True
    else:
        return False

def username_check(username):
    url='https://api.twitter.com/i/users/username_available.json?username='+username
    response=requests.get(url).json()
    if response['valid']:
        return True
    else:
        return False

def phonenumber_check(phonenumber):
    url='https://api.twitter.com/i/users/phonenumber_available.json?phonenumber='+phonenumber
    response=requests.get(url).json()
    if response['valid']:
        return True
    else:
        return False