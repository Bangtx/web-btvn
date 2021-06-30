import os, sqlite3
from typing import re

db = sqlite3.connect('db.sqlite3')
list_subject = os.listdir('question')

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

list_sql = [
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


def create_database(sql):
    global cursor
    cursor = db.cursor()
    for i in sql:
        cursor.execute(i)
    db.commit()


def insert_one(table_name, data):
    global cursor
    sql = f"""INSERT INTO `{table_name}` (`{table_name}`) VALUES ('{data}')"""
    cursor.execute(sql)
    db.commit()
    sql = f"""SELECT MAX(id) FROM `{table_name}`"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result[0][0]


def insert_one_question(**kwargs):
    global cursor
    sql = f"""INSERT INTO `question` (`subject`, `topic`, `document`, `question`, `type`, `link`)
                VALUES 
                ('{kwargs['subject']}', 
                '{kwargs['topic']}', 
                '{kwargs['document']}', 
                '{kwargs['question']}', 
                '{kwargs['type']}', 
                '{kwargs['link']}')"""
    cursor.execute(sql)
    db.commit()


def is_file(fileName):
    if fileName.find('.png') != -1:
        return True
    else:
        return False


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
        if not is_file(data):
            result.append(data)
    return result


def select_all(table_name):
    global cursor
    sql = f"""SELECT * FROM `{table_name}` WHERE 1"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def select_one(table_name, id):
    global cursor
    sql = f"""SELECT * FROM `{table_name}` WHERE `id` = {id}"""
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def is_multi_choice(name):
    if len(name) == 11:
        if name[name.index('.png') - 1: name.index('.png')] != '_':
            print(name[name.index('.png') - 1: name.index('.png')] )
            return True
    return False


def is_long_response(name):
    return not is_multi_choice(name)


print(is_multi_choice('C0201M_.png'))
print(is_long_response('C0201M_.png'))


def main():

    list_subject_id = list()
    list_topic_id = list()
    list_document_id = list()
    list_name = list()

    list_doc = list()
    for subjec in list_subject:
        list_topic = os.listdir('question/' + subjec)
        list_subject_id.append(insert_one('subject', subjec))
        for topic in list_topic:
            list_doc_question = os.listdir(f'question/{subjec}/{topic}')
            list_topic_id.append(insert_one('topic', topic))
            list_doc += get_list_doc(list_doc_question)
            list_doc = clear_duplicate(list_doc)

    for doc in list_doc:
        list_document_id.append(insert_one('document', doc))

    list_question_id = list()
    for subjec in list_subject:
        for topic in list_topic:
            list_doc_question = os.listdir(f'question/{subjec}/{topic}')
            for doc_and_file in list_doc_question:
                if is_file(doc_and_file):
                    insert_one_question(subject=subjec, topic=topic, doc='', )
                    # list_question_id.append(insert_one('question', doc_and_file))
                # print(topic)
                # print(os.listdir(f'question/{subjec}/{topic}/{doc}'))
                # list_name_2 += os.listdir(f'question/{subjec}/{topic}/{doc}')

create_database(list_sql)
# main()
# print(select_all('topic'))
# print(select_one('topic', 3))
# data = insert_one('subject', 'hoa hoc')
# print(data)