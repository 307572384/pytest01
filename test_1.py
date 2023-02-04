# Python自动化测试实战篇（1）读取xlsx中账户密码，unittest框架实现通过requests接口post登录网站请求，JSON判断登录是否成功
'通过引用封装的类方法来实现拼接项目的路径'
import os

'通过类方法来封装获取ex文件中的参数'
import xlrd  # 需要安装 版本的1.2左右即可 xlsx


class Get_xlsx:  # 定义一个类
    def __init__(self, file):  # 定义一个构造方法
        '''
        :param file: ex文件的路径 data.xlsx
        '''
        '打开指定文件获取指定文件中所有的参数'
        self.wokbook = xlrd.open_workbook(os.path.join('D:\pythonpj\pytest', file))  # 创建一个对象

    def get_ex(self, idex):  # 方法用来获取指定文件指定页中指定行列的值
        '通过sheet_by_index来获取指定文件索引对应的页，然后生成一个对象'
        sheet_idex = self.wokbook.sheet_by_index(idex)
        key = sheet_idex.row_values(0)  # 取第一行的值返回一个列表
        # print(key) #['username', 'pwd']
        l = []  # 定义一个空列表
        for i in range(1, sheet_idex.nrows):
            'nrows--方法是统计页中的行数'
            values = sheet_idex.row_values(i)
            # print(values)
            k_v = zip(key, values)  # zip函数拼接两个列表
            dit = dict(k_v)  # 然后通过字典类型转换为字典
            l.append(dit)  # 在添加到列表中存储
        # print(l)
        return l  # 返回给方法本身


if __name__ == '__main__':
    Get_xlsx('ex.xlsx').get_ex(0)
#
da_ta = Get_xlsx('ex.xlsx').get_ex(0)  # 获取ex文件中的参数信息
print(da_ta)  # [{'username': 'admin', 'pwd': 123456.0}, {'username': 'admin', 'pwd': 123457.0}]
import unittest, requests  # 导入单元框架
from ddt import ddt, data, unpack  # 导入ddt


@ddt  # ddt需要结合单元框架来完成
class Cms_logjump_ddt(unittest.TestCase):
    @data(*da_ta)
    @unpack
    def test_logjump(self, **dict):  # 定义一个测试用例 名称一定要test开头后面随意
        '登录的入参'
        url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'userAccount': dict['username'],
                'loginPwd': int(dict['pwd'])}  # 键取值存放
        reps = requests.post(url=url, headers=headers, data=data)
        print(reps.text)
        js = reps.json()
        if js['msg'] == '登录成功！':
            print('ok')
        else:
            print('no')
        assert js['msg'] == '登录成功！'
        self.assertEqual(js['msg'], '登录成功！')  # 匹配响应的值和实际预期的值是否一致
        self.assertIn(js['msg'], '登录成功！')  # x响应的值是否是预期指定的


if __name__ == '__main__':
    unittest.main()  # 引用框架中的所有用例
# import configparser
#
# import pytest
# import requests,unittest
# class Get_cofing_ini:#定义一个类
#     def __init__(self,file):
#         '''
#         :param file:  是ini文件的路径 C:\Pojmet\dcs81\dcs81_api\Cofing
#         '''
#         self.cf =configparser.ConfigParser()#创建对象
#         self.cf.read(file) #对象调用方法获取对应路径文件的参数
#     def get_ini_test(self,a,c):#定义一个方法获取节点变量的值
#         '''
#         :param a: 变量，传实参是节点名称
#         :param c: 变量，传实参是变量名称
#         :return:
#         '''
#         values =self.cf.get(a,c)
#         return values
# import os,time
# dcs81_path =os.path.abspath(os.path.dirname(__file__)) #获取包绝对路径
# # print(dcs81_path)#C:\Pojmet\dcs81\dcs81_api
# dcs81 =Get_cofing_ini(os.path.join(dcs81_path,'Config.ini')).get_ini_test('pro_path','dcs_path')
# # print(dcs81) #C:\Pojmet\dcs81
# '拼接一个存放ex文件包的路径'
# api_path=os.path.join(dcs81)
# print(dcs81)
# print(api_path)
# # print(api_path) #C:\Pojmet\dcs81\dcs81_api
# '封装一个测试报告的路径'
# ti_me =time.strftime('%Y-%m-%d-%H-%M-%S')
# # print(ti_me) #2023-02-01-14-36-28
# repot_path=os.path.join(api_path,ti_me+'repot.html')
# # print(repot_path)
# # print(repot_path) #C:\Pojmet\dcs81\dcs81_api\2023-02-01-14-37-23repot.html
# import unittest #导入单元框架
# class Cms(unittest.TestCase):#定义一个类继承单元框架测试类
#     @classmethod
#     def setUpClass(cls) -> None:
#         print('类的开始')
#     @classmethod
#     def tearDownClass(cls) -> None:
#         print('类的结束')
#     def setUp(self) -> None:
#         print('方法的开始')
#     def tearDown(self) -> None:
#         print('方法的结束')
#     def test_1(self):
#         print('测试用例1')
#     def test_2(self):
#         print('测试用例2')
# if __name__ == '__main__':
#     unittest.main()
# class Cms(unittest.TestCase):#定义一个类继承单元框架测试类
#     def test_1(self): #用例和用例是独立
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 123456}
#         reps=requests.post(url=url,headers=headers,data=data)
#         print(reps.text)
#     def test_2(self):
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 12345}
#         reps = requests.post(url=url, headers=headers, data=data)
#         print(reps.text)
# if __name__ == '__main__':
#     unittest.main()
# class Cms(unittest.TestCase):#定义一个类继承单元框架测试类
#     def test_1(self): #用例和用例是独立
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 123456}
#         reps=requests.post(url=url,headers=headers,data=data)
#         print(reps.text)
#     def test_2(self):
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 12345}
#         reps = requests.post(url=url, headers=headers, data=data)
#         print(reps.text)
#     def test_3(self):
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 12345}
#         reps = requests.post(url=url, headers=headers, data=data)
#         print(reps.text)
# if __name__ == '__main__':
#     suit =unittest.TestSuite()#创建一个容器对象
#     # suit.addTest(Cms('test_2')) #单条用例
#     suit.addTests([Cms('test_1'),Cms('test_2')]) #多条用例
#     run =unittest.TextTestRunner()#创建一个执行对象
#     run.run(suit) #通过执行对象调用方法执行选择容器中的用例
# from HTMLTestRunner3_New import HTMLTestRunner
# class Cms(unittest.TestCase):#定义一个类继承单元框架测试类
#     def test_1(self): #用例和用例是独立
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 123456}
#         reps=requests.post(url=url,headers=headers,data=data)
#         print(reps.text)
#     def test_2(self):
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 12345}
#         reps = requests.post(url=url, headers=headers, data=data)
#         print(reps.text)
# if __name__ == '__main__':
#     suit =unittest.TestSuite()#创建一个容器对象
#     # suit.addTest(Cms('test_2')) #单条用例
#     suit.addTests([Cms('test_1'),Cms('test_2')]) #多条用例
#     p =open(repot_path,'wb')#open打开文件把内容写入到此文件中 二进制转换
#     run =HTMLTestRunner(stream=p,title='Cms登录接口报告',
#                         description='执行概况如下',tester='小钱')
#     run.run(suit)
#
#
#
# from HTMLTestRunner3_New import HTMLTestRunner
# class Cms(unittest.TestCase):#定义一个类继承单元框架测试类
#     def test_1(self): #用例和用例是独立
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 123456}
#         reps=requests.post(url=url,headers=headers,data=data)
#         print(reps.text)
#     def test_2(self):
#         url = 'http://192.168.52.129:8080/cms/manage/loginJump.do'
#         headers = {'Content-Type': 'application/x-www-form-urlencoded'}
#         data = {'userAccount': 'admin', 'loginPwd': 12345}
#         reps = requests.post(url=url, headers=headers, data=data)
#         print(reps.text)
#
#
# def Cms_logjum():#定义一个函数
#     # 搜索当前项目中，指定的api_4.py文件中可执行的代码
#     discre=unittest.defaultTestLoader.discover(start_dir=api_path,
#                                                pattern='test_1.py')
#     p =open(repot_path,'wb')#open打开文件把内容写入到此文件中 二进制转换
#     run =HTMLTestRunner(stream=p,title='Cms登录接口报告',
#                             description='执行概况如下',tester='小钱')
#     run.run(discre) #运行搜索到的文件中的用例
# if __name__ == '__main__':
#     Cms_logjum() #函数调用函数自己
