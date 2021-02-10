import tkinter as tk

app = tk.Tk()
app.geometry('500x100')
app.title('Main Window')

menu1 = tk.Menu(app)
app.config(menu = menu1)
app.menu = menu1
filemenu = tk.Menu(menu1,tearoff = 0)
menu1.add_cascade(label = 'File', menu = filemenu )

def temperature():
    
    temp = tk.Toplevel(app)
    
    temp.geometry('400x100')
    val = tk.StringVar()
    check = tk.IntVar()
    tk.Label(temp,text = 'Enter temperature:').grid(row = 1,column = 1)
    entry1 = tk.Entry(temp,text = 'Enter temperature:',textvariable = val )
    entry1.grid(row = 1, column = 2)
    
    tk.Label(temp,text = 'Temperature in').grid(row = 2, column = 1 )
    tk.Radiobutton(temp, text = 'Celsius', val = 1, variable = check).grid(row = 2,column = 2)
    tk.Radiobutton(temp,text = 'Fahrenheit', val = 2, variable = check).grid(row = 2, column = 3)
    
    label = tk.Label(temp,text = '')
    label.grid(row = 5, column = 2)
    
    def conversion():
        
        try:
            num = int(val.get())
            if check.get() == 1:
                
                result = str(((9*num)/5) + 32)
                
            elif check.get() == 2:
                
                result = str(((num - 32)*5)/9)
                
            else:
                
                result = 'Wrong input'
                
        except:
            
            result = 'Wrong input'
            
        label.config(text = result)
        
    tk.Button(temp,text = 'Convert', command = conversion ).grid(row = 5,column = 2)
    
filemenu.add_command(label = 'Temperature', command = temperature)
filemenu.add_command(label = 'Sort')
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = app.destroy)

label = tk.Label(app,text = 'Welcome to My App.',font = ('Arial',30))
label.pack()

app.mainloop()