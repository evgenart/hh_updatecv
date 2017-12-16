hh_updatecv is a cross platform Python script to update your CV at hh.

You will probably need to change she-bang in hh_updatecv.py file for your system.

# Example Usage

```
hh_updatecv.py --login vasya@yandex.ru --password asfd2qwredpoi230fk0 --id 839faea0342449de430039ed99e24842446268 --url https://hh.ru

```

# Help message
```
Usage:
hh_updatecv.py --login LOGIN --password PASSWORD --id CV_ID --url URL
Options: --login      Your login (for hh.ru it is Email or phone number)
                      *tested only for Email
         --password   Your password
         --id         Identificator for Your CV
         --url        URL to hh.ru f.e. https://sochi.hh.ru
                      *tested only for https://sochi.hh.ru

*Spaces and quotation mark signs aren`t allowed in the parameters

```

# Logging
hh_updatecv loggs its execution by default:
```
[16.12.2017 15:11] hh.py: started
[16.12.2017 15:11] hh.py: finished
```
Error message from server:
```
[16.12.2017 15:31] hh.py: started
[16.12.2017 15:31] hh.py: Server responded with code != 200 OK, the code is: 409
[16.12.2017 15:31] hh.py: finished

```

# TO-DO
* Add --verbose to enable logging
* Use https://hh.ru by default
* Add some kind of encryption for login/password
* Catch errors if not loged in and if server is unavailable