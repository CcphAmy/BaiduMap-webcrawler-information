# -*- coding: utf-8 -*- 

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

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
		
		m_comboBox2Choices = [ u"上海", u"北京" ]
		self.m_comboBox2 = wx.ComboBox( self, wx.ID_ANY, u"上海", wx.DefaultPosition, wx.Size( 120,-1 ), m_comboBox2Choices, 0 )
		self.m_comboBox2.SetSelection( 0 )
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
		
		self.m_textCtrl3 = wx.TextCtrl( self, wx.ID_ANY, u"对百度地图指定类型或关键字内容采集 可获(地点，名称，价格，评价) 等等，程序仅供测试使用。\n---------------------------------------------------------\n城市必填 *\n物品必填 *\n---------------------------------------------------------", wx.DefaultPosition, wx.Size( 450,250 ), wx.TE_MULTILINE )
		self.m_textCtrl3.SetFont( wx.Font( 12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "微软雅黑" ) )
		
		bSizer1.Add( self.m_textCtrl3, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button16.Bind( wx.EVT_BUTTON, self.checkCity )
		self.m_button6.Bind( wx.EVT_BUTTON, self.startJob )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def checkCity( self, event ):
		event.Skip()
	
	def startJob( self, event ):
		event.Skip()
	

