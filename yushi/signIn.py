from hashlib import new


def signIn():
	url = 'http://ligong.deshineng.com:8082/brmclg/login.html?v=12&func=null&sn=null'
	psd = input()
	psd = new('md5', )