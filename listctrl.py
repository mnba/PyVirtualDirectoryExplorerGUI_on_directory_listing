# ListCtrl.py
# Testing lots of stuff, controls, window types, etc.
## Robin Dunn & Gary Dumer
# RCS-ID:       $Id: wxListCtrl.py,v 1.26.2.12 2003/07/31 17:12:36 RD Exp $
# Copyright:    (c) 1998 by Total Control Software
# Copyright:    (c) 2004.8 & 2015 by Minas Abrahamyan

#-from wxPython.wx import *
#-from wxPython.lib.mixins.listctrl import wxColumnSorterMixin, wxListCtrlAutoWidthMixin
import wx
from wx import *#? check this
from wx.lib.mixins.listctrl import ColumnSorterMixin, ListCtrlAutoWidthMixin
import images

#---------------------------------------------------------------------------
class MyListCtrl(ListCtrl, ListCtrlAutoWidthMixin):
	def __init__(self, parent, ID, pos=wx.DefaultPosition,
		           size=wx.DefaultSize, style=0):
		ListCtrl.__init__(self, parent, ID, pos, size, style)
		ListCtrlAutoWidthMixin.__init__(self)

class ListCtrlPanel(wx.Panel, ColumnSorterMixin):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent, -1, style=wx.WANTS_CHARS)

		tID = wx.NewId()

		self.il = wx.ImageList(16, 16)

		self.idx1  = self.il.Add(images.getSmilesBitmap())
		self.sm_up = self.il.Add(images.getSmallUpArrowBitmap())
		self.sm_dn = self.il.Add(images.getSmallDnArrowBitmap())
		self.file1Idx = self.il.Add(images.getFile1Bitmap())

		self.list = MyListCtrl(self, tID,
		                         style=wx.LC_REPORT | wx.SUNKEN_BORDER
		                         | wx.LC_EDIT_LABELS
		                         #| wx.LC_NO_HEADER
		                         #| wx.LC_VRULES | wx.LC_HRULES
		                         )
		self.list.SetImageList(self.il, wx.IMAGE_LIST_SMALL)

		self.PopulateList()

		# Now that the list exists we can init the other base class,
		# see wxPython/lib/mixins/listctrl.py
		ColumnSorterMixin.__init__(self, 3)
		#self.SortListItems(0, True)

		EVT_SIZE(self, self.OnSize)
		EVT_LIST_ITEM_SELECTED(self, tID, self.OnItemSelected)
		EVT_LIST_ITEM_DESELECTED(self, tID, self.OnItemDeselected)
		EVT_LIST_ITEM_ACTIVATED(self, tID, self.OnItemActivated)
		EVT_LIST_DELETE_ITEM(self, tID, self.OnItemDelete)
		EVT_LIST_COL_CLICK(self, tID, self.OnColClick)
		EVT_LIST_COL_RIGHT_CLICK(self, tID, self.OnColRightClick)
		EVT_LIST_COL_BEGIN_DRAG(self, tID, self.OnColBeginDrag)
		EVT_LIST_COL_DRAGGING(self, tID, self.OnColDragging)
		EVT_LIST_COL_END_DRAG(self, tID, self.OnColEndDrag)
		EVT_LIST_BEGIN_LABEL_EDIT(self, tID, self.OnBeginEdit)

		EVT_LEFT_DCLICK(self.list, self.OnDoubleClick)
		EVT_RIGHT_DOWN(self.list, self.OnRightDown)

		# for wxMSW
		EVT_COMMAND_RIGHT_CLICK(self.list, tID, self.OnRightClick)

		# for wxGTK
		EVT_RIGHT_UP(self.list, self.OnRightClick)


	def PopulateList(self):
		if 0:
		    # for normal, simple columns, you can add them like this:
		    self.list.InsertColumn(0, "Artist")
		    self.list.InsertColumn(1, "Title", wx.LIST_FORMAT_RIGHT)
		    self.list.InsertColumn(2, "Genre")
		else:
		    # but since we want images on the column header we have to do it the hard way:
		    info = wx.ListItem()
		    info.m_mask = wx.LIST_MASK_TEXT | wx.LIST_MASK_IMAGE | wx.LIST_MASK_FORMAT
		    info.m_image = -1
		    info.m_format = 0
		    info.m_text = "Filename"
		    #self.list.InsertColumnInfo(0, info) #older wxwidgets
		    self.list.InsertColumn(0, info)

		    #info.m_format = wx.LIST_FORMAT_RIGHT
		    info.m_text = "Attr"
		    self.list.InsertColumn(1, info)

		    info.m_format = 0
		    info.m_text = "Size"
		    self.list.InsertColumn(2, info)

		"""
		# real populate list
		items = musicdata.items()
		for x in range(len(items)):
		    key, data = items[x]
		    self.InsertItem(x, key, self.idx1, data[0], data[1], data[2])
		"""

		self.list.SetColumnWidth(0, 135) #wx.LIST_AUTOSIZE)
		self.list.SetColumnWidth(1, 50) #wx.LIST_AUTOSIZE)
		self.list.SetColumnWidth(2, 50)

		self.currentItem = 0

	def InsertItem(self, no, itemData, imgIdx, str0, str1, str2):
		self.list.InsertImageStringItem(no, str0, imgIdx)
		self.list.SetStringItem(no, 1, str1)
		self.list.SetStringItem(no, 2, str2)
		self.list.SetItemData(no, itemData)

	def AppendItem(self, str):
		n = self.list.GetItemCount()
		self.InsertItem(n, 0, self.file1Idx, str, "str1", "str2") #0=itemData

	# Used by the wx.ColumnSorterMixin, see wxPython/lib/mixins/listctrl.py
	def GetListCtrl(self):
		return self.list

	# Used by the ColumnSorterMixin, see wxPython/lib/mixins/listctrl.py
	def GetSortImages(self):
		return (self.sm_dn, self.sm_up)


	def OnRightDown(self, event):
		self.x = event.GetX()
		self.y = event.GetY()
		#-self.log.WriteText("x, y = %s\n" % str((self.x, self.y)))
		item, flags = self.list.HitTest((self.x, self.y))
		if flags & wx.LIST_HITTEST_ONITEM:
		    self.list.Select(item)
		event.Skip()


	def getColumnText(self, index, col):
		item = self.list.GetItem(index, col)
		return item.GetText()


	def OnItemSelected(self, event):
		##print event.GetItem().GetTextColour()
		self.currentItem = event.m_itemIndex
		#-self.log.WriteText("OnItemSelected: %s, %s, %s, %s\n" %
		#-                   (self.currentItem,
		#                    self.list.GetItemText(self.currentItem),
		#                    self.getColumnText(self.currentItem, 1),
		#                    self.getColumnText(self.currentItem, 2)))
		if self.currentItem == 10:
		    self.log.WriteText("OnItemSelected: Veto'd selection\n")
		    #event.Veto()  # doesn't work
		    # this does
		    self.list.SetItemState(10, 0, wx.LIST_STATE_SELECTED)
		event.Skip()

	def OnItemDeselected(self, evt):
		item = evt.GetItem()
		#-self.log.WriteText("OnItemDeselected: %d" % evt.m_itemIndex)

		# Show how to reselect something we don't want deselected
		if evt.m_itemIndex == 11:
		    wx.CallAfter(self.list.SetItemState, 11, wx.LIST_STATE_SELECTED, wx.LIST_STATE_SELECTED)


	def OnItemActivated(self, event):
		self.currentItem = event.m_itemIndex
		#-self.log.WriteText("OnItemActivated: %s\nTopItem: %s" %
		#-                   (self.list.GetItemText(self.currentItem), self.list.GetTopItem()))

	def OnBeginEdit(self, event):
		#-self.log.WriteText("OnBeginEdit")
		event.Allow()

	def OnItemDelete(self, event):
		#-self.log.WriteText("OnItemDelete\n")
		pass

	def OnColClick(self, event):
		#self.log.WriteText("OnColClick: %d\n" % event.GetColumn())
		pass

	def OnColRightClick(self, event):
		item = self.list.GetColumn(event.GetColumn())
		#-self.log.WriteText("OnColRightClick: %d %s\n" %
		#-                   (event.GetColumn(), (item.GetText(), item.GetAlign(),
		#-                                        item.GetWidth(), item.GetImage())))

	def OnColBeginDrag(self, event):
		#*self.log.WriteText("OnColBeginDrag\n")
		pass
		## Show how to not allow a column to be resized
		#if event.GetColumn() == 0:
		#    event.Veto()


	def OnColDragging(self, event):
		#self.log.WriteText("OnColDragging\n")
		pass

	def OnColEndDrag(self, event):
		#self.log.WriteText("OnColEndDrag\n")
		pass

	def OnDoubleClick(self, event):
		#-self.log.WriteText("OnDoubleClick item %s\n" % self.list.GetItemText(self.currentItem))
		event.Skip()

	def OnRightClick(self, event):
		#-self.log.WriteText("OnRightClick %s\n" % self.list.GetItemText(self.currentItem))

		# only do this part the first time so the events are only bound once
		if not hasattr(self, "popupID1"):
		  self.popupID1 = wx.NewId()
		  self.popupID2 = wx.NewId()
		  self.popupID3 = wx.NewId()
		  self.popupID4 = wx.NewId()
		  self.popupID5 = wx.NewId()
		  self.popupID6 = wx.NewId()
		  EVT_MENU(self, self.popupID1, self.OnPopupOne)
		  EVT_MENU(self, self.popupID2, self.OnPopupTwo)
		  EVT_MENU(self, self.popupID3, self.OnPopupThree)
		  EVT_MENU(self, self.popupID4, self.OnPopupFour)
		  EVT_MENU(self, self.popupID5, self.OnPopupFive)
		  EVT_MENU(self, self.popupID6, self.OnPopupSix)

		# make a menu
		menu = wx.Menu()
		# add some items
		menu.Append(self.popupID1, "FindItem tests")
		menu.Append(self.popupID2, "Iterate Selected")
		menu.Append(self.popupID3, "ClearAll and repopulate")
		menu.Append(self.popupID4, "DeleteAllItems")
		menu.Append(self.popupID5, "GetItem")
		menu.Append(self.popupID6, "Edit")

		# Popup the menu.  If an item is selected then its handler
		# will be called before PopupMenu returns.
		self.PopupMenu(menu, wx.Point(self.x, self.y))
		menu.Destroy()


	def OnPopupOne(self, event):
		#-self.log.WriteText("Popup one\n")
		print "FindItem:", self.list.FindItem(-1, "Roxette")
		print "FindItemData:", self.list.FindItemData(-1, 11)

	def OnPopupTwo(self, event):
		#-self.log.WriteText("Selected items:\n")
		index = self.list.GetFirstSelected()
		while index != -1:
		    #-self.log.WriteText("      %s: %s\n" % (self.list.GetItemText(index), self.getColumnText(index, 1)))
		    index = self.list.GetNextSelected(index)

	def OnPopupThree(self, event):
		#-self.log.WriteText("Popup three\n")
		self.list.ClearAll()
		wx.CallAfter(self.PopulateList)

	def OnPopupFour(self, event):
		self.list.DeleteAllItems()

	def OnPopupFive(self, event):
		item = self.list.GetItem(self.currentItem)
		print item.m_text, item.m_itemId, self.list.GetItemData(self.currentItem)

	def OnPopupSix(self, event):
		self.list.EditLabel(self.currentItem)

	def OnSize(self, event):
		w,h = self.GetClientSize()
		self.list.SetDimensions(0, 0, w, h)


def create_listctl_panel(frame, fname):
	return ListCtrlPanel(frame) #, fname)

if __name__ == '__main__':
	import sys
	from treectrl import tApp
        fname = sys.argv[1]
	app = tApp(create_listctl_panel, fname)
        app.MainLoop()
