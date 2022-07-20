# SMSPAM - Python
Python3.8*

> ### installing requirements
```
$ pip install -r requirements.txt
```



## How To Use
```
python3 main.py
```

## Apis.Json Format
```
URL:[ METHOD , BODY , SAMETIME_RETRIES , SUCCESSFUL_RESPONSE , CUSTOM_HEADERS ]
```

> URL: Url Address

> METHOD: "POST", "GET", "OTHER"

> BODY: null, json{} or string

> SAMETIME_RETRIES: 1+

> SUCCESSFUL_RESPONSE: some String that only is in successful request response

> CUSTOM_HEADERS: null(Random Hedaer) or json{}

> `$PHONE: You can Put $PHONE in Url, Headers, Body if Needed`

`$PHONE` Allways starts With 9 example: 910-000-0000

`Header` and **Body** Can be null


## About Apis.Json
- You can add more websites easily


## Features
- [ ] Adding Proxylist Handling
- [ ] Adding Threads(Speed)
