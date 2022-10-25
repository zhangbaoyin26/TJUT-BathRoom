from time import time


# 用户数据
# 不知道loginid和token的，填写12-13行的userName， psd
user = {
	'loginid': '',
	'token': '',
	'User-Agent': 'Mozilla/5.0 (Linux; Android 12; M2102K1AC Build/SKQ1.211006.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4317 MMWEBSDK/20220805 Mobile Safari/537.36 MMWEBID/8107 MicroMessenger/8.0.27.2220(0x28001B59) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64',
}
# 不知道loginid和token的，填这个
userName = ''
psd = ''

# 每次最大请求次数 建议不超过600
max_count = 100
# 每次请求中间间隔 = (base_time+random.uniform(0.5, 1)) （秒）
base_time = 0

#global value 不要修改
firstBookTime = int(1000*time())-3000
listBookTime = firstBookTime - 4
bookorderid = -1
