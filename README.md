# twittter_checker
Username and Email available checker.
```
$ git clone https://github.com/riunanon/twitter_checker.git
```
```py
from twitter_checker import twitter
   twitter.email_check('mail@example.com')
twitter.username_check('example')

#if response is 'True',it's availabel.
#if it's 'False', it is not available.
```
example
```py
response=twitter.email_check('test@example.com')
print(response)
#>>>True
if response:
    print('availabel!') #True
else:
    print('not availabel...') #False
#>>>availabel!
```