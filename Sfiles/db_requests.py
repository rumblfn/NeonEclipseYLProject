import sqlite3
import socket

con = sqlite3.connect("neoneclipse_stat.sqlite")
cur = con.cursor()


def check_user_in_system():
    name = socket.gethostname()
    data = cur.execute("""SELECT id FROM statistics WHERE username = ?""", (str(name), )).fetchall()
    if data:
        info = get_info(name)
    else:
        create_user(name)
        info = get_info(name)
    return info


def create_user(name):
    us = cur.execute("""SELECT * FROM statistics""").fetchall()
    cur.execute("""INSERT INTO statistics VALUES(?, ?, ?, ?)""",
                (len(us) + 1, name, 0, 0)).fetchall()
    con.commit()


def get_info(name):
    loses = cur.execute("""SELECT loses FROM statistics WHERE username = ?""", (str(name), )).fetchall()
    wins = cur.execute("""SELECT wins FROM statistics WHERE username = ?""", (str(name), )).fetchall()
    return [loses[0][0], wins[0][0]]


def update_loses():
    name = socket.gethostname()
    loses = cur.execute("""SELECT loses FROM statistics WHERE username = ?""", (str(name), )).fetchall()[0][0]
    cur.execute("""UPDATE statistics
                        SET loses = ?
                        WHERE username = ?""", (loses + 1, name)).fetchall()
    con.commit()


def update_wins():
    name = socket.gethostname()
    wins = cur.execute("""SELECT wins FROM statistics WHERE username = ?""", (str(name),)).fetchall()[0][0]
    cur.execute("""UPDATE statistics
                            SET wins = ?
                            WHERE username = ?""", (wins + 1, name)).fetchall()
    con.commit()