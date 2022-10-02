from time import sleep, time
import requests
import random
import config


true = True
null = None


def getPage(url: str) -> dict:
	headers = {
		'Host': 'ligong.deshineng.com:8082',
		'loginid': config.user.get('loginid'),
		'token': config.user.get('token'),
		'User-Agent': config.user.get('User-Agent'),
		'Referer': 'http://ligong.deshineng.com:8082/brmclg/html/main.html?v=3'
	}
	response = requests.post(url, headers=headers)
	return eval(response.text)


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


def cancelBook():
	url = 'http://ligong.deshineng.com:8082/brmclg/api/bathRoom/cancelOrder?time='+str(int(1000*time()))+'&bookorderid=5018797'



if __name__ == "__main__":
	baseUrl = 'http://ligong.deshineng.com:8082/brmclg/api/bathRoom/'
	url_list = 'listBookStatus?'
	url_book = 'bookOrder?'
	local_time = int(1000*time())
	url = baseUrl+url_list+'time='+str(local_time)+'&'+'bathroomid=16'
	print(url)

	# 爬取浴室信息
	resp = getPage(url)
	data = resp.get('data').get('bookStatusList')
	for value in data:
		print('id:', value.get('id'), end=', ')
		print('remain:', value.get('remain'), end=', ')
		print('period:', value.get('period'), end='\n')

	# 用户输入预约时间段id
	input_id = int(input("输入预约id: "))
	while not BOOL_check_input(data, input_id):
		input_id = int(input("输入预约id: "))

	# 开始预约
	print('Found BathRoom id:', input_id)
	url = baseUrl+url_book+'time='+str(local_time)+'&'+'bookstatusid='+str(input_id)
	resp = getPage(url)
	book_count = 0		# 每次请求不超过max_count次
	while (book_count < config.max_count) and (resp.get('code') == 200) and (resp.get('data').get('succeed') == 'N'):
		resp = getPage(url)
		sleep_time = config.base_time + random.uniform(0.3, 0.7)
		sleep(sleep_time)
		print(book_count, 'Sleep:'+str(int(1000*sleep_time))+'ms')
		book_count += 1

	# 打印预约状态
	if (book_count < config.max_count) and (resp.get('code') != 200):
		print('ERR:statue_code')
	if (book_count < config.max_count) and (resp.get('code') == 200) and (resp.get('data').get('succeed') == 'Y'):
		print('Booking_Succeed!')
		print('Time:', resp.get('data').get('bookOrderList')[0].get('period'))
