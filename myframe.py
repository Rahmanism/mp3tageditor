import wx
from mp3panel import Mp3Panel


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='MP3 Tag Editor')
        self.panel = Mp3Panel(self)
        self.createMenu()
        self.Show()

    def createMenu(self):
        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        openFolderMenuItem = fileMenu.Append(
            wx.ID_ANY, 'Open Folder',
            'Open a folder with MP3s'
        )
        menuBar.Append(fileMenu, '&File')
        self.Bind(
            event = wx.EVT_MENU,
            handler = self.OnOpenFolder,
            source = openFolderMenuItem
        )
        self.SetMenuBar(menuBar)

    def OnOpenFolder(self, event):
        title = 'Choose a directory:'
        dlg = wx.DirDialog(
            self, title,
            style = wx.DD_DEFAULT_STYLE
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.panel.UpdateMp3Listing(dlg.GetPath())
        dlg.Destroy()

