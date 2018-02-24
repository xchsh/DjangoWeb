# -*- coding: utf-8 -*-
__author__ = 'bobby'
import json
import requests


class YunPian(object):

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            #"text": "【婷婷电脑配件】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
            "text": "【慕学生鲜】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)

        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        print(re_dict)
        return re_dict


if __name__ == "__main__":
    #bobby_api_key = "d6c4ddbfseab36611dzfsze41aeb949e"
    #yun_pian = YunPian("ff38d7cefa5a1a0bce33635ec662b670")
    #yun_pian = YunPian(bobby_api_key)
    yun_pian.send_sms("2017", "18395562046")

