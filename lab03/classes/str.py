class String:
    def GetString(self):
        self.text = str(input())
    def PrintString(self):
        print(self.text.upper())
text = String()
text.GetString()
text.PrintString()