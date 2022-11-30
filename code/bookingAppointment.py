import googletrans
from googletrans import Translator

def run(language):
    user_input = ""
    t = Translator()
    Hi = t.translate("Hi! Welcome to the Appointment Booking Feature. To return to the home at any time type ""exit"".", src='en', dest=language)
    ToBook = t.translate("To book an academic advising appointment please follow the link provided below.", src='en', dest=language)
    exit = t.translate("exit", src='en', dest=language)
    print(Hi.text)
    print(ToBook.text)
    print("https://students.ok.ubc.ca/academic-success/advising-options/academic-advising/contact/")
    while user_input != exit.text:
        user_input = str(input())
        if user_input == exit.text:
            exit_msg = t.translate("Exiting Appointment Booking", src='en', dest=language)
            print(exit_msg.text)
            return
        else: 
            input_msg = t.translate("Your input is not recognised. To exit this feature please type exit", src='en', dest=language)
            print(input_msg.text)