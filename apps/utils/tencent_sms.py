# -*- coding: utf-8 -*-
# @Time    : 3/2/20 2:04 PM
# @Author  : naturegong
# @File    : tencent_sms.py
import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.sms.v20190711 import sms_client, models
from VueDjangoShopWebsite.settings import (
    TENCENT_SECRET_ID, TENCENT_SECRET_KEY
)


class TencentSms(object):

    httpProfile = HttpProfile()
    httpProfile.endpoint = "sms.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile

    def __init__(self, secretId, secretKey):
        """
        传入用户参数
        :param secretId: 在云API密钥上申请的标识身份的 SecretId，一个 SecretId 对应唯一的 SecretKey。
        :param secretKey: 用来生成请求签名 Signature。
        """
        self.cred = credential.Credential(secretId, secretKey)

    def send_sms(self, code, mobile):
        """
        发送短信
        :param code: 验证码
        :param mobile: 手机号，例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号
        :return:
        """
        try:
            client = sms_client.SmsClient(self.cred, "ap-beijing", self.clientProfile)
            req = models.SendSmsRequest()
            req.TemplateID = "543954"
            req.PhoneNumberSet = [str("+86"+mobile)]
            req.Sign = "然小狼"
            req.TemplateParamSet = [code]
            req.SmsSdkAppid = "1400324019"

            resp = client.SendSms(req)
            re_dict = json.loads(resp.to_json_string())
            return re_dict

        except TencentCloudSDKException as err:
            print(err)
            pass


if __name__ == "__main__":
    tencent_sms = TencentSms(TENCENT_SECRET_ID, TENCENT_SECRET_KEY)
    msg = tencent_sms.send_sms("2020", "+8615600565987")
    print(msg)
