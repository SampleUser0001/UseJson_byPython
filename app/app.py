# -*- coding: utf-8 -*-
import json

# サンプルのjsonファイルパス
JSON_FILE_PATH = './input/comments_PbONx9_umgE_20210421_184211.json'

JSON_KEY = ['kind','etag',]

with open(JSON_FILE_PATH, mode='r', ) as f:
    comments = json.load(f)
    # マップみたいなもんだと思えばいいっぽい。
    print(comments['pollingIntervalMillis'])

    itemsIndex = 0
    print(comments['items'][itemsIndex]['snippet']['displayMessage']); itemsIndex = itemsIndex + 1
    print(comments['items'][itemsIndex]['snippet']['displayMessage']); itemsIndex = itemsIndex + 1
