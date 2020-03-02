# -*- coding: utf-8 -*-
# @Time    : 2/27/20 2:39 PM
# @Author  : naturegong
# @File    : yunpian.py
import json
import requests


class YunPian(object):
    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send_sms(self, code, mobile):
        """
        发送短信
        :param code: 验证码
        :param mobile: 手机号，例如：13711112222
        :return:
        """
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【然小狼】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    yun_pian = YunPian("")
    yun_pian.send_sms("2017", "13711112222")
