import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            





    
    
        create table `mimic-four-377221.E4_Micro.HYT`    as
        SELECT distinct rowNum FROM `mimic-four-377221.E4_Micro.Micro_B2`   ;
        
        
        

        alter table `mimic-four-377221.E4_Micro.HYT` 
        ADD COLUMN test_name_Syn string  ;
        
        
        alter table `mimic-four-377221.E4_Micro.HYT` 
        ADD COLUMN spec_type_desc_Syn INTEGER  ;


    
##################################################################################
#query   Part 1 =

###  0



            create table `mimic-four-377221.E4_Micro.TTTT_1`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_1`   
            set test_name_Syn  = "Test001"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_1`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_1`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_1`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_1`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_1`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_1 
            from `mimic-four-377221.E4_Micro.UUUU_1`     );


        
###  1



            create table `mimic-four-377221.E4_Micro.TTTT_2`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_2`   
            set test_name_Syn  = "Test002"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_2`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_2`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_2`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_2`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_2`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_2 
            from `mimic-four-377221.E4_Micro.UUUU_2`     );


        
###  2



            create table `mimic-four-377221.E4_Micro.TTTT_3`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_3`   
            set test_name_Syn  = "Test003"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_3`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_3`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_3`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_3`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_3`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_3 
            from `mimic-four-377221.E4_Micro.UUUU_3`     );


        
###  3



            create table `mimic-four-377221.E4_Micro.TTTT_4`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_4`   
            set test_name_Syn  = "Test004"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_4`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_4`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_4`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_4`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_4`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_4 
            from `mimic-four-377221.E4_Micro.UUUU_4`     );


        
###  4



            create table `mimic-four-377221.E4_Micro.TTTT_5`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_5`   
            set test_name_Syn  = "Test005"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_5`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_5`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_5`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_5`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_5`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_5 
            from `mimic-four-377221.E4_Micro.UUUU_5`     );


        
###  5



            create table `mimic-four-377221.E4_Micro.TTTT_6`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_6`   
            set test_name_Syn  = "Test006"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_6`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_6`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_6`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_6`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_6`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_6 
            from `mimic-four-377221.E4_Micro.UUUU_6`     );


        
###  6



            create table `mimic-four-377221.E4_Micro.TTTT_7`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_7`   
            set test_name_Syn  = "Test007"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_7`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_7`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_7`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_7`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_7`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_7 
            from `mimic-four-377221.E4_Micro.UUUU_7`     );


        
###  7



            create table `mimic-four-377221.E4_Micro.TTTT_8`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_8`   
            set test_name_Syn  = "Test008"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_8`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_8`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_8`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_8`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_8`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_8 
            from `mimic-four-377221.E4_Micro.UUUU_8`     );


        
###  8



            create table `mimic-four-377221.E4_Micro.TTTT_9`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_9`   
            set test_name_Syn  = "Test009"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_9`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_9`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_9`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_9`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_9`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_9 
            from `mimic-four-377221.E4_Micro.UUUU_9`     );


        
###  9



            create table `mimic-four-377221.E4_Micro.TTTT_10`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_10`   
            set test_name_Syn  = "Test010"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_10`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_10`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_10`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_10`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_10`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_10 
            from `mimic-four-377221.E4_Micro.UUUU_10`     );


        
###  10



            create table `mimic-four-377221.E4_Micro.TTTT_11`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_11`   
            set test_name_Syn  = "Test011"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_11`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_11`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_11`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_11`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_11`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_11 
            from `mimic-four-377221.E4_Micro.UUUU_11`     );


        
###  11



            create table `mimic-four-377221.E4_Micro.TTTT_12`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_12`   
            set test_name_Syn  = "Test012"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_12`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_12`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_12`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_12`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_12`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_12 
            from `mimic-four-377221.E4_Micro.UUUU_12`     );


        
###  12



            create table `mimic-four-377221.E4_Micro.TTTT_13`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_13`   
            set test_name_Syn  = "Test013"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_13`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_13`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_13`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_13`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_13`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_13 
            from `mimic-four-377221.E4_Micro.UUUU_13`     );


        
###  13



            create table `mimic-four-377221.E4_Micro.TTTT_14`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_14`   
            set test_name_Syn  = "Test014"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_14`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_14`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_14`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_14`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_14`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_14 
            from `mimic-four-377221.E4_Micro.UUUU_14`     );


        
###  14



            create table `mimic-four-377221.E4_Micro.TTTT_15`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_15`   
            set test_name_Syn  = "Test015"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_15`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_15`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_15`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_15`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_15`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_15 
            from `mimic-four-377221.E4_Micro.UUUU_15`     );


        
###  15



            create table `mimic-four-377221.E4_Micro.TTTT_16`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_16`   
            set test_name_Syn  = "Test016"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_16`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_16`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_16`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_16`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_16`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_16 
            from `mimic-four-377221.E4_Micro.UUUU_16`     );


        
###  16



            create table `mimic-four-377221.E4_Micro.TTTT_17`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_17`   
            set test_name_Syn  = "Test017"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_17`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_17`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_17`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_17`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_17`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_17 
            from `mimic-four-377221.E4_Micro.UUUU_17`     );


        
###  17



            create table `mimic-four-377221.E4_Micro.TTTT_18`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_18`   
            set test_name_Syn  = "Test018"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_18`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_18`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_18`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_18`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_18`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_18 
            from `mimic-four-377221.E4_Micro.UUUU_18`     );


        
###  18



            create table `mimic-four-377221.E4_Micro.TTTT_19`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_19`   
            set test_name_Syn  = "Test019"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_19`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_19`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_19`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_19`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_19`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_19 
            from `mimic-four-377221.E4_Micro.UUUU_19`     );


        
###  19



            create table `mimic-four-377221.E4_Micro.TTTT_20`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_20`   
            set test_name_Syn  = "Test020"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_20`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_20`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_20`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_20`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_20`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_20 
            from `mimic-four-377221.E4_Micro.UUUU_20`     );


        
###  20



            create table `mimic-four-377221.E4_Micro.TTTT_21`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_21`   
            set test_name_Syn  = "Test021"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_21`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_21`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_21`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_21`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_21`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_21 
            from `mimic-four-377221.E4_Micro.UUUU_21`     );


        
###  21



            create table `mimic-four-377221.E4_Micro.TTTT_22`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_22`   
            set test_name_Syn  = "Test022"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_22`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_22`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_22`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_22`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_22`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_22 
            from `mimic-four-377221.E4_Micro.UUUU_22`     );


        
###  22



            create table `mimic-four-377221.E4_Micro.TTTT_23`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_23`   
            set test_name_Syn  = "Test023"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_23`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_23`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_23`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_23`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_23`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_23 
            from `mimic-four-377221.E4_Micro.UUUU_23`     );


        
###  23



            create table `mimic-four-377221.E4_Micro.TTTT_24`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_24`   
            set test_name_Syn  = "Test024"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_24`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_24`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_24`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_24`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_24`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_24 
            from `mimic-four-377221.E4_Micro.UUUU_24`     );


        
###  24



            create table `mimic-four-377221.E4_Micro.TTTT_25`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_25`   
            set test_name_Syn  = "Test025"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_25`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_25`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_25`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_25`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_25`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_25 
            from `mimic-four-377221.E4_Micro.UUUU_25`     );


        
###  25



            create table `mimic-four-377221.E4_Micro.TTTT_26`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_26`   
            set test_name_Syn  = "Test026"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_26`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_26`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_26`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_26`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_26`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_26 
            from `mimic-four-377221.E4_Micro.UUUU_26`     );


        
###  26



            create table `mimic-four-377221.E4_Micro.TTTT_27`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_27`   
            set test_name_Syn  = "Test027"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_27`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_27`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_27`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_27`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_27`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_27 
            from `mimic-four-377221.E4_Micro.UUUU_27`     );


        
###  27



            create table `mimic-four-377221.E4_Micro.TTTT_28`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_28`   
            set test_name_Syn  = "Test028"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_28`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_28`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_28`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_28`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_28`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_28 
            from `mimic-four-377221.E4_Micro.UUUU_28`     );


        
###  28



            create table `mimic-four-377221.E4_Micro.TTTT_29`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_29`   
            set test_name_Syn  = "Test029"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_29`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_29`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_29`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_29`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_29`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_29 
            from `mimic-four-377221.E4_Micro.UUUU_29`     );


        
###  29



            create table `mimic-four-377221.E4_Micro.TTTT_30`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_30`   
            set test_name_Syn  = "Test030"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_30`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_30`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_30`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_30`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_30`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_30 
            from `mimic-four-377221.E4_Micro.UUUU_30`     );


        
###  30



            create table `mimic-four-377221.E4_Micro.TTTT_31`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_31`   
            set test_name_Syn  = "Test031"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_31`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_31`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_31`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_31`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_31`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_31 
            from `mimic-four-377221.E4_Micro.UUUU_31`     );


        
###  31



            create table `mimic-four-377221.E4_Micro.TTTT_32`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_32`   
            set test_name_Syn  = "Test032"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_32`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_32`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_32`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_32`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_32`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_32 
            from `mimic-four-377221.E4_Micro.UUUU_32`     );


        
###  32



            create table `mimic-four-377221.E4_Micro.TTTT_33`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_33`   
            set test_name_Syn  = "Test033"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_33`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_33`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_33`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_33`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_33`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_33 
            from `mimic-four-377221.E4_Micro.UUUU_33`     );


        
###  33



            create table `mimic-four-377221.E4_Micro.TTTT_34`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_34`   
            set test_name_Syn  = "Test034"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_34`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_34`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_34`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_34`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_34`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_34 
            from `mimic-four-377221.E4_Micro.UUUU_34`     );


        
###  34



            create table `mimic-four-377221.E4_Micro.TTTT_35`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_35`   
            set test_name_Syn  = "Test035"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_35`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_35`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_35`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_35`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_35`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_35 
            from `mimic-four-377221.E4_Micro.UUUU_35`     );


        
###  35



            create table `mimic-four-377221.E4_Micro.TTTT_36`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_36`   
            set test_name_Syn  = "Test036"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_36`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_36`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_36`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_36`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_36`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_36 
            from `mimic-four-377221.E4_Micro.UUUU_36`     );


        
###  36



            create table `mimic-four-377221.E4_Micro.TTTT_37`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_37`   
            set test_name_Syn  = "Test037"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_37`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_37`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_37`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_37`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_37`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_37 
            from `mimic-four-377221.E4_Micro.UUUU_37`     );


        
###  37



            create table `mimic-four-377221.E4_Micro.TTTT_38`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_38`   
            set test_name_Syn  = "Test038"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_38`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_38`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_38`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_38`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_38`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_38 
            from `mimic-four-377221.E4_Micro.UUUU_38`     );


        
###  38



            create table `mimic-four-377221.E4_Micro.TTTT_39`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_39`   
            set test_name_Syn  = "Test039"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_39`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_39`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_39`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_39`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_39`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_39 
            from `mimic-four-377221.E4_Micro.UUUU_39`     );


        
###  39



            create table `mimic-four-377221.E4_Micro.TTTT_40`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_40`   
            set test_name_Syn  = "Test040"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_40`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_40`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_40`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_40`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_40`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_40 
            from `mimic-four-377221.E4_Micro.UUUU_40`     );


        
###  40



            create table `mimic-four-377221.E4_Micro.TTTT_41`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_41`   
            set test_name_Syn  = "Test041"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_41`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_41`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_41`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_41`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_41`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_41 
            from `mimic-four-377221.E4_Micro.UUUU_41`     );


        
###  41



            create table `mimic-four-377221.E4_Micro.TTTT_42`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_42`   
            set test_name_Syn  = "Test042"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_42`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_42`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_42`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_42`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_42`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_42 
            from `mimic-four-377221.E4_Micro.UUUU_42`     );


        
###  42



            create table `mimic-four-377221.E4_Micro.TTTT_43`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_43`   
            set test_name_Syn  = "Test043"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_43`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_43`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_43`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_43`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_43`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_43 
            from `mimic-four-377221.E4_Micro.UUUU_43`     );


        
###  43



            create table `mimic-four-377221.E4_Micro.TTTT_44`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_44`   
            set test_name_Syn  = "Test044"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_44`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_44`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_44`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_44`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_44`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_44 
            from `mimic-four-377221.E4_Micro.UUUU_44`     );


        
###  44



            create table `mimic-four-377221.E4_Micro.TTTT_45`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_45`   
            set test_name_Syn  = "Test045"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_45`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_45`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_45`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_45`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_45`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_45 
            from `mimic-four-377221.E4_Micro.UUUU_45`     );


        
###  45



            create table `mimic-four-377221.E4_Micro.TTTT_46`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_46`   
            set test_name_Syn  = "Test046"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_46`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_46`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_46`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_46`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_46`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_46 
            from `mimic-four-377221.E4_Micro.UUUU_46`     );


        
###  46



            create table `mimic-four-377221.E4_Micro.TTTT_47`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_47`   
            set test_name_Syn  = "Test047"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_47`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_47`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_47`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_47`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_47`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_47 
            from `mimic-four-377221.E4_Micro.UUUU_47`     );


        
###  47



            create table `mimic-four-377221.E4_Micro.TTTT_48`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_48`   
            set test_name_Syn  = "Test048"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_48`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_48`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_48`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_48`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_48`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_48 
            from `mimic-four-377221.E4_Micro.UUUU_48`     );


        
###  48



            create table `mimic-four-377221.E4_Micro.TTTT_49`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_49`   
            set test_name_Syn  = "Test049"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_49`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_49`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_49`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_49`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_49`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_49 
            from `mimic-four-377221.E4_Micro.UUUU_49`     );


        
###  49



            create table `mimic-four-377221.E4_Micro.TTTT_50`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_50`   
            set test_name_Syn  = "Test050"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_50`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_50`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_50`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_50`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_50`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_50 
            from `mimic-four-377221.E4_Micro.UUUU_50`     );


        
###  50



            create table `mimic-four-377221.E4_Micro.TTTT_51`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_51`   
            set test_name_Syn  = "Test051"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_51`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_51`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_51`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_51`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_51`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_51 
            from `mimic-four-377221.E4_Micro.UUUU_51`     );


        
###  51



            create table `mimic-four-377221.E4_Micro.TTTT_52`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_52`   
            set test_name_Syn  = "Test052"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_52`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_52`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_52`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_52`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_52`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_52 
            from `mimic-four-377221.E4_Micro.UUUU_52`     );


        
###  52



            create table `mimic-four-377221.E4_Micro.TTTT_53`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_53`   
            set test_name_Syn  = "Test053"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_53`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_53`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_53`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_53`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_53`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_53 
            from `mimic-four-377221.E4_Micro.UUUU_53`     );


        
###  53



            create table `mimic-four-377221.E4_Micro.TTTT_54`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_54`   
            set test_name_Syn  = "Test054"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_54`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_54`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_54`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_54`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_54`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_54 
            from `mimic-four-377221.E4_Micro.UUUU_54`     );


        
###  54



            create table `mimic-four-377221.E4_Micro.TTTT_55`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_55`   
            set test_name_Syn  = "Test055"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_55`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_55`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_55`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_55`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_55`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_55 
            from `mimic-four-377221.E4_Micro.UUUU_55`     );


        
###  55



            create table `mimic-four-377221.E4_Micro.TTTT_56`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_56`   
            set test_name_Syn  = "Test056"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_56`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_56`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_56`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_56`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_56`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_56 
            from `mimic-four-377221.E4_Micro.UUUU_56`     );


        
###  56



            create table `mimic-four-377221.E4_Micro.TTTT_57`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_57`   
            set test_name_Syn  = "Test057"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_57`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_57`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_57`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_57`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_57`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_57 
            from `mimic-four-377221.E4_Micro.UUUU_57`     );


        
###  57



            create table `mimic-four-377221.E4_Micro.TTTT_58`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_58`   
            set test_name_Syn  = "Test058"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_58`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_58`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_58`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_58`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_58`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_58 
            from `mimic-four-377221.E4_Micro.UUUU_58`     );


        
###  58



            create table `mimic-four-377221.E4_Micro.TTTT_59`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_59`   
            set test_name_Syn  = "Test059"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_59`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_59`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_59`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_59`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_59`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_59 
            from `mimic-four-377221.E4_Micro.UUUU_59`     );


        
###  59



            create table `mimic-four-377221.E4_Micro.TTTT_60`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_60`   
            set test_name_Syn  = "Test060"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_60`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_60`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_60`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_60`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_60`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_60 
            from `mimic-four-377221.E4_Micro.UUUU_60`     );


        
###  60



            create table `mimic-four-377221.E4_Micro.TTTT_61`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_61`   
            set test_name_Syn  = "Test061"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_61`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_61`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_61`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_61`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_61`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_61 
            from `mimic-four-377221.E4_Micro.UUUU_61`     );


        
###  61



            create table `mimic-four-377221.E4_Micro.TTTT_62`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_62`   
            set test_name_Syn  = "Test062"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_62`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_62`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_62`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_62`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_62`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_62 
            from `mimic-four-377221.E4_Micro.UUUU_62`     );


        
###  62



            create table `mimic-four-377221.E4_Micro.TTTT_63`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_63`   
            set test_name_Syn  = "Test063"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_63`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_63`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_63`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_63`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_63`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_63 
            from `mimic-four-377221.E4_Micro.UUUU_63`     );


        
###  63



            create table `mimic-four-377221.E4_Micro.TTTT_64`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_64`   
            set test_name_Syn  = "Test064"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_64`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_64`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_64`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_64`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_64`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_64 
            from `mimic-four-377221.E4_Micro.UUUU_64`     );


        
###  64



            create table `mimic-four-377221.E4_Micro.TTTT_65`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_65`   
            set test_name_Syn  = "Test065"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_65`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_65`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_65`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_65`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_65`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_65 
            from `mimic-four-377221.E4_Micro.UUUU_65`     );


        
###  65



            create table `mimic-four-377221.E4_Micro.TTTT_66`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_66`   
            set test_name_Syn  = "Test066"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_66`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_66`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_66`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_66`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_66`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_66 
            from `mimic-four-377221.E4_Micro.UUUU_66`     );


        
###  66



            create table `mimic-four-377221.E4_Micro.TTTT_67`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_67`   
            set test_name_Syn  = "Test067"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_67`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_67`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_67`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_67`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_67`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_67 
            from `mimic-four-377221.E4_Micro.UUUU_67`     );


        
###  67



            create table `mimic-four-377221.E4_Micro.TTTT_68`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_68`   
            set test_name_Syn  = "Test068"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_68`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_68`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_68`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_68`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_68`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_68 
            from `mimic-four-377221.E4_Micro.UUUU_68`     );


        
###  68



            create table `mimic-four-377221.E4_Micro.TTTT_69`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_69`   
            set test_name_Syn  = "Test069"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_69`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_69`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_69`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_69`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_69`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_69 
            from `mimic-four-377221.E4_Micro.UUUU_69`     );


        
###  69



            create table `mimic-four-377221.E4_Micro.TTTT_70`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_70`   
            set test_name_Syn  = "Test070"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_70`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_70`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_70`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_70`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_70`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_70 
            from `mimic-four-377221.E4_Micro.UUUU_70`     );


        
###  70



            create table `mimic-four-377221.E4_Micro.TTTT_71`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_71`   
            set test_name_Syn  = "Test071"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_71`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_71`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_71`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_71`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_71`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_71 
            from `mimic-four-377221.E4_Micro.UUUU_71`     );


        
###  71



            create table `mimic-four-377221.E4_Micro.TTTT_72`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_72`   
            set test_name_Syn  = "Test072"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_72`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_72`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_72`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_72`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_72`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_72 
            from `mimic-four-377221.E4_Micro.UUUU_72`     );


        
###  72



            create table `mimic-four-377221.E4_Micro.TTTT_73`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_73`   
            set test_name_Syn  = "Test073"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_73`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_73`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_73`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_73`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_73`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_73 
            from `mimic-four-377221.E4_Micro.UUUU_73`     );


        
###  73



            create table `mimic-four-377221.E4_Micro.TTTT_74`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_74`   
            set test_name_Syn  = "Test074"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_74`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_74`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_74`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_74`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_74`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_74 
            from `mimic-four-377221.E4_Micro.UUUU_74`     );


        
###  74



            create table `mimic-four-377221.E4_Micro.TTTT_75`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_75`   
            set test_name_Syn  = "Test075"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_75`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_75`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_75`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_75`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_75`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_75 
            from `mimic-four-377221.E4_Micro.UUUU_75`     );


        
###  75



            create table `mimic-four-377221.E4_Micro.TTTT_76`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_76`   
            set test_name_Syn  = "Test076"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_76`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_76`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_76`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_76`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_76`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_76 
            from `mimic-four-377221.E4_Micro.UUUU_76`     );


        
###  76



            create table `mimic-four-377221.E4_Micro.TTTT_77`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_77`   
            set test_name_Syn  = "Test077"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_77`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_77`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_77`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_77`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_77`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_77 
            from `mimic-four-377221.E4_Micro.UUUU_77`     );


        
###  77



            create table `mimic-four-377221.E4_Micro.TTTT_78`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_78`   
            set test_name_Syn  = "Test078"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_78`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_78`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_78`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_78`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_78`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_78 
            from `mimic-four-377221.E4_Micro.UUUU_78`     );


        
###  78



            create table `mimic-four-377221.E4_Micro.TTTT_79`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_79`   
            set test_name_Syn  = "Test079"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_79`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_79`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_79`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_79`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_79`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_79 
            from `mimic-four-377221.E4_Micro.UUUU_79`     );


        
###  79



            create table `mimic-four-377221.E4_Micro.TTTT_80`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_80`   
            set test_name_Syn  = "Test080"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_80`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_80`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_80`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_80`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_80`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_80 
            from `mimic-four-377221.E4_Micro.UUUU_80`     );


        
###  80



            create table `mimic-four-377221.E4_Micro.TTTT_81`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_81`   
            set test_name_Syn  = "Test081"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_81`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_81`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_81`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_81`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_81`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_81 
            from `mimic-four-377221.E4_Micro.UUUU_81`     );


        
###  81



            create table `mimic-four-377221.E4_Micro.TTTT_82`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_82`   
            set test_name_Syn  = "Test082"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_82`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_82`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_82`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_82`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_82`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_82 
            from `mimic-four-377221.E4_Micro.UUUU_82`     );


        
###  82



            create table `mimic-four-377221.E4_Micro.TTTT_83`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_83`   
            set test_name_Syn  = "Test083"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_83`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_83`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_83`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_83`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_83`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_83 
            from `mimic-four-377221.E4_Micro.UUUU_83`     );


        
###  83



            create table `mimic-four-377221.E4_Micro.TTTT_84`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_84`   
            set test_name_Syn  = "Test084"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_84`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_84`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_84`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_84`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_84`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_84 
            from `mimic-four-377221.E4_Micro.UUUU_84`     );


        
###  84



            create table `mimic-four-377221.E4_Micro.TTTT_85`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_85`   
            set test_name_Syn  = "Test085"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_85`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_85`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_85`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_85`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_85`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_85 
            from `mimic-four-377221.E4_Micro.UUUU_85`     );


        
###  85



            create table `mimic-four-377221.E4_Micro.TTTT_86`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_86`   
            set test_name_Syn  = "Test086"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_86`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_86`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_86`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_86`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_86`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_86 
            from `mimic-four-377221.E4_Micro.UUUU_86`     );


        
###  86



            create table `mimic-four-377221.E4_Micro.TTTT_87`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_87`   
            set test_name_Syn  = "Test087"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_87`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_87`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_87`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_87`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_87`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_87 
            from `mimic-four-377221.E4_Micro.UUUU_87`     );


        
###  87



            create table `mimic-four-377221.E4_Micro.TTTT_88`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_88`   
            set test_name_Syn  = "Test088"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_88`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_88`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_88`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_88`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_88`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_88 
            from `mimic-four-377221.E4_Micro.UUUU_88`     );


        
###  88



            create table `mimic-four-377221.E4_Micro.TTTT_89`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_89`   
            set test_name_Syn  = "Test089"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_89`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_89`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_89`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_89`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_89`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_89 
            from `mimic-four-377221.E4_Micro.UUUU_89`     );


        
###  89



            create table `mimic-four-377221.E4_Micro.TTTT_90`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_90`   
            set test_name_Syn  = "Test090"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_90`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_90`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_90`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_90`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_90`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_90 
            from `mimic-four-377221.E4_Micro.UUUU_90`     );


        
###  90



            create table `mimic-four-377221.E4_Micro.TTTT_91`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_91`   
            set test_name_Syn  = "Test091"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_91`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_91`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_91`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_91`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_91`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_91 
            from `mimic-four-377221.E4_Micro.UUUU_91`     );


        
###  91



            create table `mimic-four-377221.E4_Micro.TTTT_92`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_92`   
            set test_name_Syn  = "Test092"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_92`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_92`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_92`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_92`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_92`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_92 
            from `mimic-four-377221.E4_Micro.UUUU_92`     );


        
###  92



            create table `mimic-four-377221.E4_Micro.TTTT_93`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_93`   
            set test_name_Syn  = "Test093"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_93`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_93`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_93`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_93`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_93`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_93 
            from `mimic-four-377221.E4_Micro.UUUU_93`     );


        
###  93



            create table `mimic-four-377221.E4_Micro.TTTT_94`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_94`   
            set test_name_Syn  = "Test094"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_94`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_94`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_94`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_94`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_94`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_94 
            from `mimic-four-377221.E4_Micro.UUUU_94`     );


        
###  94



            create table `mimic-four-377221.E4_Micro.TTTT_95`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_95`   
            set test_name_Syn  = "Test095"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_95`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_95`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_95`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_95`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_95`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_95 
            from `mimic-four-377221.E4_Micro.UUUU_95`     );


        
###  95



            create table `mimic-four-377221.E4_Micro.TTTT_96`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_96`   
            set test_name_Syn  = "Test096"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_96`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_96`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_96`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_96`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_96`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_96 
            from `mimic-four-377221.E4_Micro.UUUU_96`     );


        
###  96



            create table `mimic-four-377221.E4_Micro.TTTT_97`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_97`   
            set test_name_Syn  = "Test097"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_97`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_97`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_97`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_97`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_97`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_97 
            from `mimic-four-377221.E4_Micro.UUUU_97`     );


        
###  97



            create table `mimic-four-377221.E4_Micro.TTTT_98`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_98`   
            set test_name_Syn  = "Test098"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_98`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_98`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_98`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_98`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_98`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_98 
            from `mimic-four-377221.E4_Micro.UUUU_98`     );


        
###  98



            create table `mimic-four-377221.E4_Micro.TTTT_99`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_99`   
            set test_name_Syn  = "Test099"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_99`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_99`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_99`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_99`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_99`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_99 
            from `mimic-four-377221.E4_Micro.UUUU_99`     );


        
###  99



            create table `mimic-four-377221.E4_Micro.TTTT_100`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_100`   
            set test_name_Syn  = "Test100"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_100`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_100`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_100`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_100`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_100`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_100 
            from `mimic-four-377221.E4_Micro.UUUU_100`     );


        
###  100



            create table `mimic-four-377221.E4_Micro.TTTT_101`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_101`   
            set test_name_Syn  = "Test101"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_101`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_101`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_101`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_101`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_101`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_101 
            from `mimic-four-377221.E4_Micro.UUUU_101`     );


        
###  101



            create table `mimic-four-377221.E4_Micro.TTTT_102`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_102`   
            set test_name_Syn  = "Test102"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_102`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_102`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_102`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_102`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_102`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_102 
            from `mimic-four-377221.E4_Micro.UUUU_102`     );


        
###  102



            create table `mimic-four-377221.E4_Micro.TTTT_103`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_103`   
            set test_name_Syn  = "Test103"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_103`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_103`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_103`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_103`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_103`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_103 
            from `mimic-four-377221.E4_Micro.UUUU_103`     );


        
###  103



            create table `mimic-four-377221.E4_Micro.TTTT_104`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_104`   
            set test_name_Syn  = "Test104"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_104`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_104`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_104`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_104`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_104`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_104 
            from `mimic-four-377221.E4_Micro.UUUU_104`     );


        
###  104



            create table `mimic-four-377221.E4_Micro.TTTT_105`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_105`   
            set test_name_Syn  = "Test105"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_105`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_105`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_105`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_105`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_105`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_105 
            from `mimic-four-377221.E4_Micro.UUUU_105`     );


        
###  105



            create table `mimic-four-377221.E4_Micro.TTTT_106`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_106`   
            set test_name_Syn  = "Test106"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_106`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_106`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_106`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_106`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_106`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_106 
            from `mimic-four-377221.E4_Micro.UUUU_106`     );


        
###  106



            create table `mimic-four-377221.E4_Micro.TTTT_107`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_107`   
            set test_name_Syn  = "Test107"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_107`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_107`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_107`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_107`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_107`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_107 
            from `mimic-four-377221.E4_Micro.UUUU_107`     );


        
###  107



            create table `mimic-four-377221.E4_Micro.TTTT_108`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_108`   
            set test_name_Syn  = "Test108"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_108`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_108`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_108`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_108`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_108`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_108 
            from `mimic-four-377221.E4_Micro.UUUU_108`     );


        
###  108



            create table `mimic-four-377221.E4_Micro.TTTT_109`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_109`   
            set test_name_Syn  = "Test109"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_109`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_109`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_109`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_109`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_109`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_109 
            from `mimic-four-377221.E4_Micro.UUUU_109`     );


        
###  109



            create table `mimic-four-377221.E4_Micro.TTTT_110`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_110`   
            set test_name_Syn  = "Test110"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_110`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_110`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_110`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_110`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_110`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_110 
            from `mimic-four-377221.E4_Micro.UUUU_110`     );


        
###  110



            create table `mimic-four-377221.E4_Micro.TTTT_111`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_111`   
            set test_name_Syn  = "Test111"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_111`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_111`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_111`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_111`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_111`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_111 
            from `mimic-four-377221.E4_Micro.UUUU_111`     );


        
###  111



            create table `mimic-four-377221.E4_Micro.TTTT_112`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_112`   
            set test_name_Syn  = "Test112"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_112`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_112`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_112`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_112`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_112`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_112 
            from `mimic-four-377221.E4_Micro.UUUU_112`     );


        
###  112



            create table `mimic-four-377221.E4_Micro.TTTT_113`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_113`   
            set test_name_Syn  = "Test113"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_113`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_113`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_113`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_113`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_113`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_113 
            from `mimic-four-377221.E4_Micro.UUUU_113`     );


        
###  113



            create table `mimic-four-377221.E4_Micro.TTTT_114`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_114`   
            set test_name_Syn  = "Test114"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_114`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_114`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_114`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_114`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_114`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_114 
            from `mimic-four-377221.E4_Micro.UUUU_114`     );


        
###  114



            create table `mimic-four-377221.E4_Micro.TTTT_115`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_115`   
            set test_name_Syn  = "Test115"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_115`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_115`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_115`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_115`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_115`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_115 
            from `mimic-four-377221.E4_Micro.UUUU_115`     );


        
###  115



            create table `mimic-four-377221.E4_Micro.TTTT_116`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_116`   
            set test_name_Syn  = "Test116"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_116`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_116`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_116`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_116`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_116`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_116 
            from `mimic-four-377221.E4_Micro.UUUU_116`     );


        
###  116



            create table `mimic-four-377221.E4_Micro.TTTT_117`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_117`   
            set test_name_Syn  = "Test117"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_117`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_117`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_117`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_117`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_117`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_117 
            from `mimic-four-377221.E4_Micro.UUUU_117`     );


        
###  117



            create table `mimic-four-377221.E4_Micro.TTTT_118`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_118`   
            set test_name_Syn  = "Test118"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_118`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_118`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_118`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_118`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_118`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_118 
            from `mimic-four-377221.E4_Micro.UUUU_118`     );


        
###  118



            create table `mimic-four-377221.E4_Micro.TTTT_119`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_119`   
            set test_name_Syn  = "Test119"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_119`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_119`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_119`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_119`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_119`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_119 
            from `mimic-four-377221.E4_Micro.UUUU_119`     );


        
###  119



            create table `mimic-four-377221.E4_Micro.TTTT_120`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_120`   
            set test_name_Syn  = "Test120"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_120`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_120`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_120`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_120`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_120`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_120 
            from `mimic-four-377221.E4_Micro.UUUU_120`     );


        
###  120



            create table `mimic-four-377221.E4_Micro.TTTT_121`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_121`   
            set test_name_Syn  = "Test121"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_121`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_121`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_121`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_121`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_121`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_121 
            from `mimic-four-377221.E4_Micro.UUUU_121`     );


        
###  121



            create table `mimic-four-377221.E4_Micro.TTTT_122`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_122`   
            set test_name_Syn  = "Test122"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_122`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_122`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_122`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_122`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_122`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_122 
            from `mimic-four-377221.E4_Micro.UUUU_122`     );


        
###  122



            create table `mimic-four-377221.E4_Micro.TTTT_123`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_123`   
            set test_name_Syn  = "Test123"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_123`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_123`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_123`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_123`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_123`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_123 
            from `mimic-four-377221.E4_Micro.UUUU_123`     );


        
###  123



            create table `mimic-four-377221.E4_Micro.TTTT_124`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_124`   
            set test_name_Syn  = "Test124"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_124`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_124`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_124`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_124`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_124`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_124 
            from `mimic-four-377221.E4_Micro.UUUU_124`     );


        
###  124



            create table `mimic-four-377221.E4_Micro.TTTT_125`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_125`   
            set test_name_Syn  = "Test125"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_125`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_125`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_125`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_125`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_125`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_125 
            from `mimic-four-377221.E4_Micro.UUUU_125`     );


        
###  125



            create table `mimic-four-377221.E4_Micro.TTTT_126`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_126`   
            set test_name_Syn  = "Test126"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_126`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_126`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_126`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_126`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_126`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_126 
            from `mimic-four-377221.E4_Micro.UUUU_126`     );


        
###  126



            create table `mimic-four-377221.E4_Micro.TTTT_127`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_127`   
            set test_name_Syn  = "Test127"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_127`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_127`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_127`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_127`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_127`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_127 
            from `mimic-four-377221.E4_Micro.UUUU_127`     );


        
###  127



            create table `mimic-four-377221.E4_Micro.TTTT_128`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_128`   
            set test_name_Syn  = "Test128"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_128`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_128`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_128`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_128`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_128`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_128 
            from `mimic-four-377221.E4_Micro.UUUU_128`     );


        
###  128



            create table `mimic-four-377221.E4_Micro.TTTT_129`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_129`   
            set test_name_Syn  = "Test129"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_129`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_129`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_129`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_129`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_129`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_129 
            from `mimic-four-377221.E4_Micro.UUUU_129`     );


        
###  129



            create table `mimic-four-377221.E4_Micro.TTTT_130`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_130`   
            set test_name_Syn  = "Test130"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_130`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_130`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_130`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_130`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_130`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_130 
            from `mimic-four-377221.E4_Micro.UUUU_130`     );


        
###  130



            create table `mimic-four-377221.E4_Micro.TTTT_131`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_131`   
            set test_name_Syn  = "Test131"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_131`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_131`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_131`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_131`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_131`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_131 
            from `mimic-four-377221.E4_Micro.UUUU_131`     );


        
###  131



            create table `mimic-four-377221.E4_Micro.TTTT_132`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_132`   
            set test_name_Syn  = "Test132"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_132`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_132`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_132`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_132`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_132`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_132 
            from `mimic-four-377221.E4_Micro.UUUU_132`     );


        
###  132



            create table `mimic-four-377221.E4_Micro.TTTT_133`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_133`   
            set test_name_Syn  = "Test133"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_133`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_133`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_133`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_133`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_133`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_133 
            from `mimic-four-377221.E4_Micro.UUUU_133`     );


        
###  133



            create table `mimic-four-377221.E4_Micro.TTTT_134`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_134`   
            set test_name_Syn  = "Test134"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_134`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_134`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_134`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_134`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_134`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_134 
            from `mimic-four-377221.E4_Micro.UUUU_134`     );


        
###  134



            create table `mimic-four-377221.E4_Micro.TTTT_135`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_135`   
            set test_name_Syn  = "Test135"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_135`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_135`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_135`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_135`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_135`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_135 
            from `mimic-four-377221.E4_Micro.UUUU_135`     );


        
###  135



            create table `mimic-four-377221.E4_Micro.TTTT_136`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_136`   
            set test_name_Syn  = "Test136"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_136`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_136`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_136`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_136`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_136`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_136 
            from `mimic-four-377221.E4_Micro.UUUU_136`     );


        
###  136



            create table `mimic-four-377221.E4_Micro.TTTT_137`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_137`   
            set test_name_Syn  = "Test137"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_137`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_137`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_137`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_137`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_137`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_137 
            from `mimic-four-377221.E4_Micro.UUUU_137`     );


        
###  137



            create table `mimic-four-377221.E4_Micro.TTTT_138`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_138`   
            set test_name_Syn  = "Test138"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_138`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_138`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_138`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_138`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_138`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_138 
            from `mimic-four-377221.E4_Micro.UUUU_138`     );


        
###  138



            create table `mimic-four-377221.E4_Micro.TTTT_139`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_139`   
            set test_name_Syn  = "Test139"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_139`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_139`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_139`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_139`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_139`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_139 
            from `mimic-four-377221.E4_Micro.UUUU_139`     );


        
###  139



            create table `mimic-four-377221.E4_Micro.TTTT_140`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_140`   
            set test_name_Syn  = "Test140"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_140`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_140`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_140`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_140`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_140`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_140 
            from `mimic-four-377221.E4_Micro.UUUU_140`     );


        
###  140



            create table `mimic-four-377221.E4_Micro.TTTT_141`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_141`   
            set test_name_Syn  = "Test141"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_141`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_141`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_141`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_141`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_141`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_141 
            from `mimic-four-377221.E4_Micro.UUUU_141`     );


        
###  141



            create table `mimic-four-377221.E4_Micro.TTTT_142`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_142`   
            set test_name_Syn  = "Test142"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_142`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_142`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_142`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_142`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_142`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_142 
            from `mimic-four-377221.E4_Micro.UUUU_142`     );


        
###  142



            create table `mimic-four-377221.E4_Micro.TTTT_143`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_143`   
            set test_name_Syn  = "Test143"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_143`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_143`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_143`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_143`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_143`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_143 
            from `mimic-four-377221.E4_Micro.UUUU_143`     );


        
###  143



            create table `mimic-four-377221.E4_Micro.TTTT_144`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_144`   
            set test_name_Syn  = "Test144"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_144`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_144`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_144`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_144`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_144`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_144 
            from `mimic-four-377221.E4_Micro.UUUU_144`     );


        
###  144



            create table `mimic-four-377221.E4_Micro.TTTT_145`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_145`   
            set test_name_Syn  = "Test145"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_145`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_145`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_145`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_145`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_145`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_145 
            from `mimic-four-377221.E4_Micro.UUUU_145`     );


        
###  145



            create table `mimic-four-377221.E4_Micro.TTTT_146`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_146`   
            set test_name_Syn  = "Test146"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_146`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_146`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_146`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_146`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_146`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_146 
            from `mimic-four-377221.E4_Micro.UUUU_146`     );


        
###  146



            create table `mimic-four-377221.E4_Micro.TTTT_147`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_147`   
            set test_name_Syn  = "Test147"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_147`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_147`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_147`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_147`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_147`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_147 
            from `mimic-four-377221.E4_Micro.UUUU_147`     );


        
###  147



            create table `mimic-four-377221.E4_Micro.TTTT_148`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_148`   
            set test_name_Syn  = "Test148"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_148`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_148`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_148`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_148`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_148`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_148 
            from `mimic-four-377221.E4_Micro.UUUU_148`     );


        
###  148



            create table `mimic-four-377221.E4_Micro.TTTT_149`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_149`   
            set test_name_Syn  = "Test149"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_149`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_149`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_149`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_149`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_149`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_149 
            from `mimic-four-377221.E4_Micro.UUUU_149`     );


        
###  149



            create table `mimic-four-377221.E4_Micro.TTTT_150`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_150`   
            set test_name_Syn  = "Test150"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_150`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_150`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_150`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_150`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_150`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_150 
            from `mimic-four-377221.E4_Micro.UUUU_150`     );


        
###  150



            create table `mimic-four-377221.E4_Micro.TTTT_151`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_151`   
            set test_name_Syn  = "Test151"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_151`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_151`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_151`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_151`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_151`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_151 
            from `mimic-four-377221.E4_Micro.UUUU_151`     );


        
###  151



            create table `mimic-four-377221.E4_Micro.TTTT_152`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_152`   
            set test_name_Syn  = "Test152"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_152`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_152`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_152`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_152`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_152`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_152 
            from `mimic-four-377221.E4_Micro.UUUU_152`     );


        
###  152



            create table `mimic-four-377221.E4_Micro.TTTT_153`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_153`   
            set test_name_Syn  = "Test153"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_153`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_153`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_153`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_153`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_153`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_153 
            from `mimic-four-377221.E4_Micro.UUUU_153`     );


        
###  153



            create table `mimic-four-377221.E4_Micro.TTTT_154`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_154`   
            set test_name_Syn  = "Test154"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_154`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_154`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_154`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_154`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_154`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_154 
            from `mimic-four-377221.E4_Micro.UUUU_154`     );


        
###  154



            create table `mimic-four-377221.E4_Micro.TTTT_155`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_155`   
            set test_name_Syn  = "Test155"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_155`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_155`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_155`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_155`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_155`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_155 
            from `mimic-four-377221.E4_Micro.UUUU_155`     );


        
###  155



            create table `mimic-four-377221.E4_Micro.TTTT_156`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_156`   
            set test_name_Syn  = "Test156"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_156`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_156`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_156`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_156`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_156`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_156 
            from `mimic-four-377221.E4_Micro.UUUU_156`     );


        
###  156



            create table `mimic-four-377221.E4_Micro.TTTT_157`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_157`   
            set test_name_Syn  = "Test157"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_157`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_157`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_157`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_157`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_157`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_157 
            from `mimic-four-377221.E4_Micro.UUUU_157`     );


        
###  157



            create table `mimic-four-377221.E4_Micro.TTTT_158`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_158`   
            set test_name_Syn  = "Test158"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_158`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_158`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_158`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_158`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_158`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_158 
            from `mimic-four-377221.E4_Micro.UUUU_158`     );


        
###  158



            create table `mimic-four-377221.E4_Micro.TTTT_159`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_159`   
            set test_name_Syn  = "Test159"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_159`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_159`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_159`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_159`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_159`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_159 
            from `mimic-four-377221.E4_Micro.UUUU_159`     );


        
###  159



            create table `mimic-four-377221.E4_Micro.TTTT_160`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_160`   
            set test_name_Syn  = "Test160"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_160`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_160`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_160`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_160`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_160`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_160 
            from `mimic-four-377221.E4_Micro.UUUU_160`     );


        
###  160



            create table `mimic-four-377221.E4_Micro.TTTT_161`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_161`   
            set test_name_Syn  = "Test161"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_161`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_161`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_161`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_161`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_161`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_161 
            from `mimic-four-377221.E4_Micro.UUUU_161`     );


        
###  161



            create table `mimic-four-377221.E4_Micro.TTTT_162`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_162`   
            set test_name_Syn  = "Test162"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_162`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_162`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_162`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_162`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_162`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_162 
            from `mimic-four-377221.E4_Micro.UUUU_162`     );


        
###  162



            create table `mimic-four-377221.E4_Micro.TTTT_163`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_163`   
            set test_name_Syn  = "Test163"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_163`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_163`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_163`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_163`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_163`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_163 
            from `mimic-four-377221.E4_Micro.UUUU_163`     );


        
###  163



            create table `mimic-four-377221.E4_Micro.TTTT_164`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_164`   
            set test_name_Syn  = "Test164"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_164`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_164`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_164`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_164`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_164`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_164 
            from `mimic-four-377221.E4_Micro.UUUU_164`     );


        
###  164



            create table `mimic-four-377221.E4_Micro.TTTT_165`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_165`   
            set test_name_Syn  = "Test165"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_165`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_165`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_165`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_165`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_165`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_165 
            from `mimic-four-377221.E4_Micro.UUUU_165`     );


        
###  165



            create table `mimic-four-377221.E4_Micro.TTTT_166`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_166`   
            set test_name_Syn  = "Test166"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_166`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_166`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_166`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_166`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_166`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_166 
            from `mimic-four-377221.E4_Micro.UUUU_166`     );


        
###  166



            create table `mimic-four-377221.E4_Micro.TTTT_167`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_167`   
            set test_name_Syn  = "Test167"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_167`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_167`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_167`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_167`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_167`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_167 
            from `mimic-four-377221.E4_Micro.UUUU_167`     );


        
###  167



            create table `mimic-four-377221.E4_Micro.TTTT_168`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_168`   
            set test_name_Syn  = "Test168"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_168`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_168`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_168`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_168`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_168`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_168 
            from `mimic-four-377221.E4_Micro.UUUU_168`     );


        
###  168



            create table `mimic-four-377221.E4_Micro.TTTT_169`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_169`   
            set test_name_Syn  = "Test169"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_169`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_169`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_169`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_169`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_169`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_169 
            from `mimic-four-377221.E4_Micro.UUUU_169`     );


        
###  169



            create table `mimic-four-377221.E4_Micro.TTTT_170`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_170`   
            set test_name_Syn  = "Test170"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_170`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_170`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_170`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_170`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_170`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_170 
            from `mimic-four-377221.E4_Micro.UUUU_170`     );


        
###  170



            create table `mimic-four-377221.E4_Micro.TTTT_171`    as
            SELECT * from `mimic-four-377221.E4_Micro.HYT`    ;


            update `mimic-four-377221.E4_Micro.TTTT_171`   
            set test_name_Syn  = "Test171"
            where test_name_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.UUUU_171`    as (
            select 
            a.rowNum ,
            a.test_name_Syn ,
            a.spec_type_desc_Syn ,
            b.spec_type_desc_Syn   as  Value_2
            from `mimic-four-377221.E4_Micro.TTTT_171`    a 
            left join `mimic-four-377221.E4_Micro.Micro_B2`    b
            on
            a.rowNum =b.rowNum 
            and
            a.test_name_Syn =b.test_name_Syn ) ;

            update `mimic-four-377221.E4_Micro.UUUU_171`  
            set spec_type_desc_Syn  = Value_2
            where spec_type_desc_Syn  is null  ;

            update `mimic-four-377221.E4_Micro.UUUU_171`  
            set spec_type_desc_Syn  = 0
            where spec_type_desc_Syn  is null  ;

            create table `mimic-four-377221.E4_Micro.VVVV_171`    as (
            select 
            rowNum ,
            spec_type_desc_Syn   as  Test_171 
            from `mimic-four-377221.E4_Micro.UUUU_171`     );


        
##################################################################################
#query   Part 3 =


        create table `mimic-four-377221.E4_Micro.Micro_B3`     as
        SELECT
        KKKK_1.rowNum,
        KKKK_1.Test_1, 
        KKKK_2.Test_2, 
        KKKK_3.Test_3, 
        KKKK_4.Test_4, 
        KKKK_5.Test_5, 
        KKKK_6.Test_6, 
        KKKK_7.Test_7, 
        KKKK_8.Test_8, 
        KKKK_9.Test_9, 
        KKKK_10.Test_10, 
        KKKK_11.Test_11, 
        KKKK_12.Test_12, 
        KKKK_13.Test_13, 
        KKKK_14.Test_14, 
        KKKK_15.Test_15, 
        KKKK_16.Test_16, 
        KKKK_17.Test_17, 
        KKKK_18.Test_18, 
        KKKK_19.Test_19, 
        KKKK_20.Test_20, 
        KKKK_21.Test_21, 
        KKKK_22.Test_22, 
        KKKK_23.Test_23, 
        KKKK_24.Test_24, 
        KKKK_25.Test_25, 
        KKKK_26.Test_26, 
        KKKK_27.Test_27, 
        KKKK_28.Test_28, 
        KKKK_29.Test_29, 
        KKKK_30.Test_30, 
        KKKK_31.Test_31, 
        KKKK_32.Test_32, 
        KKKK_33.Test_33, 
        KKKK_34.Test_34, 
        KKKK_35.Test_35, 
        KKKK_36.Test_36, 
        KKKK_37.Test_37, 
        KKKK_38.Test_38, 
        KKKK_39.Test_39, 
        KKKK_40.Test_40, 
        KKKK_41.Test_41, 
        KKKK_42.Test_42, 
        KKKK_43.Test_43, 
        KKKK_44.Test_44, 
        KKKK_45.Test_45, 
        KKKK_46.Test_46, 
        KKKK_47.Test_47, 
        KKKK_48.Test_48, 
        KKKK_49.Test_49, 
        KKKK_50.Test_50, 
        KKKK_51.Test_51, 
        KKKK_52.Test_52, 
        KKKK_53.Test_53, 
        KKKK_54.Test_54, 
        KKKK_55.Test_55, 
        KKKK_56.Test_56, 
        KKKK_57.Test_57, 
        KKKK_58.Test_58, 
        KKKK_59.Test_59, 
        KKKK_60.Test_60, 
        KKKK_61.Test_61, 
        KKKK_62.Test_62, 
        KKKK_63.Test_63, 
        KKKK_64.Test_64, 
        KKKK_65.Test_65, 
        KKKK_66.Test_66, 
        KKKK_67.Test_67, 
        KKKK_68.Test_68, 
        KKKK_69.Test_69, 
        KKKK_70.Test_70, 
        KKKK_71.Test_71, 
        KKKK_72.Test_72, 
        KKKK_73.Test_73, 
        KKKK_74.Test_74, 
        KKKK_75.Test_75, 
        KKKK_76.Test_76, 
        KKKK_77.Test_77, 
        KKKK_78.Test_78, 
        KKKK_79.Test_79, 
        KKKK_80.Test_80, 
        KKKK_81.Test_81, 
        KKKK_82.Test_82, 
        KKKK_83.Test_83, 
        KKKK_84.Test_84, 
        KKKK_85.Test_85, 
        KKKK_86.Test_86, 
        KKKK_87.Test_87, 
        KKKK_88.Test_88, 
        KKKK_89.Test_89, 
        KKKK_90.Test_90, 
        KKKK_91.Test_91, 
        KKKK_92.Test_92, 
        KKKK_93.Test_93, 
        KKKK_94.Test_94, 
        KKKK_95.Test_95, 
        KKKK_96.Test_96, 
        KKKK_97.Test_97, 
        KKKK_98.Test_98, 
        KKKK_99.Test_99, 
        KKKK_100.Test_100, 
        KKKK_101.Test_101, 
        KKKK_102.Test_102, 
        KKKK_103.Test_103, 
        KKKK_104.Test_104, 
        KKKK_105.Test_105, 
        KKKK_106.Test_106, 
        KKKK_107.Test_107, 
        KKKK_108.Test_108, 
        KKKK_109.Test_109, 
        KKKK_110.Test_110, 
        KKKK_111.Test_111, 
        KKKK_112.Test_112, 
        KKKK_113.Test_113, 
        KKKK_114.Test_114, 
        KKKK_115.Test_115, 
        KKKK_116.Test_116, 
        KKKK_117.Test_117, 
        KKKK_118.Test_118, 
        KKKK_119.Test_119, 
        KKKK_120.Test_120, 
        KKKK_121.Test_121, 
        KKKK_122.Test_122, 
        KKKK_123.Test_123, 
        KKKK_124.Test_124, 
        KKKK_125.Test_125, 
        KKKK_126.Test_126, 
        KKKK_127.Test_127, 
        KKKK_128.Test_128, 
        KKKK_129.Test_129, 
        KKKK_130.Test_130, 
        KKKK_131.Test_131, 
        KKKK_132.Test_132, 
        KKKK_133.Test_133, 
        KKKK_134.Test_134, 
        KKKK_135.Test_135, 
        KKKK_136.Test_136, 
        KKKK_137.Test_137, 
        KKKK_138.Test_138, 
        KKKK_139.Test_139, 
        KKKK_140.Test_140, 
        KKKK_141.Test_141, 
        KKKK_142.Test_142, 
        KKKK_143.Test_143, 
        KKKK_144.Test_144, 
        KKKK_145.Test_145, 
        KKKK_146.Test_146, 
        KKKK_147.Test_147, 
        KKKK_148.Test_148, 
        KKKK_149.Test_149, 
        KKKK_150.Test_150, 
        KKKK_151.Test_151, 
        KKKK_152.Test_152, 
        KKKK_153.Test_153, 
        KKKK_154.Test_154, 
        KKKK_155.Test_155, 
        KKKK_156.Test_156, 
        KKKK_157.Test_157, 
        KKKK_158.Test_158, 
        KKKK_159.Test_159, 
        KKKK_160.Test_160, 
        KKKK_161.Test_161, 
        KKKK_162.Test_162, 
        KKKK_163.Test_163, 
        KKKK_164.Test_164, 
        KKKK_165.Test_165, 
        KKKK_166.Test_166, 
        KKKK_167.Test_167, 
        KKKK_168.Test_168, 
        KKKK_169.Test_169, 
        KKKK_170.Test_170, 
        KKKK_171.Test_171 

        from `mimic-four-377221.E4_Micro.VVVV_1`  as KKKK_1
    
        left join 
        `mimic-four-377221.E4_Micro.VVVV_2`  as KKKK_2
        on
        KKKK_1.rowNum=KKKK_2.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_3`  as KKKK_3
        on
        KKKK_1.rowNum=KKKK_3.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_4`  as KKKK_4
        on
        KKKK_1.rowNum=KKKK_4.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_5`  as KKKK_5
        on
        KKKK_1.rowNum=KKKK_5.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_6`  as KKKK_6
        on
        KKKK_1.rowNum=KKKK_6.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_7`  as KKKK_7
        on
        KKKK_1.rowNum=KKKK_7.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_8`  as KKKK_8
        on
        KKKK_1.rowNum=KKKK_8.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_9`  as KKKK_9
        on
        KKKK_1.rowNum=KKKK_9.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_10`  as KKKK_10
        on
        KKKK_1.rowNum=KKKK_10.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_11`  as KKKK_11
        on
        KKKK_1.rowNum=KKKK_11.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_12`  as KKKK_12
        on
        KKKK_1.rowNum=KKKK_12.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_13`  as KKKK_13
        on
        KKKK_1.rowNum=KKKK_13.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_14`  as KKKK_14
        on
        KKKK_1.rowNum=KKKK_14.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_15`  as KKKK_15
        on
        KKKK_1.rowNum=KKKK_15.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_16`  as KKKK_16
        on
        KKKK_1.rowNum=KKKK_16.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_17`  as KKKK_17
        on
        KKKK_1.rowNum=KKKK_17.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_18`  as KKKK_18
        on
        KKKK_1.rowNum=KKKK_18.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_19`  as KKKK_19
        on
        KKKK_1.rowNum=KKKK_19.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_20`  as KKKK_20
        on
        KKKK_1.rowNum=KKKK_20.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_21`  as KKKK_21
        on
        KKKK_1.rowNum=KKKK_21.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_22`  as KKKK_22
        on
        KKKK_1.rowNum=KKKK_22.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_23`  as KKKK_23
        on
        KKKK_1.rowNum=KKKK_23.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_24`  as KKKK_24
        on
        KKKK_1.rowNum=KKKK_24.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_25`  as KKKK_25
        on
        KKKK_1.rowNum=KKKK_25.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_26`  as KKKK_26
        on
        KKKK_1.rowNum=KKKK_26.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_27`  as KKKK_27
        on
        KKKK_1.rowNum=KKKK_27.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_28`  as KKKK_28
        on
        KKKK_1.rowNum=KKKK_28.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_29`  as KKKK_29
        on
        KKKK_1.rowNum=KKKK_29.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_30`  as KKKK_30
        on
        KKKK_1.rowNum=KKKK_30.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_31`  as KKKK_31
        on
        KKKK_1.rowNum=KKKK_31.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_32`  as KKKK_32
        on
        KKKK_1.rowNum=KKKK_32.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_33`  as KKKK_33
        on
        KKKK_1.rowNum=KKKK_33.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_34`  as KKKK_34
        on
        KKKK_1.rowNum=KKKK_34.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_35`  as KKKK_35
        on
        KKKK_1.rowNum=KKKK_35.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_36`  as KKKK_36
        on
        KKKK_1.rowNum=KKKK_36.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_37`  as KKKK_37
        on
        KKKK_1.rowNum=KKKK_37.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_38`  as KKKK_38
        on
        KKKK_1.rowNum=KKKK_38.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_39`  as KKKK_39
        on
        KKKK_1.rowNum=KKKK_39.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_40`  as KKKK_40
        on
        KKKK_1.rowNum=KKKK_40.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_41`  as KKKK_41
        on
        KKKK_1.rowNum=KKKK_41.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_42`  as KKKK_42
        on
        KKKK_1.rowNum=KKKK_42.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_43`  as KKKK_43
        on
        KKKK_1.rowNum=KKKK_43.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_44`  as KKKK_44
        on
        KKKK_1.rowNum=KKKK_44.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_45`  as KKKK_45
        on
        KKKK_1.rowNum=KKKK_45.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_46`  as KKKK_46
        on
        KKKK_1.rowNum=KKKK_46.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_47`  as KKKK_47
        on
        KKKK_1.rowNum=KKKK_47.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_48`  as KKKK_48
        on
        KKKK_1.rowNum=KKKK_48.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_49`  as KKKK_49
        on
        KKKK_1.rowNum=KKKK_49.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_50`  as KKKK_50
        on
        KKKK_1.rowNum=KKKK_50.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_51`  as KKKK_51
        on
        KKKK_1.rowNum=KKKK_51.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_52`  as KKKK_52
        on
        KKKK_1.rowNum=KKKK_52.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_53`  as KKKK_53
        on
        KKKK_1.rowNum=KKKK_53.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_54`  as KKKK_54
        on
        KKKK_1.rowNum=KKKK_54.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_55`  as KKKK_55
        on
        KKKK_1.rowNum=KKKK_55.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_56`  as KKKK_56
        on
        KKKK_1.rowNum=KKKK_56.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_57`  as KKKK_57
        on
        KKKK_1.rowNum=KKKK_57.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_58`  as KKKK_58
        on
        KKKK_1.rowNum=KKKK_58.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_59`  as KKKK_59
        on
        KKKK_1.rowNum=KKKK_59.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_60`  as KKKK_60
        on
        KKKK_1.rowNum=KKKK_60.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_61`  as KKKK_61
        on
        KKKK_1.rowNum=KKKK_61.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_62`  as KKKK_62
        on
        KKKK_1.rowNum=KKKK_62.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_63`  as KKKK_63
        on
        KKKK_1.rowNum=KKKK_63.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_64`  as KKKK_64
        on
        KKKK_1.rowNum=KKKK_64.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_65`  as KKKK_65
        on
        KKKK_1.rowNum=KKKK_65.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_66`  as KKKK_66
        on
        KKKK_1.rowNum=KKKK_66.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_67`  as KKKK_67
        on
        KKKK_1.rowNum=KKKK_67.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_68`  as KKKK_68
        on
        KKKK_1.rowNum=KKKK_68.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_69`  as KKKK_69
        on
        KKKK_1.rowNum=KKKK_69.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_70`  as KKKK_70
        on
        KKKK_1.rowNum=KKKK_70.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_71`  as KKKK_71
        on
        KKKK_1.rowNum=KKKK_71.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_72`  as KKKK_72
        on
        KKKK_1.rowNum=KKKK_72.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_73`  as KKKK_73
        on
        KKKK_1.rowNum=KKKK_73.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_74`  as KKKK_74
        on
        KKKK_1.rowNum=KKKK_74.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_75`  as KKKK_75
        on
        KKKK_1.rowNum=KKKK_75.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_76`  as KKKK_76
        on
        KKKK_1.rowNum=KKKK_76.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_77`  as KKKK_77
        on
        KKKK_1.rowNum=KKKK_77.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_78`  as KKKK_78
        on
        KKKK_1.rowNum=KKKK_78.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_79`  as KKKK_79
        on
        KKKK_1.rowNum=KKKK_79.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_80`  as KKKK_80
        on
        KKKK_1.rowNum=KKKK_80.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_81`  as KKKK_81
        on
        KKKK_1.rowNum=KKKK_81.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_82`  as KKKK_82
        on
        KKKK_1.rowNum=KKKK_82.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_83`  as KKKK_83
        on
        KKKK_1.rowNum=KKKK_83.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_84`  as KKKK_84
        on
        KKKK_1.rowNum=KKKK_84.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_85`  as KKKK_85
        on
        KKKK_1.rowNum=KKKK_85.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_86`  as KKKK_86
        on
        KKKK_1.rowNum=KKKK_86.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_87`  as KKKK_87
        on
        KKKK_1.rowNum=KKKK_87.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_88`  as KKKK_88
        on
        KKKK_1.rowNum=KKKK_88.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_89`  as KKKK_89
        on
        KKKK_1.rowNum=KKKK_89.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_90`  as KKKK_90
        on
        KKKK_1.rowNum=KKKK_90.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_91`  as KKKK_91
        on
        KKKK_1.rowNum=KKKK_91.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_92`  as KKKK_92
        on
        KKKK_1.rowNum=KKKK_92.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_93`  as KKKK_93
        on
        KKKK_1.rowNum=KKKK_93.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_94`  as KKKK_94
        on
        KKKK_1.rowNum=KKKK_94.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_95`  as KKKK_95
        on
        KKKK_1.rowNum=KKKK_95.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_96`  as KKKK_96
        on
        KKKK_1.rowNum=KKKK_96.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_97`  as KKKK_97
        on
        KKKK_1.rowNum=KKKK_97.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_98`  as KKKK_98
        on
        KKKK_1.rowNum=KKKK_98.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_99`  as KKKK_99
        on
        KKKK_1.rowNum=KKKK_99.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_100`  as KKKK_100
        on
        KKKK_1.rowNum=KKKK_100.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_101`  as KKKK_101
        on
        KKKK_1.rowNum=KKKK_101.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_102`  as KKKK_102
        on
        KKKK_1.rowNum=KKKK_102.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_103`  as KKKK_103
        on
        KKKK_1.rowNum=KKKK_103.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_104`  as KKKK_104
        on
        KKKK_1.rowNum=KKKK_104.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_105`  as KKKK_105
        on
        KKKK_1.rowNum=KKKK_105.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_106`  as KKKK_106
        on
        KKKK_1.rowNum=KKKK_106.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_107`  as KKKK_107
        on
        KKKK_1.rowNum=KKKK_107.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_108`  as KKKK_108
        on
        KKKK_1.rowNum=KKKK_108.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_109`  as KKKK_109
        on
        KKKK_1.rowNum=KKKK_109.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_110`  as KKKK_110
        on
        KKKK_1.rowNum=KKKK_110.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_111`  as KKKK_111
        on
        KKKK_1.rowNum=KKKK_111.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_112`  as KKKK_112
        on
        KKKK_1.rowNum=KKKK_112.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_113`  as KKKK_113
        on
        KKKK_1.rowNum=KKKK_113.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_114`  as KKKK_114
        on
        KKKK_1.rowNum=KKKK_114.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_115`  as KKKK_115
        on
        KKKK_1.rowNum=KKKK_115.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_116`  as KKKK_116
        on
        KKKK_1.rowNum=KKKK_116.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_117`  as KKKK_117
        on
        KKKK_1.rowNum=KKKK_117.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_118`  as KKKK_118
        on
        KKKK_1.rowNum=KKKK_118.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_119`  as KKKK_119
        on
        KKKK_1.rowNum=KKKK_119.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_120`  as KKKK_120
        on
        KKKK_1.rowNum=KKKK_120.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_121`  as KKKK_121
        on
        KKKK_1.rowNum=KKKK_121.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_122`  as KKKK_122
        on
        KKKK_1.rowNum=KKKK_122.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_123`  as KKKK_123
        on
        KKKK_1.rowNum=KKKK_123.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_124`  as KKKK_124
        on
        KKKK_1.rowNum=KKKK_124.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_125`  as KKKK_125
        on
        KKKK_1.rowNum=KKKK_125.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_126`  as KKKK_126
        on
        KKKK_1.rowNum=KKKK_126.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_127`  as KKKK_127
        on
        KKKK_1.rowNum=KKKK_127.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_128`  as KKKK_128
        on
        KKKK_1.rowNum=KKKK_128.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_129`  as KKKK_129
        on
        KKKK_1.rowNum=KKKK_129.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_130`  as KKKK_130
        on
        KKKK_1.rowNum=KKKK_130.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_131`  as KKKK_131
        on
        KKKK_1.rowNum=KKKK_131.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_132`  as KKKK_132
        on
        KKKK_1.rowNum=KKKK_132.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_133`  as KKKK_133
        on
        KKKK_1.rowNum=KKKK_133.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_134`  as KKKK_134
        on
        KKKK_1.rowNum=KKKK_134.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_135`  as KKKK_135
        on
        KKKK_1.rowNum=KKKK_135.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_136`  as KKKK_136
        on
        KKKK_1.rowNum=KKKK_136.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_137`  as KKKK_137
        on
        KKKK_1.rowNum=KKKK_137.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_138`  as KKKK_138
        on
        KKKK_1.rowNum=KKKK_138.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_139`  as KKKK_139
        on
        KKKK_1.rowNum=KKKK_139.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_140`  as KKKK_140
        on
        KKKK_1.rowNum=KKKK_140.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_141`  as KKKK_141
        on
        KKKK_1.rowNum=KKKK_141.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_142`  as KKKK_142
        on
        KKKK_1.rowNum=KKKK_142.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_143`  as KKKK_143
        on
        KKKK_1.rowNum=KKKK_143.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_144`  as KKKK_144
        on
        KKKK_1.rowNum=KKKK_144.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_145`  as KKKK_145
        on
        KKKK_1.rowNum=KKKK_145.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_146`  as KKKK_146
        on
        KKKK_1.rowNum=KKKK_146.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_147`  as KKKK_147
        on
        KKKK_1.rowNum=KKKK_147.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_148`  as KKKK_148
        on
        KKKK_1.rowNum=KKKK_148.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_149`  as KKKK_149
        on
        KKKK_1.rowNum=KKKK_149.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_150`  as KKKK_150
        on
        KKKK_1.rowNum=KKKK_150.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_151`  as KKKK_151
        on
        KKKK_1.rowNum=KKKK_151.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_152`  as KKKK_152
        on
        KKKK_1.rowNum=KKKK_152.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_153`  as KKKK_153
        on
        KKKK_1.rowNum=KKKK_153.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_154`  as KKKK_154
        on
        KKKK_1.rowNum=KKKK_154.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_155`  as KKKK_155
        on
        KKKK_1.rowNum=KKKK_155.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_156`  as KKKK_156
        on
        KKKK_1.rowNum=KKKK_156.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_157`  as KKKK_157
        on
        KKKK_1.rowNum=KKKK_157.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_158`  as KKKK_158
        on
        KKKK_1.rowNum=KKKK_158.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_159`  as KKKK_159
        on
        KKKK_1.rowNum=KKKK_159.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_160`  as KKKK_160
        on
        KKKK_1.rowNum=KKKK_160.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_161`  as KKKK_161
        on
        KKKK_1.rowNum=KKKK_161.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_162`  as KKKK_162
        on
        KKKK_1.rowNum=KKKK_162.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_163`  as KKKK_163
        on
        KKKK_1.rowNum=KKKK_163.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_164`  as KKKK_164
        on
        KKKK_1.rowNum=KKKK_164.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_165`  as KKKK_165
        on
        KKKK_1.rowNum=KKKK_165.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_166`  as KKKK_166
        on
        KKKK_1.rowNum=KKKK_166.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_167`  as KKKK_167
        on
        KKKK_1.rowNum=KKKK_167.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_168`  as KKKK_168
        on
        KKKK_1.rowNum=KKKK_168.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_169`  as KKKK_169
        on
        KKKK_1.rowNum=KKKK_169.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_170`  as KKKK_170
        on
        KKKK_1.rowNum=KKKK_170.rowNum
         
        left join 
        `mimic-four-377221.E4_Micro.VVVV_171`  as KKKK_171
        on
        KKKK_1.rowNum=KKKK_171.rowNum
         
##################################################################################
#query   Part 4 =


    ;
                    drop table  `mimic-four-377221.E4_Micro.HYT`  ;
                    

                        drop table  `mimic-four-377221.E4_Micro.TTTT_1`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_2`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_3`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_4`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_5`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_6`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_7`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_8`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_9`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_10`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_11`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_12`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_13`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_14`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_15`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_16`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_17`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_18`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_19`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_20`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_21`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_22`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_23`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_24`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_25`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_26`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_27`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_28`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_29`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_30`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_31`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_32`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_33`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_34`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_35`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_36`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_37`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_38`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_39`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_40`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_41`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_42`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_43`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_44`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_45`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_46`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_47`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_48`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_49`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_50`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_51`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_52`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_53`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_54`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_55`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_56`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_57`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_58`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_59`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_60`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_61`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_62`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_63`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_64`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_65`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_66`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_67`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_68`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_69`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_70`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_71`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_72`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_73`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_74`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_75`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_76`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_77`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_78`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_79`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_80`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_81`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_82`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_83`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_84`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_85`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_86`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_87`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_88`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_89`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_90`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_91`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_92`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_93`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_94`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_95`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_96`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_97`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_98`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_99`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_100`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_101`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_102`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_103`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_104`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_105`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_106`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_107`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_108`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_109`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_110`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_111`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_112`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_113`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_114`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_115`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_116`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_117`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_118`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_119`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_120`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_121`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_122`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_123`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_124`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_125`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_126`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_127`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_128`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_129`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_130`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_131`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_132`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_133`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_134`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_135`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_136`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_137`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_138`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_139`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_140`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_141`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_142`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_143`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_144`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_145`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_146`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_147`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_148`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_149`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_150`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_151`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_152`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_153`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_154`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_155`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_156`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_157`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_158`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_159`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_160`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_161`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_162`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_163`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_164`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_165`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_166`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_167`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_168`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_169`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_170`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.TTTT_171`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_1`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_2`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_3`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_4`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_5`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_6`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_7`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_8`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_9`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_10`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_11`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_12`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_13`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_14`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_15`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_16`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_17`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_18`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_19`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_20`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_21`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_22`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_23`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_24`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_25`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_26`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_27`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_28`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_29`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_30`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_31`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_32`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_33`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_34`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_35`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_36`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_37`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_38`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_39`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_40`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_41`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_42`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_43`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_44`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_45`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_46`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_47`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_48`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_49`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_50`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_51`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_52`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_53`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_54`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_55`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_56`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_57`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_58`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_59`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_60`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_61`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_62`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_63`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_64`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_65`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_66`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_67`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_68`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_69`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_70`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_71`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_72`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_73`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_74`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_75`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_76`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_77`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_78`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_79`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_80`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_81`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_82`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_83`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_84`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_85`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_86`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_87`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_88`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_89`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_90`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_91`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_92`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_93`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_94`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_95`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_96`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_97`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_98`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_99`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_100`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_101`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_102`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_103`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_104`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_105`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_106`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_107`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_108`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_109`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_110`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_111`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_112`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_113`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_114`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_115`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_116`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_117`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_118`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_119`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_120`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_121`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_122`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_123`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_124`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_125`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_126`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_127`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_128`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_129`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_130`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_131`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_132`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_133`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_134`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_135`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_136`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_137`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_138`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_139`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_140`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_141`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_142`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_143`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_144`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_145`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_146`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_147`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_148`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_149`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_150`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_151`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_152`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_153`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_154`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_155`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_156`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_157`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_158`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_159`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_160`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_161`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_162`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_163`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_164`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_165`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_166`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_167`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_168`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_169`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_170`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.UUUU_171`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_1`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_2`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_3`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_4`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_5`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_6`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_7`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_8`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_9`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_10`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_11`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_12`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_13`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_14`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_15`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_16`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_17`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_18`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_19`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_20`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_21`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_22`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_23`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_24`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_25`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_26`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_27`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_28`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_29`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_30`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_31`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_32`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_33`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_34`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_35`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_36`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_37`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_38`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_39`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_40`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_41`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_42`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_43`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_44`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_45`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_46`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_47`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_48`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_49`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_50`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_51`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_52`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_53`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_54`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_55`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_56`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_57`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_58`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_59`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_60`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_61`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_62`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_63`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_64`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_65`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_66`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_67`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_68`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_69`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_70`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_71`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_72`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_73`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_74`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_75`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_76`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_77`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_78`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_79`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_80`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_81`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_82`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_83`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_84`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_85`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_86`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_87`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_88`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_89`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_90`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_91`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_92`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_93`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_94`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_95`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_96`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_97`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_98`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_99`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_100`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_101`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_102`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_103`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_104`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_105`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_106`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_107`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_108`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_109`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_110`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_111`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_112`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_113`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_114`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_115`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_116`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_117`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_118`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_119`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_120`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_121`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_122`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_123`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_124`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_125`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_126`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_127`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_128`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_129`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_130`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_131`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_132`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_133`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_134`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_135`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_136`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_137`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_138`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_139`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_140`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_141`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_142`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_143`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_144`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_145`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_146`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_147`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_148`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_149`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_150`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_151`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_152`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_153`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_154`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_155`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_156`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_157`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_158`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_159`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_160`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_161`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_162`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_163`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_164`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_165`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_166`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_167`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_168`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_169`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_170`  ;
                        

                        drop table  `mimic-four-377221.E4_Micro.VVVV_171`  ;
                        






'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
