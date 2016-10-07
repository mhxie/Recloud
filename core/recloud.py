#!/usr/bin/env python3
import argparse

def get_info():
    print('You get the infomation!')

def get_conf():
    print('You open the configuration!')

def get_tree():
    print('Tree!!!')

def login():
    print('You are login...')

def upload(file_from, file_to):
    print('File from ' + file_from + ' is uploading to ' + file_to + '...')

def download(file_from, file_to):
    print('File from ' + file_from + ' is downloading to ' + file_to + '...')

def doctor():
    print('Diagnosing...')


if __name__ == '__main__':
    choices = { 'info': get_info, 'conf': get_conf, 'tree': get_tree,
                'login': login, 'upload': upload, 'download': download,
                'doctor': doctor}
    parser = argparse.ArgumentParser(description='Recloud command-line client.')
    parser.add_argument('action', choices=choices, help='which action to do')
    parser.add_argument('file_from', nargs='?', help='the source path of file')
    parser.add_argument('file_to', default='/', nargs='?', help='the aim path of file')
    args = parser.parse_args()
    function = choices[args.action]
    if args.file_from != None:
        function(args.file_from, args.file_to)
    else:
        function()
