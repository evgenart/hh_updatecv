import argparse
import os


def logfile(filename):
    ''' logfile returns file object and creates directories recursively if needed'''
    # simpler version of logfile is: argparse.FileType('a+'), 
    # but it does not check directories
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    # if directory doesn't exist, the method makedirs creates it.
    return open(filename, 'a+')


def get_args():    
    parser = argparse.ArgumentParser(description='Updates your CV at HH')
    parser.add_argument('id', 
                         dest='id', 
                         metavar='CV_ID',
                         action='append',
                         help='Identificator for Your CV')
    # append to store a list of CVs to update, default action is 'store'
    parser.add_argument('-p','--password', 
                         dest='password', 
                         metavar='PASSWD',
                         required=True, 
                         help='Your password for HH')

    parser.add_argument('-l','--login', 
                         dest='login', 
                         metavar='LOGIN',
                         required=True,
                         help='Your login (Email or phone number)')

    parser.add_argument('-v','--verbose',
                         dest='verbose', 
                         action='store_true',
                         help='Output logs to stdout')

    parser.add_argument('-f','--logfile', 
                         dest='logfile', 
                         metavar='FILENAME',
                         default='/tmp/update_cv.log',
                         type=logfile,
                         help='Logs to a specified file (/tmp/update_cv.log)')

    parser.add_argument('-u','--url', 
                         dest='url', 
                         metavar='URL',
                         default='https://hh.ru',
                         help='URL to hh.ru f.e. https://sochi.hh.ru')

    return parser.parse_args()


