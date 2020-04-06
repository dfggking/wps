"""
获取企业微信用户
"""
import requests
import json
from flask import current_app


class WxServer:

    @staticmethod
    def get_token():
        """
        获取token
        :return: access_token
        """
        url = 'https://wps_test_test.gov.weixin.qq.com/cgi-bin/gettoken'
        response = requests.get(url, params={'corpid': current_app.config['CORP_ID'], 'corpsecret': current_app.config['CORP_SECRET']})
        return response.json()['access_token']

    @staticmethod
    def get_wx_user(self):
        """
        返回用户列表
        :param self:
        :return:
        """
        url = 'https://wps_test_test.gov.weixin.qq.com/cgi-bin/user/simplelist'
        # 直接请求
        response = requests.get(url, params={'access_token': self.get_token()})
        user_list = json.loads(response.text)
        return user_list


