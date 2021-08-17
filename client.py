import tkinter as tk
import random
from tkinter.ttk import Combobox
import socket
import time

concerts = ["groups"]
places = ["prices"]
text1 = 'here will be data from server'
text2 = 'here will be information from server'


sock = socket.socket()
sock.connect(('localhost', 9090))

def find():
    c0 = combo1.get()

    sock.send(str.encode(c0))
    # print(b''+c0)
    data = sock.recv(1024)
    data = data.decode('utf-8')
    op = data.find('], [')
    op1 = data[0:op:1]
    op2 = data[op + 4:-1:1]

    def get_list(tup):
        global concerts
        global places
        list1 = tup.split("'")
        list11 = []
        for each in list1:
            if each[2:4].isalnum():
                list11.append(each)
            else:
                pass
        return list11

    concerts = get_list(op1)
    places = get_list(op2)
    print(concerts, '\n', places)
    combo1['values'] = concerts
    combo2['values'] = places
    roon\
        .update()
    canvas.update()
    pass

def buy():
    c0 = combo1.get()
    c1 = combo1.get()
    c2 = combo2.get()
    print("",c0,c1,c2,)

    sock.send(str.encode('buy'+'/'+c1+'/'+c2))
    data = sock.recv(1024)
    #sock.close()
    print(data)
    pass



roon\
    = tk.Tk()
canvas = tk.Canvas(roon
                   ,height = 500, width = 1000)
canvas.pack()

background_image = tk.PhotoImage(file='sssss.png')
background_label = tk.Label(canvas, image=background_image)
background_label.place(relwidth=1, relheight=1)

button1 = tk.Button(roon
                    , text = 'Найти концерты', command =lambda: find())
button1.place(relx=0.1,rely=0.0,relwidth=0.8,relheight=0.1)

Lframe = tk.Frame(roon
                  , bg = '#b3d1ff', bd=3)
Lframe.place(relx=0.5, rely=0.15, relwidth=0.8,relheight=0.2, anchor='n')
label=tk.Label(Lframe)
label.place(relwidth=1,relheight=1)
label['text'] = text1

combo0 = Combobox(canvas)
combo0['values'] = ['regular-user','super-user']
combo0.current(0)
combo0.place(relx=0.9,rely=0.0,relwidth=0.1,relheight=0.1)

combo1 = Combobox(canvas)
combo1['values'] = concerts
combo1.current(0)
combo1.place(relx=0.1,rely=0.45,relwidth=0.8,relheight=0.05)

combo2 = Combobox(canvas)
combo2['values'] = places
combo2.current(0)
combo2.place(relx=0.1,rely=0.55,relwidth=0.8,relheight=0.05)

Lframe2 = tk.Frame(roon
                   , bg = '#b3d1ff', bd=3)
Lframe2.place(relx=0.5, rely=0.65, relwidth=0.8,relheight=0.2, anchor='n')
label=tk.Label(Lframe2)
label.place(relwidth=1,relheight=1)
label['text'] = text2

button3 = tk.Button(roon
                    , text = 'Купить', command =lambda: buy())
button3.place(relx=0.1,rely=0.9,relwidth=0.8,relheight=0.1)

roon\
    .mainloop()

















# import socket
# import time
# sock = socket.socket()
# sock.connect(('localhost', 9090))
# sock.send(b'hello, world!')
#
# data = sock.recv(1024)
# print(data)
#
# time.sleep(5)
# sock.close()
# print (data)

