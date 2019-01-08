# HackTheBox-python-api
This API is still in development, because not all of HackTheBox' api is exposed

# Usage

## Initialization
```
import hackthebox

api_token = '1234'
HTB = hackthebox.HackTheBox(api_token)
```

## Getting a user id from username
To use this functionality, you need to initialize with your API token
```
import hackthebox

api_token = '1234'
HTB = hackthebox.HackTheBox(api_token)
user_id = HTB.get_user_id('QHpix')


```

## Get the top X
You can get a top10, top50, top100, etc.
The maximum is top100
```
import hackthebox

api_token = '1234'
HTB = hackthebox.HackTheBox(api_token)

top10 = HTB.get_top(10)
top50 = HTB.get_top(50)
```

## Get the total of machines
```
import hackthebox

api_token = '1234'
HTB = hackthebox.HackTheBox(api_token)

machines = HTB.get_machines_total()
```
