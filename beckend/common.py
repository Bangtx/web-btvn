from getFPathImage import database
import json


def get_all_question():
    db = database()
    data = db.select_all('question')
    data = json.dumps(data)
    return data

