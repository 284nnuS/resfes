import cv2
from fastapi import Request, FastAPI
import numpy as np
import base64
from compute import predict
from fuzzy import fuzzy
from cachetools import TTLCache
import uuid
import json
import random

cache = TTLCache(maxsize=float('inf'), ttl=10800)
app = FastAPI()


@ app.post("/api/analyze")
async def analyze(request: Request):
    try:
        json = await request.json()
        buffer = base64.b64decode(json['payload'])
        array = np.fromstring(buffer, dtype=np.uint8)
        img = cv2.imdecode(array, cv2.IMREAD_COLOR)
        face_analyze = predict(img)

        if face_analyze is None:
            return {
                "success": False,
                "message": "Khuôn mặt của bản không được tìm thấy trong bức ảnh. Vui lòng thử lại"
            }

        id = str(uuid.uuid4())

        cache[id] = {
            "done": False,
            "data": face_analyze,
        }

        return {
            "success": True,
            "id": id
        }
    except:
        return {
            "success": False,
            "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
        }


@ app.post("/api/submit")
async def submit(request: Request):
    try:
        json = await request.json()
        id = json["id"]
        scores = json["scores"]

        print(scores)

        if (type(id) != str or type(scores) != list or len(scores) != 4):
            return {
                "success": False,
                "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
            }

        if id not in cache:
            return {
                "success": False,
                "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
            }

        el = cache[id]

        if el['done'] is True:
            return {
                "success": False,
                "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
            }

        face_analyze = el['data']
        result = []

        for i in range(0, len(scores)):
            result.append(fuzzy(face_analyze[i], scores[i]))

        cache[id] = {
            "done": True,
            "data": result,
        }

        return {
            "success": True,
        }
    except:
        return {
            "success": False,
            "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
        }


@ app.get("/api/view/{id}")
async def view(id: str):
    try:
        if id not in cache:
            return {
                "success": False,
                "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
            }
        el = cache[id]

        if el['done'] is False:
            return {
                "success": False,
                "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
            }
        return {
            "success": True,
            "result": el['data']
        }

    except:
        return {
            "success": False,
            "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
        }


def read_to_json(filename):
    with open(filename, 'r') as data_file:
        json_data = data_file.read()
    return json.loads(json_data)


it = read_to_json('../quizs/it.json')
business = read_to_json('../quizs/business.json')
graphics = read_to_json('../quizs/graphics.json')
language = read_to_json('../quizs/language.json')

num_of_question = 3


@ app.get("/api/quiz/{id}")
async def quiz(id: str):
    if id not in cache:
        return {
            "success": False,
            "message": "Yêu cầu bị lỗi. Vui lòng thử lại"
        }

    result = []

    temp = it
    random.shuffle(temp)
    for i in range(num_of_question):
        result.append({
            'content': temp[i],
            'type': 'it'
        })

    temp = business
    random.shuffle(temp)
    for i in range(num_of_question):
        result.append({
            'content': temp[i],
            'type': 'business'
        })

    temp = graphics
    random.shuffle(temp)
    for i in range(num_of_question):
        result.append({
            'content': temp[i],
            'type': 'graphics'
        })

    temp = language
    random.shuffle(temp)
    for i in range(num_of_question):
        result.append({
            'content': temp[i],
            'type': 'language'
        })

    random.shuffle(result)
    return {
        "success": True,
        "result": result,
    }
