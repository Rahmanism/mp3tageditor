import wx


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='MP3 Tag Editor')
        self.Show()
