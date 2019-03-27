import wx
from mp3panel import Mp3Panel


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='MP3 Tag Editor')
        self.panel = Mp3Panel(self)
        self.Show()
