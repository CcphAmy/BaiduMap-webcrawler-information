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
import threading

from wx.lib.pubsub import pub
from bs4 import BeautifulSoup

class BaiduMap():
	"""docstring for BaiduMap"""
	def __init__(self):
		super(BaiduMap, self).__init__()

	def getCityData(self,cityName):

		try:
			webData = requests.get("http://map.baidu.com/?newmap=1&qt=cur&ie=utf-8&wd=" + cityName + "&oue=1&res=jc").text
			jsonData = json.loads(webData)

			if 'weather' in jsonData: #存在天气预报的情况下
				weatherData = json.loads(jsonData['weather'])
				wx.CallAfter(pub.sendMessage, "updateText", content=weatherData['OriginQuery']+" PM2.5:"+weatherData['pm25']+weatherData['weather0']+"["+weatherData['temp0']+"]["+weatherData['wind0']+"]")
			if 'cur_area_id' in jsonData:
				wx.CallAfter(pub.sendMessage, "updateText", content="城市id:" + str(jsonData['cur_area_id']))
				return jsonData['cur_area_id']
			else:
				return -1

		except Exception as e:
			raise

	def createAndWrite(self,fileName,rowHeader,rowData=[]):

		if os.path.exists(fileName):
			fileName = str(time.time()) + "_" + fileName
		wx.CallAfter(pub.sendMessage, "updateText", content="writing:" + fileName)
		csvFile = open(fileName,'w',newline='')
		writer  = csv.writer(csvFile)

		writer.writerow(rowHeader)
		if len(rowData) > 0:
			writer.writerows(rowData)
		csvFile.close()

	def checkArr(self,checkArr,argv):
		pass

	def getMapData(self,cityId,info_): 

		if cityId < 0 :
			return -1

		loopValue = 1
		loopCount = 1

		allData   = []

		qt        = "s"
		rn        = "10" 
		modNum    = "10"

		while loopValue <= loopCount:

			getUrl    = "http://api.map.baidu.com/?qt=" + qt + "&c=" + str(cityId) + "&wd=" + info_ + "&rn=" + rn + "&pn=" + str(loopValue - 1) + "&ie=utf-8&oue=1&fromproduct=jsapi&res=api&callback=BMap._rd._cbk7303&ak=E4805d16520de693a3fe707cdc962045";

			webData   = requests.get(getUrl).text
			tempValue = int(re.search("\"total\":([\\s\\S]*?),",webData).group(1)) #数量

			print(getUrl)
			if tempValue > 0:
				if loopValue == 1:
					modNum    = tempValue % 10 # 第一次
					if modNum > 0:
						loopCount = (int)(tempValue / 10 + 1)
					else :
						loopCount = (int)(tempValue / 10)

					wx.CallAfter(pub.sendMessage, "updateText", content="总共需要循环：" + str(loopCount))

				reJson   = re.search("content\":([\\s\\S]*?),\"current_city",webData).group(1)
				jsonData = json.loads(reJson)
				# 数据处理
				wx.CallAfter(pub.sendMessage, "updateText", content="retrieving: page " + str(loopValue))
				# print(jsonData)
				for x in range(0,len(jsonData)):
					try:
						# print(jsonData[x]['name'] + " " + jsonData[x]['address_norm'] + " " + jsonData[x]['addr'])
						# 
						# 得来个信息校验
						# 
						tempArr = [jsonData[x]['name'],jsonData[x]['addr']] # 名称 地址
						tempArr.append(jsonData[x]['ext']['detail_info']['phone']) 

						tempArr.append(jsonData[x]['ext']['detail_info']['point']['x'])
						tempArr.append(jsonData[x]['ext']['detail_info']['point']['y'])
						tempArr.append(jsonData[x]['address_norm']) # 详细地址
						allData.append(tempArr)
					except Exception as e:
						print(str(e))
						# print(jsonData[x])
						# exit()
					
				# 处理结束
				loopValue = loopValue + 1
			else :
				break

		if len(allData) > 0:
			wx.CallAfter(pub.sendMessage, "updateText", content="ok . writing file!!!")

			rowHeader = ['name','address','phone','point_x','point_y','address_norm']
			self.createAndWrite(str(cityId) + "_" + re.sub(r"[\/\\\:\*\?\"\<\>\|\$$]","_",info_) + ".csv",rowHeader,allData)

			wx.CallAfter(pub.sendMessage, "updateText", content="over")
		else :
			wx.CallAfter(pub.sendMessage, "updateText", content="error content")

class windowGUI(frame.MyFrame1):
	"""docstring for windowGUI"""
	obj = BaiduMap()
	starting = False
	def __init__(self,parent):
		super(windowGUI, self).__init__(parent)
		pub.subscribe(self.setStBool, "setStBool")

	def __del__(self):
		pass

	def checkCity( self, event ):
		if int(self.obj.getCityData(self.m_comboBox2.GetValue())) > 0:
			wx.MessageDialog(None, u"信息正确!", u"城市验证",wx.ICON_QUESTION).ShowModal()
		else :
			wx.MessageDialog(None, u"验证失败!", u"城市验证",wx.ICON_QUESTION).ShowModal()

	def startJob( self, event ):

		if not self.starting:

			cityText     = self.m_comboBox2.GetValue() # 城市
			locationText = self.m_textCtrl4.GetValue() # 地点
			articleText  = self.m_textCtrl5.GetValue() # 物品

			if cityText.strip():
				if articleText.strip():
					if  locationText.strip():
						articleText = locationText + "$$" + articleText
					self.starting = True
					newThread = webThread(1,"Thread-1",1,cityText,articleText)
					newThread.start()
				else :
					wx.MessageDialog(None, u"检索物不能为空", u"Tip:",wx.ICON_QUESTION).ShowModal()
			else :
				wx.MessageDialog(None, u"城市不能为空", u"Tip:",wx.ICON_QUESTION).ShowModal()
		else : 
			wx.MessageDialog(None, u"线程运行中", u"Tip:",wx.ICON_QUESTION).ShowModal()

	def setStBool(self, msg) :
		self.starting = msg

class webThread(threading.Thread):
	"""docstring for webThread"""
	def __init__(self,threadID, name,counter,cityText,articleText):

		super(webThread, self).__init__()
		threading.Thread.__init__(self)
		self.threadID    = threadID
		self.name        = name
		self.counter     = counter
		self.cityText    = cityText
		self.articleText = articleText

	def run(self):
		obj = BaiduMap()
		obj.getMapData(obj.getCityData(self.cityText),self.articleText)

	def __del__(self):
		wx.CallAfter(pub.sendMessage, "setStBool", msg=False)

if __name__ == '__main__':

	app    = wx.App(False)
	frame1 = windowGUI(None)
	frame1.Show(True)
	app.MainLoop()