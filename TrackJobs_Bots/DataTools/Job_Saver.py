from datetime import datetime
from os import cpu_count
import random
import json
from typing import Counter
import DataTools.Converter
import DataTools.Shifters

class JobSaver(object):
    def __init__(self):
        self.Jobs = json.load(open("TJobs.json"))
        self.Data = json.load(open("TData.json"))
        
        #//India/Haryana/Kaithal/Engineer/Mechanical/Bachelor/JOBID
        #self.Data["India"]["Haryana"]["Kaithal"]["Engineer"]["Mechanical"]["Bachelor"]
        
        
    def Random_Id(self):
        now = datetime.now()
        return (now.strftime("%d%m%Y%H%M%S") + str(random.randint(0, 10000)))


    def Job_Saver(self, job):
        DTC = DataTools.Converter.DTConverter()
        Sftrs = DataTools.Shifters.Shifters()

        #locs = str(job["Location"]).replace(" ", "").split(",")

        idis = self.Random_Id()
        self.Jobs[idis] = job
        
        #Country = DTC.Words2Num(job["Country"])
        #State = DTC.Words2Num(job["State"])
        #City = DTC.Words2Num(job["City"])
        #Programe = DTC.Words2Num(job["Programe"])
        #Course = DTC.Words2Num(job["Course"])
        #Qualification = "bachelor"

        Country = DTC.Words2Num(job["Country"])
        State = DTC.Words2Num(job["State"])
        City = DTC.Words2Num(job["City"])
        Programe = DTC.Words2Num(job["Programe"])
        Course = DTC.Words2Num(job["Course"])
        Qualification = DTC.Words2Num("bachelor")
        JobID = idis

        if Sftrs.Is_Diploma(str(job["Qualifications"]).lower()):
            Qualification = DTC.Words2Num("diploma")

        elif Sftrs.Is_Bachelors(str(job["Qualifications"]).lower()):
            Qualification = DTC.Words2Num("bachelor")

        elif Sftrs.Is_Masters(str(job["Qualifications"]).lower()):
            Qualification = DTC.Words2Num("master")

        elif Sftrs.Is_Doctorate(str(job["Qualifications"]).lower()):
            Qualification = DTC.Words2Num("doctrate")
        

        SDCountry = {}
        if Country not in self.Data:
                self.Data[Country] = {}
        SDCountry = self.Data[Country]
       

        SDState = {}
        if State not in SDCountry:
            SDCountry[State] = {}
        SDState = SDCountry[State]
        
        
        SDCity = {}
        if City not in SDState:
            SDState[City] = {}
        SDCity = SDState[City]


        SDPrograme = {}
        if Programe not in SDCity:
            SDCity[Programe] = {}
        SDPrograme = SDCity[Programe]
        


        SDCourse = {}
        if Course not in SDPrograme:
            SDPrograme[Course] = {}
        SDCourse = SDPrograme[Course]
        

        SDQualification = {}
        if Qualification not in SDCourse:
            SDCourse[Qualification] = []
        SDQualification = SDCourse[Qualification]
        
        
        SDQualification.append(idis)
        
        SDCourse[Qualification] = SDQualification
        SDPrograme[Course] = SDCourse
        SDCity[Programe] = SDPrograme
        SDState[City] = SDCity
        SDCountry[State] = SDState
        self.Data[Country] = SDCountry

        #print("\n",SDCountry,"\n")
        


    def Set_Data(self, data):
        self.Data = data

        

    def Save(self):
        with open("TJobs.json", "w") as outfile:
            json.dump(self.Jobs, outfile)

        print(self.Data)
        jsn = json.dumps(self.Data)
        with open("TData.json", "w") as Datafile:
            Datafile.write(jsn)


