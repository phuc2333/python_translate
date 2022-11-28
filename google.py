import googletrans
from googletrans import Translator
# print(googletrans.LANGUAGES)
t = Translator()
a=t.translate("em",src="vi",dest="en")
print(a.text)