import selenium.webdriver as webdriver
from wx import *
from wx.lib.agw.hyperlink import *
from turtle import *

class Torrent(Dialog):
    def __init__(self, parent, id):
        Dialog.__init__(self, parent, id, 'Torrent Downloader')
        self.panel = Panel(self)

        self.links = []
        self.resultName = []
        self.resultLink = []
        self.resultSize = []
        self.resultUploader = []
        self.blue = Colour(141, 149, 224)
        self.font12 = Font(12, DEFAULT, NORMAL, NORMAL)
        self.font13 = Font(13, DEFAULT, NORMAL, NORMAL)
        self.font14 = Font(14, DEFAULT, NORMAL, NORMAL)
        self.font22 = Font(22, SWISS, NORMAL, NORMAL)
        firefox_PATH = 'C://Program Files//Mozilla Firefox//firefox'
        firefoxDRIVER_PATH = 'C://Users//mayur//geckodriver'
        WINDOW_SIZE = "1920,1080"
        firefox_options = webdriver.FirefoxOptions()  
        firefox_options.add_argument("--headless")
        firefox_options.add_argument("--window-size=%s".format(WINDOW_SIZE))
        firefox_options.binary_location = firefox_PATH
        self.browser = webdriver.Firefox(executable_path=firefoxDRIVER_PATH, firefox_options=firefox_options)


        bmp1 = Image("Background.jpg", BITMAP_TYPE_ANY).ConvertToBitmap()
        self.bitmap = StaticBitmap(self.panel, -1, bmp1, (0, 0))

        self.timer = Timer(self)
        self.Bind(wx.EVT_TIMER, self.Initiate, self.timer)
        self.timer.Start(5000)

    def Initiate(self, event):
        self.timer.Destroy()
        self.bitmap.Destroy()

        self.select = Choice(self.panel, -1, choices=["Pirate Bay"], pos=(875, 35), size=(400, 25))
        self.select.SetFont(self.font13)
        self.select.SetSelection(0)

        StaticText(self.panel, -1, "Search Torrents", (17,15)).SetFont(self.font13)
        self.textBox = TextCtrl(self.panel, -1, pos=(17,35), size=(850, 27))
        self.textBox.SetFont(self.font13)
        self.button = Button(self.panel, -1, "Download", pos=(17,75), size=(280, 50))
        self.button.SetFont(self.font22)
        self.button.SetBackgroundColour("Green")
        self.Bind(EVT_BUTTON, self.Download, self.button)
        
        self.check = CheckBox(self.panel, -1, label="Automatic Download", pos=(1175, 70), size=(167, 23))
        self.check.SetFont(self.font13)
        self.check.SetValue(1)


    def Download(self, event):
        self.x = 0
        if self.select.GetSelection() == 0:
            self.url = "https://thepiratebay.org/"
            self.browser.get(self.url)
            self.search_box = self.browser.find_element_by_name("q")
            self.search_box.send_keys(self.textBox.GetValue())
            self.search_box.submit()
            
            while len(self.links) == 0:
                if self.browser.current_url != self.url:
                    self.links = self.browser.find_elements_by_xpath("//a[@class='detLink']")
                    self.magnets = self.browser.find_elements_by_xpath("//a[@title='Download this torrent using magnet']")
                    self.fonts = self.browser.find_elements_by_xpath("//font[@class='detDesc']")

            for i in range(len(self.links)):
                href = self.magnets[i].get_attribute("href")
                Name = self.links[i].text
                self.resultName.append(Name)
                self.resultLink.append(href)
                a = self.fonts[i].text.split("Size ")
                if "MiB" in self.fonts[i].text:
                    b = a[1].split(" MiB, ULed by ")
                    self.resultSize.append(b[0]+" MB")
                    self.resultUploader.append(b[1])
                elif "GiB" in self.fonts[i].text:
                    b = a[1].split(" GiB, ULed by ")
                    self.resultSize.append(b[0]+" GB")
                    self.resultUploader.append(b[1])

        if self.check.GetValue():
            try:
                HyperLinkCtrl.GotoURL(self, self.resultLink[0])
            except:
                pass

        self.text1 = StaticText(self.panel, -1, "Name", (17, 175), (850, 27), ALIGN_CENTER)
        self.text1.SetFont(self.font14)
        self.text1.SetBackgroundColour(Colour(255,155,106))
        self.text2 = StaticText(self.panel, -1, "Size", (869, 175), (179, 27), ALIGN_CENTER)
        self.text2.SetFont(self.font14)
        self.text2.SetBackgroundColour(Colour(255,155,106))
        self.text3 = StaticText(self.panel, -1, "Uploaded By", (1050, 175), (300, 27), ALIGN_CENTER)
        self.text3.SetFont(self.font14)
        self.text3.SetBackgroundColour(Colour(255,155,106))
        self.Next = Button(self.panel, label="Next Page >>", pos=(600,480), size=(100,30))
        self.Bind(EVT_BUTTON, self.NextPage, self.Next)
        self.Previous = Button(self.panel, label="<< Previous page", pos=(495,480), size=(100,30))
        self.Bind(EVT_BUTTON, self.PreviousPage, self.Previous)

        self.showResult()
        

    def showResult(self):
        try:
            self.LinkButton0.Destroy()
            self.text0b.Destroy()
            self.text0c.Destroy()
            self.LinkButton1.Destroy()
            self.text1b.Destroy()
            self.text1c.Destroy()
            self.LinkButton2.Destroy()
            self.text2b.Destroy()
            self.text2c.Destroy()
            self.LinkButton3.Destroy()
            self.text3b.Destroy()
            self.text3c.Destroy()
            self.LinkButton4.Destroy()
            self.text4b.Destroy()
            self.text4c.Destroy()
            self.LinkButton5.Destroy()
            self.text5b.Destroy()
            self.text5c.Destroy()
            self.LinkButton6.Destroy()
            self.text6b.Destroy()
            self.text6c.Destroy()
            self.LinkButton7.Destroy()
            self.text7b.Destroy()
            self.text7c.Destroy()
            self.LinkButton8.Destroy()
            self.text8b.Destroy()
            self.text8c.Destroy()
            self.LinkButton9.Destroy()
            self.text9b.Destroy()
            self.text9c.Destroy()
            self.LinkButton10.Destroy()
            self.text10b.Destroy()
            self.text10c.Destroy()
        except:
            pass
        finally:
            if (len(self.resultName) - self.x) > 11:
                self.Next.Enable()
            else:
                self.Next.Disable()
                
            if self.x > 10:
                self.Previous.Enable()
            else:
                self.Previous.Disable()
                            
            self.LinkButton0 = Button(self.panel, label=self.resultName[self.x], pos=(17, 200), size=(850, 25))
            self.LinkButton0.SetFont(self.font12)
            self.LinkButton0.SetForegroundColour("Blue")
            self.LinkButton0.SetBackgroundColour(Colour(255,235,225))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton0)
            self.text0b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 202), (179, -1), ALIGN_CENTER)
            self.text0b.SetFont(self.font12)
            self.text0b.SetBackgroundColour(Colour(255,235,225))
            self.text0c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 202), (300, -1), ALIGN_CENTER)
            self.text0c.SetFont(self.font12)
            self.text0c.SetBackgroundColour(Colour(255,235,225))

            self.x+=1
            self.LinkButton1 = Button(self.panel, label=self.resultName[self.x], pos=(17, 225), size=(850, 25))
            self.LinkButton1.SetFont(self.font12)
            self.LinkButton1.SetForegroundColour("Blue")
            self.LinkButton1.SetBackgroundColour(Colour(255,217,198))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton1)
            self.text1b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 227), (179, -1), ALIGN_CENTER)
            self.text1b.SetFont(self.font12)
            self.text1b.SetBackgroundColour(Colour(255,217,198))
            self.text1c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 227), (300, -1), ALIGN_CENTER)
            self.text1c.SetFont(self.font12)
            self.text1c.SetBackgroundColour(Colour(255,217,198))

            self.x+=1
            self.LinkButton2 = Button(self.panel, label=self.resultName[self.x], pos=(17, 250), size=(850, 25))
            self.LinkButton2.SetFont(self.font12)
            self.LinkButton2.SetForegroundColour("Blue")
            self.LinkButton2.SetBackgroundColour(Colour(255,235,225))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton2)
            self.text2b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 252), (179, -1), ALIGN_CENTER)
            self.text2b.SetFont(self.font12)
            self.text2b.SetBackgroundColour(Colour(255,235,225))
            self.text2c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 252), (300, -1), ALIGN_CENTER)
            self.text2c.SetFont(self.font12)
            self.text2c.SetBackgroundColour(Colour(255,235,225))

            self.x+=1
            self.LinkButton3 = Button(self.panel, label=self.resultName[self.x], pos=(17, 275), size=(850, 25))
            self.LinkButton3.SetFont(self.font12)
            self.LinkButton3.SetForegroundColour("Blue")
            self.LinkButton3.SetBackgroundColour(Colour(255,217,198))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton3)
            self.text3b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 277), (179, -1), ALIGN_CENTER)
            self.text3b.SetFont(self.font12)
            self.text3b.SetBackgroundColour(Colour(255,217,198))
            self.text3c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 277), (300, -1), ALIGN_CENTER)
            self.text3c.SetFont(self.font12)
            self.text3c.SetBackgroundColour(Colour(255,217,198))

            self.x+=1
            self.LinkButton4 = Button(self.panel, label=self.resultName[self.x], pos=(17, 300), size=(850, 25))
            self.LinkButton4.SetFont(self.font12)
            self.LinkButton4.SetForegroundColour("Blue")
            self.LinkButton4.SetBackgroundColour(Colour(255,235,225))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton4)
            self.text4b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 302), (179, -1), ALIGN_CENTER)
            self.text4b.SetFont(self.font12)
            self.text4b.SetBackgroundColour(Colour(255,235,225))
            self.text4c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 302), (300, -1), ALIGN_CENTER)
            self.text4c.SetFont(self.font12)
            self.text4c.SetBackgroundColour(Colour(255,235,225))

            self.x+=1        
            self.LinkButton5 = Button(self.panel, label=self.resultName[self.x], pos=(17, 325), size=(850, 25))
            self.LinkButton5.SetFont(self.font12)
            self.LinkButton5.SetForegroundColour("Blue")
            self.LinkButton5.SetBackgroundColour(Colour(255,217,198))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton5)
            self.text5b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 327), (179, -1), ALIGN_CENTER)
            self.text5b.SetFont(self.font12)
            self.text5b.SetBackgroundColour(Colour(255,217,198))
            self.text5c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 327), (300, -1), ALIGN_CENTER)
            self.text5c.SetFont(self.font12)
            self.text5c.SetBackgroundColour(Colour(255,217,198))

            self.x+=1
            self.LinkButton6 = Button(self.panel, label=self.resultName[self.x], pos=(17, 350), size=(850, 25))
            self.LinkButton6.SetFont(self.font12)
            self.LinkButton6.SetForegroundColour("Blue")
            self.LinkButton6.SetBackgroundColour(Colour(255,235,225))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton6)
            self.text6b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 352), (179, -1), ALIGN_CENTER)
            self.text6b.SetFont(self.font12)
            self.text6b.SetBackgroundColour(Colour(255,235,225))
            self.text6c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 352), (300, -1), ALIGN_CENTER)
            self.text6c.SetFont(self.font12)
            self.text6c.SetBackgroundColour(Colour(255,235,225))
            
            self.x+=1
            self.LinkButton7 = Button(self.panel, label=self.resultName[self.x], pos=(17, 375), size=(850, 25))
            self.LinkButton7.SetFont(self.font12)
            self.LinkButton7.SetForegroundColour("Blue")
            self.LinkButton7.SetBackgroundColour(Colour(255,217,198))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton7)
            self.text7b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 375), (179, -1), ALIGN_CENTER)
            self.text7b.SetFont(self.font12)
            self.text7b.SetBackgroundColour(Colour(255,217,198))
            self.text7c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 375), (300, -1), ALIGN_CENTER)
            self.text7c.SetFont(self.font12)
            self.text7c.SetBackgroundColour(Colour(255,217,198))

            self.x+=1
            self.LinkButton8 = Button(self.panel, label=self.resultName[self.x], pos=(17, 400), size=(850, 25))
            self.LinkButton8.SetFont(self.font12)
            self.LinkButton8.SetForegroundColour("Blue")
            self.LinkButton8.SetBackgroundColour(Colour(255,235,225))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton8)
            self.text8b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 402), (179, -1), ALIGN_CENTER)
            self.text8b.SetFont(self.font12)
            self.text8b.SetBackgroundColour(Colour(255,235,225))
            self.text8c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 402), (300, -1), ALIGN_CENTER)
            self.text8c.SetFont(self.font12)
            self.text8c.SetBackgroundColour(Colour(255,235,225))

            self.x+=1        
            self.LinkButton9 = Button(self.panel, label=self.resultName[self.x], pos=(17, 425), size=(850, 25))
            self.LinkButton9.SetFont(self.font12)
            self.LinkButton9.SetForegroundColour("Blue")
            self.LinkButton9.SetBackgroundColour(Colour(255,217,198))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton9)
            self.text9b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 427), (179, -1), ALIGN_CENTER)
            self.text9b.SetFont(self.font12)
            self.text9b.SetBackgroundColour(Colour(255,217,198))
            self.text9c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 427), (300, -1), ALIGN_CENTER)
            self.text9c.SetFont(self.font12)
            self.text9c.SetBackgroundColour(Colour(255,217,198))

            self.x+=1
            self.LinkButton10 = Button(self.panel, label=self.resultName[self.x], pos=(17, 450), size=(850, 25))
            self.LinkButton10.SetFont(self.font12)
            self.LinkButton10.SetForegroundColour("Blue")
            self.LinkButton10.SetBackgroundColour(Colour(255,235,225))
            self.Bind(EVT_BUTTON, self.clicked, self.LinkButton10)
            self.text10b = StaticText(self.panel, -1, self.resultSize[self.x], (869, 452), (179, -1), ALIGN_CENTER)
            self.text10b.SetFont(self.font12)
            self.text10b.SetBackgroundColour(Colour(255,235,225))
            self.text10c = StaticText(self.panel, -1, self.resultUploader[self.x], (1050, 452), (300, -1), ALIGN_CENTER)
            self.text10c.SetFont(self.font12)
            self.text10c.SetBackgroundColour(Colour(255,235,225))

    def clicked(self, event):
        if event.Id == self.LinkButton0.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[0+(self.x//11)*11])
        elif event.Id == self.LinkButton1.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[1+(self.x//11)*11])
        elif event.Id == self.LinkButton2.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[2+(self.x//11)*11])
        elif event.Id == self.LinkButton3.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[3+(self.x//11)*11])
        elif event.Id == self.LinkButton4.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[4+(self.x//11)*11])
        elif event.Id == self.LinkButton5.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[5+(self.x//11)*11])
        elif event.Id == self.LinkButton6.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[6+(self.x//11)*11])
        elif event.Id == self.LinkButton7.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[7+(self.x//11)*11])
        elif event.Id == self.LinkButton8.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[8+(self.x//11)*11])
        elif event.Id == self.LinkButton9.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[9+(self.x//11)*11])
        elif event.Id == self.LinkButton10.Id:
            HyperLinkCtrl.GotoURL(self, self.resultLink[10+(self.x//11)*11])
 
    def NextPage(self, event):
        self.x += 1
        self.showResult()

        
    def PreviousPage(self, event):
        self.x = (self.x//11 - 1)*11
        self.showResult()


if __name__ == "__main__":
    app = App()
    frame = Torrent(parent=None, id=-1)
    frame.Show()
    frame.Maximize(True)
    app.MainLoop()

