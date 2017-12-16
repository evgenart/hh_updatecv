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


def log_start():
    print(f'[{now()}] hh.py: started')


def log_end():    
    print(f'[{now()}] hh.py: finished ')


def log_error_code(code):
    print(f'[{now()}] hh.py: Server responded with code != 200 OK, the code is: {code}')


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
            'backUrl'  : '{url}/',
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
