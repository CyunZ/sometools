
import pynput 
import pyautogui
import cv2
import numpy as np
from cnocr import CnOcr
import httpx
import asyncio

url = 'http://127.0.0.1:5000'

ocr = CnOcr(det_model_name='naive_det')

async def main():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            # print(response)
    except Exception as e:
        print(e)

def on_click(x, y, button, pressed): 
    if pressed: 
        print('{0} at {1}'.format(button, (x, y))) 
        if button == pynput.mouse.Button.left: 
            img = pyautogui.screenshot(region=[x-30,y-20,60,40])
            # img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            
            #不断更新在cv2.imshow中 
            # cv2.imshow("img", img) 
            # cv2.waitKey(0) 
            # cv2.destroyAllWindows() 

            text =ocr.ocr(img)
            for line in text:
                print(line)
                if '呼叫' in line['text'] :
                    print('呼叫!!!!!')
                    # try:
                    #     res = requests.get(url)
                    #     print(res.text)
                    # except Exception as e:
                    #     print(e)
                    asyncio.run(main())

            

def on_scroll(x, y, dx, dy): 
    print('Scrolled {0} at {1}'.format(dy, (x, y))) 

# Collect events until released 
with pynput.mouse.Listener( 
        on_click=on_click, 
        # on_scroll=on_scroll
        ) as listener: 
    listener.join()  
  




  