import Indeed.Web_Scrapper
import Indeed.Data_Refiner

print("Welcome to Indeed Web Scrapper\n\n")
job_name = input("Put the name of job you want to scrap: ")
job_location = input("Put the location of job you want to scrap: ")

#indeed_s = Indeed.Web_Scrapper.Indeed_Scrapper("https://in.indeed.com/jobs?q=software%20engineer&l=India&fromage=1")
indeed_s = Indeed.Web_Scrapper.Indeed_Scrapper("https://in.indeed.com/jobs?q="+ str(job_name) +"&l="+ str(job_location) +"&fromage=1")
indeed_s.Execute()


#ir = Indeed.Data_Refiner.Indeed_Refiner()
#ir.Execute()