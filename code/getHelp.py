import googletrans
from googletrans import Translator

def get_help(language):
    import csv
    t = Translator()
    issues = []
    filename = "issues.csv"
    rows = []
    true = 0
    
    # while loop that lopps until user is satisfied with conversation
    while true == 0:
        inp_msg = t.translate("What can I help you with? I'd like some pointers or Report an issue. Type exit to return to main",src='en',dest=language).text
        val = input(inp_msg)
    
        # if statement to branch off according to issue
        report = t.translate("report an issue", src='en', dest=language).text
        ret = t.translate("Return and enter a valid input",src='en',dest=language).text
        pointers = t.translate("I'd like some pointers",src='en',dest=language).text
        exit = t.translate("exit", src='en',dest=language).text
        if val == report:
            iss_msg = t.translate("Which category would your issue fit in? No Response Misinterpretation Other",src='en',dest=language).text
            iss = input(iss_msg)
            noresponse = t.translate("No response", src='en',dest=language).text
            mis = t.translate("misinterpretation", src='en',dest=language).text
            other = t.translate("other", src='en',dest=language).text
            des_msg = t.translate("Please decribe the issue:",src='en',dest=language).text
            no = t.translate("no",src='en',dest=language).text
            sat_msg = t.translate("Thank you for logging your issue. Do you need more help? (Yes/No)",src='en',dest=language).text
            if iss == noresponse:
                des = input(des_msg)
                rows.append(["No Response", des])
                sat = input(sat_msg)
                if sat == no:
                    true = 1
        
            elif iss == mis:
                des = input(des_msg)
                rows.append(["Misinterpretation", des])
                sat = input(sat_msg)
                if sat == no:
                    true = 1
                
            elif iss == other:
                des = input(des_msg)
                rows.append(["Other", des])
                sat = input(sat_msg)
                if sat == no:
                    true = 1
                
            else:
                print(ret)
    
            # giving tips on how to use chatbot  
        elif val == pointers:
            msg1 = t.translate("My abilities can be reduced to five features that I hope you take advantage of! If you want to know a class' prerequisites, ask me something like this, 'How can I take COSC 301'. You can get statistics on a computer science course by asking a question about a specific course. Possible job oppourtunites based on your course experice can be provided if you ask about work. I can help you make an acedmic advising appointment aswell, just ask me how! If you're unnsure what courses your experience qualifies you for, I can provide you with a list of courses you've completed the prerequisites for if you ask for help with course scheduling. I hope you found this helpful!!", src='en',dest=language).text
            print(msg1)
            help_msg = t.translate("Do you need more help? (Yes/No)",src='en',dest=language)
            sat = input(help_msg)
            yes = t.translate("yes",src='en',dest=language).text
            if sat != yes:
                ret_main = t.translate("returning you to main...",src='en',dest=language).text
                print(ret_main)
                true = 1
        elif val == exit:
            true=1
        else:
            print(ret)
            
    
    # writing issues to issues.csv
    with open(filename, 'a') as csvfile:
        csvwriter = csv.writer(csvfile)    
        csvwriter.writerows(rows)
        
    
