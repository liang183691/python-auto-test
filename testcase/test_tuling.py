import unittest
import request


class TestTuling(unittest.TestCase):
    def test_post(self):
        self.url = 'http://www.tuling123.com/openapi/api'
        self.data = {'key': '1', 'coneent': ''}
        self.headers = ''
        self.result = request.HttpUtil.post(self)
        self.assertEqual(self.result['code'], 40000, msg='接口返回标识符有误')
