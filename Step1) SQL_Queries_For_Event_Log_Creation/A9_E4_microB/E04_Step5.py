import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

    
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=0
            where org_name="no organism grew";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=1
            where org_name="YEAST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=2
            where org_name="HAFNIA ALVEI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=3
            where org_name="CANDIDA KEFYR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=4
            where org_name="KOCURIA ROSEA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=5
            where org_name="CANDIDA KRUSEI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=6
            where org_name="HAEMOPHILUS SP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=7
            where org_name="GEMELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=8
            where org_name="PANTOEA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=9
            where org_name="PROTEUS HAUSERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=10
            where org_name="PROTEUS PENNERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=11
            where org_name="PROTEUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=12
            where org_name="TRICHODERMA SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=13
            where org_name="CANDIDA ALBICANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=14
            where org_name="CANDIDA GLABRATA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=15
            where org_name="ENTEROCOCCUS SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=16
            where org_name="ESCHERICHIA COLI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=17
            where org_name="MYROIDES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=18
            where org_name="PROTEUS VULGARIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=19
            where org_name="RHIZOPUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=20
            where org_name="SERRATIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=21
            where org_name="SHEWANELLA ALGAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=22
            where org_name="ACHROMOBACTER SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=23
            where org_name="ACINETOBACTER SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=24
            where org_name="AEROMONAS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=25
            where org_name="NEISSERIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=26
            where org_name="PROTEUS MIRABILIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=27
            where org_name="CANDIDA TROPICALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=28
            where org_name="CITROBACTER KOSERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=29
            where org_name="ENTEROBACTERIACEAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=30
            where org_name="ENTEROCOCCUS AVIUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=31
            where org_name="GRAM POSITIVE RODS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=32
            where org_name="KLEBSIELLA OXYTOCA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=33
            where org_name="NOCARDIA FARCINICA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=34
            where org_name="SERRATIA ODORIFERA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=35
            where org_name="ALCALIGENES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=36
            where org_name="ASPERGILLUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=37
            where org_name="ASPERGILLUS TERREUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=38
            where org_name="CITROBACTER SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=39
            where org_name="DELFTIA ACIDOVORANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=40
            where org_name="EIKENELLA CORRODENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=41
            where org_name="ESCHERICHIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=42
            where org_name="MORGANELLA MORGANII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=43
            where org_name="PASTEURELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=44
            where org_name="PSEUDOMONAS PUTIDA ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=45
            where org_name="SERRATIA MARCESCENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=46
            where org_name="STAPH AUREUS COAG +";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=47
            where org_name="AEROMONAS HYDROPHILA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=48
            where org_name="ALCALIGENES FAECALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=49
            where org_name="CANDIDA DUBLINIENSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=50
            where org_name="CANDIDA PARAPSILOSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=51
            where org_name="ENTEROBACTER CLOACAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=52
            where org_name="ENTEROBACTER SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=53
            where org_name="ENTEROCOCCUS FAECIUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=54
            where org_name="GRAM NEGATIVE ROD #1";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=55
            where org_name="GRAM NEGATIVE ROD #2";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=56
            where org_name="GRAM NEGATIVE ROD(S)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=57
            where org_name="PROVIDENCIA RETTGERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=58
            where org_name="PROVIDENCIA STUARTII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=59
            where org_name="PSEUDOMONAS STUTZERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=60
            where org_name="ACHROMOBACTER SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=61
            where org_name="ACINETOBACTER LWOFFII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=62
            where org_name="ASPERGILLUS FUMIGATUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=63
            where org_name="ENTEROCOCCUS FAECALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=64
            where org_name="ESCHERICHIA HERMANNII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=65
            where org_name="KLEBSIELLA PNEUMONIAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=66
            where org_name="LACTOBACILLUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=67
            where org_name="MIXED BACTERIAL FLORA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=68
            where org_name="MORAXELLA CATARRHALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=69
            where org_name="PASTEURELLA MULTOCIDA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=70
            where org_name="PROBABLE ENTEROCOCCUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=71
            where org_name="SERRATIA LIQUEFACIENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=72
            where org_name="STAPHYLOCOCCUS LENTUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=73
            where org_name="STAPHYLOCOCCUS SCIURI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=74
            where org_name="STREPTOCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=75
            where org_name="VIRIDANS STREPTOCOCCI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=76
            where org_name="CAPNOCYTOPHAGA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=77
            where org_name="ENTEROBACTER AEROGENES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=78
            where org_name="GRAM POSITIVE BACTERIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=79
            where org_name="NEISSERIA MENINGITIDIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=80
            where org_name="PROTEUS VULGARIS GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=81
            where org_name="PSEUDOMONAS AERUGINOSA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=82
            where org_name="STAPHYLOCOCCUS CAPITIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=83
            where org_name="STAPHYLOCOCCUS WARNERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=84
            where org_name="STREPTOCOCCUS GORDONII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=85
            where org_name="ACINETOBACTER BAUMANNII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=86
            where org_name="CARDIOBACTERIUM HOMINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=87
            where org_name="ENTEROCOCCUS GALLINARUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=88
            where org_name="PSEUDOMONAS FLUORESCENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=89
            where org_name="STAPHYLOCOCCUS SIMULANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=90
            where org_name="STREPTOCOCCUS ANGINOSUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=91
            where org_name="STREPTOCOCCUS SANGUINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=92
            where org_name="ALCALIGENES XYLOSOXIDANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=93
            where org_name="CITROBACTER AMALONATICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=94
            where org_name="CORYNEBACTERIUM STRIATUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=95
            where org_name="SACCHAROMYCES CEREVISIAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=96
            where org_name="STREPTOCOCCUS PNEUMONIAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=97
            where org_name="SPHINGOMONAS PAUCIMOBILIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=98
            where org_name="BETA STREPTOCOCCUS GROUP A";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=99
            where org_name="BETA STREPTOCOCCUS GROUP B";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=100
            where org_name="BETA STREPTOCOCCUS GROUP C";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=101
            where org_name="BETA STREPTOCOCCUS GROUP G";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=102
            where org_name="HAEMOPHILUS PARAINFLUENZAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=103
            where org_name="STAPHYLOCOCCUS EPIDERMIDIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=104
            where org_name="STAPHYLOCOCCUS INTERMEDIUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=105
            where org_name="STAPHYLOCOCCUS LUGDUNENSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=106
            where org_name="STREPTOCOCCUS MITIS/ORALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=107
            where org_name="GRAM POSITIVE COCCUS(COCCI)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=108
            where org_name="STAPHYLOCOCCUS HAEMOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=109
            where org_name="ACINETOBACTER RADIORESISTENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=110
            where org_name="CITROBACTER FREUNDII COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=111
            where org_name="ENTEROBACTER CLOACAE COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=112
            where org_name="NOCARDIA ASTEROIDES COMPLEX ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=113
            where org_name="PROBABLE MICROCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=114
            where org_name="STENOTROPHOMONAS MALTOPHILIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=115
            where org_name="ASPERGILLUS FUMIGATUS COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=116
            where org_name="BETA STREPTOCOCCI, NOT GROUP A";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=117
            where org_name="COCCIDIOIDES IMMITIS/POSADASII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=118
            where org_name="ACINETOBACTER BAUMANNII COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=119
            where org_name="BACILLUS SPECIES; NOT ANTHRACIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=120
            where org_name="PRESUMPTIVE STREPTOCOCCUS BOVIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=121
            where org_name="STAPHYLOCOCCUS PSEUDINTERMEDIUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=122
            where org_name="MICROCOCCUS/STOMATOCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=123
            where org_name="ABIOTROPHIA/GRANULICATELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=124
            where org_name="HAEMOPHILUS SPECIES NOT INFLUENZAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=125
            where org_name="STAPHYLOCOCCUS, COAGULASE NEGATIVE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=126
            where org_name="YEAST, PRESUMPTIVELY NOT C. ALBICANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=127
            where org_name="CORYNEBACTERIUM SPECIES (DIPHTHEROIDS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=128
            where org_name="GAMMA(I.E. NON-HEMOLYTIC) STREPTOCOCCUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=129
            where org_name="STREPTOCOCCUS ANGINOSUS (MILLERI) GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=130
            where org_name="ACHROMOBACTER (ALCALIGENES) DENTRIFICANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=131
            where org_name="ACHROMOBACTER (ALCALIGENES) XYLOSOXIDANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=132
            where org_name="NON-FERMENTER, NOT PSEUDOMONAS AERUGINOSA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=133
            where org_name="CANDIDA ALBICANS, PRESUMPTIVE IDENTIFICATION";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=134
            where org_name="ASPERGILLUS SP. NOT FUMIGATUS, FLAVUS OR NIGER";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=135
            where org_name="HAEMOPHILUS INFLUENZAE, BETA-LACTAMASE NEGATIVE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=136
            where org_name="POSITIVE FOR METHICILLIN RESISTANT STAPH AUREUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=137
            where org_name="NEISSERIA GONORRHOEAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=138
            where org_name="NEISSERIA SPECIES, NOT GONORRHOEAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=139
            where org_name="CANCELLED";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=140
            where org_name="SHIGELLA BOYDII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=141
            where org_name="SHIGELLA SONNEI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=142
            where org_name="SHIGELLA FLEXNERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=143
            where org_name="SALMONELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=144
            where org_name="SALMONELLA THOMPSON";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=145
            where org_name="SALMONELLA SAINTPAUL";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=146
            where org_name="SALMONELLA BRAENDERUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=147
            where org_name="SALMONELLA HEIDELBERG";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=148
            where org_name="SALMONELLA MONTEVIDEO";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=149
            where org_name="SALMONELLA ENTERITIDIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=150
            where org_name="SALMONELLA ORANIENBURG";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=151
            where org_name="SALMONELLA TYPHIMURIUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=152
            where org_name="SALMONELLA BARRANQUILLA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=153
            where org_name="MOLD";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=154
            where org_name="ACIDFAST BACILLI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=155
            where org_name="BACILLUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=156
            where org_name="KLUYVERA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=157
            where org_name="PASTEURELLA CANIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=158
            where org_name="CANDIDA LUSITANIAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=159
            where org_name="SERRATIA FONTICOLA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=160
            where org_name="SHEWANELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=161
            where org_name="PEDIOCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=162
            where org_name="PSEUDOMONAS LUTEOLA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=163
            where org_name="PSEUDOMONAS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=164
            where org_name="SALMONELLA SANDIEGO";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=165
            where org_name="GRAM NEGATIVE ROD #3";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=166
            where org_name="STREPTOCOCCUS BOVIS ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=167
            where org_name="ENTEROBACTER ASBURIAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=168
            where org_name="PAENIBACILLUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=169
            where org_name="SALMONELLA TELELKEBIR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=170
            where org_name="PEPTOSTREPTOCOCCUS SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=171
            where org_name="STAPHYLOCOCCUS HOMINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=172
            where org_name="AGGREGATIBACTER SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=173
            where org_name="CAPNOCYTOPHAGA OCHRACEA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=174
            where org_name="CRYPTOCOCCUS NEOFORMANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=175
            where org_name="GRANULICATELLA ADIACENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=176
            where org_name="MYCOBACTERIUM FORTUITUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=177
            where org_name="PROPIONIBACTERIUM ACNES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=178
            where org_name="LECLERCIA ADECARBOXYLATA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=179
            where org_name="PLESIOMONAS SHIGELLOIDES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=180
            where org_name="ACTINOMYCES ODONTOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=181
            where org_name="ENTEROBACTER AMNIGENUS 2 ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=182
            where org_name="PROPIONIBACTERIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=183
            where org_name="STREPTOCOCCUS INTERMEDIUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=184
            where org_name="ACHROMOBACTER XYLOSOXIDANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=185
            where org_name="ENTEROCOCCUS CASSELIFLAVUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=186
            where org_name="STREPTOCOCCUS PARASANGUINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=187
            where org_name="CHRYSEOBACTERIUM INDOLOGENES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=188
            where org_name="STAPHYLOCOCCUS SAPROPHYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=189
            where org_name="ANAEROBIC GRAM POSITIVE ROD(S)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=190
            where org_name="PRESUMPTIVE GARDNERELLA VAGINALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=191
            where org_name="CRONOBACTER (ENTEROBACTER) SAKAZAKII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=192
            where org_name="KLEBSIELLA (RAOULTELLA) ORNITHINOLYTICA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=193
            where org_name="RESEMBLING MICROCOCCUS/STOMATOCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=194
            where org_name="STREPTOCOCCUS GALLOLYTICUS SSP. PASTEURIANUS (STREPTOCOCCUS BOVIS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=195
            where org_name="BACTERIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=196
            where org_name="ORGANISM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=197
            where org_name="2ND ISOLATE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=198
            where org_name="AEROCOCCUS URINAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=199
            where org_name="SERRATIA RUBIDAEA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=200
            where org_name="AEROCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=201
            where org_name="ALPHA STREPTOCOCCI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=202
            where org_name="BETA STREPTOCOCCUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=203
            where org_name="ENTEROCOCCUS HIRAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=204
            where org_name="KLEBSIELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=205
            where org_name="SALMONELLA JAVIANA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=206
            where org_name="AEROCOCCUS VIRIDANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=207
            where org_name="PROVIDENCIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=208
            where org_name="BURKHOLDERIA CEPACIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=209
            where org_name="CITROBACTER SEDLAKII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=210
            where org_name="OCHROBACTRUM ANTHROPI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=211
            where org_name="PSEUDOMONAS MENDOCINA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=212
            where org_name="RAOULTELLA PLANTICOLA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=213
            where org_name="RHIZOBIUM RADIOBACTER";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=214
            where org_name="ENTEROBACTER GERGOVIAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=215
            where org_name="GARDNERELLA  VAGINALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=216
            where org_name="HAEMOPHILUS INFLUENZAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=217
            where org_name="STAPHYLOCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=218
            where org_name="CLOSTRIDIUM PERFRINGENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=219
            where org_name="ENTEROCOCCUS RAFFINOSUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=220
            where org_name="ENTEROBACTER CANCEROGENUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=221
            where org_name="STREPTOCOCCUS BOVIS GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=222
            where org_name="BURKHOLDERIA CEPACIA GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=223
            where org_name="RAOULTELLA ORNITHINOLYTICA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=224
            where org_name="STREPTOCOCCUS MILLERI GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=225
            where org_name="KLEBSIELLA (RAOULTELLA) PLANTICOLA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=226
            where org_name="PANTOEA (ENTEROBACTER) AGGLOMERANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=227
            where org_name="CORYNEBACTERIUM UREALYTICUM SP. NOV.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=228
            where org_name="ELIZABETHKINGIA (CHRYSEOBACTERIUM) MENIGOSEPTICA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=229
            where org_name="STAPHYLOCOCCUS SAPROPHYTICUS, PRESUMPTIVE IDENTIFICATION";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=230
            where org_name="LOMENTOSPORA PROLIFICANS (FORMERLY SCEDOSPORIUM PROLIFICANS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=231
            where org_name="STAPHYLOCOCCUS, COAGULASE NEGATIVE, PRESUMPTIVELY NOT S. SAPROPHYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=232
            where org_name="VIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=233
            where org_name="ADENOVIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=234
            where org_name="RHINOVIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=235
            where org_name="ENTEROVIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=236
            where org_name="CYTOMEGALOVIRUS ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=237
            where org_name="INFLUENZA A VIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=238
            where org_name="INFLUENZA B VIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=239
            where org_name="VARICELLA-ZOSTER VIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=240
            where org_name="PARAINFLUENZA VIRUS TYPE 1";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=241
            where org_name="PARAINFLUENZA VIRUS TYPE 3";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=242
            where org_name="HERPES SIMPLEX VIRUS TYPE 1";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=243
            where org_name="HERPES SIMPLEX VIRUS TYPE 2";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=244
            where org_name="RESPIRATORY SYNCYTIAL VIRUS (RSV)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=245
            where org_name="MUCOR SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=246
            where org_name="ACTINOMYCES SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=247
            where org_name="FUSARIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=248
            where org_name="DEMATIACEOUS MOLD";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=249
            where org_name="KOCURIA KRISTINAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=250
            where org_name="MORAXELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=251
            where org_name="STREPTOCOCCUS MITIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=252
            where org_name="ESCHERICHIA VULNERIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=253
            where org_name="SPHINGOMONAS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=254
            where org_name="TRICHOPHYTON SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=255
            where org_name="STAPHYLOCOCCUS CAPRAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=256
            where org_name="MALASSEZIA PACHYDERMATIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=257
            where org_name="STAPHYLOCOCCUS SCHLEIFERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=258
            where org_name="CORYNEBCATERIUM AMYCOLATUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=259
            where org_name="AEROMONAS HYDROPHILA COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=260
            where org_name="ANAEROBIC GRAM NEGATIVE ROD(S)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=261
            where org_name="CHRYSEOBACTERIUM MENINGOSEPTICUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=262
            where org_name="BETA STREPTOCOCCUS NOT GROUP A OR B";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=263
            where org_name="NUTRITIONALLY VARIANT STREPTOCOCCUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=264
            where org_name="ACTINOBACILLUS ACTINOMYCETEMCOMITANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=265
            where org_name="CORYNEBACTERIUM ACCOLANS (CDC GROUP 6)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=266
            where org_name="AGGREGATIBACTER (HAEMOPHILUS) APHROPHILUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=267
            where org_name="BETA STREP NOT GROUP A OR ANGINOSUS (MILLERI)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=268
            where org_name="BETA STREP NOT GROUP A, B OR ANGINOSUS (MILLERI)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=269
            where org_name="ACHROMOBACTER (ALCALIGENES) XYLOSOXIDANS SS DENTRIFICANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=270
            where org_name="STREPTOCOCCUS GALLOLYTICUS SSP. GALLOLYTICUS (STREPTOCOCCUS BOVIS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=271
            where org_name="STREPTOCOCCUS MUTANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=272
            where org_name="LISTERIA MONOCYTOGENES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=273
            where org_name="PRESUMPTIVE CLOSTRIDIUM PERFRINGENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=274
            where org_name="FUNGUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=275
            where org_name="ALTERNARIA SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=276
            where org_name="CANDIDA FAMATA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=277
            where org_name="ULOCLADIUM SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=278
            where org_name="STEMPHYLIUM SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=279
            where org_name="MYCELIA STERILIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=280
            where org_name="ASPERGILLUS NIGER";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=281
            where org_name="EXOPHIALA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=282
            where org_name="ASPERGILLUS FLAVUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=283
            where org_name="CHAETOMIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=284
            where org_name="FONSECAEA PEDROSOI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=285
            where org_name="GRAM VARIABLE RODS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=286
            where org_name="GRAPHIUM EUMORPHUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=287
            where org_name="RHINOCLADIELLA SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=288
            where org_name="GEOTRICHIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=289
            where org_name="PENICILLIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=290
            where org_name="CLADOSPORIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=291
            where org_name="PAECILOMYCES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=292
            where org_name="PERONEUTYPA SCOPARIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=293
            where org_name="TRICHOSPORON SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=294
            where org_name="ARTHROGRAPHIS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=295
            where org_name="PENICILLIUM MARNEFFEI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=296
            where org_name="RHODATORULA MUCILAGINOSA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=297
            where org_name="SCOPULARIOPSIS BREVICAULIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=298
            where org_name="CUNNINGHAMELLA BERTHOLLETIAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=299
            where org_name="EXOPHIALA JEANSELMEI COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=300
            where org_name="SPOROTHRIX SCHENCKII COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=301
            where org_name="ASPERGILLUS VERSICOLOR GROUP ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=302
            where org_name="NOCARDIA TRANSVALENSIS COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=303
            where org_name="EXOPHIALA (WANGIELLA) DERMATITIDIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=304
            where org_name="SCEDOSPORIUM (APIOSPERMUM) BOYDII COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=305
            where org_name="ROTHIA DENTOCARIOSA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=306
            where org_name="VEILLONELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=307
            where org_name="CLOSTRIDIUM SEPTICUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=308
            where org_name="FUSOBACTERIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=309
            where org_name="VIBRIO PARAHAEMOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=310
            where org_name="ENTAMOEBA SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=311
            where org_name="GIARDIA CYSTS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=312
            where org_name="STRONGYLOIDES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=313
            where org_name="ENDOLIMAX NANA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=314
            where org_name="ENTAMOEBA COLI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=315
            where org_name="GIARDIA LAMBLIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=316
            where org_name="CHILOMASTIX MESNILI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=317
            where org_name="ENTAMOEBA HARTMANNI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=318
            where org_name="IODAMOEBA BUTSCHLII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=319
            where org_name="BLASTOCYSTIS HOMINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=320
            where org_name="DIENTAMOEBA FRAGILIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=321
            where org_name="DIPHYLLOBOTHRIUM SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=322
            where org_name="ENTEROBIUS VERMICULARIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=323
            where org_name="FEW BLASTOCYSTIS HOMINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=324
            where org_name="MANY BLASTOCYSTIS HOMINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=325
            where org_name="RARE BLASTOCYSTIS HOMINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=326
            where org_name="STRONGYLOIDES STERCORALIS ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=327
            where org_name="ENTAMOEBA HISTOLYTICA/DISPAR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=328
            where org_name="MODERATE BLASTOCYSTIS HOMINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=329
            where org_name="CRYPTOSPORIDIUM PARVUM OOCYSTS SEEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=330
            where org_name="CANDIDA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=331
            where org_name="FUSOBACTERIUM NUCLEATUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=332
            where org_name="BACTEROIDES FRAGILIS GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=333
            where org_name="ANAEROBIC GRAM POSITIVE COCCUS(I)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=334
            where org_name="PRESUMPTIVE PROPIONIBACTERIUM ACNES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=335
            where org_name="CLOSTRIDIUM SPECIES NOT C. PERFRINGENS OR C. SEPTICUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=336
            where org_name="NEGATIVE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=337
            where org_name="POSITIVE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=338
            where org_name="CLOSTRIDIUM DIFFICILE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=339
            where org_name="NOCARDIA NOVA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=340
            where org_name="NOCARDIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=341
            where org_name="NOCARDIA OTITIDISCAVIARUM (CAVIAE)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=342
            where org_name="ACTINOMYCETE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=343
            where org_name="GORDONIA SPUTI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=344
            where org_name="MYCOBACTERIUM AVIUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=345
            where org_name="NOCARDIA ASTEROIDES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=346
            where org_name="STREPTOMYCES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=347
            where org_name="MYCOBACTERIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=348
            where org_name="MYCOBACTERIUM SZULGAI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=349
            where org_name="MYCOBACTERIUM TRIPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=350
            where org_name="MYCOBACTERIUM CHELONAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=351
            where org_name="MYCOBACTERIUM GORDONAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=352
            where org_name="MYCOBACTERIUM KANSASII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=353
            where org_name="MYCOBACTERIUM ABSCESSUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=354
            where org_name="MYCOBACTERIUM MALMOENSE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=355
            where org_name="MYCOBATERIUM HAEMOPHILUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=356
            where org_name="MYCOBACTERIUM LENTIFLAVUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=357
            where org_name="MYCOBACTERIUM MUCOGENICUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=358
            where org_name="MYCOBACTERIUM MARSEILLENSE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=359
            where org_name="MYCOBACTERIUM AVIUM COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=360
            where org_name="MYCOBACTERIUM ABSCESSUS GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=361
            where org_name="MYCOBACTERIUM TUBERCULOSIS COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=362
            where org_name="MYCOBACTERIUM CHIMAERA INTRACELLULARE GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=363
            where org_name="AFB GROWN IN CULTURE; ADDITIONAL INFORMATION TO FOLLOW";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=364
            where org_name="DESULFOVIBRIO SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=365
            where org_name="MYCOPLASMA HOMINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=366
            where org_name="MYCOPLASMA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=367
            where org_name="PREVOTELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=368
            where org_name="BACTEROIDES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=369
            where org_name="CUTIBACTERIUM ACNES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=370
            where org_name="EUBACTERIUM LIMOSUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=371
            where org_name="BACTEROIDES FRAGILIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=372
            where org_name="PORPHYROMONAS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=373
            where org_name="CLOSTRIDIUM CLOSTRIDIIFORME";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=374
            where org_name="BACTEROIDES UREOLYTICUS GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=375
            where org_name="PRESUMPTIVE VEILLONELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=376
            where org_name="PREVOTELLA (BACTEROIDES) SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=377
            where org_name="PRESUMPTIVE PEPTOSTREPTOCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=378
            where org_name="CUTIBACTERIUM (PROPIONIBACTERIUM) ACNES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=379
            where org_name="FINEGOLDIA (PEPTOSTREPTOCOCCUS) SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=380
            where org_name="PRESUMPTIVE FUSOBACTERIUM MORTIFERUM/VARIUM GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=381
            where org_name="MYCOBACTERIUM MARINUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=382
            where org_name="LEGIONELLA PNEUMOPHILA, GROUP 1";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=383
            where org_name="GRAM NEGATIVE ROD #4";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=384
            where org_name="MICROSPORIDIUM SPECIES SEEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=385
            where org_name="POSITIVE FOR MICROSPORIDIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=386
            where org_name="ALACALIGENES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=387
            where org_name="BURKHOLDERIA GLADIOLI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=388
            where org_name="LACTOBACILLUS GASSERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=389
            where org_name="YOKENELLA REGENSBURGEI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=390
            where org_name="HAEMOPHILUS HAEMOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=391
            where org_name="NOCARDIA CYRIACIGEORGICA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=392
            where org_name="PSEUDALLESCHERIA BOYDII ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=393
            where org_name="BORDETELLA BRONCHISEPTICA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=394
            where org_name="PSEUDOMONAS ORYZIHABITANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=395
            where org_name="ACHROMOBACTER  DENTRIFICANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=396
            where org_name="SERRATIA LIQUEFACIENS COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=397
            where org_name="PSEUDOMONAS PUTIDA/FLUORESCENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=398
            where org_name="HAEMOPHILUS INFLUENZAE, BETA-LACTAMASE POSITIVE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=399
            where org_name="CUPRIAVIDUS PAUCULUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=400
            where org_name="POSITIVE FOR CRYPTOCOCCAL ANTIGEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=401
            where org_name="CAMPYLOBACTER JEJUNI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=402
            where org_name="ATOPOBIUM RIMAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=403
            where org_name="SALMONELLA TYPHI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=404
            where org_name="SALMONELLA DUBLIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=405
            where org_name="BACILLUS SUBTILIS ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=406
            where org_name="ROSEOMONAS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=407
            where org_name="ALLOIOCOCCUS OTITIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=408
            where org_name="CLOSTRIDIUM RAMOSUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=409
            where org_name="CLOSTRIDIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=410
            where org_name="CLOSTRIDIUM TERTIUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=411
            where org_name="ENTEROCOCCUS DURANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=412
            where org_name="GEMELLA HAEMOLYSANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=413
            where org_name="GEMELLA MORBILLORUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=414
            where org_name="LACTOCOCCUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=415
            where org_name="MORAXELLA OSLOENSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=416
            where org_name="RHODOTORULA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=417
            where org_name="ROSEOMONAS GILARDII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=418
            where org_name="ROTHIA MUCILAGINOSA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=419
            where org_name="BURKHOLDERIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=420
            where org_name="LEPTOTRICHIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=421
            where org_name="OCHROBACTRUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=422
            where org_name="STREPTOCOCCUS ORALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=423
            where org_name="CLOSTRIDIUM SAUDIENSE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=424
            where org_name="WAUTERSIELLA FALSENII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=425
            where org_name="ACTINOMYCES TURICENSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=426
            where org_name="BIFIDOBACTERIUM LONGUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=427
            where org_name="HERBASPIRILLUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=428
            where org_name="LEPTOTRICHIA HOFSTADII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=429
            where org_name="SALMONELLA PARATYPHI A";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=430
            where org_name="AUREOBASIDIUM PULLULANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=431
            where org_name="BURKHOLDERIA XENOVORANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=432
            where org_name="LACTOBACILLUS FERMENTUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=433
            where org_name="GRAM NEGATIVE DIPLOCOCCI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=434
            where org_name="OCHROBACTRUM INTERMEDIUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=435
            where org_name="STREPTOCOCCUS SALIVARIUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=436
            where org_name="AGROBACTERIUM RADIOBACTER";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=437
            where org_name="BREVUNDIMONAS VESICULARIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=438
            where org_name="CUPRIAVIDUS METALLIDURANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=439
            where org_name="MORAXELLA NONLIQUIFACIENS ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=440
            where org_name="STAPHYLOCOCCUS AURICULARIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=441
            where org_name="STREPTOCOCCUS VESTIBULARIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=442
            where org_name="STREPTOCOCCUS ALACTOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=443
            where org_name="STREPTOCCUS SALIVARIUS GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=444
            where org_name="BACILLUS CEREUS/THURINGIENSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=445
            where org_name="STAPHYLOCOCCUS CAPRAE/CAPITIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=446
            where org_name="ANAEROBIC GRAM NEGATIVE ROD #2";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=447
            where org_name="STAPHYLOCOCCUS WARNERI/PASTEURI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=448
            where org_name="PRESUMPTIVE CLOSTRIDIUM SEPTICUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=449
            where org_name="LACTOBACILLUS CASEI/PARACASEI/ZEAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=450
            where org_name="LACTOBACILLUS SALIVARIUS SS. SALIVARIUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=451
            where org_name="STREPTOCOCCUS SALIVARIUS SSP. SALIVARIUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=452
            where org_name="STREPTOCOCCUS INFANTARIUS SSP. COLI (STR. LUTETIENSIS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=453
            where org_name="STREPTOCOCCUS INFANTARIUS SSP. COLI (STREPTOCOCCUS BOVIS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=454
            where org_name="STREPTOCOCCUS INFANTARIUS SSP. INFANTARIUS (STREPTOCOCCUS BOVIS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=455
            where org_name="POSITIVE FOR GROUP B BETA STREPTOCOCCI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=456
            where org_name="S. AUREUS POSITIVE; MRSA NEGATIVE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=457
            where org_name="S. AUREUS POSITIVE; MRSA POSITIVE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=458
            where org_name="TRICHOMONAS VAGINALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=459
            where org_name="POSITIVE FOR M. TUBERCULOSIS BY MTD";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=460
            where org_name="PARAINFLUENZA VIRUS TYPE 2";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=461
            where org_name="POSITIVE FOR PARAINFLUENZA VIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=462
            where org_name="PRESUMPTIVE POSITIVE FOR LEGIONELLA SEROGROUP 1 ANTIGEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=463
            where org_name="WORM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=464
            where org_name="ASCARIS LUMBRICOIDES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=465
            where org_name="YERSINIA INTERMEDIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=466
            where org_name="GIARDIA LAMBLIA SEEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=467
            where org_name="POSITIVE FOR INFLUENZA A VIRAL ANTIGEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=468
            where org_name="POSITIVE FOR INFLUENZA B VIRAL ANTIGEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=469
            where org_name="DERMATOPHYTE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=470
            where org_name="CURVULARIA SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=471
            where org_name="NIGROSPORA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=472
            where org_name="SCOPULARIOPSIS SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=473
            where org_name="TRICHOSPORON MUCOIDES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=474
            where org_name="NEOSCYTALIDIUM DIMIDIATUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=475
            where org_name="IXODES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=476
            where org_name="TICK CONSISTENT WITH IXODES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=477
            where org_name="TICK NOT CONSISTENT WITH IXODES SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=478
            where org_name="POSITIVE FOR ADENOVIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=479
            where org_name="POSITIVE FOR PARAINFLUENZA TYPE 1";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=480
            where org_name="POSITIVE FOR PARAINFLUENZA TYPE 2";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=481
            where org_name="POSITIVE FOR PARAINFLUENZA TYPE 3";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=482
            where org_name="POSITIVE FOR RESPIRATORY SYNCYTIAL VIRUS (RSV)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=483
            where org_name="ESCHERICHIA COLI O157:H7";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=484
            where org_name="POSITIVE FOR HERPES SIMPLEX TYPE 1 (HSV1)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=485
            where org_name="POSITIVE FOR HERPES SIMPLEX TYPE 2 (HSV2)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=486
            where org_name="POSITIVE FOR VARICELLA ZOSTER";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=487
            where org_name="POSITIVE FOR CYTOMEGALOVIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=488
            where org_name="POSITIVE FOR HERPES SIMPLEX (HSV)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=489
            where org_name="POSITIVE FOR PNEUMOCYSTIS JIROVECII (CARINII)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=490
            where org_name="CHLAMYDIA TRACHOMATIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=491
            where org_name="MICROCOCCUS LUTEUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=492
            where org_name="OLIGELLA URETHRALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=493
            where org_name="LACTOBACILLUS RHAMNOSUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=494
            where org_name="SALMONELLA AGONA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=495
            where org_name="SALMONELLA NEWPORT";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=496
            where org_name="SALMONELLA MBANDAKA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=497
            where org_name="SALMONELLA CORVALLIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=498
            where org_name="SALMONELLA SCHWARZENGRUND";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=499
            where org_name="CITROBACTER YOUNGAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=500
            where org_name="CORYNEBACTERIUM GLUCURONOLYTICUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=501
            where org_name="CORYNEBACTERIUM PYRUVICIPRODUCENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=502
            where org_name="ESCHERICHIA FERGUSONII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=503
            where org_name="PROBABLE GARDNERELLA VAGINALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=504
            where org_name="CANDIDA KRUSEI / CANDIDA INCONSPICUA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=505
            where org_name="LEUCONOSTOC MESENTEROIDES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=506
            where org_name="IRPEX LACTEUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=507
            where org_name="PHOMA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=508
            where org_name="MICROSPORUM CANIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=509
            where org_name="ACREMONIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=510
            where org_name="TRICHOPHYTON RUBRUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=511
            where org_name="CONIDIOBOLUS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=512
            where org_name="ACRODONTIUM SALMONEUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=513
            where org_name="SYNCEPHALASTRUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=514
            where org_name="SPOROBOLOMYCES SALMONICOLOR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=515
            where org_name="NEISSERIA MUCOSA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=516
            where org_name="MUCOR IRREGULARIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=517
            where org_name="CANDIDA GUILLIERMONDII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=518
            where org_name="HOOKWORM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=519
            where org_name="HYMENOLEPIS NANA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=520
            where org_name="ASPERGILLUS NIDULANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=521
            where org_name="GORDONIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=522
            where org_name="MYCOBACTERIUM BOVIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=523
            where org_name="MYCOBACTERIUM XENOPI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=524
            where org_name="MYCOBACTERIUM CELATUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=525
            where org_name="MYCOBACTERIUM TUBERCULOSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=526
            where org_name="ANAEROBIC BACTERIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=527
            where org_name="CUTIBACTERIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=528
            where org_name="CUNNINGHAMELLA SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=529
            where org_name="NEUROSPORA SITOPHILA (FORMERLY CHRYSONILLA SITOPHILA)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=530
            where org_name="CAMPYLOBACTER SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=531
            where org_name="GEMELLA BERGERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=532
            where org_name="PARACOCCUS YEEI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=533
            where org_name="BRUCELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=534
            where org_name="KINGELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=535
            where org_name="LEUCONOSTOC SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=536
            where org_name="CLOSTRIDIUM INNOCUUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=537
            where org_name="GLOBICATELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=538
            where org_name="ACTINOMYCES NAESLUNDII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=539
            where org_name="DESULFOVIBRIO LEGALLII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=540
            where org_name="LEPTOTRICHIA TREVISANII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=541
            where org_name="STREPTOCOCCUS SALIVARUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=542
            where org_name="BACILLUS CIRCULANS GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=543
            where org_name="CAMPYLOBACTER UREOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=544
            where org_name="STREPTOCOCCUS PORCINUS/PSEUDOPORCINUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=545
            where org_name="PEPTONIPHILUS (PEPTOSTREPTOCOCCUS) SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=546
            where org_name="TRICHOMONAS VAGINALIS SEEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=547
            where org_name="MYCOBACTERIUM NEOAURUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=548
            where org_name="YERSINIA ENTEROCOLITICA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=549
            where org_name="PITHOMYCES SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=550
            where org_name="HUMICOLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=551
            where org_name="TICK";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=552
            where org_name="CANDIDA AURIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=553
            where org_name="ROTHIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=554
            where org_name="VIBRIO SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=555
            where org_name="ACETOBACTER SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=556
            where org_name="KOCURIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=557
            where org_name="SALMONELLA OSLO";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=558
            where org_name="EMMONSIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=559
            where org_name="MALASSEZIA FURFUR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=560
            where org_name="SALMONELLA ANATUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=561
            where org_name="BEAUVERIA BASSIANA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=562
            where org_name="SALMONELLA STANLEY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=563
            where org_name="SALMONELLA MUENCHEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=564
            where org_name="ACTINOMYCES ISRAELII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=565
            where org_name="NOCARDIA BRASILIENSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=566
            where org_name="FRANCISELLA TULARENSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=567
            where org_name="GLOBICATELLA SANGUINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=568
            where org_name="STREPTOCOCCUS PORCINUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=569
            where org_name="LEGIONELLA PNEUMOPHILA ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=570
            where org_name="PHAEOACREMONIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=571
            where org_name="EPIDERMOPHYTON FLOCCOSUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=572
            where org_name="CAMPYLOBACTER UPSALIENSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=573
            where org_name="PREVOTELLA MELANINOGENICA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=574
            where org_name="STREPTOCOCCUS MITIS GROUP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=575
            where org_name="BACTEROIDES DOREI/VULGATUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=576
            where org_name="DESULFOVIBRIO DESULFURICANS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=577
            where org_name="ERYSIPELOTHRIX RHUSIOPATHIAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=578
            where org_name="HAEMOPHILUS PARAHAEMOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=579
            where org_name="SAPROCHAETE (FORMERLY GEOTRICHUM) CAPITATA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=580
            where org_name="LISTERIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=581
            where org_name="SALMONELLA INFANTIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=582
            where org_name="SALMONELLA MUENSTER";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=583
            where org_name="SPHINGOBACTERIUM MULTIVORUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=584
            where org_name="ZYGOSACCHAROMYCES FERMENTATI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=585
            where org_name="STREPTOCOCCUS CONSTELLATUS SSP. CONSTELLATUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=586
            where org_name="CORYNEBACTERIUM JEIKEIUM (C.D.C. GROUP JK)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=587
            where org_name="MICROBACTERIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=588
            where org_name="BASIDIOMYCETE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=589
            where org_name="CRYPTOCOCCUS LAURENTII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=590
            where org_name="PENICILLIUM FELLUTANUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=591
            where org_name="SCEDOSPORIUM APIOSPERMUM COMPLEX";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=592
            where org_name="CYCLOSPORA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=593
            where org_name="MYCOBACTERIUM FLAVESCENS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=594
            where org_name="MYCOBACTERIUM MAGERITENSE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=595
            where org_name="CUTIBACTERIUM AVIDUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=596
            where org_name="LEGIONELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=597
            where org_name="VIBRIO ALGINOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=598
            where org_name="CANDIDA RUGOSA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=599
            where org_name="PREVOTELLA ORALIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=600
            where org_name="BREVIBACTERIUM CASEI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=601
            where org_name="BREVUNDIMONAS DIMINUTA/VESICULARIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=602
            where org_name="TAENIA SAGINATA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=603
            where org_name="SYTALIDIUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=604
            where org_name="HERPES SIMPLEX VIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=605
            where org_name="HEMOPHILUS HEMOLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=606
            where org_name="EPICOCCUM SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=607
            where org_name="VERTICILLIUM SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=608
            where org_name="NEOASCOCHYTA DESMAZIERI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=609
            where org_name="MYCOBACTERIUM ASIATICUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=610
            where org_name="MALASSEZIA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=611
            where org_name="CAMPYLOBACTER COLI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=612
            where org_name="SLACKIA EXIGUA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=613
            where org_name="DOLOSIGRANULUM PIGRUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=614
            where org_name="NO GROWTH";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=615
            where org_name="BIPOLARIS SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=616
            where org_name="BACTEROIDIES THETAIOTAOMICRON";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=617
            where org_name="MICROMONOSPORA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=618
            where org_name="TSUKAMURELLA SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=619
            where org_name="MYCOBACTERIUM TERRAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=620
            where org_name="MYCOBACTERIUM SCROFULACEUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=621
            where org_name="FUSOBACTERIUM NECROPHORUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=622
            where org_name="CAMPYLOBACTER LARI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=623
            where org_name="RHODOTORULA GLUTINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=624
            where org_name="ROSEOMONAS MUCOSA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=625
            where org_name="ACTINOTIGNUM SANGUINIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=626
            where org_name="ARCANOBACTERIUM HAEMOLYTICUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=627
            where org_name="CIMEX SPECIES (BEDBUG)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=628
            where org_name="TAENIA SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=629
            where org_name="YERSINIA SP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=630
            where org_name="VIBRIO CHOLERAE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=631
            where org_name="SALMONELLA HADAR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=632
            where org_name="USTILAGO SPECIES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=633
            where org_name="SALMONELLA KIAMBU";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=634
            where org_name="STACHYBOTRYS SPP.";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=635
            where org_name="NEISSERIA SUBFLAVA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=636
            where org_name="PINWORM EGG(S) SEEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=637
            where org_name="PHIALEMONIUM INFLATUM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=638
            where org_name="HAEMOPHILUS APHROPHILUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=639
            where org_name="DIALISTER MICRAEROPHILUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=640
            where org_name="ANAEROBIC GRAM NEGATIVE COCCI";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=641
            where org_name="STAPHYLOCOCCUS SACCHAROLYTICUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set org_name_Syn=642
            where org_name="ANAEROBIC GRAM POSITIVE BACTERIA";


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
