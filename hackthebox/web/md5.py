import requests
import re
import hashlib

while(1):
	url="http://docker.hackthebox.eu:34401/"
	r=requests.session()
	res=r.get(url)
	code=re.findall("[a-zA-Z0-9]{20}",res.text)
	code=hashlib.md5(str(code)[2:-2].encode('utf-8')).hexdigest()  #[2:-2]作用：将findall取回的list类型转化为str
	                                                               #等同于list[0]或者formula = "".join(formula)
	data={"hash":code}
	result=r.post(url,data=data)
	print(result.text)
