import requests

url = 'http://jszx.cuit.edu.cn/Logo/F_118.jpg'  # 这个是计算中心的图
req = requests.get(url)

#保存到本地
with open('logo.png', 'wb') as file:
    file.write(req.content)

