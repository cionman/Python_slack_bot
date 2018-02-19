import requests
import datetime

from util import get_secret


def main():
    url = get_secret("WEBHOOK") # 웹훅 URL
    text = "테스트 메세지 입니다 : " + str(datetime.datetime.now())
    payload = {
        "text" : text
        , "username": "webhookbot"
        , "channel" : "general"
        , "icon_emoji" : ":ghost:"
    }

    requests.post(url, json=payload)

if __name__ == "__main__":
    main()