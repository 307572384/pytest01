import os
import requests  # 导入单元框架
import unittest

import xlrd
from ddt import ddt, data, unpack  # 导入ddt


class read_xlsx:
    def __init__(self, file):
        self.read_file = xlrd.open_workbook(os.path.join('D:\pythonpj\pytest', file))  # 读取本地xlsx的地址包

    def get_xlsx(self, idex):
        sheet_idex = self.read_file.sheet_by_index(idex)
        key = sheet_idex.row_values(0)
        l = []
        for i in range(1, sheet_idex.nrows):  # 统计页中行数
            values = sheet_idex.row_values(i)
            key_values = zip(key, values)  # 创建迭代器
            dt = dict(key_values)  # 对key和values值进行字典拼接
            l.append(dt)  # 添加值进去l中
        return l


da_ta = read_xlsx('ex.xlsx').get_xlsx(0)  # 获取ex文件中的参数信息


@ddt  # 使用ddt
class logjump(unittest.TestCase):
    @data(*da_ta)
    @unpack
    def test_lojump(self, **tst):  # 需要用test命名才能用unittest的测试框架
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': tst['username'],
                'loginPwd': int(tst['pwd'])}  # 将键值对存放
        rps = requests.post(url=url, headers=headers, data=data)  # 传参
        print(rps.text)
        js = rps.json()  # 获取json值
        if js['msg'] == '登录成功！':  # 设定断言
            print('恭喜你接口登录成功')
        else:
            print('接口登录不成功')
        assert js['msg'] == '登录成功！'  # 捕获断言


if __name__ == '__main__':
    unittest.main()
