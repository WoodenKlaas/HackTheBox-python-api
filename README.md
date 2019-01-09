# HackTheBox-python-api
This API is still in development, because not all of HackTheBox' api is exposed

# Usage

## Initialization
```
import hackthebox

API_TOKEN = '1234'
HTB = hackthebox.HackTheBox(API_TOKEN)
```

## Getting a user id from username
To use this functionality, you need to initialize with your API token
```
import hackthebox

API_TOKEN = '1234'
HTB = hackthebox.HackTheBox(API_TOKEN)
user_id = HTB.get_user_id('QHpix')


```

## Get the top X
You can get a top10, top50, top100, etc.
The maximum is top100
```
import hackthebox

API_TOKEN = '1234'
HTB = hackthebox.HackTheBox(API_TOKEN)

top10 = HTB.get_top(10)
top50 = HTB.get_top(50)
```

## Get the total of machines
```
import hackthebox

API_TOKEN = '1234'
HTB = hackthebox.HackTheBox(API_TOKEN)

machines = HTB.get_machines_total()
```

## Get owns
```
import hackthebox

API_TOKEN = '1234'
HTB = hackthebox.HackTheBox(API_TOKEN)

roots = HTB.get_owns('roots')
users = HTB.get_owns('users')
```

## Get machine status
```
import hackthebox

API_TOKEN = '1234'
HTB = hackthebox.HackTheBox(API_TOKEN)

vpn = '1'
machine_id = 3
status = HTB.get_status(vpn, machine_id)
```

