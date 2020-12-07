import os
from pathlib import Path
import plistlib


def searchDic(dic, findstr):
    found = False
    for key, item in dic.items():
        if type(item) is str:
            if findstr in str(item):
                print(f'     {key}:{item}')
                return True
        elif type(item) is dict:
            if searchDic(item, findstr):
                print(f'         on key {key}')
                return True
        elif type(item) is list:
            i = 0
            for s in item:
                if type(s) is dict:
                    if searchDic(s, findstr):
                        print(f'         on key {key} list<{i}>')
                        return True
                elif findstr in str(s):
                    print(f'         {key}:{s} list<{i}>')
                    return True
                i += 1
    return found


def grepPlist(filename, findstr):
    if not filename.is_file():
        return False
    try:
        with open(filename, 'rb') as file:
            pl = plistlib.load(file)
    except Exception as e:
        print('?' * 20, f'{os.path.basename(filename)} ===={e}====')
        return False
    return searchDic(pl, findstr)


def findPlistInDir(dir0, findstr):
    print(f'GrepPlist <{findstr}> in Dir "{dir0}"')
    flists = [f for f in os.listdir(dir0) if 'com.apple.' in f and '.plist' in f]
    for f in flists:
        fname = Path.joinpath(dir0, f)
        if grepPlist(fname, findstr):
            head, tail = f.find('com.apple.'), f.find('.plist')
            print('^' * 10 + f'{f[head + 10:tail]}' + '^' * 30)


def grepEncoding(file, findstr, encoding):
    with file.open('r', encoding=encoding) as f:
        i = 0
        for line in f:
            i += 1
            if findstr in line:
                print(f'     <{i}> {line[:-1]}')
                return True
    return False


def grep(file, findstr):
    if not file.is_file():
        return False
    try:
        try:
            return grepEncoding(file, findstr, 'utf-8')
        except UnicodeDecodeError:
            return grepEncoding(file, findstr, 'cp1252')
    except Exception as e:
        print('?' * 20, f'{file.relative_to(baseDir)} ===={e}====')
    return False


def findInDir(dir0, findstr):
    if not dir0.is_dir():
        print(f'{dir0} is not a dir!')
        return False
    flists = [f for f in os.listdir(dir0)]
    for f in flists:
        fname = dir0 / f
        if fname.is_dir():
            findInDir(fname, findstr)
        elif f[-3:] == '.cc' or f[-2:] == '.h' in f:
            if grep(fname, findstr):
                print('^' * 5 + f'  {fname.relative_to(baseDir)}  ' + '^' * 25)


if __name__ == '__main__':
    # findPlistInDir(Path.cwd() / 'Preferences', '終端')
    baseDir = Path.home() / 'electron11/src'
    findInDir(baseDir, 'avformat_find_stream_info')
