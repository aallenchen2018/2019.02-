#coding=utf-8
import pymongo
conn=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=conn.toto  #名字叫toto的数据库, 下面建立一个叫做jianli的表格

while 1:
	chose=input('1-查询;2-增加:3-删减;4-更新;5-预览表格')
	#查询
	if chose =='1':
		chosefind=input('输入名字')
		namefind=db.jianli.find({'name':chosefind},{'_id':0})
		for i in namefind:
			print(i)
	#增加(如果表中有此名字,不会添加;否则添加)
	elif chose=='2':
		add=input('输入名字')
		check=db.jianli.find({'name':add})
		if check.count()!=0:
			print('此名字已有')
		else:
			add_tel=int(input('输入电话'))
			add_exp=int(input('输入经历'))
			db.jianli.insert({'name':add,'tel':add_tel,'exp':add_exp})		
	#删减(如果表中无此名字,不会删除;否则删除)
	elif chose=='3':
		
		del2=input('输入名字')
		check=db.jianli.find({'name':del2})
		if check.count()!=0:
			db.jianli.remove({'name':del2})
		else:
			print('name not exists')

	#修改
	elif chose=='4':
		update_name=input('输入修改的名字')
		update_tel=int(input('输入修改的电话'))
		update_exp=int(input('输入修改的经历'))	
		db.jianli.update({'name':update_name},{'$set':{'tel':update_tel,'exp':update_exp}})
	#阅览
	elif chose=='5':
		阅览=db.jianli.find({},{'_id':0})
		for i in 阅览:
			print(i)
	else:
		print('please chose between 1-5')
