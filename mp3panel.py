import eyed3
import glob
import wx
from mp3editdialog import EditDialog


class Mp3Panel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.rowObjDict = {}

        self.listCtrl = wx.ListCtrl(
            self, size=(-1, 300),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        self.Mp3DefaultColumns()
        mainSizer.Add(self.listCtrl, 0, wx.ALL | wx.EXPAND, 5)

        self.editBtn = wx.Button(self, label='Edit')
        self.editBtn.Bind(wx.EVT_BUTTON, self.OnEdit)
        mainSizer.Add(self.editBtn, 0, wx.ALL | wx.CENTER, 5)

        self.onEditStx = wx.StaticText(self)
        mainSizer.Add(self.onEditStx, 0, wx.ALL | wx.EXPAND, 5)

        self.msgStx = wx.StaticText(self)
        mainSizer.Add(self.msgStx, 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(mainSizer)

    def Mp3DefaultColumns(self):
        self.listCtrl.ClearAll()
        self.listCtrl.InsertColumn(0, 'Track No.', width=50)
        self.listCtrl.InsertColumn(1, 'Artist', width=140)
        self.listCtrl.InsertColumn(2, 'Album', width=140)
        self.listCtrl.InsertColumn(3, 'Title', width=140)

    def OnEdit(self, event):
        self.onEditStx.SetLabelText('in OnEdit')
        selection = self.listCtrl.GetFocusedItem()
        if selection >= 0:
            mp3 = self.rowObjDict[selection]
            dlg = EditDialog(mp3)
            dlg.ShowModal()
            self.UpdateMp3Listing(self.currentFolderPath)
            dlg.Destroy()

    def UpdateMp3Listing(self, folderPath):
        self.msgStx.SetLabelText(folderPath)
        self.currentFolderPath = folderPath
        self.Mp3DefaultColumns()

        mp3s = glob.glob(folderPath + '/*.mp3')
        mp3Objects = []
        index = 0
        for mp3 in mp3s:
            mp3Object = eyed3.load(mp3)
            self.listCtrl.InsertItem(index, str(mp3Object.tag.track_num[0]))
            self.listCtrl.SetItem(index, 1, mp3Object.tag.artist)
            self.listCtrl.SetItem(index, 2, mp3Object.tag.album)
            self.listCtrl.SetItem(index, 3, mp3Object.tag.title)
            mp3Objects.append(mp3Object)
            self.rowObjDict[index] = mp3Object
            index += 1
