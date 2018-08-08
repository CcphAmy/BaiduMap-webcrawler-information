# -*- coding: utf-8 -*- 

import requests
import os
import re
import csv
import json
import time

import wx
import wx.xrc

import frame

from bs4 import BeautifulSoup

class BaiduMap(object):
	"""docstring for BaiduMap"""
	def __init__(self):
		super(BaiduMap, self).__init__()
	
	def getCityData(self,cityName):

		try:
			webData = requests.get("http://map.baidu.com/?newmap=1&qt=cur&ie=utf-8&wd=" + cityName + "&oue=1&res=jc").text
			jsonData = json.loads(webData)
			# print(jsonData,end="\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

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

	def createAndWrite(self,fileName,rowHeader,rowData=[]):

		if os.path.exists(fileName):
			fileName = str(time.time()) + "_" + fileName

		csvFile = open(fileName,'w',newline='')
		writer  = csv.writer(csvFile)

		writer.writerow(rowHeader)
		if len(rowData) > 0:
			writer.writerows(rowData)
		csvFile.close()

	def getMapData(self,cityId,info_): 

		if cityId < 0 :
			return -1

		loopValue = 1
		loopCount = 1

		allData   = []

		qt        = "s"
		rn        = "10" 
		modNum    = "10"

		rowHeader = ['name','address','address_norm']
		

		while loopValue <= loopCount:

			getUrl    = "http://api.map.baidu.com/?qt=" + qt + "&c=" + str(cityId) + "&wd=" + info_ + "&rn=" + rn + "&pn=" + str(loopValue - 1) + "&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk7303&ak=E4805d16520de693a3fe707cdc962045";
			print(getUrl)

			webData   = requests.get(getUrl).text
			tempValue = int(re.search("\"total\":([\\s\\S]*?),",webData).group(1)) #数量

			if tempValue > 0:
				if loopValue == 1:
					modNum    = tempValue % 10 # 第一次
					if modNum > 0:
						loopCount = (int)(tempValue / 10 + 1)
					else :
						loopCount = (int)(tempValue / 10)
					print("总共需要循环：" + str(loopCount))

				reJson   = re.search("content\":([\\s\\S]*?),\"current_city",webData).group(1)
				jsonData = json.loads(reJson)
				# 数据处理
				print(str(loopValue) + ":" + str(len(jsonData)),end="")
				# print(jsonData)
				for x in range(0,len(jsonData)):
					try:
						# print(jsonData[x]['name'] + " " + jsonData[x]['address_norm'] + " " + jsonData[x]['addr'])
						tempArr = [jsonData[x]['name'],jsonData[x]['addr'],jsonData[x]['address_norm']]
						allData.append(tempArr)
					except Exception as e:
						print(jsonData[x])
						# exit()
					
				# 处理结束
				loopValue = loopValue + 1
			else :
				
				break

		if len(allData) > 0:
			print('ok ... writing file')
			rstr = r"[\/\\\:\*\?\"\<\>\|\$$]"
			print(allData)
			self.createAndWrite(str(cityId) + "_" + re.sub(rstr,"_",info_) + ".csv",rowHeader,allData)
			print("over")

		else :
			print('error content')

if __name__ == '__main__':

	app    = wx.App(False)
	frame1 = frame.MyFrame1(None)
	frame1.Show(True)
	app.MainLoop()
	exit()
	obj   = BaiduMap()
	obj.getMapData(obj.getCityData("潮州"),"古巷镇$$美食")

