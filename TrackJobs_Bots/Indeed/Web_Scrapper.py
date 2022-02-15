import requests
from bs4 import BeautifulSoup
import json
import re
import os
from requests import status_codes
import random
import Indeed.Data_Refiner

class Indeed_Scrapper(object):

    
    def __init__(self, url):
        global URL
        self.URL = url
        self.Step = 0
        self.PageSource = ""
        self.AllJBs = []

        self.srch_keywords = []
        self.location = ""
        

        self.proxies = [
                {"http": "http://92.222.108.217:3128"},
                {"http": "http://139.59.1.14:1080"},
                {"http": "http://150.129.151.62:6667"},
                {"http": "http://103.250.166.4:6667"},
                {"http": "http://182.72.150.242:8080"},
                {"http": "http://223.30.190.74:8080"},
                {"http": "http://117.208.148.72:3128"},
                {"http": "http://103.88.127.178:8080"},
                {"http": "http://112.133.215.24:8080"},
                {"http": "http://202.134.191.156:8080"},
                {"http": "http://103.241.227.106:6666"},
                {"http": "http://103.46.233.190:83"},
                {"http": "http://103.240.161.109:6666"},
                {"http": "http://103.248.93.5:8080"},
                {"http": "http://103.35.132.189:83"}
            ]



    def Page_Counts(self):
        
        try:

            rndip = random.randint(0, 14)
        
            self.PageSource = requests.get(self.URL + "&start=" + str(self.Step), proxies=self.proxies[rndip])
            print("Proxy is : ", self.proxies[rndip]["http"])
        
            if self.PageSource.status_code == 200:
                PS = self.PageSource.text
                PS_HTML = BeautifulSoup(PS, 'html.parser')


                Job_Count = PS_HTML.find("div", {"id":"searchCountPages"})
                Total_User = Job_Count.text if Job_Count != None else "0"
                Total_Users_InNumber = re.findall("[0-9]", Total_User)
            
                total_jobs = ""
                for i in range(1, len(Total_Users_InNumber)):
                    total_jobs += Total_Users_InNumber[i]

                self.Total_Jobs = int(total_jobs)

                print("Total Jobs: ", self.Total_Jobs)

        except:
            print("Wow")





    def Load_URL(self):
        rndip = random.randint(0, 14)
        self.PageSource = requests.get(self.URL + "&start=" + str(self.Step), proxies=self.proxies[rndip])
        self.Step += 10
        self.Load_Data()
        

    def Load_JobView(self, job_id):
        rndip = random.randint(0, 14)
        Job_Data = requests.get("https://in.indeed.com/viewjob?jk=" + job_id, proxies=self.proxies[rndip])

        if Job_Data.status_code == 200:
            JD_HTML = BeautifulSoup(Job_Data.text, 'html.parser')
            Title = JD_HTML.find("h1", attrs = {"class":"jobsearch-JobInfoHeader-title"})
            Company_Location = JD_HTML.find("div", attrs = {"class":"jobsearch-CompanyInfoWithoutHeaderImage"})
            Company_Name = JD_HTML.find("div", attrs = {"class":"jobsearch-InlineCompanyRating"})
            
            Job_Description = JD_HTML.find("div", attrs = {"id":"jobDescriptionText"})
            Job_Salary = JD_HTML.find("div", attrs = {"class":"jobsearch-JobMetadataHeader-item "})
            

            SalaryIs = "Not given"
            if Job_Salary != None:
                Salary = Job_Salary.text
            else:
                SalaryIs = "Not given"

            JB = {
                "URL":"https://in.indeed.com/viewjob?jk=" + job_id, 
                "Title": Title.text if Title != None else "",
                "Location": Company_Location.text.replace(Company_Name.text, ""),
                "Company Name": Company_Name.text.replace("review", ""),
                "Details": Job_Description.text,
                "Salary" : SalaryIs
            }

            self.AllJBs.append(JB)
            self.Save_to_JSON()


    def Save_to_JSON(self):
        jsn = json.dumps(self.AllJBs)
        #print(jsn)
        with open("indeed_jobs_output.json", "w") as outfile:
            outfile.write(jsn)

   
    def Load_Data(self):
        if self.PageSource.status_code == 200:
            PS = self.PageSource.text
            PS_HTML = BeautifulSoup(PS, 'html.parser')
            J_Section = PS_HTML.findAll("a", attrs={"class":"tapItem"})

            for JItem in J_Section:

                J_ID = JItem["id"].split("_")[1]

                self.Load_JobView(J_ID)
                

    def Set_Infos(self, title, location):
        self.srch_keywords = str(title).split(" ")
        self.location = location



    def Execute(self):
        self.Page_Counts()

        if self.Total_Jobs > 0:
            for i in range(0, self.Total_Jobs, 10):
                os.system('CLS')  

                iscomplete = round((i/self.Total_Jobs) * 100, 2)
                output_msg = str(iscomplete) + "% of "+ str(self.Total_Jobs) +" indeed jobs downloaded\n TrackJobs, An Akshay Kotish & Co. Product"
                #print(output_msg)
                self.Load_URL()

            ir = Indeed.Data_Refiner.Indeed_Refiner()
            ir.Set_Infos(self.srch_keywords, self.location)
            ir.Execute()

    
    




