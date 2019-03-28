import wx
from mp3panel import Mp3Panel
import wx.adv


class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='MP3 Tag Editor', size=(500, 500))
        self.panel = Mp3Panel(self)
        self.createMenu()
        self.Show()

    def createMenu(self):
        fileMenu = wx.Menu()
        openFolderMenuItem = fileMenu.Append(
            wx.ID_OPEN, '&Open Folder\tCtrl+O',
            'Open a folder with MP3s'
        )
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.OnOpenFolder,
            source=openFolderMenuItem
        )
        fileMenu.AppendSeparator()
        quitMenuItem = fileMenu.Append(
            wx.ID_EXIT, '&Quit\tCtrl+Q',
            'Closes the app!',
        )
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.QuitApp,
            source=quitMenuItem
        )

        editMenu = wx.Menu()
        editMenuItem = editMenu.Append(
            wx.ID_EDIT, '&Edit Selected MP3\tF2',
        )
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.EditMp3,
            source=editMenuItem
        )

        helpMenu = wx.Menu()
        aboutMenuItem = helpMenu.Append(
            wx.ID_ABOUT, '&About\tF1',
            'About me and this small GUI app.'
        )
        self.Bind(
            event=wx.EVT_MENU,
            handler=self.About,
            source=aboutMenuItem
        )

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, '&File')
        menuBar.Append(editMenu, '&Edit')
        menuBar.Append(helpMenu, '&Help')
        self.SetMenuBar(menuBar)

    def OnOpenFolder(self, event):
        title = 'Choose a directory:'
        dlg = wx.DirDialog(
            self, title,
            style=wx.DD_DEFAULT_STYLE
        )
        if dlg.ShowModal() == wx.ID_OK:
            self.panel.UpdateMp3Listing(dlg.GetPath())
        dlg.Destroy()

    def QuitApp(self, event):
        self.Destroy()

    def EditMp3(self, event):
        self.panel.OnEdit(event)

    def About(self, event):
        aboutInfo = wx.adv.AboutDialogInfo()
        aboutInfo.SetName(self.Title)
        aboutInfo.SetVersion("1.0")
        aboutInfo.SetDescription(
            """
            With this app you can open a folder and see the list of MP3 files.
            You can edit some ID3 tags of the selected MP3 file.
            I did this to learn programming GUI python apps.
            """
        )
        aboutInfo.SetCopyright("(C) 2019-2022")
        aboutInfo.SetWebSite(
            "https://github.com/Rahmanism/mp3tageditor", "This Project in GitHub")
        aboutInfo.AddDeveloper("Rahmanism")

        wx.adv.AboutBox(aboutInfo)
