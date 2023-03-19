# Bir iskelet belirleyip json patterni oluşturma
import json

textArr = ["Kızarıklık", "Kaşıntı", "Kuruluk", "Pullanma", "Yanma hissi", "Sivilce", "Lezyonlar", "Kabarcıklar", "Egzama", "Dermatit", "mantar", "çatlak", "Kepek", "kurdeşen", "beze", "leke"]
text2Arr = ["elimde", "ayağımda", "saçımda", "cildimde", "kolumda", "yüzümde", "bileğimde", "derimde", "karnımda", "topuğumda"]
resultDict = {"patterns":[]}

for text2 in text2Arr:
    for text in textArr:
        result = text2 + " " + text + " var"
        resultDict["patterns"].append(result)
        
resultJson = json.dumps(resultDict, ensure_ascii=False) 
print(resultJson)


# json dosyasındaki patterne ekleme
i = 0
for text2 in text2Arr:
    for text in textArr:
        result = text2 + ' ' + text + ' var'
        print('"' + result + '",')
        i += 1
        
print(i)



# di� 
textArr = ["di� a�r�m", "di� hassasiyetim", "az� di�im", "di�imde a�r�", "di� ��r�mesi", "di�imde ��r�me", "��r�k di�", "��r�k di�im", "di�imde lezyon", "di�imde iltihap", "di� iltihab�", "di� apsesi", "di�imde apse", "di� eti iltihab�", "di�imde iltihap", "a��z kurulu�u", "a��z kurulu�um", "di� eti hastal���", "di� etimde hassaiyet", "di� sararmas�", "di�imde renk de�i�imi", "�ene a�r�s�", "�ene a�r�m", "di� sallanmas�", "di� ��r�mesi", "di�imde ��r�me", "di� eti kanamas�", "di� etinde kanama", "di� e�rili�i", "di�im e�ri", "di� g�c�rdatmas�", "di� implant�"]
text2Arr = ["var"]
i = 0
for text2 in text2Arr:
    for text in textArr:
        result = text + " " + text2
        print('"' + result + '",')
        i += 1