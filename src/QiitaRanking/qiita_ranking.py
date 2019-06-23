import json
import requests
from datetime import datetime, timedelta
from pytz import timezone
import os


def get_ranking(event, context):
    type = 'weekly'
    date = datetime.now(timezone('Asia/Tokyo'))
    # 今日を指定するとデータが取得できないので前日を指定する
    date = (date - timedelta(days=1)).strftime('%Y-%m-%d')
    url = os.environ['qiitaScraipingUrl'] + type + '/' + date
    response = requests.get(url).json()

    data_list = response['data']
    msg = '*週間いいねランキング* \n\n'
    count = 1
    for data in data_list:
        msg += str(count) + '位：<' + data['url'] + '|' + data['title'] + '> \n'
        count += 1

    send_data = {
        'text': msg
    }
    slack_url = os.environ['slackWebhookUrl']
    slack_send_data = {
        "payload": json.dumps(send_data)
    }
    requests.post(slack_url, slack_send_data)


# if __name__ == '__main__':
#     os.environ['qiitaScraipingUrl'] = 'https://us-central1-qiita-trend-web-scraping.cloudfunctions.net/qiitaScraiping/'
#     os.environ['slackWebhookUrl'] = ''
#     get_ranking(None, None)



