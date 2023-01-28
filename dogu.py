import json as pd



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



tr=pd.read_csv("Testing.csv")



tr.replace({'prognosis':{'Mantar Enfeksiyonu':0,'Alerji':1,'Reflü':2,'Kronik Kolestaz':3,'İlaç Reaksiyonu':4,
    'Peptik Ülser':5,'AIDS':6,'Şeker':7,'Bağırsak Enfeksiyonu':8,'Bronşiyal Astım':9,'Hipertansiyon':10,
    'Migren':11,'Boyun Kireçlenmesi':12,
    'Felç (Beyin Kanaması)':13,'Sarılık':14,'Sıtma':15,'Çiçeği':16,'Dang Humması':17,'Tifo':18,'Hepatit A':19,
    'Hepatit B':20,'Hepatit C':21,'Hepatit D':22,'Hepatit E':23,'Alkolik Hepatit':24,'Tüberküloz':25,
    'Soğuk Algınlığı':26,'Pnömoni (Zatürre)':27,'Hemoroid':28,'Kalp Krizi':29,'Varis Damar':30,'Hipotiroidi':31,
    'Hipertiroidi':32,'Hipoglisemi':33,'Kireçlenme':34,'Artrit':35,
    'Vertigo':36,'Akne':37,'İdrar Yolu Enfeksiyonu':38,'Sedef':39,
    'İmpetigo':40}},inplace=True)





df=pd.read_csv("Training.csv")





df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
    'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
    'Migraine':11,'Cervical spondylosis':12,
    'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
    'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
    'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
    'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
    '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
    'Impetigo':40}},inplace=True)