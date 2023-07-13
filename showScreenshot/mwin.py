import tkinter
import pyautogui
from PIL import Image, ImageTk

x = 509
y = 261
x2 = 1099
y2 = 624
win1_width = '640'
win1_height = '480'
win1_posX = '200'
win1_posY = '200'




with open('mwin.cf','r',encoding='utf-8') as f:
    for line in f.readlines():
        cc = line.split()
        if not cc :
            continue
        if(cc[0] == 'x'):
            x = int(cc[1])
        if(cc[0] == 'y'):
            y = int(cc[1])
        if(cc[0] == 'x2'):
            x2 = int(cc[1])
        if(cc[0] == 'y2'):
            y2 = int(cc[1])
        if(cc[0] == 'win1_width'):
            win1_width = cc[1]
        if(cc[0] == 'win1_height'):
            win1_height = cc[1]
        if(cc[0] == 'win1_posX'):
            win1_posX = cc[1]
        if(cc[0] == 'win1_posY'):
            win1_posY = cc[1]



window = tkinter.Tk()
window.title("控制端")
window.geometry("100x60+900+300")
window.wm_attributes('-topmost',1)
window.attributes('-toolwindow',2)

win1 = tkinter.Toplevel()
win1.title("")
win1.geometry(f'{win1_width}x{win1_height}+{win1_posX}+{win1_posY}')
win1.wm_attributes('-topmost',1)
win1.attributes('-toolwindow',2)

win1_lab2 = tkinter.Label(win1)
win1_lab2.pack()

def updatewin1():
    img = pyautogui.screenshot(region=[x,y,x2-x,y2-y])
    img.save("img.jpg")
    iii = Image.open('img.jpg')
    iii = iii.resize((int(win1_width),int(win1_height)))
    tkImg = ImageTk.PhotoImage(iii)
    win1_lab2.configure(image=tkImg)
    win1_lab2.image = tkImg
    window.after(2500,updatewin1)


def click():
    win1.withdraw()

def click2():
    win1.deiconify()

btn = tkinter.Button(window, text="隐藏",command=click)
btn.pack()
btn = tkinter.Button(window, text="显示",command=click2)
btn.pack()

def win1Start():
    window.after(1000,updatewin1)
    win1.mainloop()
    
window.after(1000,win1Start)
window.mainloop()