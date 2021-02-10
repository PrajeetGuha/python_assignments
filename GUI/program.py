import tkinter as tk
import os

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
        
    tk.Button(temp,text = 'Convert', command = conversion ).grid(row = 4,column = 2)
    
def sort_list():
    
    new = tk.Toplevel(app)
    new.geometry('500x400')
    new.title('Sort_list')
    
    canvas = tk.Canvas(new,bd = 3, relief = 'groove')
    canvas.pack(expand = True, fill = 'both')
    
    l_frame = tk.Frame(canvas)
    label1 = tk.Label(l_frame,text = 'Your list:')
    label1.pack()
    canvas.create_window(100,50,window = l_frame)
    
    l2_frame = tk.Frame(canvas)
    label2 = tk.Label(l2_frame,text = 'Sorted list')
    label2.pack()
    canvas.create_window(350,50,window = l2_frame)
    
    list_frame1 = tk.Frame(canvas)
    friendlist = tk.Listbox(list_frame1)
    friendlist.pack()
    
    canvas.create_window(100,150,window = list_frame1)
    
    list_frame2 = tk.Frame(canvas)
    list_frnd = tk.Listbox(list_frame2)
    list_frnd.pack()
    
    canvas.create_window(350,150,window = list_frame2)
    
    itemlist = []
    
    def add_item(s):
        
        if s.get() == '':
            return
        
        friendlist.insert(friendlist.size()+1,s.get())
        itemlist.append(s.get())
        
        list_frnd.delete(0,tk.END)
        itemlist.sort()
        for i,j in enumerate(itemlist,1):
            list_frnd.insert(i,j) 
            
        s.set('')
            
    def remove():
        
        if friendlist.get(tk.ANCHOR) == '':
            return
        
        itemlist.remove(friendlist.get(tk.ANCHOR))
        friendlist.delete(tk.ANCHOR)
        itemlist.sort()
        list_frnd.delete(0,tk.END)
        for i,j in enumerate(itemlist,1):
            list_frnd.insert(i,j) 
    
    def create():
        
        with open('list.txt','w') as f:
            for i in itemlist:
                f.write(f'{i}\n')
                
        file = "notepad.exe list.txt"
        os.system(file)
        
    s = tk.StringVar()
    entry = tk.Entry(canvas,textvariable = s)
    canvas.create_window(200,290,window = entry)
    
    entry.bind('<Return>', lambda x: add_item(s))
    friendlist.bind('<Delete>',lambda x: remove() )
    
    b1_frame = tk.Frame(canvas)
    button1 = tk.Button(b1_frame,text = 'Add', command = lambda: add_item(s))
    button1.pack()
    canvas.create_window(300,290,window = b1_frame)
    
    b2_frame = tk.Frame(canvas)
    button2 = tk.Button(b2_frame,text = 'Close', command = new.destroy, fg = 'red')
    button2.pack()
    canvas.create_window(230,350,window = b2_frame)
    
    b3_frame = tk.Frame(canvas)
    button3 = tk.Button(b3_frame,text = 'Print', command = create, fg = 'blue')
    button3.pack()
    canvas.create_window(270,350,window = b3_frame)
    
    b4_frame = tk.Frame(canvas)
    button4 = tk.Button(b4_frame,text = 'Remove', command = remove)
    button4.pack()
    canvas.create_window(200,200,window = b4_frame)

    
filemenu.add_command(label = 'Temperature', command = temperature)
filemenu.add_command(label = 'Sort', command = sort_list)
filemenu.add_separator()
filemenu.add_command(label = 'Exit', command = app.destroy)

label = tk.Label(app,text = 'Welcome to My App.',font = ('Arial',30))
label.pack()

app.mainloop()