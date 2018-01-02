import os
from time import localtime, strftime


common_headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
                   'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate, br',
                   'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
                   'Connection':'keep-alive',
                   'DNT':'1' 
                 }


login_dir = '/account/login?backurl=%2F'
update_cv_dir = '/applicant/resumes/touch'


def now():
    return strftime('%d.%m.%Y %H:%M', localtime())


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class Logger(object):
    def __init__(self):
        self.verbose = None
        self.logfilename = None


    def config(self, verbose=False, logfilename=None):
        self.verbose = verbose
        if logfilename:
            self.logfilename = self.__preplogfile(logfilename)


    def __log(self, text):
        if self.verbose:
            print(text)
        if self.logfilename is not None:
            with open(self.logfilename, 'a+') as f:
                print(text, file=f)


    def __preplogfile(self, filename):
        ''' __preplogfile creates directories recursively if needed'''
        filelocation = os.path.dirname(filename)
        if filelocation:
            os.makedirs(filelocation, exist_ok=True)
        # if directory doesn't exist, the method makedirs creates it.
        return filename


    def start_msg(self):
        self.__log(f'[{now()}] hh_updatecv: Started')


    def end_msg(self):
        self.__log(f'[{now()}] hh_updatecv: Finished')


    def log_error_code(self, code, cv_id=''):
        self.__log(f'[{now()}] hh_updatecv: ERROR, CV_ID = {cv_id}, HTTP STATUS CODE: {code}')


    def log_success(self, cv_id):
        self.__log(f'[{now()}] hh_updatecv: Updated CV, CV_ID = {cv_id}')


def prep_headers(new_headers):
    return {**common_headers, **new_headers}


def get_xsrf(headers):
    xsrf = headers['Set-Cookie']
    xsrf = xsrf.split(' ')
    xsrf = xsrf[0][6:-1] # I think there is better way 
    return xsrf


def login_data(url, login, password, xsrf):
    return {'username' : login,
            'password' : password,
            'backUrl'  : f'{url}/',
            '_xsrf'    : xsrf,
            #'remember' : 'yes',  # try to clear this field
            'action'   : 'Войти'} 


def cv_data(cv_id):
    return {'resume':cv_id, 'undirectable':'true'}


def cv_headers(url, cv_id, xsrf):
    update_cv_headers = {'X-Xsrftoken':xsrf,
                         'X-Requested-With':'XMLHttpRequest',
                         'Referer': f'{url}/applicant/resumes/{cv_id}'}
    return prep_headers(update_cv_headers)


if __name__ != '__main__':
    logger = Logger()