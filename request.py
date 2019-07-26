from urllib import parse
import requests
import json


class HttpUtil:
    def get(self):
        try:
            if self.data == '':
                response = requests.get(self.url, headers=self.headers)
            else:
                response = requests.get(self.url + '?' + parse.urlencode(self.data), headers=self.headers)
            response = json.loads(response.text)
            print(response)
            return response
        except Exception as e:
            print("请求异常:", e)

    def post(self):
        try:
            if self.headers == '':
                self.headers = {'Content-Type': 'application/json'}
            response = requests.post(self.url, data=json.dumps(self.data), headers=self.headers)
            response = json.loads(response.text)
            print(response)
            return response
        except Exception as e:
            print("请求异常:", e)
