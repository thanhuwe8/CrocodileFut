
from tkinter import Text
import sys

class GUIconsole(Text):
    def __init__(self, *args, **kwargs):
        kwargs.update({"state":"disabled"})
        Text.__init__(self, *args, **kwargs)
        self.bind("<Destroy>", self.reset)
        self.old_stdout = sys.stdout
        self.stdout = self
    
    def delete(self, *args, **kwargs):
        self.config(state="normal")
        self.delete(*args, **kwargs)
        self.config(state='disabled')
    
    def write(self, content):
        self.config(state="normal")
        self.insert("end", content)
        self.config(state='disabled')
    
    def reset(self, event):
        sys.stdout = self.old_stdout