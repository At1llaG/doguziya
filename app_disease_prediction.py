from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd

l1=['kasinti','deri_dokuntusu','nodal_deri_dokuntuleri','surekli_hapsirma','titreme','titreme_nobeti','eklem_agrisi',
    'mide_agrisi','asitlik','dilde_ulserler','kas_erimesi','kusma','agrili_idrara_cikma','idarda_kan','yorgunluk',
    'kilo_alma','kaygi','ellerde_ve_ayaklarda_sogukluk','ani_duygu_degisimi','kilo_kaybi','huzursuzluk','uyusukluk','bademcik_yaralari',
    'duzensiz_seker_seviyesi','oksuruk','yuksek_ates','gozlerde_cokukluk','nefes_darlıgı','terlemek','sivi_kaybi','hazimsizlik',
    'bas_agrisi','ciltte_sararma','koyu_idrar','mide_bulantisi ','istah_kaybi','goz_arkasinda_agrı','sirt_agrisi','kabizlik',
    'bel_agrisi','ishal','hafif_ates','sari_idrar','gozlerin_sararmasi','akut_karaciger_yetmezligi','asiri_sivi_yuklenmesi',
    'midede_siskinlik','sismis_lenf_dugumleri','halsizlik','bulanik_ve_bozuk_gorus','balgam','bogazda_tahris',
    'gozlerde_kizarma','sinus_basinci','burun_akmasi','tikaniklik','gogus_agrisi','uzuvlarda_zayiflik','hizli_kalp_atisi',
    'bagirsak_hareketleri_sirasinda_agri','anal_bolgede_agri','kanli_diski','anuste_tahris','boyun_agrisi','bas_donmesi','kramplar',
    'morarma','obezite','bacaklarda_sisme','kan_damarlarinda_sisme','yüz_ve_gozlerde_kabariklik','tiroitte_buyume','tirnaklarda_kirilganlik',
    'uzuvlarda_sisme','asiri_aclik','evlilik_disi_iliski','dudaklarda_kuruma_ve_karincalanma','konusma_bozuklugu','diz_agrısı','kalca_ekleminde_agrı',
    'kas_gucsuzlugu','boyun_tutulmasi','eklemlerde_sisme','hareketlerde_zorlanma','hareketlerde_bukulme','denge_kaybi','sabit_olamama','vucudun_bir_tarafinda_gucsuzluk',
    'koku_kaybi','mesane _rahatsizligi','idrarin_kotu_kokmasi','surekli_idrar_hissi','gaz_kacirma','ic_kasinti','kiskirtici_olma',
    'depresyon','sinirlilik','kas_agrısı','net_dusunememe','vucut_uzerinde_kirmizi_noktalar','karin_agrisi','anormal_adet_gorme','deride_pigment_bozuklugu',
    'gozlerin_sulanmasi','istah_artisi','asiri_idrar_cikisi','aile_gecmisi','mukuslu_balgam','pasli_balgam','konsantrasyon_eksikligi','gorsel_rahatsizliklar',
    'kan _nakli_almak','steril_olmayan_enjeksiyonlar_almak','koma','mide_kanamasi','karin_siskinligi','alkol_tuketimi_oykusu',
    'asiri_sivi_yuklenmesi','balgamda_kan','baldırda_belirgin_damarlar','carpinti','agrılı_yuruyus','irinli_sivilce_cıkmasi','siyah_noktalar','yuzde_kasinti','ciltte_soyulma',
    'cilt_renginde_degısme','tirnaklarda_kucuk_ezikler','iltihapli_tirnaklar','su_toplama','burun_cevresinde_kirmizi_yara','deride_kabuklu_yaralar']



disease=['Mantar Enfeksiyonu','Alerji','Reflü','Kronik Kolestaz','İlaç Reaksiyonu',
        'Peptik Ülser','AIDS','Şeker','Bağırsak Enfeksiyonu','Bronşiyal Astım','Hipertansiyon',
        'Migren','Boyun Kireçlenmesi',
        'Felç (Beyin Kanaması)','Sarılık','Sıtma','Su Çiçeği','Dang Humması','Tifo','Hepatit A',
        'Hepatit B','Hepatit C','Hepatit D','Hepatit E','Alkolik Hepatit','Tüberküloz',
        'Soğuk Algınlığı','Pnömoni (Zatürre)','Hemoroid',
        'Kalp Krizi','Varis Damar','Hipotiroidi','Hipertiroidi','Hipoglisemi','Kireçlenme',
        'Artrit','Vertigo','Akne','İdrar Yolu Enfeksiyonu','Sedef',
        'İmpetigo']

l2=[]

for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA
# tr=pd.read_csv("Testing.csv")
tr=pd.read_csv("Data_EXCEL/testing_csv.csv", encoding='utf8')
tr.replace({'prognosis':{'Mantar Enfeksiyonu':0,'Alerji':1,'Reflü':2,'Kronik Kolestaz':3,'İlaç Reaksiyonu':4,
            'Peptik Ülser':5,'AIDS':6,'Şeker':7,'Bağırsak Enfeksiyonu':8,'Bronşiyal Astım':9,'Hipertansiyon':10,
            'Migren':11,'Boyun Kireçlenmesi':12,
            'Felç (Beyin Kanaması)':13,'Sarılık':14,'Sıtma':15,'Çiçeği':16,'Dang Humması':17,'Tifo':18,'Hepatit A':19,
            'Hepatit B':20,'Hepatit C':21,'Hepatit D':22,'Hepatit E':23,'Alkolik Hepatit':24,'Tüberküloz':25,
            'Soğuk Algınlığı':26,'Pnömoni (Zatürre)':27,'Hemoroid':28,'Kalp Krizi':29,'Varis Damar':30,'Hipotiroidi':31,
            'Hipertiroidi':32,'Hipoglisemi':33,'Kireçlenme':34,'Artrit':35,
            'Vertigo':36,'Akne':37,'İdrar Yolu Enfeksiyonu':38,'Sedef':39,
            'İmpetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["tehsis"]]
np.ravel(y_test)

# TRAINING DATA
df=pd.read_csv("Data_EXCEL/dataset_csv.csv",  encoding='utf8')

df.replace({'prognosis':{'Mantar Enfeksiyonu':0,'Alerji':1,'Reflü':2,'Kronik Kolestaz':3,'İlaç Reaksiyonu':4,
            'Peptik Ülser':5,'AIDS':6,'Şeker':7,'Bağırsak Enfeksiyonu':8,'Bronşiyal Astım':9,'Hipertansiyon':10,
            'Migren':11,'Boyun Kireçlenmesi':12,
            'Felç (Beyin Kanaması)':13,'Sarılık':14,'Sıtma':15,'Su Çiçeği':16,'Dang Humması':17,'Tifo':18,'Hepatit A':19,
            'Hepatit B':20,'Hepatit C':21,'Hepatit D':22,'Hepatit E':23,'Alkolik Hepatit':24,'Tüberküloz':25,
            'Soğuk Algınlığı':26,'Pnömoni (Zatürre)':27,'Hemoroid':28,'Kalp Krizi':29,'Varis Damar':30,'Hipotiroidi':31,
            'Hipertiroidi':32,'Hipoglisemi':33,'Kireçlenme':34,'Artrit':35,
            'Vertigo':36,'Akne':37,'İdrar Yolu Enfeksiyonu':38,'Sedef':39,
            'İmpetigo':40}},inplace=True)

X= df[l1]

y = df[["tehsis"]]
np.ravel(y)

def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
    else :
        NaiveBayes()

def NaiveBayes():
    from sklearn.naive_bayes import MultinomialNB
    gnb = MultinomialNB()
    gnb=gnb.fit(X,np.ravel(y))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(disease[predicted] == disease[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")

root = Tk()
root.title(" Disease Prediction From Symptoms")
root.configure()

Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

S1Lb = Label(root,  text="Symptom 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="Symptom 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root,  text="Symptom 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root,  text="Symptom 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root,  text="Symptom 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

lr = Button(root, text="Predict",height=2, width=20, command=message)
lr.config(font=("Elephant", 15))
lr.grid(row=15, column=1,pady=20)

OPTIONS = sorted(l1)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=2)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=2)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=2)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=2)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=2)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=1, pady=10,  sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=18, column=1, pady=10,  sticky=W)

t3 = Text(root, height=2, width=30)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1 , padx=10)

root.mainloop()
