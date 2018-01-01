#!/usr/bin/python3.6
import requests
import sys
from hhaux import get_xsrf
from hhaux import login_dir, update_cv_dir
from hhaux import log_start, log_end, log_error_code
from hhaux import common_headers, cv_headers
from hhaux import login_data, cv_data
from hhcli_old import get_args

def main():
    log_start()
    login, password, cv_id, url = get_args(sys.argv)
    update_cv(login, password, cv_id, url)
    log_end()


def update_cv(login, password, cv_id, url):
    with requests.Session() as session:
        req = session.get(url, headers = common_headers) 
        xsrf = get_xsrf(req.headers)
        req = session.post(url + login_dir, 
                           data    = login_data(url, login, password, xsrf),  
                           headers = common_headers)
        req = session.post(url + update_cv_dir, 
                           data    = cv_data(cv_id),
                           headers = cv_headers(url, cv_id, xsrf)) 
        if req.status_code != 200:
            log_error_code(req.status_code)


if __name__ == '__main__':
    main()
