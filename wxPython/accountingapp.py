#App for company accounting

import wx

products = [['Blume', 20, 5, 0], ['Becher', 5, 2, 0],
            ['Buch', 10, 5, 0]]

class MyFrame(wx.Frame):
  def __init__(self, *args, **kwargs):
    super(MyFrame, self).__init__(*args, **kwargs)
    
    self.index()

  def index(self):
    panel = wx.Panel(self)
    leftPanel = wx.Panel(panel)
    rightPanel = wx.Panel(panel)
    hbox = wx.BoxSizer(wx.HORIZONTAL)
    vboxa = wx.BoxSizer(wx.VERTICAL)
    vboxb = wx.BoxSizer(wx.VERTICAL)

    self.list = wx.ListCtrl(rightPanel, style=wx.LC_REPORT|wx.LC_EDIT_LABELS)
    self.list.EnableCheckBoxes(True)
    self.list.InsertColumn(0, 'Produkt', width=150)
    self.list.InsertColumn(1, 'Preis')
    self.list.InsertColumn(2, 'Ausgabe')
    self.list.InsertColumn(3, 'Stück')
     
    idx=0
    for i in products:
      index = self.list.InsertItem(idx, i[0])
      self.list.SetItem(index, 1, str(i[1]))
      self.list.SetItem(index, 2, str(i[2]))
      self.list.SetItem(index, 3, str(i[3]))
      idx+=1
    
    
    vboxb.Add(self.list, 4, wx.EXPAND|wx.TOP, 5)
    vboxb.Add((-1,10))
    rightPanel.SetSizer(vboxb)

    btn2 = wx.Button(leftPanel, label="Produkt Löschen", size=((150,60)))
    btn3 = wx.Button(leftPanel, label="+", size=((150,60)))
    btn4 = wx.Button(leftPanel, label="-", size=((150,60)))
    btn5 = wx.Button(leftPanel, label="Ergebnis", size=((150,60)))
    btn6 = wx.Button(leftPanel, label="Alle Produkte Wählen", size=((150,60)))

    self.st = wx.StaticText(leftPanel, label="------",
                            style=wx.ALIGN_LEFT)
    
    btn2.Bind(wx.EVT_BUTTON, self.onClickDelete)
    btn3.Bind(wx.EVT_BUTTON, self.onClickInc)
    btn4.Bind(wx.EVT_BUTTON, self.onClickDec)
    btn5.Bind(wx.EVT_BUTTON, self.onClickResult)
    btn6.Bind(wx.EVT_BUTTON, self.onSelectAll)
    
    vboxa.Add(btn2, 0, wx.TOP|wx.BOTTOM, 5)
    vboxa.Add(btn3, 0, wx.BOTTOM, 5)
    vboxa.Add(btn4, 0, wx.BOTTOM, 5)
    vboxa.Add(btn5, 0, wx.BOTTOM, 5)
    vboxa.Add(btn6, 0, wx.BOTTOM, 10)
    vboxa.Add(self.st)
    leftPanel.SetSizer(vboxa)

    hbox.Add(leftPanel, 0, wx.EXPAND|wx.RIGHT, 5)
    hbox.Add(rightPanel, 1, wx.EXPAND)
    panel.SetSizer(hbox)
    
    self.SetSize((700,600))
    self.Centre()

  def onClickDelete(self, e):
    num = self.list.GetItemCount()
    for i in range(num):
      if self.list.IsItemChecked(i):
        self.list.DeleteItem(i)
        

  def onClickInc(self, e):
    num = self.list.GetItemCount()
    for i in range(num):
      if self.list.IsItemChecked(i):
        products[i][3]+=1
        a = products[i][3]
        self.list.SetItem(i, 3, str(products[i][3]))
        
          
  def onClickDec(self, e):
    num = self.list.GetItemCount()
    for i in range(num):
      if self.list.IsItemChecked(i):
        products[i][3]-=1
        a = products[i][3]
        self.list.SetItem(i, 3, str(products[i][3]))

  def onClickResult(self, e):
    total = 0
    given = 0
    num = self.list.GetItemCount()
    for i in range(num):
      mult_total = products[i][3]*products[i][1]
      mult_given = products[i][3]*products[i][2]
      total+=mult_total
      given+=mult_given

    text = "Umsatz: " + str(total) + " Euro" + "\n" + "Ausgabe: " + str(given) + " Euro" + "\n" +"Gewinn: " + str(total-given) + " Euro"
    
    self.st.SetLabel(text)
    

  def onSelectAll(self, e):
    num = self.list.GetItemCount()
    for i in range(num):
      self.list.CheckItem(i, True)

  
def main():
  app = wx.App()
  frame = MyFrame(None, title="Buchhaltung")
  frame.Show()
  app.MainLoop()

if __name__ == "__main__":
  main()
