import requests
from time import time
import config


true = True
null = None


def checkBook() -> dict:
	url = 'http://ligong.deshineng.com:8082/brmclg/api/bathRoom/getBookOrderList?time=' + str(int(1000*time())) + '&_=' + str(config.listBookTime)
	headers = {
		# GET http://ligong.deshineng.com:8082/brmclg/api/bathRoom/getBookOrderList?time=1666446801353&_=1666446741799 HTTP/1.1
		'Host': 'ligong.deshineng.com:8082',
		'Proxy-Connection': 'keep-alive',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'X-Requested-With': 'XMLHttpRequest',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
		'loginid': config.user.get('loginid'),
		'token': config.user.get('token'),
		'Referer': 'http://ligong.deshineng.com:8082/brmclg/html/main.html?v=3',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
		'Accept-Encoding': 'gzip, deflate'
		}
	resp = requests.get(url=url, headers=headers)
	config.listBookTime += 1
	resp = eval(resp.text)
	if not resp.get('data').get('bookOrderList'):
		# 未预约过
		bookExist = False
		bookID = ""
		period = ""
		createTime = ""
	else:
		# 有预约过
		if resp.get('data').get('bookOrderList')[0].get('enterTimeStr') is not None:
			# 有预约且未使用
			bookExist = True
		else:
			# 有预约但是使用过
			bookExist = False
		bookID = resp.get('data').get('bookOrderList')[0].get('id')
		period = resp.get('data').get('bookOrderList')[0].get('period')
		createTime = resp.get('data').get('bookOrderList')[0].get('createTimeStr')
	return {
		'bookExist': bookExist,
		'bookID': bookID,
		'period': period,
		'createTime': createTime
	}


def printIsBooked() -> bool:
	resp = checkBook()
	config.bookorderid = resp.get('bookID')
	if not resp.get('bookExist'):
		canBook = True
		if resp.get('bookID') == "":
			print('你还没有预约，可以进行预约')
		else:
			print('已使用预约：\n' + str({'bookID': resp.get('bookID'), 'period': resp.get('period'), 'createTime': resp.get('createTime')}))
	else:
		canBook = False
		print('已有未使用的预约', end=':')
		print(str({'bookID': resp.get('bookID'), 'period': resp.get('period'), 'createTime': resp.get('createTime')}))
		print('不能再次预约')
	return canBook



'''
{"message":"Ok",
"code":200,
"data":{
	"bookOrderList":[
		{
			"bookID":5271924,
			"bathRoomId":16,
			"studentId":58922,
			"status":"0",
			"period":"22:15-22:30",
			"bookStatusId":677,
			"bathRoomName":"北区男浴室",
			"periodStartTime":1666448100000,
			"periodEndTime":1666449000000,
			"enterTime":null,
			"leaveTime":null,
			"cardNo":20213927,
			"orderNo":"2148892",
			"studentName":"20213927",
			"category":"A",
			"createTime":1666447551000,
			"enterTimeStr":"",
			"leaveTimeStr":"",
			"createTimeStr":"2022-10-22 22:05:51"
		},
		{
			"bookID":5270958,
			"bathRoomId":16,
			"studentId":58922,
			"status":"2",
			"period":"21:15-21:30",
			"bookStatusId":477,
			"bathRoomName":"北区男浴室",
			"periodStartTime":1666444500000,
			"periodEndTime":1666445400000,
			"enterTime":1666444645000,
			"leaveTime":null,
			"cardNo":20213927,
			"orderNo":"2147926",
			"studentName":"20213927",
			"category":"A",
			"createTime":1666444141000,
			"enterTimeStr":"2022-10-22 21:17:25",
			"leaveTimeStr":"",
			"createTimeStr":"2022-10-22 21:09:01"
		}
	],
	"classRoomOrderList":[]
	}
}

'''
