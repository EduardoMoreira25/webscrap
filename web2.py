import html
from bs4 import BeautifulSoup
import requests
from datetime import datetime
import time


print("Type the skills you don't have.")
unfamiliar_skill = input(">")
print(f'Filtering out {unfamiliar_skill}')
#request is just requesting to website
def find_jobs():
    html_text = requests.get("https://www.net-empregos.com/pesquisa-empregos.asp?chaves=python&cidade=&categoria=0&zona=0&tipo=0").text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all("div", class_="job-item media")  #pode ser .find_all

    found_unfamiliar_skill = False
    for index, job in enumerate(jobs):
        lists = job.find_all("li")
        date = lists[-4].text.replace(" ","")
        date_object = datetime.strptime(date, '%d-%m-%Y').date()
        today = datetime.now().date()
        if (date_object - today).days < 30:   
            company_name = job.find("li", style="font-weight:bold").text.replace(" ","")
            skills = lists[-2].text.replace(" ","")
            more_info = job.div.h2.a["href"]
            if unfamiliar_skill not in skills:
                with open(f"posts/{index}.txt", "w") as f:      #the w is the permission in file (write)
                    f.write(f"Company Name: {company_name.strip()} \n")
                    f.write(f"Required Skill : {skills.strip()} \n") 
                    f.write(f"Time of offer: {date_object} \n")
                    f.write(f"More info: https://www.net-empregos.com{more_info}") 
                    
            else:
                found_unfamiliar_skill = True
        else:
            print("oops")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_wait = 10
        print(f"Waiting{time_wait}...minutes")
        time.sleep(time_wait * 60)   #wait certain amount of time to start, in this case runs every10mins



#run in file directory

#The issue with random returns I had wass because i was using break to 
#exit the for loop when I encountered a job with the unfamiliar skill
#in it. However, this might cause the loop to exit before processing all
#of the jobs, leading to random results.
#Used a flag variable to keep track of whether a 
#job with the unfamiliar skill has been encountered, and only exit the 
#loop after processing all of the jobs.

#exemplo
#dentro de 1 span dentro de outro span
#job.find("span", class_="sim-posted").span.text