import wx

class MyFrame(wx.Frame):
  def __init__(self, *args, **kwargs):
    super(MyFrame, self).__init__(*args, **kwargs)

    self.index()

  def index(self):
    pnl = wx.Panel(self)

    vbox = wx.BoxSizer(wx.VERTICAL)
    hbox1 = wx.BoxSizer(wx.HORIZONTAL)
    hbox2 = wx.BoxSizer(wx.HORIZONTAL)
    hbox3 = wx.BoxSizer(wx.HORIZONTAL)

    self.tc = wx.TextCtrl(pnl, wx.ID_ANY, value="To Do...", size=((300,20)))
    btn_new = wx.Button(pnl, label="Add")
    btn_new.Bind(wx.EVT_BUTTON, self.onAddClicked)

    hbox1.Add(self.tc, proportion=1, flag=wx.LEFT|wx.RIGHT, border=30)
    hbox1.Add(btn_new, proportion=1, flag=wx.RIGHT, border=30)
    vbox.Add(hbox1, proportion=1, flag=wx.TOP, border=40)

    self.lb = wx.ListBox(pnl, size=((350,350)))
    hbox2.Add(self.lb, proportion=1, flag=wx.EXPAND|wx.ALL, border=20)
    vbox.Add(hbox2, proportion=1, flag=wx.TOP, border=20)

    btn_clr = wx.Button(pnl, label="Clear")
    btn_clr.Bind(wx.EVT_BUTTON, self.onClrClicked)
    btn_del = wx.Button(pnl, label="Delete a Task")
    btn_del.Bind(wx.EVT_BUTTON, self.onDelClicked)
    hbox3.Add(btn_clr, proportion=1, flag=wx.LEFT, border=50)
    hbox3.Add(btn_del, proportion=1, flag=wx.RIGHT, border=50)
    vbox.Add(hbox3, proportion=1, flag=wx.BOTTOM, border=30)
    
    pnl.SetSizer(vbox)
    self.SetSize((500,600))
    self.Centre()

  def onAddClicked(self, e):
    text = self.tc.GetValue()
    str_text = str(text)
    if str_text != "":
      self.lb.Append(str_text)
    else:
      print("Enter your task")
      

  def onClrClicked(self, e):
    self.lb.Clear()

  def onDelClicked(self, e):
    sel = self.lb.GetSelection()
    if sel != -1:
      self.lb.Delete(sel)

def main():
  app = wx.App()
  frame = MyFrame(None, title="To Do App")
  frame.Show()
  app.MainLoop()

if __name__ == "__main__":
  main()
