#!/usr/bin/env python3
import argparse
import authenticate
from adaptor.adaptor import add_adaptor
from file_manager.file_manager import manager


# System Initialization
authenticate.initialize()
system_file_manager = manager()
system_file_manager.recover()

def get_info():
    tree_nodes_info(1)

def set_conf():
    print('Choose the configuration !')

def get_tree(path='/'):
    print('Tree root is %s' % path)
    system_file_manager.list(path)

def login():
    print('You are login...')
    (seq, adaptor) = add_adaptor()
    try:
        authenticate.update_when_node_added(seq, adaptor)
    except Exception as e:
        print(e)

def remove():
    print('Here is all your nodes:')
    tree_nodes_info()
    seq = input('Which node do you want to remove?')
    try:
        authenticate.update_when_node_deleted(int(seq))
    except Exception as e:
        print(e)

def upload(file_from, file_to):
    print('File from ' + file_from + ' is uploading to ' + file_to + '...')
    try:
        system_file_manager.upload(file_from, file_to)
    except Exception as e:
        print(e)

def download(file_from, file_to):
    print('File from ' + file_from + ' is downloading to ' + file_to + '...')
    try:
        system_file_manager.download(file_from, file_to)
    except Exception as e:
        print(e)

def doctor():
    print('Diagnosing...')
    print('Account check: pass/fail')
    print('Configuration check: pass/fail')
    print('Fragments check: X%')
    print('You can defrag recloud with command optimize...')
    print('You have a+b nodes...')
    print('Nodes work fine: a')
    print('Nodes work abnormal: b')

def optimize():
    print('Before: ...')
    print('Defraging...')
    print('Retriving account...')
    print('After: ...')


if __name__ == '__main__':
    choices = { 'info': get_info, 'conf': set_conf, 'tree': get_tree,
                'login': login, 'upload': upload, 'download': download,
                'remove': remove, 'doctor': doctor, 'optimize': optimize,}
    parser = argparse.ArgumentParser(description='Recloud command-line client.')

    parser.add_argument('action', choices=choices, help='Choose action to do')
    parser.add_argument('file_from', nargs='?', help='The source path of file')
    parser.add_argument('file_to', default='/', nargs='?', help='The aim path of file')
    args = parser.parse_args()
    function = choices[args.action]
    if args.file_from != None:
        if function == get_tree:
            function(args.file_from)
        else:
            function(args.file_from, args.file_to)
    else:
        function()
