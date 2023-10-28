import pyttsx3
import PyPDF2
droid = pyttsx3.init()
droid.say("bonjour je suis une intelligence artificielle  ")
#qui lit des fichiers audio 
droid.runAndWait()
livre= open('pip install pyttsx3.pdf','rb')
lecture = PyPDF2.PdfReader(livre)
pages = len(lecture.pages)
print (pages)
for i in range(pages):
    page = lecture.pages[i]
    texte = page.extract_text()
    droid.say(texte)
    droid.runAndWait()

"""debutlecture = lecture.pages[1]
texte= debutlecture.extract_text()
droid.say(texte)"""
