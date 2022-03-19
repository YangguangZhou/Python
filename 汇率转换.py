import urllib.request
import re
srt_usd = input("请输入美元：")
url = "https://huobiduihuan.51240.com/?f=USD&t=CNY&j="+ srt_usd +""
result = urllib.request.urlopen(url)
data = result.read().decode("utf8")
pat = re.compile(r'color:#CC0000;">(.*?)</span>')
res = re.findall(pat,data)
print(res[1]+"人民币")