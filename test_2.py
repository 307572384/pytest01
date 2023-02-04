# Python自动化测试实战篇（2）unittest实现批量接口测试，并用HTMLTestRunner输出测试报告
import configparser
import os
import requests
import time
import unittest

from HTMLTestRunner3_New import HTMLTestRunner


class Get_config_ini:
    def __init__(self, file):
        self.cf = configparser.ConfigParser()
        self.cf.read(file)

    def get_ini_test(self, a, c):
        values = self.cf.get(a, c)
        return values


a1_path = os.path.abspath(os.path.dirname(__file__))
a1 = Get_config_ini(os.path.join(a1_path, 'Config.ini')).get_ini_test('a_path', 'ar_path')
a2_path = os.path.join(a1_path)
t_ime = time.strftime('%Y-%m-%H-%M-%S')
report_path = os.path.join(a2_path, t_ime + 'report.html')
print(report_path)


class Cms(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('类的开始')

    @classmethod
    def tearDownClass(cls) -> None:
        print('类的结束')

    def setUp(self) -> None:
        print('方法的开始')

    def tearDown(self) -> None:
        print('方法的结束')

    def test_1(self):
        print('测试用例1')

    def test_2(self):
        print('测试用例2')

    def test_3(self):
        print('测试用例3')

    def test_4(self):
        print('测试用例4')

    def test_5(self):
        print('测试用例5')

    def test_6(self):
        print('测试用例6')

    def test_7(self):
        print('测试用例7')

    def test_8(self):
        print('测试用例8')

    def test_9(self):
        print('测试用例9')

    def test_10(self):
        print('测试用例10')


class Cms(unittest.TestCase):  # 定义一个测试框架的类
    def test_1(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': 123456}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_2(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': '123Aa'}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_3(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': '123456@@'}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_4(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': ' '}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_5(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': '/.;'}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_6(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': '一二三四五六'}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_7(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': 'abcdefg'}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_8(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': 'いち'}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_9(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': '하나 둘 셋 넷 다섯 여섯'}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)

    def test_10(self):
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': 'admin', 'loginPwd': 'адзін два тры чатыры пяць шэсць'}
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTests([Cms('test_1'), Cms('test_2'), Cms('test_3'),
                   Cms('test_4'), Cms('test_5'), Cms('test_6'),
                   Cms('test_7'), Cms('test_8'), Cms('test_9'),
                   Cms('test_10')])
    p = open(report_path, 'wb')
    run = HTMLTestRunner(stream=p, title='Cms登录接口报告', description='执行概况如下', tester='cxc')
    run.run(suit)
