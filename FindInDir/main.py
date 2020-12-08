
import os
import plistlib
import sys
from pathlib import Path

from PyQt5.QtWidgets import *

from Ui_mainWin import *


class Form(Ui_Dialog, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.baseDir = Path.home()
        self.countFound = 0

    def resizeEvent(self, event):
        self.resizeWidget()

    def resizeWidget(self):
        p0 = 4
        w0, h0 = self.width() - 8, self.height() - 100
        self.listMessage.move(p0, p0)
        self.listMessage.resize(w0, h0)
        h1 = self.height() - h0 - p0 * 2
        self.container.resize(w0, h1)
        self.container.move(p0, h0 + p0)
        y2, h2 = self.labelStatus.y(), self.labelStatus.height()
        self.labelStatus.resize(w0, h2)
        self.labelStatus.move(0, h1 - h2)

    def showMessage(self, msg):
        self.listMessage.addItem(msg)
        QApplication.processEvents()
    
    def showStatus(self, msg):
        self.labelStatus.setText(str(msg))
        QApplication.processEvents()

    def searchDic(self, dic, findstr):
        found = False
        for key, item in dic.items():
            if type(item) is str:
                if findstr in str(item):
                    self.showMessage(f'     {key}:{item}')
                    return True
            elif type(item) is dict:
                if self.searchDic(item, findstr):
                    self.showMessage(f'         on key {key}')
                    return True
            elif type(item) is list:
                i = 0
                for s in item:
                    if type(s) is dict:
                        if self.searchDic(s, findstr):
                            self.showMessage(f'         on key {key} list<{i}>')
                            return True
                    elif findstr in str(s):
                        self.showMessage(f'         {key}:{s} list<{i}>')
                        return True
                    i += 1
        return found

    def grepPlist(self, filename, findstr):
        if not filename.is_file():
            return False
        try:
            with open(filename, 'rb') as file:
                pl = plistlib.load(file)
        except PermissionError as e:
            self.showMessage('?' * 10 + f' {e} ====')
            return False
        except Exception as e:
            self.showMessage('?' * 10 + f' {os.path.basename(filename)} ===={e}====')
            return False
        return self.searchDic(pl, findstr)

    def findPlistInDir(self, dir0, findstr):
        self.showMessage(f'GrepPlist <{findstr}> in Dir "{dir0}"')
        flists = [f for f in os.listdir(dir0) if '.plist' in f]
        for f in flists:
            fname = Path.joinpath(dir0, f)
            self.showStatus(str(f))
            if self.grepPlist(fname, findstr):
                self.countFound += 1
                tail = f.find('.plist')
                self.showMessage('^' * 10 + f' {f[0:tail]} ' + '-' * 30)

    def grepEncoding(self, file, findstr, encoding):
        with file.open('r', encoding=encoding) as f:
            i = 0
            for line in f:
                i += 1
                if findstr in line:
                    self.showMessage(f'     <{i}> {line[:-1]}')
                    return True
        return False

    def grep(self, file, findstr):
        if not file.is_file():
            return False
        try:
            try:
                return self.grepEncoding(file, findstr, 'utf-8')
            except UnicodeDecodeError:
                return self.grepEncoding(file, findstr, 'cp1252')
        except Exception as e:
            self.showMessage('?' * 20 + f'{file.relative_to(self.baseDir)} ===={e}====')
        return False

    def findInDirRecursive(self, dir0, findstr):
        if not dir0.is_dir():
            self.showMessage(f'{dir0} is not a dir!')
            return False
        self.showStatus(dir0)
        flists = [f for f in os.listdir(dir0)]
        for f in flists:
            fname = dir0 / f
            if fname.is_dir():
                self.findInDirRecursive(fname, findstr)
            elif f[-3:] == '.cc' or f[-2:] == '.h' in f:
                if self.grep(fname, findstr):
                    rel_dir = str(fname.relative_to(self.baseDir))
                    l0 = 100 - len(rel_dir) if len(rel_dir) < 97 else 3
                    self.countFound += 1
                    self.showMessage('^' * 5 + f'  {rel_dir}  ' + '-' * l0)

    def doFindText(self):
        self.baseDir = Path.home() / self.comboDir.currentText().strip()
        findstr = self.lineEdit.text().strip()
        self.countFound = 0
        self.findInDirRecursive(self.baseDir, findstr)
        self.showMessage(f'==> Search <{findstr}> done! Total {self.countFound} files found!\n')
        self.showStatus(f'Total {self.countFound} files found "{findstr}"')

    def doFindPlist(self):
        self.baseDir = Path.home() / self.comboDir.currentText().strip()
        findstr = self.lineEdit.text().strip()
        self.countFound = 0
        self.findPlistInDir(self.baseDir, findstr)
        self.showMessage('==> Search plist done!\n')
        self.showStatus(f'Total {self.countFound} files found "{findstr}"')


def main():
    # QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()

    # findPlistInDir(Path.cwd() / 'Preferences', '終端')
    # findInDir(baseDir, 'avformat_find_stream_info')
