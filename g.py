# 用户登录测试用例
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
report_path = os.path.join(a2_path, t_ime + '测试报告.html')


class login_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('用例测试开始')

    @classmethod
    def tearDownClass(cls) -> None:
        print('用例测试结束')

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


class login_test(unittest.TestCase):  # 定义一个测试框架的类
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


def logjum():
    discre = unittest.defaultTestLoader.discover(start_dir=a1_path, pattern='g*.py')
    p = open(report_path, 'wb')
    run = HTMLTestRunner(stream=p, title='CMS总计报告', description='执行情况', tester='cxc')
    run.run(discre)


def test():
    suit = unittest.TestSuite()
    suit.addTests([login_test('test_1'), login_test('test_2'), login_test('test_3'),
                   login_test('test_4'), login_test('test_5'), login_test('test_6'),
                   login_test('test_7'), login_test('test_8'), login_test('test_9'),
                   login_test('test_10')])
    p = open(report_path, 'wb')
    run = HTMLTestRunner(stream=p, title='登录接口报告', description='执行概况如下', tester='for_you')
    run.run(suit)


if __name__ == '__main__':
    logjum()
#         test()
