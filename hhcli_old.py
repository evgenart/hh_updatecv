def print_usage(scriptname):
    print(f'Usage: \n{scriptname} --login LOGIN --password PASSWORD --id CV_ID --url URL\n'
           'Options: --login      Your login (for hh.ru it is Email or phone number)\n'
           '                      *tested only for Email\n'
           '         --password   Your password\n'
           '         --id         Identificator for Your CV\n'
           '         --url        URL to hh.ru f.e. https://sochi.hh.ru\n'
           '                      *tested only for https://sochi.hh.ru and https://hh.ru\n'
           '\n'
           '*Spaces and quotation mark signs aren`t allowed in the parameters\n')


def get_args(argv):
    if argv is None or not argv:
        print('smth so wrong, argv in get_args (hhcli.py) is empty or None')
        exit(1)
    scriptname = argv[0].split('\\')[-1]
    if len(argv) == 2 and argv[1] == '--help':
        print_usage(scriptname)
        exit(0)
    if len(argv) != 9:
        print_usage(scriptname)
        exit(1)
    argstr  = ' '.join(argv[1:])
    arglst  = argstr.split(' --')
    arglst[0] = arglst[0].replace('--','')
    argdict = dict(( kv.split(' ') for kv in arglst ))
    if ('login'    in argdict and
        'password' in argdict and
        'id'       in argdict):
        return argdict['login'], argdict['password'], argdict['id'], argdict['url']
    else:
        print_usage(scriptname)
        exit(1)

