import wx
from mp3panel import Mp3Panel
from myframe import MyFrame

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    # mp3panel = Mp3Panel(frame)
    # mp3panel.SetSize(wx.Window.GetClientSize(frame))
    app.MainLoop()
