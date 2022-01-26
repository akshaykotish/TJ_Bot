import json
from os import W_OK

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
                t_qualification.append(word)
            elif word.lower() in self.programs:
                t_programs.append(word)
            elif self.Extract_Salary(word) == True:
                Salaries.append(word)
            elif word.lower() in self.Experience:
                t_experience.append(word)
            else:
                t_extra_words.append(word)
                
        
        print("Qualifications: ", t_qualification)
        print("Programs: ", t_programs)
        print("Experience", t_experience)
        #print("Extra: ", t_extra_words)

        if len(Salaries) >= 2:
            print("Salary: ", Salaries[0], " - ", Salaries[len(Salaries) - 1])
        elif len(Salaries) > 0:
            print("Salary: ", Salaries[0])

        print("\n")

        Refined_Output = {
            "Qualifications": t_qualification,
            "Programs": t_programs,
            "Experience": t_experience,
            "Salary": Salaries,
            "Courses": t_courses
        }

        return Refined_Output
        


    def Refine(self):

        for job in self.json_data:
            Details  = job["Details"]
            
            RO = self.Extract_Qualification(Details)

            JB = {
                "URL": job["URL"], 
                "Title": job["Title"],
                "Location": job["Location"],
                "Company Name": job["Company Name"],
                "Details": job["Details"],
                "Salary" : job["Salary"],
                "Qualifications": RO["Qualifications"],
                "Programs": RO["Programs"],
                "Experience": RO["Experience"],
                "Salary": RO["Salary"],
                "Courses": RO["Courses"]
            }

            self.Refined_JBs.append(JB)
        

    def Save_to_JSON(self):
        jsn = json.dumps(self.Refined_JBs)
        with open("indeed_jobs_refined_data.json", "w") as outfile:
            outfile.write(jsn)

    def Execute(self):
        self.Read()
        self.Save_to_JSON()

        

