hh_updatecv is a cross platform Python script to update your CV at hh.

You will probably need to change she-bang in `updatecv.py` file for your system.

# Example Usage

```
updatecv.py -l vasya@yandex.ru -p asfd2qwredpoi230fk0 -f hh_cv.log 01fe3fecabcd51582300def41f575631fh4b00 9abcf677f018513860afbcef1f6a6b00565a76

```

# Example Usage in cron
```
01  9 * * * bash -c 'cd ~ && source .bashrc && cat hh_cvs.txt | xargs -d "\n"  hh_updatecv/updatecv.py -l vasya@yandex.ru -p asfd2qwredpoi230fk0 -f ~/log_hh.txt'
# Where hh_cvs.txt contains all CV_IDs (one by line)
```

# Help message
```
usage: updatecv.py [-h] -p PASSWD -l LOGIN [-v] [-f FILENAME] [-u URL]
                   CV_ID [CV_ID ...]

Updates your CV at HH

positional arguments:
  CV_ID                            an identificator(or multiple ids) for your
                                   CV

optional arguments:
  -h, --help                       show this help message and exit
  -p PASSWD, --password PASSWD     your password for HH
  -l LOGIN, --login LOGIN          your login (Email or phone number)
  -v, --verbose                    output logs to stdout
  -f FILENAME, --logfile FILENAME  log to a specified file
  -u URL, --url URL                url to hh.ru f.e. https://sochi.hh.ru
```

# Logging
updatecv.py can log its execution:
```
[16.12.2017 15:11] hh_updatecv: Started
[16.12.2017 15:11] hh_updatecv: Finished
```
Error message from server:
```
[01.01.2018 15:49] hh_updatecv: Started
[01.01.2018 15:49] hh_updatecv: ERROR, CV_ID = 01fe3fecabcd51582300def41f575631fh4b00, HTTP STATUS CODE: 409
[01.01.2018 15:49] hh_updatecv: ERROR, CV_ID = 9abcf677f018513860afbcef1f6a6b00565a76, HTTP STATsUS CODE: 409
[01.01.2018 15:49] hh_updatecv: Finished

```

# TO-DO
* Catch errors if not loged in and if server is unavailable
* Add some kind of encryption for login/password
