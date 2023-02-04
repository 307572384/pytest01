import pymysql

db = pymysql.connect(host='192.168.52.129',  # 数据库的ip地址
                     user='root',  # 连接名
                     passwd='123456',  # 你的密码
                     database='test',  # 数据库名称
                     port=3306)  # 端口号
curs = db.cursor()
# 查询数据库
# sql1 ='select name,dept_name from abs_incoming ;'
# curs.execute(sql1)
# print(curs.fetchall())
# print(curs.fetchone())
# 1.列出每个部门里面有那些员工及部门名称
# sql1 ='select name,dept_name from dept left join emp on dept.dept1 = emp.dept2;'
# curs.execute(sql1)
# print(curs.fetchall())

# 2.运维部门的收入总和''
# sql1 ='select sum(incoming) from dept left join emp on dept.dept1 = emp.dept2 where dept_name="yunwei";'
# curs.execute(sql1)
# print(curs.fetchall())
# 3.HR部入职员工的员工号
# sql1 ='select id from dept left join emp on dept.dept1 = emp.dept2 where dept_name="zhubo";'
# curs.execute(sql1)
# print(curs.fetchall())
# 4.财务部门收入超过5000元的员工姓名
# sql1 ='select name from dept left join emp on dept.dept1 = emp.dept2 where dept_name="chaiwu" and incoming>3000;'
# curs.execute(sql1)
# print(curs.fetchall())
# 5.找出销售部收入最低的员工的入职时间；
# sql1 ='select min(incoming),worktime from dept left join emp on dept.dept1 = emp.dept2 where dept_name="zhubo" GROUP BY worktime;'
# curs.execute(sql1)
# print(curs.fetchall())
# 6.找出年龄小于平均年龄的员工的姓名，ID和部门名称
# sql1 ='select name,id,dept_name from dept left join emp on dept.dept1 = emp.dept2 where age<(select avg(age) from emp);'
# curs.execute(sql1)
# print(curs.fetchall())
# 7.列出每个部门收入总和高于10000的部门名称
# sql1 ='select dept_name from dept left join emp on dept.dept1 = emp.dept2 group by dept_name having sum(incoming)>5000;'
# curs.execute(sql1)
# print(curs.fetchall())
# 8.查出财务部门工资少于10000元的员工姓名
# sql1 ='select name from dept left join emp on dept.dept1 = emp.dept2 where incoming<10000 and dept_name = "chaiwu";'
# curs.execute(sql1)
# print(curs.fetchall())
# 9.求收入最低的员工姓名及所属部门名称\
# sql1 ='select name,dept_name from dept left join emp on dept.dept1 = emp.dept2 where incoming=(select max(incoming) from emp join dept on emp.dept2 = dept.dept1) ;'
# curs.execute(sql1)
# print(curs.fetchall())
# 10.求员工收入小于8000元的员工部门编号名字及其部门名称；
# sql1 ='select name,id,dept_name from dept left join emp on dept.dept1 = emp.dept2 where incoming<5000 '
# curs.execute(sql1)
# print(curs.fetchall())
# sql1='select * from abs_incoming where age=20;'
# curs.execute(sql1)
# print(curs.fetchall())
# print(curs.fetchone())
# 插入数据
# sql='insert into abs_incoming(name,age,incoming)values("zhangsan",20,8000);'
# curs.execute(sql)
# db.commit()
# db.close()
# sql1 = 'insert into abs_incoming(name,age,incoming)values(%s,%s,%s);'
# n_ame='zhangsanlei'
# a_age='26'
# i_incoming='7500'
# curs.execute(sql1,(n_ame,a_age,i_incoming))
# db.commit()
# db.close()
# sql3 = 'insert into abs_incoming(name,age,incoming)values(%s,%s,%s);'
# data=[('zhangersan','18','4200'),('leishen','20','3600'),('zhangwu','22','5400')]
# curs.executemany(sql3,data)
# db.commit()
# db.close()
# #更改数据
# sql ='update abs_incoming set age = 30 where name="zhangwu";'
# curs.execute(sql)
# db.commit()
# db.close()
# sql = 'update abs_incoming set age =40 where name =%s'
# na = "leishen"
# curs.execute(sql,[na])
# db.commit()
# db.close()
# 删除数据
# sql4 = 'delete from abs_incoming where name="leishen";'
# curs.execute(sql4)
# db.commit()
# db.close()
# sql4 = 'delete from abs_incoming where name=%s;'
# s_name = "zhangersan"
# curs.execute(sql4,[s_name])
# db.commit()
# db.close()
# 1、查询1946班的成绩信息
# sql1 ='select * from grade where class=1946 ;'
# curs.execute(sql1)
# print(curs.fetchall())
# 2，查询1944班，语文成绩大于60小于90的成绩信息
# sql1 ='select chinese from grade where class=1944 and 60<chinese<90  ;'
# curs.execute(sql1)
# print(curs.fetchall())
# 3，查询学生表中1到6行的数据
# sql1 ='select * from grade limit 1,6 ;'
# curs.execute(sql1)
# print(curs.fetchall())
# # 4，显示1944班英语成绩为90，数学成绩为40的姓名与学号,
# sql1 ='select sid,name from grade where english=90 and math =40 ;'
# curs.execute(sql1)
# print(curs.fetchall())
# # 5，查询出1946班成绩并且按英语成绩
# sql1 ='select chinese,math,english from grade where class=1946 ;'
# curs.execute(sql1)
# print(curs.fetchall())
# # 6、求出每个班级英语成绩总分
# sql1 ='select sum(english),class from grade group by class ;'
# curs.execute(sql1)
# print(curs.fetchall())
# 7、求出每个班英语成绩最高的那个人的姓名和班级名称
# sql1 ='select name,class from grade where (class,english)in(select class,MAX(english)from grade group by class);'
# curs.execute(sql1)
# print(curs.fetchall())
# 8、英语、语文二科分数都大于60分的人名和年纪
# sql1 ='select name,age from grade where english>60 and chinese>60 ;'
# curs.execute(sql1)
# print(curs.fetchall())
# 9、求出语文分数高于60且其它任何一科目大于60分的人和班级
# sql1 ='select name,class from grade where chinese>60 and(math>60 or english>60) ;'
# curs.execute(sql1)
# print(curs.fetchall())
# 10、统计每个班的人数
# sql1 ='select count(class),class from grade group by class;'
# curs.execute(sql1)
# print(curs.fetchall())
# 1.查询出学习成绩60分以上的学生姓名与成绩与学科；
# sql1 ='select name,grade,cname from a,b,c where a.id = b.id and c.bid = b.bid and grade >60;'
# curs.execute(sql1)
# print(curs.fetchall())
# 2.查询姓名以qi结尾的学生姓名及其任课老师姓名
# sql1 ='select name,teacher from a,b,c where a.id = b.id and c.bid = b.bid and name like "%qi";'
# curs.execute(sql1)
# print(curs.fetchall())
# 3.选修课名为english的学生学号与姓名;
# sql1 ='select avg(grade),cname  from a,b,c where a.id = b.id and c.bid = b.bid group by cname;'
# curs.execute(sql1)
# print(curs.fetchall())
# 4.选修课号为c1的学生学号；
# 5.请问每科各有那些学生求姓名成绩；
# 6.请问70分以上的学生姓名及学科；
# 7.请问考试不及格的考生姓名以及科目名称；
# 8.找出所有科目中最高分的学生姓名成绩
# 9.各个科目的平均成绩各是多少；
# 10.显示出参加考试的学生的学号和姓名；
