#!/usr/bin/python3.6
import requests
import sys
from hhaux import get_xsrf
from hhaux import login_dir, update_cv_dir
from hhaux import logger
from hhaux import common_headers, cv_headers
from hhaux import login_data, cv_data
from hhcli import get_args

def main():
    #login, password, cv_id, url = get_args(sys.argv)
    args = get_args()
    logger.config(verbose=args.verbose,
                  logfilename=args.logfilename)
    logger.start_msg()
    update_cv(args.login, args.password, args.ID, url=args.url)
    logger.end_msg()


def update_cv(login, password, cv_ids, url='https://hh.ru'):
    with requests.Session() as session:
        req = session.get(url, headers = common_headers) 
        xsrf = get_xsrf(req.headers)
        req = session.post(url + login_dir, 
                           data    = login_data(url, login, password, xsrf),
                           headers = common_headers)
        for cv_id in cv_ids:
            req = session.post(url + update_cv_dir,
                               data    = cv_data(cv_id),
                               headers = cv_headers(url, cv_id, xsrf))
            if req.status_code != 200:
                logger.log_error_code(req.status_code, cv_id=cv_id)
            else:
                logger.log_success(cv_id)


if __name__ == '__main__':
    main()
