import wx
import eyed3


class EditDialog(wx.Dialog):
    def __init__(self, mp3):
        title = f'Editing "{mp3.tag.title}"'
        super().__init__(parent=None, title=title, size=(400,200))
        self.mp3 = mp3
        self.mainSizer = wx.BoxSizer(wx.VERTICAL)
        self.artist = wx.TextCtrl(self, value=self.mp3.tag.artist)
        self.AddWidgets('Artist', self.artist)
        self.album = wx.TextCtrl(self, value=self.mp3.tag.album)
        self.AddWidgets('Album', self.album)
        self.title = wx.TextCtrl(self, value=self.mp3.tag.title)
        self.AddWidgets('Title', self.title)
        btnSizer = wx.BoxSizer()
        saveBtn = wx.Button(self, label='Save')
        saveBtn.Bind(wx.EVT_BUTTON, self.OnSave)
        btnSizer.Add(saveBtn, 0, wx.ALL, 5)
        btnSizer.Add(wx.Button(
            self, id=wx.ID_CANCEL), 0, wx.ALL, 5
        )
        self.mainSizer.Add(btnSizer, 0, wx.CENTER)
        self.SetSizer(self.mainSizer)

    def AddWidgets(self, labelText, textCtrl):
        rowSizer = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(self, label=labelText, size=(50, -1))
        rowSizer.Add(label, 0, wx.ALL, 5)
        rowSizer.Add(textCtrl, 1, wx.ALL | wx.EXPAND, 5)
        self.mainSizer.Add(rowSizer, 0, wx.EXPAND)

    def OnSave(self):
        pass
