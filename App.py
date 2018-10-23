#!/usr/bin/env python
# App for wxPy ls laLr file GUI explorer
# Copyright(C) 2004,2015 MA
#from 2004:"wx Explorer Main D:\Source\PyDisk_browser"
import wx
import sys, os

from treectrl import TreeCtrlPanel
from listctrl import ListCtrlPanel

class App(wx.App):
    Win_title = "PyDisk Browser / ls+lalR file explorer v1.0"

    def __init__(self, fname):
        self.fname = fname
        wx.App.__init__(self, 0)

    def OnInit(self):
        frame = wx.Frame(None, -1, App.Win_title, pos=(50,50), size=(0,0),
                        style= #wx.NO_FULL_REPAINT_ON_RESIZE|
                         wx.DEFAULT_FRAME_STYLE)
        frame.CreateStatusBar()
        
        menuBar = self.create_menubar()
        frame.SetMenuBar(menuBar)
        # ready
        frame.Show()
        #win = explorer.create_explorer_window(frame, self.fname)
        self.splitter1 = wx.SplitterWindow(frame, -1)
        self.tree_pn = TreeCtrlPanel(self.splitter1, self.fname)
        self.list_pn = ListCtrlPanel(self.splitter1)
        self.splitter1.SetMinimumPaneSize(60)
        self.splitter1.SplitVertically(self.tree_pn, self.list_pn, 200)

        # Set the frame to a good size
        frame.SetSize((640, 480))
        self.tree_pn.SetFocus()
        self.window = self.splitter1
        self.SetTopWindow(frame)
        self.frame = frame
        return True
    
    def create_menubar(self):
        # menu
        menuBar = wx.MenuBar()
        # File Menu
        menu = wx.Menu()
        menu.Append(101, "&Open\tCtrl-O", "Open virtual directory")
        menu.Append(102, "E&xit\tAlt-X", "Exit demo")
        wx.EVT_MENU(self, 101, self.OnFileOpen)
        wx.EVT_MENU(self, 102, self.OnExit)
        menuBar.Append(menu, "&File")
        
        menu2 = wx.Menu()
        menu2.Append(105, "&Open\tCtrl-O", "Open virtual directory")
        menu2.Append(106, "E&xit\tAlt-X", "Exit demo")
        wx.EVT_MENU(self, 105, self.OnFileOpen)
        wx.EVT_MENU(self, 106, self.OnExit)
        menuBar.Append(menu2, "E&xplorer")
        return menuBar
    
    def OnExit(self, evt): #,evt):
        self.frame.Close()
    
    def OnFileOpen(self,evt):
        wildcard = "Text files (*.txt)|*.txt|" \
         "ls -laR files (*.lar)|*.lar|" \
         "All files (*.*)|*.*"
        dlg = wx.FileDialog(self.frame, "Choose a file", os.getcwd(), "", wildcard,
         wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        #log= self.window.log
        if dlg.ShowModal() == wx.ID_OK:
            paths = dlg.GetPaths()
            ##log.WriteText('You selected %d files:' % len(paths))
            #-for path in paths:
            #-   log.WriteText('  %s\n'%path)
        ##log.WriteText("CWD: %s\n" % os.getcwd())
        self.window.path=dlg.GetPaths()[0]
        dlg.Destroy()

        # send message to tree ctrl to Update 
        self.list_pn.list.DeleteAllItems()
        self.tree_pn.reload_tree(self.window.path)
        evt.Skip()

def test_explorer():
    import sys,os
    from treectrl import tApp #tApp is simple App for testing from treectl
    app = tApp(create_explorer_window, sys.argv[1])
    app.MainLoop()

def main(argv):
    if len(argv)>1:
      input_fname = argv[1]
    else:
      input_fname = ""
    app = App(input_fname)
    app.MainLoop()

if __name__ == "__main__":
    #test_explorer()
    main(sys.argv)
