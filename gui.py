
from tkinter import *
fields = ['amp', 'freq_hz', 'phase_rad', 'len_str', 'len_data', 'fs_hz']

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 

def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

if __name__ == '__main__':
   root = Tk()
   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
   b1 = Button(root, text='Show',
          command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()
   
   
'''
    def time_domain_wave_creation(self):


        self.amp_l = Label(master, text="amp")
        self.freq_hz_l = Label(master, text="freq_hz")
        self.phase_rad_l = Label(master, text="phase_rad")
        self.len_str_l = Label(master, text="len_str")
        self.len_data_l = Label(master, text="len_data")
        self.fs_hz_l = Label(master, text="fs_hz")
        
        vcmd = master.register(self.store) # we have to wrap the command
        self.amp_e = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.freq_hz_e = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
        self.phase_rad_e = Entry(master, validate="key", validatecommand=(vcmd, '%P'))
'''

