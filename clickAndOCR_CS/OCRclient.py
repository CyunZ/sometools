
import pynput 
import pyautogui
import tkinter
import requests 

url = 'http://127.0.0.1:5000/photo'  
window = tkinter.Tk()
#保持最上层  
window.wm_attributes('-topmost', 1)
window.title('文本识别')
window.geometry('100x40+100+100')
window.attributes('-toolwindow', 2)
   
label = tkinter.Label(window, text='测试', font=('Arial', 14))
label.pack()


def on_click(x, y, button, pressed): 
    if pressed: 
        print('{0} at {1}'.format(button, (x, y))) 
        if button == pynput.mouse.Button.left: 
            img = pyautogui.screenshot(region=[x-30,y-20,80,40])
            img.save('test.png')
            files = {'file': open('test.png', 'rb')}
            data = {'name':'test.png'}
            r = requests.post(url, files=files,data=data)
            #显示文字
            label.configure(text=r.text)
            print(r.text)                  

            
def listerStart():
    listener = pynput.mouse.Listener(on_click=on_click) 
    listener.start()

window.after(0,listerStart)
window.mainloop()
  




  