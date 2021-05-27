import requests


data= {"nm": "chad",
    "addr": "the moon",
        "city": "chicago",
            "pin": "1234"}


requests.post("http://10.0.196.93:2224/addrec", data)
