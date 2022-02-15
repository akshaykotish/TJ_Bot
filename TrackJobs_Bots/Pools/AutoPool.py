import json
import Indeed.Web_Scrapper
import Indeed.Data_Refiner
import datetime 
import time
import win32gui, win32con



class AutoPool(object):

    def __init__(self):
        #self.PoolData = {}
        print("Hello")

    def Run(self):

        #current_time_hour = datetime.datetime.now().hour
        #current_time_minute = datetime.datetime.now().minute
        
        #print( current_time_hour, current_time_minute )

        the_program_to_hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

        while True:
            current_time_minute = datetime.datetime.now().minute
            if current_time_minute == 15:
                self.PoolData = json.load(open("PoolData.json"))
                self.Execute()
            else:
                print("waiting")

            time.sleep(55)

    
        


    def Execute(self):

        for data in self.PoolData:
            parts = str(data).split(";")

            #indeed_s = Indeed.Web_Scrapper.Indeed_Scrapper("https://in.indeed.com/jobs?q=software%20engineer&l=India&fromage=1")
            indeed_s = Indeed.Web_Scrapper.Indeed_Scrapper("https://in.indeed.com/jobs?q="+ str(parts[0]) +"&l="+ str(parts[1]) +"&fromage=1")
            indeed_s.Set_Infos(parts[0], parts[1])
            indeed_s.Execute()

        self.PoolData.clear()


        with open("PoolData.json", "w") as outfile:
            outfile.write("[]")




