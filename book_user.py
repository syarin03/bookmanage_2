import sqlite3
import random
import os
import time


class User():
    def __init__(self):
        self.userID  = None
        self.userPW = None
        self.userName = None
        self.userPhone = None

    def setuser(self):
        self.


con = sqlite3.connect("book.db",isolation_level=None)

c = con.cursor()

def login():
    c.execute("SELECT COUNT(*) FROM usertbl")


