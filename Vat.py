from tkinter import *
from tkinter import ttk

class Vat:

    def __init__(self,master):

        self.vat2=IntVar()

        master.title("Vat Calculator")
        master.resizable(False,False)

        self.style=ttk.Style()

        self.style.configure('Header.TLabel', font=('Arial', 19,'bold'), padi=10)
        self.style.configure('Header.TButton', font=('Arial', 19,'bold'), padi=10 )

        self.frame_header=ttk.Frame(master)
        self.frame_header.pack()

        self.logo=PhotoImage(file='vat2.png')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0,column=1)
        ttk.Label(self.frame_header, text='Vat Calculator', style='Header.TLabel').grid(row=1, column=1,)
        Label(self.frame_header,text='Amount', padx=10, font=('arial', 19, 'bold')).grid(row=2,column=1, sticky=W)
        self.entry_amount = ttk.Entry(self.frame_header,width=24,  font=('Arial', 19),textvariable=self.vat2)
        self.entry_amount.grid(row=2, column=1)

        Label(self.frame_header, text='Result', padx=10, font=('arial', 19, 'bold')).grid(row=3, column=1, sticky=W)
        self.entry_result = ttk.Entry(self.frame_header, width=24, font=('Arial', 19))
        self.entry_result.grid(row=3, column=1)

        ttk.Button(self.frame_header,text='Calculate', style='Header.TButton', command=self.calculate).grid(row=4,column=1, padx=5)
        ttk.Button(self.frame_header, text='Clear', style='Header.TButton', command=self.clear).grid(row=5, column=1)


    def calculate(self):
        self.vat3 = self.vat2.get()
        self.vat4 =(self.vat3*20)/100
        self.entry_result.delete(0,END)
        self.entry_result.insert(0, self.vat4)

    def clear(self):
        self.entry_amount.delete(0,END)
        self.entry_result.delete(0,END)

def main():
    root=Tk()
    root.geometry()
    vat=Vat(root)
    root.mainloop()

if __name__ == "__main__":main()
