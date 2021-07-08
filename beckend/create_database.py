from getFPathImage import database
from getFPathImage import *


db = database()
base = 'static'
base_url = 'http://127.0.0.1:8000'


def begin():

    list_subject_id = list()
    list_topic_id = list()
    list_document_id = list()
    list_name = list()

    list_doc = list()
    list_subject = os.listdir(base)
    for subjec in list_subject:
        list_topic = os.listdir(base + '/' + subjec)
        list_subject_id.append(db.insert_one('subject', subjec))
        for topic in list_topic:
            list_doc_question = os.listdir(f'{base}/{subjec}/{topic}')
            list_topic_id.append(db.insert_one('topic', topic))
            list_doc += get_list_doc(list_doc_question)
            list_doc = clear_duplicate(list_doc)

    for doc in list_doc:
        list_document_id.append(db.insert_one('document', doc))


def get_data():
    list_subject = db.select_all('subject')
    list_topic = db.select_all('topic')
    list_doc = db.select_all('document')

    list_question_id = list()
    for subjec in list_subject:
        for topic in list_topic:
            try:
                list_doc_question = os.listdir(f"{base}/{subjec[1]}/{topic[1]}")
                for doc_and_file in list_doc_question:
                    if is_file(doc_and_file) and is_question(doc_and_file):
                        doc = ''
                        if is_multi_choice(doc_and_file):
                            type = 'multi choice'
                        if is_long_response(doc_and_file):
                            type = 'long response'
                        db.insert_one_question(
                            subject=subjec[0],
                            topic=topic[0],
                            document=doc,
                            question=convert_question_name(doc_and_file),
                            type=type,
                            link=f'{base_url}/{base}/{subjec[1]}/{topic[1]}/{doc_and_file}'
                        )

                    if not is_file(doc_and_file):
                        print('????', list_doc)
                        for i in list_doc:
                            if doc_and_file == i[1]:
                                doc_and_file = i[1]
                            print(f'{base}/{subjec[1]}/{topic[1]}/{doc_and_file}')
                            list_question = os.listdir(f'{base}/{subjec[1]}/{topic[1]}/{doc_and_file}')
                            for question in list_question:
                                if is_file(question) and is_question(question):
                                    print(f'{base}/{subjec[1]}/{topic[1]}/{doc_and_file}/{question}')
                                    if is_multi_choice(question):
                                        type = 'multi choice'
                                    if is_long_response(question):
                                        type = 'long response'
                                    db.insert_one_question(
                                        subject=subjec[0],
                                        topic=topic[0],
                                        document=doc_and_file,
                                        question=convert_question_name(question),
                                        type=type,
                                        link=f'{base_url}/{base}/{subjec[1]}/{topic[1]}/{doc_and_file}/{question}'
                                    )
            except:
                pass


if __name__ == '__main__':
    db.create_database()
    begin()
    get_data()