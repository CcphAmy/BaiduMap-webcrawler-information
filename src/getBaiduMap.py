import requests
import os
import re
import json
from bs4 import BeautifulSoup

class BaiduMap(object):
	"""docstring for BaiduMap"""
	def __init__(self):
		super(BaiduMap, self).__init__()

	#城市获取数据
	def getCityData(self,cityName):
		# http://map.baidu.com/?newmap=1&qt=cur&ie=utf-8&wd=  &oue=1&res=jc
		try:
			webData = requests.get("http://map.baidu.com/?newmap=1&qt=cur&ie=utf-8&wd=" + cityName + "&oue=1&res=jc").text
			jsonData = json.loads(webData)
			print(jsonData,end="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


			if 'weather' in jsonData: #存在天气预报的情况下
				weatherData = json.loads(jsonData['weather'])
				print(weatherData['OriginQuery']," PM2.5:",weatherData['pm25'],weatherData['weather0'],"[",weatherData['temp0'],"][",weatherData['wind0'],"]",end=' ')

			if 'cur_area_id' in jsonData:
				print("城市id:",jsonData['cur_area_id'])
				return jsonData['cur_area_id']
			else:
				return -1

		except Exception as e:
			raise

	def getMapData(self,cityId,info_): 

		qt        = "s"
		rn        = "10"
		modNum    = "10"
		loopValue = 1

		if cityId < 0 :
			return -1

		getUrl   = "http://api.map.baidu.com/?qt=" + qt + "&c=" + str(cityId) + "&wd=" + info_ + "&rn=" + rn + "&pn=1" + "&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk7303&ak=E4805d16520de693a3fe707cdc962045";
		webData  = requests.get(getUrl).text
		# print(webData)
		loopNum = re.search("\"total\":([\\s\\S]*?),",webData).group(1) #数量
		reJson = re.search("content\":([\\s\\S]*?),\"current_city",webData).group(1)
		print(loopNum)
		jsonData = json.loads(reJson)
		print(jsonData)

if __name__ == '__main__':
	obj = BaiduMap()
	obj.getMapData(obj.getCityData("潮州"),"酒店")
