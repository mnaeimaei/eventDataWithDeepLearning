import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            

################################################################################

create table `mimic-four-377221.E4_Micro.Micro_B1` as

select distinct * from
(SELECT
subject_id, hadm_id, charttime as Timestamp, test_name, spec_type_desc
FROM `mimic-four-377221.E4_Micro.Micro_A` 
where charttime is not null 

union all

select
subject_id, hadm_id, chartdate as Timestamp, test_name, spec_type_desc
FROM `mimic-four-377221.E4_Micro.Micro_A` 
where charttime is  null );


################################################################################

  


'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)


#******************************************************************************************
#******************************************************************************************
#******************************************************************************************

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

query1 = f'''            

##########################################################

update  `mimic-four-377221.E4_Micro.Micro_B1` 
set hadm_id = 0
where hadm_id is null	;

update  `mimic-four-377221.E4_Micro.Micro_B1`
set spec_type_desc = "NULL"
where spec_type_desc=""	;

##########################################################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)


#******************************************************************************************
#******************************************************************************************
#******************************************************************************************

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

query1 = f'''            

##########################################################

alter table  `mimic-four-377221.E4_Micro.Micro_B1`
add column test_name_Syn string;

alter table  `mimic-four-377221.E4_Micro.Micro_B1`
add column spec_type_desc_Syn INTEGER;

##########################################################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)



#******************************************************************************************
#******************************************************************************************
#******************************************************************************************

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

query1 = f'''            

##########################################################

            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="TestND"
            where test_name="ND";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test001"
            where test_name="TISSUE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test002"
            where test_name="voided";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test003"
            where test_name="Problem";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test004"
            where test_name="Lyme IgG";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test005"
            where test_name="Lyme IgM";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test006"
            where test_name="MONOSPOT";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test007"
            where test_name="ASO TITER";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test008"
            where test_name="ASO Screen";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test009"
            where test_name="GRAM STAIN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test010"
            where test_name="MRSA SCREEN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test011"
            where test_name="R/O GC Only";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test012"
            where test_name="HCV GENOTYPE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test013"
            where test_name="FECAL CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test014"
            where test_name="FLUID CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test015"
            where test_name="LYME SEROLOGY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test016"
            where test_name="URINE CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test017"
            where test_name="VIRAL CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test018"
            where test_name="WOUND CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test019"
            where test_name="AEROBIC BOTTLE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test020"
            where test_name="CMV Viral Load";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test021"
            where test_name="FUNGAL CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test022"
            where test_name="HBV Viral Load";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test023"
            where test_name="HCV VIRAL LOAD";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test024"
            where test_name="ACID FAST SMEAR";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test025"
            where test_name="GENITAL CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test026"
            where test_name="ISOLATE FOR MIC";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test027"
            where test_name="OVA + PARASITES";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test028"
            where test_name="SWAB- R/O YEAST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test029"
            where test_name="ANAEROBIC BOTTLE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test030"
            where test_name="BRUCELLA CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test031"
            where test_name="C. difficile PCR";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test032"
            where test_name="CMV IgG ANTIBODY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test033"
            where test_name="CMV IgM ANTIBODY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test034"
            where test_name="CYCLOSPORA STAIN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test035"
            where test_name="FOCUSED ANALYSIS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test036"
            where test_name="NOCARDIA CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test037"
            where test_name="QUANTITATIVE RPR";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test038"
            where test_name="ACID FAST CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test039"
            where test_name="ANAEROBIC CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test040"
            where test_name="BLOOD/AFB CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test041"
            where test_name="CHLAMYDIA CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test042"
            where test_name="LEGIONELLA CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test043"
            where test_name="MUMPS IgG ANTIBODY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test044"
            where test_name="POSTMORTEM CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test045"
            where test_name="Stool Hold Request";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test046"
            where test_name="TISSUE CULTURE-CVS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test047"
            where test_name="Enterovirus Culture";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test048"
            where test_name="MICROSPORIDIA STAIN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test049"
            where test_name="RESPIRATORY CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test050"
            where test_name="Staph aureus Screen";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test051"
            where test_name="BLOOD/FUNGAL CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test052"
            where test_name="CRYPTOCOCCAL ANTIGEN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test053"
            where test_name="Malaria Antigen Test";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test054"
            where test_name="REFLEX URINE CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test055"
            where test_name="RUBELLA IgG SEROLOGY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test056"
            where test_name="TISSUE CULTURE-FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test057"
            where test_name="CAMPYLOBACTER CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test058"
            where test_name="RUBEOLA ANTIBODY, IgG";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test059"
            where test_name="Swab - R/O Yeast - IC";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test060"
            where test_name="TISSUE CULTURE-TISSUE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test061"
            where test_name="BRUCELLA BLOOD CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test062"
            where test_name="Blood Culture, Neonate";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test063"
            where test_name="Blood Culture, Routine";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test064"
            where test_name="Cipro Resistant Screen";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test065"
            where test_name="GRAM STAIN- R/O THRUSH";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test066"
            where test_name="R/O Beta Strep Group A";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test067"
            where test_name="R/O GROUP B BETA STREP";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test068"
            where test_name="Staph aureus Preop PCR";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test069"
            where test_name="CHROMOSOME ANALYSIS-CVS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test070"
            where test_name="ED Gram Stain for Yeast";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test071"
            where test_name="M. furfur Blood Culture";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test072"
            where test_name="RPR w/check for Prozone";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test073"
            where test_name="SCOTCH TAPE PREP/PADDLE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test074"
            where test_name="TOXOPLASMA IgG ANTIBODY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test075"
            where test_name="TOXOPLASMA IgM ANTIBODY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test076"
            where test_name="TRICHOMONAS SALINE PREP";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test077"
            where test_name="YEAST VAGINITIS CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test078"
            where test_name="ADDITIONAL CELLS COUNTED";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test079"
            where test_name="FISH ANALYSIS, 3-5 CELLS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test080"
            where test_name="Fluid Culture in Bottles";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test081"
            where test_name="MTB Direct Amplification";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test082"
            where test_name="Myco-F Bottle Gram Stain";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test083"
            where test_name="RAPID PLASMA REAGIN TEST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test084"
            where test_name="Rubella IgG/IgM Antibody";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test085"
            where test_name="TREPONEMAL ANTIBODY TEST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test086"
            where test_name="VARICELLA-ZOSTER CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test087"
            where test_name="Aerobic Bottle Gram Stain";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test088"
            where test_name="CHROMOSOME ANALYSIS-BLOOD";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test089"
            where test_name="CHROMOSOME ANALYSIS-FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test090"
            where test_name="POST-MORTEM VIRAL CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test091"
            where test_name="Respiratory Viral Culture";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test092"
            where test_name="Stem Cell Aer/Ana Culture";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test093"
            where test_name="TISSUE CULTURE-LYMPHOCYTE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test094"
            where test_name="URINE-GRAM STAIN - UNSPUN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test095"
            where test_name="Blood Culture, Post Mortem";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test096"
            where test_name="CHROMOSOME ANALYSIS-TISSUE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test097"
            where test_name="FECAL CULTURE - R/O VIBRIO";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test098"
            where test_name="FISH ANALYSIS, 10-30 CELLS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test099"
            where test_name="STEM CELL - AEROBIC BOTTLE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test100"
            where test_name="Tissue Culture-Bone Marrow";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test101"
            where test_name="Anaerobic Bottle Gram Stain";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test102"
            where test_name="Legionella Urinary Antigen ";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test103"
            where test_name="O&P MACROSCOPIC EXAM - WORM";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test104"
            where test_name="FECAL CULTURE - R/O YERSINIA";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test105"
            where test_name="POST MORTEM MYCOLOGY CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test106"
            where test_name="STEM CELL - ANAEROBIC BOTTLE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test107"
            where test_name="Cryptosporidium/Giardia (DFA)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test108"
            where test_name="EPSTEIN-BARR VIRUS VCA-IgG AB";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test109"
            where test_name="EPSTEIN-BARR VIRUS VCA-IgM AB";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test110"
            where test_name="SMEAR FOR BACTERIAL VAGINOSIS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test111"
            where test_name="TISSUE CULTURE-AMNIOTIC FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test112"
            where test_name="VARICELLA-ZOSTER IgG SEROLOGY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test113"
            where test_name="Additional Cells and Karyotype";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test114"
            where test_name="EPSTEIN-BARR VIRUS EBNA IgG AB";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test115"
            where test_name="CHROMOSOME ANALYSIS-BONE MARROW";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test116"
            where test_name="DIRECT INFLUENZA A ANTIGEN TEST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test117"
            where test_name="DIRECT INFLUENZA B ANTIGEN TEST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test118"
            where test_name="GENITAL CULTURE FOR TOXIC SHOCK";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test119"
            where test_name="HIV-1 Viral Load/Ultrasensitive";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test120"
            where test_name="POTASSIUM HYDROXIDE PREPARATION";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test121"
            where test_name="C. difficile Toxin antigen assay";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test122"
            where test_name="FUNGAL CULTURE (HAIR/SKIN/NAILS)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test123"
            where test_name="MOLECULAR CYTOGENETICS-DNA Probe";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test124"
            where test_name="O&P MACROSCOPIC EXAM - ARTHROPOD";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test125"
            where test_name="Respiratory Viral Antigen Screen";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test126"
            where test_name="Respiratory Virus Identification";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test127"
            where test_name="CLOSTRIDIUM DIFFICILE TOXIN ASSAY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test128"
            where test_name="Deparaffinization, Lysis of Cells";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test129"
            where test_name="HELICOBACTER PYLORI ANTIBODY TEST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test130"
            where test_name="QUANTITATIVE CRYPTOCOCCAL ANTIGEN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test131"
            where test_name="Tissue Culture - Neoplastic Blood";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test132"
            where test_name="CHROMOSOME ANALYSIS-AMNIOTIC FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test133"
            where test_name="FECAL CULTURE - R/O E.COLI 0157:H7";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test134"
            where test_name="MOLECULAR CYTOGENETICS - DNA PROBE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test135"
            where test_name="VIRAL CULTURE: R/O CYTOMEGALOVIRUS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test136"
            where test_name="Acid Fast Stain for Cryptosporidium";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test137"
            where test_name="Concentration and Stain for Giardia";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test138"
            where test_name="Tissue culture for additional cells";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test139"
            where test_name="CHROMOSOME ANALYSIS-NEOPLASTIC BLOOD";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test140"
            where test_name="Sonication culture, prosthetic joint";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test141"
            where test_name="INTERPHASE FISH ANALYSIS, 25-99 CELLS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test142"
            where test_name="MODIFIED ACID-FAST STAIN FOR NOCARDIA";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test143"
            where test_name="R/O VANCOMYCIN RESISTANT ENTEROCOCCUS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test144"
            where test_name="CLOSTRIDIUM DIFFICILE TOXIN A & B TEST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test145"
            where test_name="R/O Group B Strep - Penicillin Allergy";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test146"
            where test_name="INTERPHASE FISH ANALYSIS, 100-300 CELLS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test147"
            where test_name="VIRAL CULTURE: R/O HERPES SIMPLEX VIRUS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test148"
            where test_name="Anaerobic culture, Prosthetic Joint Fluid";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test149"
            where test_name="CHROMOSOME ANALYSIS - ADDITIONAL KARYOTYPE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test150"
            where test_name="DIRECT ANTIGEN TEST FOR VARICELLA-ZOSTER VIRUS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test151"
            where test_name="IMMUNOFLUORESCENT TEST FOR PNEUMOCYSTIS CARINII";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test152"
            where test_name="Carbapenemase Resistant Enterobacteriaceae Screen";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test153"
            where test_name="POTASSIUM HYDROXIDE PREPARATION (HAIR/SKIN/NAILS)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test154"
            where test_name="GEN-PROBE AMPLIFIED M. TUBERCULOSIS DIRECT TEST (MTD)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test155"
            where test_name="CYTOMEGALOVIRUS EARLY ANTIGEN TEST (SHELL VIAL METHOD)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test156"
            where test_name="Direct Antigen Test for Herpes Simplex Virus Types 1 & 2";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test157"
            where test_name="Immunofluorescent test for Pneumocystis jirovecii (carinii)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test158"
            where test_name="Chlamydia trachomatis, Nucleic Acid Probe, with Amplification";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test159"
            where test_name="NEISSERIA GONORRHOEAE (GC), NUCLEIC ACID PROBE, WITH AMPLIFICATION";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test160"
            where test_name="BARTONELLA BLOOD CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test161"
            where test_name="Cryopreservation - Cells";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test162"
            where test_name="Pediatric Bottle Gram Stain";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test163"
            where test_name="POST-MORTEM ACID-FAST CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test164"
            where test_name="CVS NEEDLE ASPIRATION EVALUATION";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test165"
            where test_name="POST-MORTEM DIRECT ACID-FAST STAIN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test166"
            where test_name="DIRECT RSV ANTIGEN TEST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test167"
            where test_name="Reflex HCV Qual PCR";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test168"
            where test_name="CRE/ESBL/AMP-C Screening";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test169"
            where test_name="Malassezia furfur Culture";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test170"
            where test_name="STOOL SMEAR FOR POLYMORPHONUCLEAR LEUKOCYTES";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set test_name_Syn="Test171"
            where test_name="M.FURFUR CULTURE";
        

##########################################################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)



#******************************************************************************************
#******************************************************************************************
#******************************************************************************************

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

query1 = f'''            

##########################################################
 update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=1
            where spec_type_desc="URINE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=2
            where spec_type_desc="BLOOD CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=3
            where spec_type_desc="SKIN SCRAPINGS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=4
            where spec_type_desc="SWAB";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=5
            where spec_type_desc="SEROLOGY/BLOOD";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=6
            where spec_type_desc="STOOL";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=7
            where spec_type_desc="BONE MARROW - CYTOGENETICS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=8
            where spec_type_desc="MRSA SCREEN";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=9
            where spec_type_desc="TISSUE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=10
            where spec_type_desc="Blood (Toxo)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=11
            where spec_type_desc="Blood (EBV)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=12
            where spec_type_desc="CSF;SPINAL FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=13
            where spec_type_desc="IMMUNOLOGY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=14
            where spec_type_desc="FLUID RECEIVED IN BLOOD CULTURE BOTTLES";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=15
            where spec_type_desc="Staph aureus swab";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=16
            where spec_type_desc="Mini-BAL";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=17
            where spec_type_desc="SPUTUM";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=18
            where spec_type_desc="BRONCHOALVEOLAR LAVAGE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=19
            where spec_type_desc="Blood (LYME)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=20
            where spec_type_desc="Blood (CMV AB)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=21
            where spec_type_desc="Immunology (CMV)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=22
            where spec_type_desc="PERITONEAL FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=23
            where spec_type_desc="Rapid Respiratory Viral Screen & Culture";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=24
            where spec_type_desc="ANORECTAL/VAGINAL";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=25
            where spec_type_desc="Swab R/O Yeast Screen";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=26
            where spec_type_desc="AMNIOTIC FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=27
            where spec_type_desc="Stem Cell - Blood Culture";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=28
            where spec_type_desc="THROAT FOR STREP";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=29
            where spec_type_desc="BIOPSY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=30
            where spec_type_desc="JOINT FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=31
            where spec_type_desc="ABSCESS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=32
            where spec_type_desc="BRONCHIAL WASHINGS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=33
            where spec_type_desc="BLOOD CULTURE ( MYCO/F LYTIC BOTTLE)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=34
            where spec_type_desc="CATHETER TIP-IV";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=35
            where spec_type_desc="VIRAL CULTURE:R/O HERPES SIMPLEX VIRUS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=36
            where spec_type_desc="FLUID,OTHER";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=37
            where spec_type_desc="PLEURAL FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=38
            where spec_type_desc="BILE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=39
            where spec_type_desc="DIRECT ANTIGEN TEST FOR VARICELLA-ZOSTER VIRUS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=40
            where spec_type_desc="Influenza A/B by DFA";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=41
            where spec_type_desc="BLOOD CULTURE - NEONATE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=42
            where spec_type_desc="NAIL SCRAPINGS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=43
            where spec_type_desc="POST-MORTEM VIRAL CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=44
            where spec_type_desc="DIALYSIS FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=45
            where spec_type_desc="ASPIRATE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=46
            where spec_type_desc="PROSTHETIC JOINT FLUID";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=47
            where spec_type_desc="Direct Antigen Test for Herpes Simplex Virus Types 1 & 2";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=48
            where spec_type_desc="THROAT CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=49
            where spec_type_desc="FOREIGN BODY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=50
            where spec_type_desc="STOOL (RECEIVED IN TRANSPORT SYSTEM)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=51
            where spec_type_desc="CORNEAL EYE SCRAPINGS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=52
            where spec_type_desc="NEOPLASTIC BLOOD";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=53
            where spec_type_desc="Isolate";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=54
            where spec_type_desc="FOOT CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=55
            where spec_type_desc="CHORIONIC VILLUS SAMPLE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=56
            where spec_type_desc="BONE MARROW";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=57
            where spec_type_desc="RAPID RESPIRATORY VIRAL ANTIGEN TEST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=58
            where spec_type_desc="FECAL SWAB";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=59
            where spec_type_desc="EYE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=60
            where spec_type_desc="Influenza A/B by DFA - Bronch Lavage";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=61
            where spec_type_desc="URINE,KIDNEY";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=62
            where spec_type_desc="Swab";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=63
            where spec_type_desc="POSTMORTEM CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=64
            where spec_type_desc="VIRAL CULTURE: R/O CYTOMEGALOVIRUS";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=65
            where spec_type_desc="CRE Screen";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=66
            where spec_type_desc="Blood (Malaria)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=67
            where spec_type_desc="SCOTCH TAPE PREP/PADDLE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=68
            where spec_type_desc="EAR";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=69
            where spec_type_desc="BRONCHIAL BRUSH";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=70
            where spec_type_desc="Infection Control Yeast";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=71
            where spec_type_desc="VIRAL CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=72
            where spec_type_desc="Cipro Resistant Screen";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=73
            where spec_type_desc="URINE,SUPRAPUBIC ASPIRATE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=74
            where spec_type_desc="THROAT";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=75
            where spec_type_desc="Foreign Body - Sonication Culture";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=76
            where spec_type_desc="SWAB - R/O YEAST";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=77
            where spec_type_desc="BLOOD CULTURE (POST-MORTEM)";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=78
            where spec_type_desc="VARICELLA-ZOSTER CULTURE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=79
            where spec_type_desc="ARTHROPOD";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=80
            where spec_type_desc="TRACHEAL ASPIRATE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=81
            where spec_type_desc="RECTAL - R/O GC";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=82
            where spec_type_desc="PERIPHERAL BLOOD LYMPHOCYTES";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=83
            where spec_type_desc="WORM";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=84
            where spec_type_desc="BRONCHIAL BRUSH - PROTECTED";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=85
            where spec_type_desc="Touch Prep/Sections";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=86
            where spec_type_desc="BLOOD";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=87
            where spec_type_desc="HAIR";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=88
            where spec_type_desc="SWAB, R/O GC";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=89
            where spec_type_desc="XXX";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=90
            where spec_type_desc="FLUID WOUND";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=91
            where spec_type_desc="MICRO PROBLEM PATIENT";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=92
            where spec_type_desc="C, E, & A Screening";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=93
            where spec_type_desc="URINE,PROSTATIC MASSAGE";
        
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=94
            where spec_type_desc="BLOOD BAG FLUID";
              
            update `mimic-four-377221.E4_Micro.Micro_B1`  
            set spec_type_desc_Syn=99
            where spec_type_desc="NULL";

##########################################################

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
