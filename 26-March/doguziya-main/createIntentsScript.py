# Bir iskelet belirleyip json patterni oluÅŸturma
import json

textArr = ["KÄ±zarÄ±klÄ±k", "KaÅŸÄ±ntÄ±", "Kuruluk", "Pullanma", "Yanma hissi", "Sivilce", "Lezyonlar", "KabarcÄ±klar", "Egzama", "Dermatit", "mantar", "Ã§atlak", "Kepek", "kurdeÅŸen", "beze", "leke"]
text2Arr = ["elimde", "ayaÄŸÄ±mda", "saÃ§Ä±mda", "cildimde", "kolumda", "yÃ¼zÃ¼mde", "bileÄŸimde", "derimde", "karnÄ±mda", "topuÄŸumda"]
resultDict = {"patterns":[]}

for text2 in text2Arr:
    for text in textArr:
        result = text2 + " " + text + " var"
        resultDict["patterns"].append(result)
        
resultJson = json.dumps(resultDict, ensure_ascii=False) 
print(resultJson)


# json dosyasÄ±ndaki patterne ekleme
i = 0
for text2 in text2Arr:
    for text in textArr:
        result = text2 + ' ' + text + ' var'
        print('"' + result + '",')
        i += 1
        
print(i)



# diþ 
textArr = ["diþ aðrým", "diþ hassasiyetim", "azý diþim", "diþimde aðrý", "diþ çürümesi", "diþimde çürüme", "çürük diþ", "çürük diþim", "diþimde lezyon", "diþimde iltihap", "diþ iltihabý", "diþ apsesi", "diþimde apse", "diþ eti iltihabý", "diþimde iltihap", "aðýz kuruluðu", "aðýz kuruluðum", "diþ eti hastalýðý", "diþ etimde hassaiyet", "diþ sararmasý", "diþimde renk deðiþimi", "çene aðrýsý", "çene aðrým", "diþ sallanmasý", "diþ çürümesi", "diþimde çürüme", "diþ eti kanamasý", "diþ etinde kanama", "diþ eðriliði", "diþim eðri", "diþ gýcýrdatmasý", "diþ implantý"]
text2Arr = ["var"]
i = 0
for text2 in text2Arr:
    for text in textArr:
        result = text + " " + text2
        print('"' + result + '",')
        i += 1