#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/24 21:37
# @Author  : pxg
# @File    : SQLite.py

import sqlite3

con = sqlite3.connect("测试.db")
cur = con.cursor()
# sql = "CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name TEXT,age INTEGER)"
# cur.execute(sql)
# ①：添加单条数据
data = "1,'Desire',5"
cur.execute('INSERT INTO  test VALUES (%s)' % data)
# ②：添加单条数据
cur.execute("INSERT INTO test values(?,?,?)", (6, "zgq", 20))
# ③：添加多条数据
cur.executemany('INSERT INTO test VALUES (?,?,?)', [(3, 'name3', 19), (4, 'name4', 26)])
cur.execute("select * from test")
print(cur.fetchall())
con.commit()
cur.close()
con.close()

