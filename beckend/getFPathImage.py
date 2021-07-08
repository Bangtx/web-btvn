import os, sqlite3
from builtins import type
from typing import re


# cursor = db.cursor()
# sql = """CREATE TABLE IF NOT EXISTS `subject` (
#             id INTEGER PRIMARY KEY,
#             subject TEXT NOT NULL
#             )"""
# cursor.execute(sql)
# sql = """CREATE TABLE IF NOT EXISTS `topic` (
#             id INTEGER PRIMARY KEY,
#             topic TEXT NOT NULL
#             )"""
# cursor.execute(sql)
# sql = """CREATE TABLE IF NOT EXISTS `document` (
#             id INTEGER PRIMARY KEY,
#             document TEXT NOT NULL
#             )"""
# cursor.execute(sql)


class database:
    def __init__(self):
        self.db = sqlite3.connect('db.sqlite3')
        self.base = 'static'
        self.list_subject = os.listdir(self.base)
        self.list_sql = [
            """CREATE TABLE IF NOT EXISTS `account` (
                `id` INTEGER PRIMARY KEY,
                `username` TEXT NOT NULL ,
                `password` TEXT NOT NULL        
                )""",
            """CREATE TABLE IF NOT EXISTS `point` (
                `id` INTEGER PRIMARY KEY,
                `id_user` INTEGER NOT NULL,
                `point` INTEGER NOT NULL
                )""",
            """CREATE TABLE IF NOT EXISTS `result` (
                `id` INTEGER PRIMARY KEY,
                `id_user` INTEGER NOT NULL,
                `id_question` INTEGER NOT NULL ,
                `result` TEXT NOT NULL
                )""",
            """CREATE TABLE IF NOT EXISTS `subject` (
                    `id` INTEGER PRIMARY KEY,
                    `subject` TEXT NOT NULL)""",
            """CREATE TABLE IF NOT EXISTS `topic` (
                    `id` INTEGER PRIMARY KEY,
                    `topic` TEXT NOT NULL
                    )""",
            """CREATE TABLE IF NOT EXISTS `document` (
                `id` INTEGER PRIMARY KEY,
                `document` TEXT NOT NULL
                )""",
            """CREATE TABLE IF NOT EXISTS `question` (
                `id` INTEGER PRIMARY KEY,
                `subject` INTEGER NOT NULL ,
                `topic` INTEGER NOT NULL ,
                `document` INTEGER NULL DEFAULT NULL,
                `question` TEXT NOT NULL,
                `type` TEXT NOT NULL ,
                `link` TEXT NOT NULL 
                )"""
        ]

    def create_database(self):
        cursor = self.db.cursor()
        for i in self.list_sql:
            cursor.execute(i)
        self.db.commit()

    def insert_one(self, table_name, data):
        cursor = self.db.cursor()
        sql = f"""INSERT INTO `{table_name}` (`{table_name}`) VALUES ('{data}')"""
        cursor.execute(sql)
        self.db.commit()
        sql = f"""SELECT MAX(id) FROM `{table_name}`"""
        cursor.execute(sql)
        result = cursor.fetchall()
        return result[0][0]

    def insert_one_question(self, **kwargs):
        cursor = self.db.cursor()
        sql = f"""INSERT INTO `question` (`subject`, `topic`, `document`, `question`, `type`, `link`)
                    VALUES 
                    ('{kwargs['subject']}', 
                    '{kwargs['topic']}', 
                    '{kwargs['document']}', 
                    '{kwargs['question']}', 
                    '{kwargs['type']}', 
                    '{kwargs['link']}')
                    """
        cursor.execute(sql)
        self.db.commit()

    def select_all(self, table_name):
        cursor = self.db.cursor()
        sql = f"""SELECT * FROM `{table_name}` WHERE 1"""
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def select_one(self, table_name, id):
        cursor = self.db.cursor()
        sql = f"""SELECT * FROM `{table_name}` WHERE `id` = {id}"""
        cursor.execute(sql)
        result = cursor.fetchall()
        return result


def is_file(fileName):
    if fileName.find('.png') != -1:
        return True
    else:
        return False


def is_question(file_name):
    if file_name.find('M.png') != -1:
        return False
    else:
        return True


def clear_duplicate(list_data):
    result = list()
    for data in list_data:
        try:
            index = result.index(data)
        except:
            result.append(data)
    return result


def get_list_doc(list_data):
    result = list()
    for data in list_data:
        print(is_file(data), is_question(data))
        if not is_file(data):
            result.append(data)
    return result


def is_multi_choice(name):
    if len(name) == 11:
        if name[name.index('.png') - 1: name.index('.png')] != '_':
            print(name[name.index('.png') - 1: name.index('.png')])
            return True
    return False


def is_long_response(name):
    return not is_multi_choice(name)


def ans_multi_choice(name):
    return name[name.index('.png') - 1: name.index('.png')]


def convert_question_name(name):
    index = name.find('.png')
    return name[: index - 1] + name[index:]
