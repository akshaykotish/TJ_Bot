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

            
        #print(tokens)
        


    def Refine(self):

        for job in self.json_data:
            Details  = job["Details"]
            
            self.Extract_Qualification(Details)
        

    def Execute(self):
        self.Read()
        

