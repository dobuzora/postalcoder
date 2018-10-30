#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
from tkinter import *

fp = open("./okinawa-post/47OKINAW.CSV", "rt", encoding="shift_jis")
for line in fp:
    line = line.replace(' ', '')
    line = line.replace('"', '')
    cells = line.split(",")
    zipno = cells[2] # 郵便番号
    ken = cells[6] # 都道府県
    shi = cells[7] # 市区
    cho = cells[8] # 市区以下
    title = ken + shi + cho
    print(zipno + ":" + title)
fp.close()

root = Tk()
root.title(u"postalcoder")
root.geometry("400x300")

#ラベル
Empty = Label(text=u'')
Empty.pack()
Static1 = Label(text=u'郵便番号を入力してください')
Static1.pack()

#エントリー
EditBox = Entry()
EditBox.pack()

#ボタン
Button = Button(text=u'検索')
Button.pack()

root.mainloop()


