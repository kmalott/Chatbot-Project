import googletrans
from googletrans import Translator
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')
from nltk.corpus import wordnet
nltk.download('omw-1.4')
import spacy
from spacy import displacy

def main():
    LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'he': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'or': 'odia',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'ug': 'uyghur',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
    }

    print("Hi I'm an academic advising chatbot! \n")
    valid_lang = False
    while(valid_lang != True):
        lang = input("Please enter what language you would like our conversation to be in: \n")
        try:
            search_lang = (list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)])
            if('english' in search_lang):
                lang = 'en'
                valid_lang = True
            elif(search_lang != None):
                lang = search_lang
                valid_lang = True
            else:
                print("Im sorry your langauge is supported at this time. Please enter another language:")
        except:
            print("Im sorry your langauge is supported at this time. Please enter another language:")
        

    t = Translator()
    p1 = t.translate('Thank you for selecting your language!', src='en', dest=lang)
    print(p1.text)
    NER = spacy.load("en_core_web_sm")

    if(lang == 'en'):
        ans = input("Before we get started tell me a bit about yourself:\n")
        ans = NER(ans)
        name = ""
        for word in ans.ents:
            if "PERSON" in word.label_:
                name = word.text
        if name != "":
            print(f"Hello {name}! It's great to meet you!")
        else:
            print("Hi! It's great to meet you!")

        sent = SentimentIntensityAnalyzer()
        ans = input("What can I help you with today? :)\n")
        sent_dict = sent.polarity_scores(ans)
        max_value = max(sent_dict, key=sent_dict.get)

        help = "help"

        prereqs = "prerequisites"
        prereqs_syn = []
        for syn in wordnet.synsets(prereqs):
            for l in syn.lemmas():
                prereqs_syn.append(l.name())

        courses = "courses"
        courses_syn = []
        for syn in wordnet.synsets(courses):
            for l in syn.lemmas():
                courses_syn.append(l.name())
        
        stat = "stat"
        stat_syn = []
        for syn in wordnet.synsets(stat):
            for l in syn.lemmas():
                stat_syn.append(l.name())

        advisor = "advisor"
        advisor_syn = []
        for syn in wordnet.synsets(advisor):
            for l in syn.lemmas():
                advisor_syn.append(l.name())

        appointment = "appointment"
        app_syn = []
        for syn in wordnet.synsets(appointment):
            for l in syn.lemmas():
                app_syn.append(l.name())

        work = "work"
        work_syn = []
        for syn in wordnet.synsets(work):
            for l in syn.lemmas():
                work_syn.append(l.name())

        job = "job"
        job_syn = []
        for syn in wordnet.synsets(job):
            for l in syn.lemmas():
                job_syn.append(l.name())

        nothing = "nothing"
        nothing2 = "Nothing"
        nothing_syn = []
        for syn in wordnet.synsets(nothing):
            for l in syn.lemmas():
                nothing_syn.append(l.name())

        direction = "directions"

        true = 0

        while true == 0:
            if max_value == "neg":
                ans = input("I'm sorry this conversation wasn't helpful. Would you like to continue?\n")
                if "no" in ans:
                    print("test")
                    return
                else:
                    main()
                    break

            if courses in ans or ans in courses_syn:
                from coursesAvail import coursesAvail
                coursesAvail()
            elif work in ans or job in ans or ans in work_syn or ans in work_syn:
                from jobPossibilities import run
                run(lang)
            elif stat in ans or ans in stat_syn:
                from coursestats import coursestats
                coursestats()
            elif advisor in ans or appointment in ans or ans in advisor_syn or ans in app_syn:
                from bookingAppointment import run
                run(lang)
            elif prereqs in ans or ans in prereqs_syn: 
                from prereq import prereq
                prereq(lang)
            elif direction in ans:
                from directions import direction
                direction()
            else:
                from getHelp import get_help
                get_help(lang)
            

            ans = input("What else can I help you with?\n")
            sent_dict = sent.polarity_scores(ans)
            max_value = max(sent_dict, key=sent_dict.get)
            if nothing in ans or nothing2 in ans:
                ans = input("How did you feel about our conversation?")
                sent_dict = sent.polarity_scores(ans)
                max_value = max(sent_dict, key=sent_dict.get)

                if max_value == "neg":
                    print("I'm sorry I wasn't very useful. Thank you for the feedback!")
                elif max_value == "neu" or max_value == "compound":
                    print("Thanks for the feedback!")
                elif max_value == "pos":
                    print("I'm glad you had a good conversation with me!")
                true = 1

    else:
        p2 = t.translate("Hi I'm an academic advising chatbot!", src='en', dest=lang)
        print(p2.text)
        p3 = t.translate("What can I help you with today? :)\n", src='en', dest=lang)
        ans = input(p3.text)

        help = t.translate("help", src='en', dest=lang)
        help = help.text
        prereqs = t.translate("prerequisites", src='en', dest=lang)
        prereqs = prereqs.text
        stat = t.translate("stat", src='en', dest=lang)
        stat = stat.text
        advisor = t.translate("advisor", src='en', dest=lang)
        advisor = advisor.text
        appointment = t.translate("appointment", src='en', dest=lang)
        appointment = appointment.text
        work = t.translate("work", src='en', dest=lang)
        work = work.text
        job = t.translate("job", src='en', dest=lang)
        job = job.text
        nothing = t.translate("nothing", src='en', dest=lang)
        nothing = nothing.text
        nothing2 = t.translate("Nothing", src='en', dest=lang)
        nothing2 = nothing2.text
        
        loop = True

        while(loop):
            if work in ans or job in ans:
                from jobPossibilities import run
                run(lang)
            elif stat in ans:
                from coursestats import coursestats
                coursestats()
            elif advisor in ans or appointment in ans:
                from bookingAppointment import run
                run(lang)
            elif prereqs in ans: 
                from prereq import prereq
                prereq(lang)
            else:
                from getHelp import get_help
                get_help(lang)
            
            p4 = t.translate("What else can I help you with?", src='en', dest=lang)
            ans = input(p4.text)
            if nothing in ans or nothing2 in ans:
                loop = False
                p3 = t.translate("Thank you for talking to me!", src='en', dest=lang)
                print(p3.text)

    

main()


