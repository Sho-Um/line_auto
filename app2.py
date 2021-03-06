import requests
# import datetime
# import pytz
import os

# time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
# time = time.strftime('%Y年%m月%d日 %H:%M:%S')

TOKEN = os.environ['LINE_MY_TOKEN']
api_url = 'https://notify-api.line.me/api/notify'
send_contents = "\n13時だよ！\n午前中にやったことの振り返りをしよう！"

TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}

# image_file = './sky.jpg'
# binary = open(image_file, mode='rb')
# image_dic = {'imageFile': binary}

# requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)
requests.post(api_url, headers=TOKEN_dic, data=send_dic)