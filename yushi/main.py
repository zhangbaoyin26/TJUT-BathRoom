from time import sleep, time, strftime, localtime
import requests
import random
from signIn import signIn
from checkBook import printIsBooked
from checkBook import checkBook
import config

true = True
null = None


baseUrl = 'http://ligong.deshineng.com:8082/brmclg/login.html?v=12&func=null&sn=null'


def postPage(url: str) -> dict:
	headers = {
		'Host': 'ligong.deshineng.com:8082',
		'loginid': config.user.get('loginid'),
		'token': config.user.get('token'),
		'User-Agent': config.user.get('User-Agent'),
		'Referer': 'http://ligong.deshineng.com:8082/brmclg/html/main.html?v=3'
	}
	response = requests.post(url, headers=headers)
	return eval(response.text)


def getPage(url: str) -> dict:
	headers = {
		'Host': 'ligong.deshineng.com:8082',
		'loginid': config.user.get('loginid'),
		'token': config.user.get('token'),
		'User-Agent': config.user.get('User-Agent'),
		'Referer': 'http://ligong.deshineng.com:8082/brmclg/html/main.html?v=3'
	}
	response = requests.get(url, headers=headers)
	return eval(response.text)


def spiderRoomMsg(url):
	res = postPage(url)
	data = res.get('data').get('bookStatusList')
	for value in data:
		print('id:', value.get('id'), end=', ')
		print('remain:', value.get('remain'), end=', ')
		print('period:', value.get('period'), end='\n')
	return res


def BOOL_check_input(dat: dict, id_num: int) -> bool:
	BOOL_IS_FOUND = False
	for value in dat:
		if id_num != int(value.get('id')):
			continue
		else:
			BOOL_IS_FOUND = True
	if BOOL_IS_FOUND:
		return True
	else:
		return False


def inputId(res) -> int:
	input_id = int(input("输入预约id(0重新查询): "))
	while not BOOL_check_input(res.get('data').get('bookStatusList'), input_id):
		if input_id == 0:
			spiderRoomMsg('http://ligong.deshineng.com:8082/brmclg/api/bathRoom/listBookStatus?time=' + str(
							int(1000 * time())) + '&bathroomid=16')
		input_id = int(input("输入预约id(0重新查询): "))
	return input_id


def Booking(input_id) -> int:
	print('Found BathRoom id:', input_id)
	url = 'http://ligong.deshineng.com:8082/brmclg/api/bathRoom/bookOrder?time=' + str(
		int(1000 * time())) + '&bookstatusid=' + str(input_id)
	resp = postPage(url)
	book_count = 0  # 每次请求不超过max_count次
	while (book_count < config.max_count) and (resp.get('code') == 200) and (resp.get('data').get('succeed') == 'N'):
		resp = postPage(url)
		sleep_time = config.base_time + random.uniform(0.3, 0.7)
		sleep(sleep_time)
		print(book_count, 'Sleep:' + str(int(1000 * sleep_time)) + 'ms')
		book_count += 1
	# 打印预约状态
	if (book_count < config.max_count) and (resp.get('code') != 200):
		print('ERR:statue_code')
		return 0
	if (book_count < config.max_count) and (resp.get('code') == 200) and (resp.get('data').get('succeed') == 'Y'):
		print('Booking_Succeed!')
		print('Time:', resp.get('data').get('bookOrderList')[0].get('period'))
		return resp.get('data').get('bookOrderList')[0].get('id')


def cancelBook(id: int) -> bool:
	url = 'http://ligong.deshineng.com:8082/brmclg/api/bathRoom/cancelOrder?time=' + str(
		int(1000 * time())) + '&bookorderid=' + str(id)
	resp = postPage(url)
	if (resp.get('message') == 'Ok') and (resp.get('code') != 200):
		print('Fail to cancel')
		return False
	if (resp.get('message') == 'Ok') and (resp.get('code') == 200) and (resp.get('data').get('succeed') == 'Y'):
		print('Cancel_Succeed!')
		return True



def main():
	# 检查是否存在token
	if config.user.get('token') == '':
		if config.userName == '' and config.psd == '':
			return
		else:
			config.user['token'] = signIn()
	# 开始主程序
	t = int(strftime('%H%M%S', localtime()))
	if (t > 220000) or (t < 65959):
		print("此时段不能预约")
	# 符合预约时段
	else:
		config.firstBookTime = int(1000 * time())
		url_list = 'http://ligong.deshineng.com:8082/brmclg/api/bathRoom/listBookStatus?time=' + str(
			config.firstBookTime) + '&bathroomid=16'
		print(url_list)
		# 爬取浴室信息
		resp = spiderRoomMsg(url_list)
		# 检查是否有预约的没有使用的浴室
		# 开始预约
		if not printIsBooked():
			BOOL_ISCANCLE = eval(input("是否取消预约： "))
			if BOOL_ISCANCLE:
				cancelBook(config.bookorderid)
				# 用户输入预约时间段id
				input_id = inputId(resp)
				# 检查成功
				config.bookorderid = Booking(input_id)
				BOOL_ISCANCLE = eval(input("是否取消预约： "))
				if BOOL_ISCANCLE:
					cancelBook(config.bookorderid)
		else:
			# 用户输入预约时间段id
			input_id = inputId(resp)
			# 检查成功
			config.bookorderid = Booking(input_id)
			BOOL_ISCANCLE = eval(input("是否取消预约： "))
			if BOOL_ISCANCLE:
				cancelBook(config.bookorderid)




if __name__ == "__main__":
	main()