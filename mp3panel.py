import eyed3
import glob
import wx


class Mp3Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.rowObjDict = {}

        self.listCtrl = wx.ListCtrl(
            self, size=(-1, 100),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.listCtrl.InsertColumn(0, 'Track No.', width=140)
        self.listCtrl.InsertColumn(1, 'Artist', width=140)
        self.listCtrl.InsertColumn(2, 'Album', width=140)
        self.listCtrl.InsertColumn(3, 'Title', width=140)
        mainSizer.Add(self.listCtrl, 0, wx.ALL | wx.EXPAND, 5)

        self.editBtn = wx.Button(self, label='Edit')
        self.editBtn.Bind(wx.EVT_BUTTON, self.onEdit)
        mainSizer.Add(self.editBtn, 0, wx.ALL | wx.CENTER, 5)

        self.msgStx = wx.StaticText(self)
        mainSizer.Add(self.msgStx, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(mainSizer)

    def onEdit(self, event):
        self.msgStx.SetLabelText('in onEdit')

    def updateMp3Listing(self, folderPath):
        self.msgStx.SetLabelText(folderPath)
