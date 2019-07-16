import os
from time import sleep

from tkinter import *


class DirList(object):

    def __init__(self, initdir=None):
        self.top = Tk()
        self.top.title('列出当前文件夹下的所有文件')
        self.label = Label(self.top, text='Directory Lister v1.1')
        self.label.pack()
        self.cmd = StringVar(self.top)
        print(self.cmd)
        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width=50, textvariable=self.cmd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()


        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir, bg='red', activeforeground='white', activebackground='blue')

        self.ls = Button(self.bfm, text='List Directory', command=self.doLS, activeforeground='white', activebackground='green')

        self.quit = Button(self.bfm, text='QUIT', command=self.top.quit, activeforeground='white', activebackground='red')

        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        if initdir:
            print('****11****')
            self.cmd.set(os.curdir)
            self.doLS()

    def clrDir(self, en=None):
        self.cmd.set('')

    def setDirAndGo(self, en=None):
        self.last = self.cmd.get();
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir
        self.cmd.set(check)
        self.doLS()

    def doLS(self, en=None):
        error=''
        tdir = self.cmd.get()
        if not tdir : tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            error = tdir + ':not a directory'
        if error:
            self.cmd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir

            self.cmd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return

        self.cmd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()
        dirList = os.listdir(tdir)
        dirList.sort()
        os.chdir(tdir)

        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)#当前目录macos .
        self.dirs.insert(END, os.pardir)#上级目录 ..
        for eachFile in dirList:
            self.dirs.insert(END, eachFile)
        self.cmd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')


def main():
    d = DirList(os.curdir)
    mainloop()


if __name__ == '__main__':
    main()
