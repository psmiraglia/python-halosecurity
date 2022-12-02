# HaloSecurity

Python library for interfacing with Halo Security platform API.

## How to install

~~~.sh
# init a virtual environment
$ virtualenv -p python3 .venv
$ . .venv/bin/activate

# install requirements
$ pip install -r requirements.txt
$ pip install -r requirements.dev.txt

# install the library
$ pip install -e .
~~~

## How to use

~~~.py

import json
from halosecurity import HaloSecurity

# obtain it from https://www.halosecurity.com/user/account/api
api_key = '***************************************'

with HaloSecurity(api_key=api_key) as api:
    for target in api.target.list(sort_desc=1):
        print(json.dumps(target, indent=2))

    for dns in api.dns.list():
        print(json.dumps(dns, indent=2))

    for port in api.port.list(port=22, state='open'):
        print(json.dumps(port, indent=2))
    
    for user in api.user.list(name='riccardo'):
        print(json.dumps(user, indent=2))

    try:
        target = api.traget.get(12345)
        data = target.get_data()
        print(json.dumps(data, indent=2))
        
        port = api.port.get(12345)
        data = port.get_data()
        print(json.dumps(data, indent=2))
    except Exception as e:
        print(f'Error: {e}')
~~~

## References

* [Halo Security API](https://docs.halosecurity.com/api/)
