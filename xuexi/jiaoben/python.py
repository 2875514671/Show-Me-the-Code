# -*- coding: utf-8 -*-
__author__ = 'HongLei'

from tkinter import *
from tkinter import ttk
import pymysql


def connmysql():
	conn = pymysql.connect(host='localhost', user='root', passwd='mysql', db='test', port=3306, charset='utf8')
	return conn


def getdata(*args):
	value = feet.get()
	res = '%' + value + '%'
	conn1 = connmysql()
	cur1 = conn1.cursor()
	cur1.execute(
		"select (@rn :=@rn+1)as rn, ename, cname, znarea from record a, (select @rn:=0) b "
        "where ename like '%s' union select (@rn:=@rn+1) as rn, ename, cname, znarea from record c, "
        "(select @rn:=0) d where cname like '%s'" % (
		res, res))
	data = cur1.fetchall()
	cur1.close()
	conn1.close()

	for res1 in data:
		ename.set(res1[1])
		meters.set(res1[2])
		znarea.set(res1[3])
		ttk.Label(mainframe, text="Ename:").grid(column=2, row=int(2 + (res1[0] - 1) * 4), sticky=(W, E))
		ttk.Label(mainframe, text="Cname:").grid(column=2, row=int(3 + (res1[0] - 1) * 4), sticky=(W, E))
		ttk.Label(mainframe, text="Znarea:").grid(column=3, row=int(3 + (res1[0] - 1) * 4), sticky=(W, E))
		ttk.Label(mainframe, textvariable=ename).grid(column=3, row=int(2 + (res1[0] - 1) * 4), sticky=(W, E))
		ttk.Label(mainframe, textvariable=meters).grid(column=2, row=int(4 + (res1[0] - 1) * 4), sticky=(W, E))
		ttk.Label(mainframe, textvariable=znarea).grid(column=3, row=int(4 + (res1[0] - 1) * 4), sticky=(W, E))
		ttk.Label(mainframe, text="-" * 20).grid(column=2, row=int(5 + (res1[0] - 1) * 4), sticky=(W, E))
		ttk.Label(mainframe, text="-" * 20).grid(column=3, row=int(5 + (res1[0] - 1) * 4), sticky=(W, E))


root = Tk()
root.title("Ename to Cname")

mainframe = ttk.Frame(root, padding=" 3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()
znarea = StringVar()
ename = StringVar()
feet_entry = ttk.Entry(mainframe, width=20, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))
ttk.Button(mainframe, text="Get", command=getdata).grid(column=3, row=1, sticky=(W, E))

for child in mainframe.winfo_children():
	child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', getdata)

root.mainloop()
