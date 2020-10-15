import pyttsx3 as text
import PyPDF2 as pdf
book = open('E:\IIIT\sem I\MACHINE LEARNING\AI1.pdf', 'rb')
reader = pdf.PdfFileReader(book)
pages = reader.numPages
print(pages)
speak = text.init()
for i in range(1, pages):
    read = reader.getPage(i)
    text = read.extractText()
    speak.say(text)
    speak.runAndWait()