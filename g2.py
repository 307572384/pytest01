# Python自动化测试实战篇（3）优化unittest批量自动化接口测试代码，ddt驱动+yaml实现用例调用，输出HTMLTestRunner测试报告


import os  # 导入路径拼接
import requests
import time
import unittest

import yaml  # 导入yaml模块获取yaml文件值
from ddt import ddt, data, unpack  # 导入数据驱动

from HTMLTestRunner3_New import HTMLTestRunner

f = open(os.path.join('D:\pythonpj\pytest\lojump.yaml'), 'r', encoding='utf-8')
ts_et = yaml.safe_load(f)
url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
headers = {'Content-Type': 'application/x-www-form-urlencoded'}


# report_path = os.path.join(a1_path,'测试报告.html')
@ddt
class lg(unittest.TestCase):
    @data(*ts_et)
    @unpack
    def test_logjump(self, **dict):  # 定义一个测试用例
        reps = requests.post(url=url, headers=headers,
                             data={'userAccount': dict['userAccount'],
                                   'loginPwd': dict['loginPwd']})
        print(reps.text)


def logjum():
    t_ime = time.strftime('%Y-%m-%H-%M-%S')
    a1_path = os.path.abspath(os.path.dirname(__file__))
    report_path = os.path.join(a1_path, t_ime + '测试报告.html')
    discre = unittest.defaultTestLoader.discover(start_dir=a1_path, pattern='g*.py')
    p = open(report_path, 'wb')
    run = HTMLTestRunner(stream=p, title='CMS总计报告', description='执行情况', tester='you')
    run.run(discre)


if __name__ == '__main__':
    logjum()
    unittest.main()
