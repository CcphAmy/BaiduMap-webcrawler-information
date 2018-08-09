# -*- coding: utf-8 -*- 

import wx
import wx.xrc

from wx.lib.pubsub import pub
class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"百度地图采集器", pos = wx.DefaultPosition, size = wx.Size( 450,431 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )
		
		self.m_staticText5.SetFont( wx.Font( 1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u" * 选择城市:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		
		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.m_staticText2.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer3.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		m_comboBox2Choices = [u"北京",u"上海",u"天津",u"重庆",u"合肥",u"安庆",u"蚌埠",u"亳州",u"巢湖",u"池州",u"滁州",u"阜阳",u"淮北",u"淮南",u"黄山",u"六安",u"马鞍山",u"宿州",u"铜陵",u"芜湖",u"宣城",u"福州",u"龙岩",u"南平",u"宁德",u"莆田",u"泉州",u"三明",u"厦门",u"漳州",u"兰州",u"白银",u"定西",u"甘南州",u"嘉峪关",u"金昌",u"酒泉",u"临夏州",u"平凉",u"庆阳",u"天水",u"武威",u"张掖",u"广州",u"潮州",u"东莞",u"佛山",u"河源",u"惠州",u"江门",u"揭阳",u"茂名",u"梅州",u"清远",u"汕头",u"汕尾",u"韶关",u"深圳",u"阳江",u"云浮",u"湛江",u"肇庆",u"中山",u"珠海",u"南宁",u"百色",u"北海",u"崇左",u"防城港",u"桂林",u"贵港",u"河池",u"贺州",u"来宾",u"柳州",u"钦州",u"梧州",u"玉林",u"贵阳",u"安顺",u"毕节地区",u"六盘水",u"铜仁地区",u"遵义",u"黔西南州",u"海口",u"白沙",u"保亭",u"昌江",u"儋州",u"澄迈",u"琼海",u"琼中",u"乐东",u"临高",u"陵水",u"三亚",u"屯昌",u"万宁",u"文昌",u"五指山",u"石家庄",u"保定",u"沧州",u"承德",u"邯郸",u"衡水",u"廊坊",u"秦皇岛",u"唐山",u"邢台",u"张家口",u"郑州",u"安阳",u"鹤壁",u"焦作",u"开封",u"洛阳",u"漯河",u"南阳",u"平顶山",u"濮阳",u"三门峡",u"商丘",u"新乡",u"信阳",u"许昌",u"周口",u"驻马店",u"哈尔滨",u"大庆",u"大兴安岭地区",u"鹤岗",u"黑河",u"鸡西",u"佳木斯",u"牡丹江",u"七台河",u"齐齐哈尔",u"双鸭山",u"绥化",u"伊春",u"武汉",u"鄂州",u"恩施",u"黄冈",u"黄石",u"荆门",u"荆州",u"潜江",u"神农架林区",u"十堰",u"随州",u"天门",u"仙桃",u"咸宁",u"襄樊",u"孝感",u"宜昌",u"长沙",u"常德",u"郴州",u"衡阳",u"怀化",u"娄底",u"邵阳",u"湘潭",u"益阳",u"永州",u"岳阳",u"张家界",u"株洲",u"南京",u"常州",u"淮安",u"连云港",u"南通",u"苏州",u"宿迁",u"泰州",u"无锡",u"徐州",u"盐城",u"扬州",u"镇江",u"南昌",u"抚州",u"赣州",u"吉安",u"景德镇",u"九江",u"萍乡",u"上饶",u"新余",u"宜春",u"鹰潭",u"长春",u"白城",u"白山",u"吉林市",u"辽源",u"四平",u"松原",u"通化",u"延边",u"沈阳",u"鞍山",u"本溪",u"朝阳",u"大连",u"丹东",u"抚顺",u"阜新",u"葫芦岛",u"锦州",u"辽阳",u"盘锦",u"铁岭",u"营口",u"呼和浩特",u"包头",u"巴彦淖尔",u"赤峰",u"鄂尔多斯呼伦贝尔",u"通辽",u"乌海",u"乌兰察布",u"兴安盟",u"银川",u"固原",u"石嘴山",u"吴忠",u"中卫",u"西宁",u"果洛州",u"海东地区",u"海北州",u"海南州",u"海西州",u"黄南州",u"玉树州",u"济南",u"滨州",u"东营",u"德州",u"菏泽",u"济宁",u"莱芜",u"聊城",u"临沂",u"青岛",u"日照",u"泰安",u"威海",u"潍坊",u"烟台",u"枣庄",u"淄博",u"太原",u"长治",u"大同",u"晋城",u"晋中",u"临汾",u"吕梁",u"朔州",u"忻州",u"阳泉",u"运城",u"西安",u"安康",u"宝鸡",u"汉中",u"商洛",u"铜川",u"渭南",u"咸阳",u"延安",u"榆林",u"成都",u"阿坝州",u"巴中",u"达州",u"德阳",u"甘孜州",u"广安",u"广元",u"乐山",u"凉山州",u"泸州",u"南充",u"眉山",u"绵阳",u"内江",u"攀枝花",u"遂宁",u"雅安",u"宜宾",u"资阳",u"自贡",u"拉萨",u"阿里地区",u"昌都地区",u"林芝地区",u"那曲地区",u"日喀则地区",u"山南地区",u"乌鲁木齐",u"阿拉尔",u"阿克苏地区",u"阿勒泰地区",u"昌吉州",u"哈密地区",u"和田地区",u"喀什地区",u"克拉玛依",u"石河子",u"塔城地区",u"吐鲁番地区",u"昆明",u"保山",u"楚雄州",u"大理州",u"德宏州",u"迪庆州",u"红河州",u"丽江",u"临沧",u"怒江州",u"普洱",u"曲靖",u"昭通",u"文山",u"玉溪",u"杭州",u"湖州",u"嘉兴",u"金华",u"丽水",u"宁波",u"衢州",u"绍兴",u"台州",u"温州",u"舟山"]
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"潮州", wx.DefaultPosition, wx.Size( 120,-1 ), m_comboBox2Choices, 0 )
		# self.m_comboBox2.SetSelection( 50 )
		self.m_comboBox2.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer3.Add( self.m_comboBox2, 0, wx.ALL, 5 )
		
		self.m_button16 = wx.Button( self, wx.ID_ANY, u"城市验证", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button16.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer3.Add( self.m_button16, 0, wx.ALL, 5 )
		
		self.m_button6 = wx.Button( self, wx.ID_ANY, u"开始作业", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer3.Add( self.m_button6, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer3, 1, 0, 1 )
		
		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"   地点要求:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		
		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.m_staticText3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer4.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
		bSizer4.Add( self.m_textCtrl4, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"* 搜索物品:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		
		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.m_staticText4.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer4.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_textCtrl5 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 120,-1 ), 0 )
		bSizer4.Add( self.m_textCtrl5, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer4, 1, wx.EXPAND, 3 )
		
		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, u"  (ccphamy) :带 * 为必填项 ,城市必须先验通过后才能搜索", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText6.Wrap( -1 )
		
		self.m_staticText6.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		self.m_staticText6.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNTEXT ) )
		
		bSizer2.Add( self.m_staticText6, 0, wx.ALL, 5 )
		
		
		bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"对百度地图指定类型或关键字内容采集 可获(地点，名称，价格，评价) 等等，程序仅供测试使用。\n----------------------------------------------------\n城市必填 *\n物品必填 *\n----------------------------------------------------\n", wx.DefaultPosition, wx.Size( 450,250 ), wx.TE_MULTILINE )
		self.m_textCtrl3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button16.Bind( wx.EVT_BUTTON, self.checkCity )
		self.m_button6.Bind( wx.EVT_BUTTON, self.startJob )
		
		pub.subscribe(self.append, "updateText")

	def append(self,content):
		self.m_textCtrl3.AppendText(content + "\n")

	def __del__( self ):
		pass
	
	def checkCity( self, event ):
		event.Skip()
	
	def startJob( self, event ):
		event.Skip()