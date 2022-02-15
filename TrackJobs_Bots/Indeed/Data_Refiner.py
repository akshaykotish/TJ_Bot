import json
from os import W_OK
import DataTools.Job_Saver


class Indeed_Refiner(object):
    
    def __init__(self): 
        self.file_data = ""
        self.json_data = []

        self.qualifications = json.load(open("Qualifications.json"))
        self.programs = json.load(open("Programs.json"))
        self.courses =  json.load(open("Courses.json"))
        self.toremove = json.load(open("toRemove.json"))
        self.Experience = json.load(open("Experience.json"))
        self.Refined_JBs = []

        self.Programe = "any"
        self.Course = "any"
        
        self.srch_keywords = []
        self.location = ""

        self.data = {}



    def Read(self):
        f = open("indeed_jobs_output.json", "r")
        self.file_data = f.read()

        self.json_data = json.loads(self.file_data)
        
        self.Refine()

    def Remove_Grammer(self, tokens):
        for word_2_rmv in tokens:
            if word_2_rmv in self.toremove:
                tokens.remove(word_2_rmv)

        return tokens


    def Refine_Tags(self, DataIn):
        DataIn = DataIn.replace(".", " ")
        DataIn = DataIn.replace(":", " ")
        DataIn = DataIn.replace("\n", " ")
        DataIn = DataIn.replace("\r", " ")
        DataIn = DataIn.replace("\t", " ")

        return DataIn
    
    
    def Extract_Salary(self, token):
        if '₹' in token:
            return True
        elif 'INR' in token:
            return True
        elif 'inr' in token:
            return True
        elif '$' in token:
            return True
        elif 'USD' in token:
            return True
        
        return False


    def Extract_Qualification(self, J_Details):
        isqualification = False
        tokens = self.Refine_Tags(J_Details).split(" ")
        tokens = self.Remove_Grammer(tokens)
        
        t_courses = []
        t_qualification = []
        t_programs = []
        t_experience = []
        t_extra_words = []


        Salaries = []

        for word in tokens:
            
            if word.lower() in self.qualifications:
                t_qualification.append(word.lower())
            elif word.lower() in self.programs:
                t_programs.append(word.lower())
            elif self.Extract_Salary(word) == True:
                Salaries.append(word.lower())
            elif word.lower() in self.Experience:
                t_experience.append(word.lower())
            else:
                t_extra_words.append(word.lower())
                
        
        #print("Qualifications: ", t_qualification)
        #print("Programs: ", t_programs)
        #print("Experience", t_experience)
        #print("Extra: ", t_extra_words)

        #if len(Salaries) >= 2:
            #print("Salary: ", Salaries[0], " - ", Salaries[len(Salaries) - 1])
        #elif len(Salaries) > 0:
            #print("Salary: ", Salaries[0])

        #print("\n")

        Refined_Output = {
            "Qualifications": t_qualification,
            "Programs": t_programs,
            "Experience": t_experience,
            "Salary": Salaries,
            "Courses": t_courses
        }

        return Refined_Output
        
    
    def Refine(self):

        JS = DataTools.Job_Saver.JobSaver()
        
        country = "India"
        

        for job in self.json_data:
            Details  = job["Details"]
            
            RO = self.Extract_Qualification(Details)

        
            locs = str(job["Location"]).replace(" ", "").split(",")
            if len(locs) == 0:
                locs.append("anycity")
                locs.append("anystate")
                locs.append("anycountry")
            elif len(locs) == 1:
                locs.append("anystate")
                locs.append("anycountry")
            elif len(locs) == 2:
                locs.append("anycountry")
                


            JB = {
                "URL": job["URL"], 
                "Title": job["Title"],
                "Location": job["Location"],
                "City": locs[0],
                "State": locs[1],
                "Country": locs[2],
                "Company Name": job["Company Name"],
                "Details": job["Details"],
                "Salary" : job["Salary"],
                "Qualifications": RO["Qualifications"],
                "Programs": RO["Programs"],
                "Experience": RO["Experience"],
                "Salary": RO["Salary"],
                "Courses": RO["Courses"],
                "Programe": self.Programe,
                "Course": self.Course
            }


            JS.Job_Saver(JB)

            
            #Country/State/City/Qualification/Program/Experience/JobID
            #Country/State/City/Qualification/Program/Experience/JobID
            self.Refined_JBs.append(JB)
        JS.Save()
        

    def Save_to_JSON(self):
        jsn = json.dumps(self.Refined_JBs)
        with open("indeed_jobs_refined_data.json", "w") as outfile:
            outfile.write(jsn)

    def Set_Infos(self, title, location):
        self.srch_keywords = title
        self.location = location
        self.Find_Course_Sub_Course()


    def Find_Course_Sub_Course(self):
        Programe = "any"
        Course = "any"

        for word in self.srch_keywords:
            temp_c = ""
            try:
                temp_c = str(self.courses[word])
            except:
                temp_c = "any"

            if temp_c != "any":
                self.Programe = str(word)
                break

        if Programe != "any":
            crs = self.courses[Programe]
            for c in crs:
                if c in self.srch_keywords:
                    self.Course = c
                    break

        elif Programe == "any":
            for prgrms in self.courses:
                crs = self.courses[prgrms]
                for cours in crs:
                    if cours in self.srch_keywords:
                        self.Course = cours
                        self.Programe = prgrms

        #print(self.Programe, self.Course)
    

    def Execute(self):
        self.Read()
        self.Save_to_JSON()

        

