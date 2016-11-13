#!/usr/bin/env python3
import argparse
from authenticator.authenticate import RecloudConfig
# from adaptor.adaptor import add_adaptor

def get_info():
    print('You get the infomation!')
    print('Total quota size: XXX MB')
    print('Available quota size(before redundant): XXX MB')
    print('Available quota size(after redundant): XXX MB')
    print('Estimate upload speed: XXX KB/s')
    print('Estimate download speed: XXX KB/s')

def set_conf():
    print('Choose the configuration !')

def get_tree():
    print('Tree!!!')

def login():
    print('You are login...')

    print('Which way do you want?')

def remove():
    print('Which node do you want to remove?')

def upload(file_from, file_to):
    print('File from ' + file_from + ' is uploading to ' + file_to + '...')

def download(file_from, file_to):
    print('File from ' + file_from + ' is downloading to ' + file_to + '...')

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
        function(args.file_from, args.file_to)
    else:
        function()
