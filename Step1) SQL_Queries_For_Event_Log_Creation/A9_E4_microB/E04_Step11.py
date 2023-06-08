import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            



##################################################################################
#query   Part 0 =


    
    
        create table `mimic-four-377221.E4_MicroB.HYT`    as
        SELECT distinct rowNum FROM `mimic-four-377221.E4_MicroB.Micro_C4`   ;
        
        
        

        alter table `mimic-four-377221.E4_MicroB.HYT` 
        ADD COLUMN ab_name_Syn string  ;
        
        
        alter table `mimic-four-377221.E4_MicroB.HYT` 
        ADD COLUMN interpretation_Syn INTEGER  ;


    
##################################################################################
#query   Part 1 =

###  0



            create table `mimic-four-377221.E4_MicroB.TTTT_1`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_1`   
            set ab_name_Syn  = "ab_00"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_1`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_1`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_1`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_1`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_1`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_00 
            from `mimic-four-377221.E4_MicroB.UUUU_1`     );


        
###  1



            create table `mimic-four-377221.E4_MicroB.TTTT_2`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_2`   
            set ab_name_Syn  = "ab_01"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_2`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_2`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_2`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_2`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_2`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_01 
            from `mimic-four-377221.E4_MicroB.UUUU_2`     );


        
###  2



            create table `mimic-four-377221.E4_MicroB.TTTT_3`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_3`   
            set ab_name_Syn  = "ab_02"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_3`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_3`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_3`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_3`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_3`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_02 
            from `mimic-four-377221.E4_MicroB.UUUU_3`     );


        
###  3



            create table `mimic-four-377221.E4_MicroB.TTTT_4`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_4`   
            set ab_name_Syn  = "ab_03"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_4`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_4`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_4`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_4`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_4`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_03 
            from `mimic-four-377221.E4_MicroB.UUUU_4`     );


        
###  4



            create table `mimic-four-377221.E4_MicroB.TTTT_5`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_5`   
            set ab_name_Syn  = "ab_04"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_5`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_5`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_5`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_5`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_5`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_04 
            from `mimic-four-377221.E4_MicroB.UUUU_5`     );


        
###  5



            create table `mimic-four-377221.E4_MicroB.TTTT_6`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_6`   
            set ab_name_Syn  = "ab_05"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_6`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_6`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_6`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_6`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_6`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_05 
            from `mimic-four-377221.E4_MicroB.UUUU_6`     );


        
###  6



            create table `mimic-four-377221.E4_MicroB.TTTT_7`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_7`   
            set ab_name_Syn  = "ab_06"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_7`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_7`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_7`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_7`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_7`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_06 
            from `mimic-four-377221.E4_MicroB.UUUU_7`     );


        
###  7



            create table `mimic-four-377221.E4_MicroB.TTTT_8`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_8`   
            set ab_name_Syn  = "ab_07"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_8`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_8`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_8`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_8`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_8`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_07 
            from `mimic-four-377221.E4_MicroB.UUUU_8`     );


        
###  8



            create table `mimic-four-377221.E4_MicroB.TTTT_9`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_9`   
            set ab_name_Syn  = "ab_08"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_9`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_9`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_9`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_9`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_9`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_08 
            from `mimic-four-377221.E4_MicroB.UUUU_9`     );


        
###  9



            create table `mimic-four-377221.E4_MicroB.TTTT_10`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_10`   
            set ab_name_Syn  = "ab_09"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_10`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_10`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_10`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_10`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_10`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_09 
            from `mimic-four-377221.E4_MicroB.UUUU_10`     );


        
###  10



            create table `mimic-four-377221.E4_MicroB.TTTT_11`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_11`   
            set ab_name_Syn  = "ab_10"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_11`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_11`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_11`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_11`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_11`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_10 
            from `mimic-four-377221.E4_MicroB.UUUU_11`     );


        
###  11



            create table `mimic-four-377221.E4_MicroB.TTTT_12`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_12`   
            set ab_name_Syn  = "ab_11"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_12`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_12`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_12`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_12`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_12`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_11 
            from `mimic-four-377221.E4_MicroB.UUUU_12`     );


        
###  12



            create table `mimic-four-377221.E4_MicroB.TTTT_13`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_13`   
            set ab_name_Syn  = "ab_12"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_13`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_13`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_13`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_13`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_13`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_12 
            from `mimic-four-377221.E4_MicroB.UUUU_13`     );


        
###  13



            create table `mimic-four-377221.E4_MicroB.TTTT_14`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_14`   
            set ab_name_Syn  = "ab_13"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_14`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_14`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_14`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_14`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_14`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_13 
            from `mimic-four-377221.E4_MicroB.UUUU_14`     );


        
###  14



            create table `mimic-four-377221.E4_MicroB.TTTT_15`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_15`   
            set ab_name_Syn  = "ab_14"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_15`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_15`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_15`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_15`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_15`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_14 
            from `mimic-four-377221.E4_MicroB.UUUU_15`     );


        
###  15



            create table `mimic-four-377221.E4_MicroB.TTTT_16`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_16`   
            set ab_name_Syn  = "ab_15"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_16`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_16`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_16`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_16`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_16`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_15 
            from `mimic-four-377221.E4_MicroB.UUUU_16`     );


        
###  16



            create table `mimic-four-377221.E4_MicroB.TTTT_17`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_17`   
            set ab_name_Syn  = "ab_16"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_17`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_17`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_17`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_17`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_17`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_16 
            from `mimic-four-377221.E4_MicroB.UUUU_17`     );


        
###  17



            create table `mimic-four-377221.E4_MicroB.TTTT_18`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_18`   
            set ab_name_Syn  = "ab_17"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_18`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_18`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_18`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_18`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_18`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_17 
            from `mimic-four-377221.E4_MicroB.UUUU_18`     );


        
###  18



            create table `mimic-four-377221.E4_MicroB.TTTT_19`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_19`   
            set ab_name_Syn  = "ab_18"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_19`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_19`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_19`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_19`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_19`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_18 
            from `mimic-four-377221.E4_MicroB.UUUU_19`     );


        
###  19



            create table `mimic-four-377221.E4_MicroB.TTTT_20`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_20`   
            set ab_name_Syn  = "ab_19"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_20`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_20`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_20`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_20`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_20`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_19 
            from `mimic-four-377221.E4_MicroB.UUUU_20`     );


        
###  20



            create table `mimic-four-377221.E4_MicroB.TTTT_21`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_21`   
            set ab_name_Syn  = "ab_20"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_21`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_21`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_21`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_21`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_21`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_20 
            from `mimic-four-377221.E4_MicroB.UUUU_21`     );


        
###  21



            create table `mimic-four-377221.E4_MicroB.TTTT_22`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_22`   
            set ab_name_Syn  = "ab_21"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_22`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_22`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_22`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_22`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_22`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_21 
            from `mimic-four-377221.E4_MicroB.UUUU_22`     );


        
###  22



            create table `mimic-four-377221.E4_MicroB.TTTT_23`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_23`   
            set ab_name_Syn  = "ab_22"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_23`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_23`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_23`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_23`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_23`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_22 
            from `mimic-four-377221.E4_MicroB.UUUU_23`     );


        
###  23



            create table `mimic-four-377221.E4_MicroB.TTTT_24`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_24`   
            set ab_name_Syn  = "ab_23"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_24`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_24`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_24`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_24`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_24`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_23 
            from `mimic-four-377221.E4_MicroB.UUUU_24`     );


        
###  24



            create table `mimic-four-377221.E4_MicroB.TTTT_25`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_25`   
            set ab_name_Syn  = "ab_24"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_25`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_25`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_25`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_25`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_25`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_24 
            from `mimic-four-377221.E4_MicroB.UUUU_25`     );


        
###  25



            create table `mimic-four-377221.E4_MicroB.TTTT_26`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_26`   
            set ab_name_Syn  = "ab_25"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_26`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_26`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_26`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_26`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_26`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_25 
            from `mimic-four-377221.E4_MicroB.UUUU_26`     );


        
###  26



            create table `mimic-four-377221.E4_MicroB.TTTT_27`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_27`   
            set ab_name_Syn  = "ab_26"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_27`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_27`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_27`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_27`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_27`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_26 
            from `mimic-four-377221.E4_MicroB.UUUU_27`     );


        
###  27



            create table `mimic-four-377221.E4_MicroB.TTTT_28`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_28`   
            set ab_name_Syn  = "ab_27"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_28`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_28`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_28`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_28`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_28`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_27 
            from `mimic-four-377221.E4_MicroB.UUUU_28`     );


        
###  28



            create table `mimic-four-377221.E4_MicroB.TTTT_29`    as
            SELECT * from `mimic-four-377221.E4_MicroB.HYT`    ;


            update `mimic-four-377221.E4_MicroB.TTTT_29`   
            set ab_name_Syn  = "ab_99"
            where ab_name_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.UUUU_29`    as (
            select 
            a.rowNum ,
            a.ab_name_Syn ,
            a.interpretation_Syn ,
            b.interpretation_Syn   as  Value_2
            from `mimic-four-377221.E4_MicroB.TTTT_29`    a 
            left join `mimic-four-377221.E4_MicroB.Micro_C4`    b
            on
            a.rowNum =b.rowNum 
            and
            a.ab_name_Syn =b.ab_name_Syn ) ;

            update `mimic-four-377221.E4_MicroB.UUUU_29`  
            set interpretation_Syn  = Value_2
            where interpretation_Syn  is null  ;

            update `mimic-four-377221.E4_MicroB.UUUU_29`  
            set interpretation_Syn  = 9
            where interpretation_Syn  is null  ;

            create table `mimic-four-377221.E4_MicroB.VVVV_29`    as (
            select 
            rowNum ,
            interpretation_Syn   as  ab_99 
            from `mimic-four-377221.E4_MicroB.UUUU_29`     );


        
##################################################################################
#query   Part 3 =


        create table `mimic-four-377221.E4_MicroB.Micro_C5`     as
        SELECT
        KKKK_1.rowNum,
        KKKK_1.ab_00, 
        KKKK_2.ab_01, 
        KKKK_3.ab_02, 
        KKKK_4.ab_03, 
        KKKK_5.ab_04, 
        KKKK_6.ab_05, 
        KKKK_7.ab_06, 
        KKKK_8.ab_07, 
        KKKK_9.ab_08, 
        KKKK_10.ab_09, 
        KKKK_11.ab_10, 
        KKKK_12.ab_11, 
        KKKK_13.ab_12, 
        KKKK_14.ab_13, 
        KKKK_15.ab_14, 
        KKKK_16.ab_15, 
        KKKK_17.ab_16, 
        KKKK_18.ab_17, 
        KKKK_19.ab_18, 
        KKKK_20.ab_19, 
        KKKK_21.ab_20, 
        KKKK_22.ab_21, 
        KKKK_23.ab_22, 
        KKKK_24.ab_23, 
        KKKK_25.ab_24, 
        KKKK_26.ab_25, 
        KKKK_27.ab_26, 
        KKKK_28.ab_27, 
        KKKK_29.ab_99 

        from `mimic-four-377221.E4_MicroB.VVVV_1`  as KKKK_1
    
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_2`  as KKKK_2
        on
        KKKK_1.rowNum=KKKK_2.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_3`  as KKKK_3
        on
        KKKK_1.rowNum=KKKK_3.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_4`  as KKKK_4
        on
        KKKK_1.rowNum=KKKK_4.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_5`  as KKKK_5
        on
        KKKK_1.rowNum=KKKK_5.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_6`  as KKKK_6
        on
        KKKK_1.rowNum=KKKK_6.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_7`  as KKKK_7
        on
        KKKK_1.rowNum=KKKK_7.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_8`  as KKKK_8
        on
        KKKK_1.rowNum=KKKK_8.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_9`  as KKKK_9
        on
        KKKK_1.rowNum=KKKK_9.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_10`  as KKKK_10
        on
        KKKK_1.rowNum=KKKK_10.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_11`  as KKKK_11
        on
        KKKK_1.rowNum=KKKK_11.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_12`  as KKKK_12
        on
        KKKK_1.rowNum=KKKK_12.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_13`  as KKKK_13
        on
        KKKK_1.rowNum=KKKK_13.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_14`  as KKKK_14
        on
        KKKK_1.rowNum=KKKK_14.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_15`  as KKKK_15
        on
        KKKK_1.rowNum=KKKK_15.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_16`  as KKKK_16
        on
        KKKK_1.rowNum=KKKK_16.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_17`  as KKKK_17
        on
        KKKK_1.rowNum=KKKK_17.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_18`  as KKKK_18
        on
        KKKK_1.rowNum=KKKK_18.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_19`  as KKKK_19
        on
        KKKK_1.rowNum=KKKK_19.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_20`  as KKKK_20
        on
        KKKK_1.rowNum=KKKK_20.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_21`  as KKKK_21
        on
        KKKK_1.rowNum=KKKK_21.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_22`  as KKKK_22
        on
        KKKK_1.rowNum=KKKK_22.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_23`  as KKKK_23
        on
        KKKK_1.rowNum=KKKK_23.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_24`  as KKKK_24
        on
        KKKK_1.rowNum=KKKK_24.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_25`  as KKKK_25
        on
        KKKK_1.rowNum=KKKK_25.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_26`  as KKKK_26
        on
        KKKK_1.rowNum=KKKK_26.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_27`  as KKKK_27
        on
        KKKK_1.rowNum=KKKK_27.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_28`  as KKKK_28
        on
        KKKK_1.rowNum=KKKK_28.rowNum
         
        left join 
        `mimic-four-377221.E4_MicroB.VVVV_29`  as KKKK_29
        on
        KKKK_1.rowNum=KKKK_29.rowNum
         
##################################################################################
#query   Part 4 =


    ;
                    drop table  `mimic-four-377221.E4_MicroB.HYT`  ;
                    

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_1`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_2`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_3`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_4`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_5`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_6`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_7`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_8`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_9`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_10`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_11`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_12`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_13`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_14`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_15`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_16`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_17`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_18`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_19`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_20`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_21`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_22`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_23`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_24`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_25`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_26`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_27`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_28`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.TTTT_29`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_1`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_2`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_3`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_4`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_5`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_6`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_7`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_8`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_9`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_10`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_11`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_12`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_13`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_14`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_15`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_16`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_17`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_18`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_19`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_20`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_21`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_22`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_23`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_24`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_25`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_26`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_27`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_28`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.UUUU_29`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_1`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_2`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_3`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_4`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_5`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_6`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_7`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_8`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_9`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_10`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_11`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_12`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_13`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_14`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_15`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_16`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_17`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_18`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_19`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_20`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_21`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_22`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_23`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_24`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_25`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_26`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_27`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_28`  ;
                        

                        drop table  `mimic-four-377221.E4_MicroB.VVVV_29`  ;
                        





'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
