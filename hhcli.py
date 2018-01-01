import argparse
import os

usage_example = f'f.e.: %(prog)s -v -p qV3L1 -l x@mail.ru 2afec5ecff8715d80111ede9384315944e'

class MyFormatter(argparse.HelpFormatter):
    def __init__(self, prog):
        super(MyFormatter,self).__init__(prog, max_help_position=45)


def get_args():    
    parser = argparse.ArgumentParser(description='Updates your CV at HH',
                                     formatter_class=MyFormatter,
                                     epilog=usage_example)

    parser.add_argument('ID', 
                         metavar='CV_ID',
                         nargs='+',
                         help='an identificator(or multiple ids) for your CV ')

    parser.add_argument('-p','--password', 
                         dest='password', 
                         metavar='PASSWD',
                         required=True, 
                         help='your password for HH')

    parser.add_argument('-l','--login', 
                         dest='login', 
                         metavar='LOGIN',
                         required=True,
                         help='your login (Email or phone number)')

    parser.add_argument('-v','--verbose',
                         dest='verbose', 
                         action='store_true',
                         help='output logs to stdout')

    parser.add_argument('-f','--logfile', 
                         dest='logfilename', 
                         metavar='FILENAME',
                         #default='/tmp/update_cv.log',
                         help='log to a specified file')

    parser.add_argument('-u','--url', 
                         dest='url', 
                         metavar='URL',
                         default='https://hh.ru',
                         help='url to hh.ru f.e. https://sochi.hh.ru')

    return parser.parse_args()


