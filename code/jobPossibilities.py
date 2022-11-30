import googletrans
from googletrans import Translator

def run(language):
    job_Dict = {
        "301": "Data Scientist, Data Analyist",
        "303": "Quantitative Analyist, Quantitative Developer",
        "304": "Database Analyst, Database Administrator",
        "305": "Project Manager",
        "310": "Software Developer",
        "315": "Operating System Developer",
        "320": "Software Developer, Predictive Modeler, Algorithm Researcher",
        "322": "AI Developer, ML Developer",
        "328": "Network Engineer, Infastructure Engineer",
        "335": "Medical Physicist, Medical Researcher",
        "341": "UI Designer, Frontend Developer",
        "344": "Image Processing Engineer",
        "360": "Web Developer",
        "404": "Database Manager, Database Administrator",
        "407": "Parallel Computing Engineer",
        "414": "Rendering Engineer, UI Developer",
        "421": "Network Science Researcher",
        "444": "Computer Vision Engineer"
    }

    user_input = ""
    t = Translator()
    Hi = t.translate("Hi! Welcome to the Job Possibilities Feature. To return to the home at any time type ""exit"".", src='en', dest=language)
    print(Hi.text)
    exit = t.translate("exit", src='en', dest=language)
    enterthe = t.translate("Enter the three digit code associated with the COSC class you are taking:", src='en', dest=language)
    exiting = t.translate("Exiting Job Possibilities", src='en', dest=language)
    theabove = t.translate("The above jobs are associated with the course you are taking", src='en', dest=language)
    error_msg = t.translate("The course code you have entered is not recognised. Please try again or exit.", src='en', dest=language)

    while user_input != exit.text:
        while True:
            try:
                print(enterthe.text)
                user_input = str(input())
                if user_input == exit.text:
                    print(exiting.text)
                    return
                else:
                    possibilities = job_Dict[user_input]
                    possibilities = t.translate(possibilities, src='en', dest=language)
                    print(possibilities.text)
                    print(theabove.text)
                break
            except NameError:
                print(error_msg.text)
            except KeyError:
                print(error_msg.text)

    final_msg = t.translate("Press the enter key if you wish to search for another course. If not type exit.", src='en', dest=language)
    print(final_msg.text)
    user_input = str(input())
