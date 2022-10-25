import json
import requests
from hashlib import new
from time import time
import config


true = True
null = None


def signIn() -> str:
	postUrl = 'http://ligong.deshineng.com:8082/brmclg/api/logon/login?time=' + str(int(1000*time()))
	headers = {
		'Host': 'ligong.deshineng.com:8082',
		'Connection': 'keep-alive',
		'Accept': 'application/json, text/javascript, */*; q=0.01',
		'X-Requested-With': 'XMLHttpRequest',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
		'Content-Type': 'application/json',
		'Origin': 'http://ligong.deshineng.com:8082',
		'Referer': 'http://ligong.deshineng.com:8082/brmclg/login.html?v=12&func=null&sn=null',
		'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5',
		'Accept-Encoding': 'gzip, deflate',
		'Content-Length': '65'
	}
	user = config.userName
	psd = new('md5', config.psd.encode('utf-8')).hexdigest()
	js = {"code": user, "password": psd}
	data = json.dumps(js)
	response = requests.post(url=postUrl, headers=headers, data=data)
	response = eval(response.text)
	print(response.get('data').get('token'))
	return str(response.get('data').get('token'))



'''
{"message":"Ok",
"code":200,
"data":{
	"bookOrderList":[],
	"loginid":58922,
	"student":{
		"id":58922,
		"code":"20213927",
		"name":"20213927",
		"password":"",
		"sex":"M",
		"state":true,
		"email":null,
		"phone":null,
		"cardNo":20213927,
		"role":""
	},
	"succeed":"Y",
	"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzQyMTE1ODc3MjIsInBheWxvYWQiOiJ7XCJpZFwiOjU4OTIyLFwiY29kZVwiOlwiMjAyMTM5MjdcIixcInBhc3N3b3JkXCI6XCJiYTAyMTYwNzM2NTZjMTVlMjIzNTZjNjY4MzA4NjFkOVwiLFwic3R1ZGVudFwiOm51bGx9In0.wpGeR3r9vW2V2Reo9L_KPLS8_YwlG5DiTML1FOf9J-8"}
}
'''