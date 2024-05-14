import random
import readline
import sqlite3

# SQL Injection

db = sqlite3.Connection(":memory:")
db.execute("CREATE TABLE Students(name);")
db.execute("INSERT INTO Students VALUES ('John');")


def add_name(name):
    cmd = "INSERT INTO Students VALUES ('" + name + "');"
    print("Executing:", cmd)
    db.executescript(cmd)
    print("Students:", db.execute("select * from Students").fetchall())


def add_name_safe(name):
    db.execute("INSERT INTO Students VALUES (?)", [name])
    print("Students:", db.execute("select * from Students").fetchall())


add_name_safe("Jack")
add_name_safe("Jill")
add_name_safe("Robert'); DROP TABLE Students; --")
