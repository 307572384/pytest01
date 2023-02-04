# name = 'admin'
# pwd = '123456'
# a = input('输入账号')
# count =0
# if a ==name:
#     while count < 3:
#         pd = input('请输入密码')
#         if pd == pwd:
#             count=3
#             print('登录成功')
#             break;
#         else:
#             count+=1
#             print('密码错误，请重试')
#     else:
#         print('输入错误超过3次，退出程序')
#         quit()
#
def cnl():
    year_num = 0
    year = 18
    count = 0
    while year_num != year:
        year_num = int(input('告诉我年龄：'))
        if year_num != year:
            print('你猜错了;')
            count += 1
        if count >= 3:
            jus = input('你已经错了三次是否要继续？（y/Y or n/N)')
            if jus.upper() == 'Y':
                count = 0
            else:
                return
        if year_num == year:
            print("你猜对了")
            return


cnl()
