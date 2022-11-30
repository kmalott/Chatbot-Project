import googletrans
from googletrans import Translator

def prereq(language):  
        courses = ["COSC 101", "COSC 111", "COSC 121", "COSC 122", "COSC 123", "COSC 210", "COSC 211", "COSC 221", "COSC 222", "COSC 301", "COSC 303", "COSC 304", "COSC 305", "COSC 310", "COSC 315", "COSC 320", "COSC 322", "COSC 328", "COSC 335", "COSC 341", "COSC 344", "COSC 360", "COSC 404", "COSC 407", "COSC 414", "COSC 421", "COSC 444", "COSC 499"]
        t = Translator()

        def user_input():
            inp_msg = t.translate("What COSC course would you like a prereq for? (enter in format COSC xxx)", src='en', dest=language)
            inp = input(inp_msg.text)
            return inp

        def validate(str):
            if  str in courses:
                if(str=="COSC 101" or str=="COSC 111" or str=="COSC 122"):
                    print(t.translate("There are no prereqs for these courses.", src='en', dest=language).text)
                elif(str=="COSC 121"):
                    print(t.translate("A score of 60 percent or higher in one of COSC 111, COSC 123.",src='en',dest=language).text)
                elif(str=="COSC 123"):
                    print(t.translate("One of COSC 111, COSC 122.",src='en',dest=language).text)
                elif(str=="COSC 210"):
                    print(t.translate("One of APSC 177, COSC 111.",src='en',dest=language).text)
                elif(str=="COSC 211"):
                    print(t.translate(" COSC 121.", src='en',dest=language).text)
                elif(str=="COSC 221"):
                    print(t.translate("One of MATH 101, MATH 142, APSC 173.",src='en',dest=language).text)
                elif(str=="COSC 222"):
                    print(t.translate(" A score of 60 percent or higher in COSC 121.",src='en',dest=language).text)
                elif(str=="COSC 301"):
                    print(t.translate("(Either (a) third-year standing, or (b) one of COSC 111 or COSC 122).",src='en',dest=language).text)
                elif(str=="COSC 303"):
                    print(t.translate("All of MATH 200, MATH 221 and either (a) COSC 111 or (b) DATA 301.",src='en',dest=language).text)
                elif(str=="COSC 304"):
                    print(t.translate("One of COSC 111, COSC 123, COSC 210. (Third-year standing.)",src='en',dest=language).text)
                elif(str=="COSC 305"):
                    print(t.translate("There are no prereqs, but COSC 310 is a coreq.",src='en',dest=language).text)
                elif(str=="COSC 310"):
                    print(t.translate("One of COSC 210, COSC 222, COSC 223. (and third-year standing.)",src='en',dest=language).text)
                elif(str=="COSC 315"):
                    print(t.translate("All of COSC 221, COSC 222.",src='en',dest=language).text)
                elif(str=="COSC 320"):
                    print(t.translate("All of COSC 221, COSC 222 and one of MATH 221, APSC 179.",src='en',dest=language).text)
                elif(str=="COSC 322"):
                    print(t.translate("All of COSC 221, COSC 222.",src='en',dest=language).text)
                elif(str=="COSC 328"):
                    print(t.translate("All of COSC 211, COSC 222.",src='en',dest=language).text)
                elif(str=="COSC 335"):
                    print(t.translate("A score more than 60 percent in COSC 222 and a score more than 60 percent in one of PHYS 102, PHYS 121, PHYS 122. (PHYS 102 or PHYS 121 preferred.)",src='en',dest=language).text)
                elif(str=="COSC 341"):
                    print(t.translate("One of COSC 111, COSC 121, COSC 123, DATA 301. (and Third-year standing.)",src='en',dest=language).text)
                elif(str=="COSC 344"):
                    print(t.translate("One of COSC 210, COSC 222 and one of MATH 200, APSC 248 and one of MATH 221, APSC 179.",src='en',dest=language).text)
                elif(str=="COSC 360"):
                    print(t.translate("All of COSC 121, COSC 304. (and third-year standing.)",src='en',dest=language).text)
                elif(str=="COSC 404"):
                    print(t.translate("COSC 304. (and third-year standing.)",src='en',dest=language).text)
                elif(str=="COSC 407"):
                    print(t.translate("Either (a) COSC 111 or (b) APSC 177. (Third-year standing is required.)",src='en',dest=language).text)
                elif(str=="COSC 414"):
                    print(t.translate("All of COSC 221, COSC 222 and one of MATH 221, APSC 179.",src='en',dest=language).text)
                elif(str=="COSC 421"):
                    print(t.translate("STAT 230.",src='en',dest=language).text)
                elif(str=="COSC 444"):
                    print(t.translate("COSC 344.",src='en',dest=language).text)
                elif(str=="COSC 499"):
                    print(t.translate("All of COSC 304, COSC 310, COSC 341.",src='en',dest=language).text)
            
        inp = user_input()

        while((inp in courses)==False):
            error_msg = t.translate("Please enter in correct format", src='en', dest=language)
            print(error_msg.text)
            inp = user_input()

        validate(inp)


