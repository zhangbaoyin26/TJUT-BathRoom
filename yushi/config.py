from time import time


# 用户数据
user = {
	'loginid': '58922',
	'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NzA0ODcwMDM0NTgsInBheWxvYWQiOiJ7XCJpZFwiOjU4OTIyLFwiY29kZVwiOlwiMjAyMTM5MjdcIixcInBhc3N3b3JkXCI6XCJiYTAyMTYwNzM2NTZjMTVlMjIzNTZjNjY4MzA4NjFkOVwiLFwic3R1ZGVudFwiOm51bGx9In0.izyDfsq9msZvNckPvVzubTSvoNaYxvHuQcbSZlDAazs',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102K1AC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220805 Mobile Safari/537.36 MMWEBID/8107 MicroMessenger/8.0.27.2220(0x28001B59) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
}
userName = '20213927'
psd = '213927'

# 每次最大请求次数
max_count = 100
# 每次请求中间间隔+random.uniform(0.5, 1)
base_time = 0

#global value int(1000*time())
firstBookTime = int(1000*time())
listBookTime = firstBookTime - 4
bookorderid = -1

