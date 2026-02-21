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
            "job": get_input("Enter job title [Eg: Software Developer, Data Analyst]"),
            "level": get_input("Enter job level [Eg: Intern, Full-time]"),
            "employer": get_input("Enter employer name [Eg: Blackrock, Microsoft]"),
            "date_range": get_input("Enter date range [Eg: Jan 2020 - Dec 2021]"),
            "description": get_dynamic_list("experience description bullets [one bullet at a time]")
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
            "pr_cr_name": get_input("Enter project name]"),
            "timeframe": get_input("Enter project timefram [Eg: Jan 2020 - Dec 2021]"),
            "description": get_dynamic_list("project description [one bullet at a time]"),
            "framework": get_dynamic_list("the frameworks/libraries which you used in this project [one at a time]"),
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
            "linkedin": get_input("Enter your LinkedIn url")
        },

        "education": [
            {
                "school": get_input("Enter your college name"),
                "grad_date": get_input("Enter your graduation timeline [Eg: 2024 - 2028]"),
                "degree": get_input("Enter degree you're pursuing/pursued (Eg: B.Tech in ECE [WRITE IN FULL FORM])"),
                "coursework": get_dynamic_list("your coursework (Eg: WebDev, DBMS, DSA, ML, Data Science etc. [WRITE IN FULL FORM, one at a time])")
            }
        ],

        "experience": get_experiences(),
        "projects": get_projects(),

        "skills": {
            "prog_lang": get_dynamic_list("any programming languages that you know [one at a time]"),
            "frm_lib": get_dynamic_list("any frameworks/libraries/tools that you know [one at a time]"),
            "duties": get_dynamic_list("any duties/soft skills you might have [Enter a sentence, one at a time]"),
        }
    }
    return resume_data
