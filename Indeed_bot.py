import requests
from bs4 import BeautifulSoup
import re


jobname = input("Enter Job Name: ")
location = input("Enter Job Location: ")

url = "https://in.indeed.com/jobs?q=" + jobname + "&l="+ location

Site_Response = requests.get(url)
print(url)

totaljobs = 0

start_v= 10

def Load_Site():
    updated_url = url + "&start=" + str(start_v)
    global Site_Response
    Site_Response = requests.get(updated_url)
    

def Get_Total_Jobs():
    if Site_Response.status_code == 200:
        soup = BeautifulSoup(Site_Response.text, 'html.parser')
        counts = soup.find("div", {"id":"searchCountPages"})
        total_users = counts.text
        numbrs = re.findall("[0-9]", total_users)

        total_jobs = ""
        for i in range(1, len(numbrs)):
            total_jobs += numbrs[i]

        global totaljobs
        totaljobs = int(total_jobs)
        print(totaljobs)


def Load_Jobs():
    if Site_Response.status_code == 200:
        soup = BeautifulSoup(Site_Response.text, 'html.parser')
        counts = soup.findAll("div", {"class":"slider_item"})
        #print(counts)
        for row in counts:
            #print(row)
            title = row.find("h2", {"class":"jobTitle"})
            company_location = row.find("div", {"class":"companyLocation"})
            salary_snippet = row.find("div", {"class":"salary-snippet"})

            job_snippet = row.find("div", {"class":"job-snippet"})
            uls = job_snippet.find("ul")
            
            
            if salary_snippet == None:
                salary_snippet = "Good in Market"
                print("Company Name: ", title.text)
                print("Company Location: ", company_location.text)
                print("Company Salary: ", salary_snippet)
            else:
                print("Company Name: ", title.text)
                print("Company Location: ", company_location.text)
                print("Company Salary: ", salary_snippet.text)

            if uls != None:
                lss = uls.findAll("li")
                if lss != None:
                    print("Important Points")
                    for ls in lss:
                        print("\t\t", ls.text)

            print("\n")



Get_Total_Jobs()
print(totaljobs)

Load_Jobs()

print(totaljobs)
for indx in range(10, totaljobs, 10):
    start_v = indx
    Load_Site()
    Load_Jobs()
