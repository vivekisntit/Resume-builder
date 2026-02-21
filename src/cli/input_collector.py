def get_input(user_inp):
    return input(f"{user_inp}\n> ").strip()
    
def get_dynamic_list(user_inp):
    dyn_items=[]
    print(f"Enter {user_inp} (type 'stop' to finish):")
    while True:
        item = input("> ").strip()
        if item.lower() == "stop":
            break
        if item:
            dyn_items.append(item)
    return dyn_items
    
def get_experiences():
    experiences=[]
    i=1
    while True:
        print(f"\n--- Experience {i} ---")
        exp={
            "job": get_input("Enter job title"),
            "level": get_input("Enter job level (Eg: Intern, Full-time)"),
            "employer": get_input("Enter employer name"),
            "date_range": get_input("Enter date range (Eg: Jan 2020 - Dec 2021)"),
            "description": get_dynamic_list("experience description bullets")
        }
        experiences.append(exp)
        more=get_input(f"Experience {i+1}? (y/n)").lower()
        if more!="y":
            break
        i+=1
    return experiences
    
def get_projects():
    projects=[]
    i=1
    while True:
        print(f"\n--- Project {i} ---")
        proj={
            "pr_cr_name": get_input("Enter project name"),
            "timeframe": get_input("Enter project timeframe"),
            "description": get_dynamic_list("project description bullets"),
            "framework": get_dynamic_list("Mention the frameworks/libraries which you used in this project"),
            "domain": get_input("Enter project domain (Eg: Web dev, App dev, ML engineer etc. [WRITE IN FULL FORM])")
        }
        projects.append(proj)
        more=get_input(f"Project {i+1}? (y/n)").lower()
        if more!="y":
            break
        i+=1
    return projects

def build_resume():
    resume_data={
        "name_and_contact": {
            "name": get_input("Enter your full name"),
            "phone": get_input("Enter your phone number"),
            "email": get_input("Enter your email"),
            "github": get_input("Enter your GitHub username"),
            "linkedin": get_input("Enter your LinkedIn handle")
        },

        "education": [
            {
                "school": get_input("Enter your school/college name"),
                "grad_date": get_input("Enter your graduation year"),
                "degree": get_input("Enter your degree"),
                "coursework": get_input("Enter your coursework (Eg: WebDev, DBMS, DSA, ML, Data Science etc. [WRITE IN FULL FORM] ")
            }
        ],

        "experience": get_experiences(),
        "projects": get_projects(),

        "skills": {
            "prog_lang": get_dynamic_list("Mention the programming languages you know"),
            "frm_lib": get_dynamic_list("Mention any frameworks/libraries/tools you know"),
            "duties": get_dynamic_list("Mention any duties/soft skills you have")
        }
    }
    return resume_data
