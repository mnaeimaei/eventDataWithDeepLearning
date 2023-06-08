import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

##########################################################

        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=1
            where test_name="TISSUE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=2
            where test_name="voided";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=3
            where test_name="Problem";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=4
            where test_name="Lyme IgG";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=5
            where test_name="Lyme IgM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=6
            where test_name="MONOSPOT";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=7
            where test_name="ASO TITER";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=8
            where test_name="ASO Screen";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=9
            where test_name="GRAM STAIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=10
            where test_name="MRSA SCREEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=11
            where test_name="R/O GC Only";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=12
            where test_name="HCV GENOTYPE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=13
            where test_name="FECAL CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=14
            where test_name="FLUID CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=15
            where test_name="LYME SEROLOGY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=16
            where test_name="URINE CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=17
            where test_name="VIRAL CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=18
            where test_name="WOUND CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=19
            where test_name="AEROBIC BOTTLE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=20
            where test_name="CMV Viral Load";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=21
            where test_name="FUNGAL CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=22
            where test_name="HBV Viral Load";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=23
            where test_name="HCV VIRAL LOAD";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=24
            where test_name="ACID FAST SMEAR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=25
            where test_name="GENITAL CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=26
            where test_name="ISOLATE FOR MIC";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=27
            where test_name="OVA + PARASITES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=28
            where test_name="SWAB- R/O YEAST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=29
            where test_name="ANAEROBIC BOTTLE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=30
            where test_name="BRUCELLA CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=31
            where test_name="C. difficile PCR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=32
            where test_name="CMV IgG ANTIBODY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=33
            where test_name="CMV IgM ANTIBODY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=34
            where test_name="CYCLOSPORA STAIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=35
            where test_name="FOCUSED ANALYSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=36
            where test_name="NOCARDIA CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=37
            where test_name="QUANTITATIVE RPR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=38
            where test_name="ACID FAST CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=39
            where test_name="ANAEROBIC CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=40
            where test_name="BLOOD/AFB CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=41
            where test_name="CHLAMYDIA CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=42
            where test_name="LEGIONELLA CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=43
            where test_name="MUMPS IgG ANTIBODY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=44
            where test_name="POSTMORTEM CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=45
            where test_name="Stool Hold Request";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=46
            where test_name="TISSUE CULTURE-CVS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=47
            where test_name="Enterovirus Culture";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=48
            where test_name="MICROSPORIDIA STAIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=49
            where test_name="RESPIRATORY CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=50
            where test_name="Staph aureus Screen";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=51
            where test_name="BLOOD/FUNGAL CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=52
            where test_name="CRYPTOCOCCAL ANTIGEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=53
            where test_name="Malaria Antigen Test";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=54
            where test_name="REFLEX URINE CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=55
            where test_name="RUBELLA IgG SEROLOGY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=56
            where test_name="TISSUE CULTURE-FLUID";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=57
            where test_name="CAMPYLOBACTER CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=58
            where test_name="RUBEOLA ANTIBODY, IgG";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=59
            where test_name="Swab - R/O Yeast - IC";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=60
            where test_name="TISSUE CULTURE-TISSUE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=61
            where test_name="BRUCELLA BLOOD CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=62
            where test_name="Blood Culture, Neonate";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=63
            where test_name="Blood Culture, Routine";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=64
            where test_name="Cipro Resistant Screen";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=65
            where test_name="GRAM STAIN- R/O THRUSH";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=66
            where test_name="R/O Beta Strep Group A";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=67
            where test_name="R/O GROUP B BETA STREP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=68
            where test_name="Staph aureus Preop PCR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=69
            where test_name="CHROMOSOME ANALYSIS-CVS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=70
            where test_name="ED Gram Stain for Yeast";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=71
            where test_name="M. furfur Blood Culture";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=72
            where test_name="RPR w/check for Prozone";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=73
            where test_name="SCOTCH TAPE PREP/PADDLE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=74
            where test_name="TOXOPLASMA IgG ANTIBODY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=75
            where test_name="TOXOPLASMA IgM ANTIBODY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=76
            where test_name="TRICHOMONAS SALINE PREP";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=77
            where test_name="YEAST VAGINITIS CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=78
            where test_name="ADDITIONAL CELLS COUNTED";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=79
            where test_name="FISH ANALYSIS, 3-5 CELLS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=80
            where test_name="Fluid Culture in Bottles";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=81
            where test_name="MTB Direct Amplification";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=82
            where test_name="Myco-F Bottle Gram Stain";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=83
            where test_name="RAPID PLASMA REAGIN TEST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=84
            where test_name="Rubella IgG/IgM Antibody";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=85
            where test_name="TREPONEMAL ANTIBODY TEST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=86
            where test_name="VARICELLA-ZOSTER CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=87
            where test_name="Aerobic Bottle Gram Stain";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=88
            where test_name="CHROMOSOME ANALYSIS-BLOOD";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=89
            where test_name="CHROMOSOME ANALYSIS-FLUID";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=90
            where test_name="POST-MORTEM VIRAL CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=91
            where test_name="Respiratory Viral Culture";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=92
            where test_name="Stem Cell Aer/Ana Culture";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=93
            where test_name="TISSUE CULTURE-LYMPHOCYTE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=94
            where test_name="URINE-GRAM STAIN - UNSPUN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=95
            where test_name="Blood Culture, Post Mortem";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=96
            where test_name="CHROMOSOME ANALYSIS-TISSUE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=97
            where test_name="FECAL CULTURE - R/O VIBRIO";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=98
            where test_name="FISH ANALYSIS, 10-30 CELLS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=99
            where test_name="STEM CELL - AEROBIC BOTTLE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=100
            where test_name="Tissue Culture-Bone Marrow";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=101
            where test_name="Anaerobic Bottle Gram Stain";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=102
            where test_name="Legionella Urinary Antigen ";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=103
            where test_name="O&P MACROSCOPIC EXAM - WORM";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=104
            where test_name="FECAL CULTURE - R/O YERSINIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=105
            where test_name="POST MORTEM MYCOLOGY CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=106
            where test_name="STEM CELL - ANAEROBIC BOTTLE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=107
            where test_name="Cryptosporidium/Giardia (DFA)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=108
            where test_name="EPSTEIN-BARR VIRUS VCA-IgG AB";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=109
            where test_name="EPSTEIN-BARR VIRUS VCA-IgM AB";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=110
            where test_name="SMEAR FOR BACTERIAL VAGINOSIS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=111
            where test_name="TISSUE CULTURE-AMNIOTIC FLUID";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=112
            where test_name="VARICELLA-ZOSTER IgG SEROLOGY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=113
            where test_name="Additional Cells and Karyotype";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=114
            where test_name="EPSTEIN-BARR VIRUS EBNA IgG AB";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=115
            where test_name="CHROMOSOME ANALYSIS-BONE MARROW";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=116
            where test_name="DIRECT INFLUENZA A ANTIGEN TEST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=117
            where test_name="DIRECT INFLUENZA B ANTIGEN TEST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=118
            where test_name="GENITAL CULTURE FOR TOXIC SHOCK";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=119
            where test_name="HIV-1 Viral Load/Ultrasensitive";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=120
            where test_name="POTASSIUM HYDROXIDE PREPARATION";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=121
            where test_name="C. difficile Toxin antigen assay";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=122
            where test_name="FUNGAL CULTURE (HAIR/SKIN/NAILS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=123
            where test_name="MOLECULAR CYTOGENETICS-DNA Probe";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=124
            where test_name="O&P MACROSCOPIC EXAM - ARTHROPOD";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=125
            where test_name="Respiratory Viral Antigen Screen";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=126
            where test_name="Respiratory Virus Identification";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=127
            where test_name="CLOSTRIDIUM DIFFICILE TOXIN ASSAY";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=128
            where test_name="Deparaffinization, Lysis of Cells";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=129
            where test_name="HELICOBACTER PYLORI ANTIBODY TEST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=130
            where test_name="QUANTITATIVE CRYPTOCOCCAL ANTIGEN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=131
            where test_name="Tissue Culture - Neoplastic Blood";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=132
            where test_name="CHROMOSOME ANALYSIS-AMNIOTIC FLUID";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=133
            where test_name="FECAL CULTURE - R/O E.COLI 0157:H7";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=134
            where test_name="MOLECULAR CYTOGENETICS - DNA PROBE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=135
            where test_name="VIRAL CULTURE: R/O CYTOMEGALOVIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=136
            where test_name="Acid Fast Stain for Cryptosporidium";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=137
            where test_name="Concentration and Stain for Giardia";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=138
            where test_name="Tissue culture for additional cells";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=139
            where test_name="CHROMOSOME ANALYSIS-NEOPLASTIC BLOOD";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=140
            where test_name="Sonication culture, prosthetic joint";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=141
            where test_name="INTERPHASE FISH ANALYSIS, 25-99 CELLS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=142
            where test_name="MODIFIED ACID-FAST STAIN FOR NOCARDIA";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=143
            where test_name="R/O VANCOMYCIN RESISTANT ENTEROCOCCUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=144
            where test_name="CLOSTRIDIUM DIFFICILE TOXIN A & B TEST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=145
            where test_name="R/O Group B Strep - Penicillin Allergy";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=146
            where test_name="INTERPHASE FISH ANALYSIS, 100-300 CELLS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=147
            where test_name="VIRAL CULTURE: R/O HERPES SIMPLEX VIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=148
            where test_name="Anaerobic culture, Prosthetic Joint Fluid";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=149
            where test_name="CHROMOSOME ANALYSIS - ADDITIONAL KARYOTYPE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=150
            where test_name="DIRECT ANTIGEN TEST FOR VARICELLA-ZOSTER VIRUS";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=151
            where test_name="IMMUNOFLUORESCENT TEST FOR PNEUMOCYSTIS CARINII";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=152
            where test_name="Carbapenemase Resistant Enterobacteriaceae Screen";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=153
            where test_name="POTASSIUM HYDROXIDE PREPARATION (HAIR/SKIN/NAILS)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=154
            where test_name="GEN-PROBE AMPLIFIED M. TUBERCULOSIS DIRECT TEST (MTD)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=155
            where test_name="CYTOMEGALOVIRUS EARLY ANTIGEN TEST (SHELL VIAL METHOD)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=156
            where test_name="Direct Antigen Test for Herpes Simplex Virus Types 1 & 2";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=157
            where test_name="Immunofluorescent test for Pneumocystis jirovecii (carinii)";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=158
            where test_name="Chlamydia trachomatis, Nucleic Acid Probe, with Amplification";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=159
            where test_name="NEISSERIA GONORRHOEAE (GC), NUCLEIC ACID PROBE, WITH AMPLIFICATION";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=160
            where test_name="BARTONELLA BLOOD CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=161
            where test_name="Cryopreservation - Cells";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=162
            where test_name="Pediatric Bottle Gram Stain";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=163
            where test_name="POST-MORTEM ACID-FAST CULTURE";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=164
            where test_name="CVS NEEDLE ASPIRATION EVALUATION";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=165
            where test_name="POST-MORTEM DIRECT ACID-FAST STAIN";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=166
            where test_name="DIRECT RSV ANTIGEN TEST";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=167
            where test_name="Reflex HCV Qual PCR";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=168
            where test_name="CRE/ESBL/AMP-C Screening";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=169
            where test_name="Malassezia furfur Culture";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=170
            where test_name="STOOL SMEAR FOR POLYMORPHONUCLEAR LEUKOCYTES";
        
            update `mimic-four-377221.E4_MicroB.Micro_C1`  
            set test_name_Syn=171
            where test_name="M.FURFUR CULTURE";


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
