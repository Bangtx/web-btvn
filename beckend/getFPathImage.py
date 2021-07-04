import os, sqlite3
from builtins import type
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
                '{kwargs['link']}')
                """
    cursor.execute(sql)
    db.commit()


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


def ans_multi_choice(name):
    return name[name.index('.png') - 1: name.index('.png')]


def begin():

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


def get_data():
    list_subject = select_all('subject')
    list_topic = select_all('topic')
    list_doc = select_all('document')

    list_question_id = list()
    for subjec in list_subject:
        for topic in list_topic:
            list_doc_question = os.listdir(f"question/{subjec[1]}/{topic[1]}")
            for doc_and_file in list_doc_question:
                if is_file(doc_and_file) and is_question(doc_and_file):
                    doc = ''
                    if is_multi_choice(doc_and_file):
                        type = 'multi choice'
                    if is_long_response(doc_and_file):
                        type = 'long response'
                    insert_one_question(
                        subject=subjec[0],
                        topic=topic[0],
                        document=doc,
                        question=doc_and_file,
                        type=type,
                        link=f'question/{subjec[1]}/{topic[1]}/{doc_and_file}'
                    )
                    # print(f'question/{subjec[1]}/{topic[1]}/{doc}/{doc_and_file}')
                    # print(is_file(doc_and_file))
                if not is_file(doc_and_file):
                    print('????', list_doc)
                    for i in list_doc:
                        if doc_and_file == i[1]:
                            doc_and_file = i[1]
                        print(f'question/{subjec[1]}/{topic[1]}/{doc_and_file}')
                        list_question = os.listdir(f'question/{subjec[1]}/{topic[1]}/{doc_and_file}')
                        for question in list_question:
                            if is_file(question) and is_question(question):
                                print(f'question/{subjec[1]}/{topic[1]}/{doc_and_file}/{question}')
                                if is_multi_choice(question):
                                    type = 'multi choice'
                                if is_long_response(question):
                                    type = 'long response'
                                insert_one_question(
                                    subject=subjec[0],
                                    topic=topic[0],
                                    document=doc_and_file,
                                    question=question,
                                    type=type,
                                    link=f'question/{subjec[1]}/{topic[1]}/{doc_and_file}/{question}'
                                )


if __name__ == '__main__':
    create_database(list_sql)
    begin()
    get_data()
