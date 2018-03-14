from pycricbuzz import Cricbuzz
import requests
import ctypes
import time
c = Cricbuzz()
#print (c.matches())

def run():
        for i in c.matches():
            s = str(i['mchdesc'])
            #print(s)
            if 'IND' in s:
                id=i['id']
                #print(id)
                if str(i['mchstate']) == 'inprogress':
                    ctypes.windll.user32.MessageBoxW(0, i['status'], "Alert!", 0)
                    print(str(i['status']))
                    #print(c.livescore(id))
                    #print(c.commentary(id))
        time.sleep(20)
        run()
run()

