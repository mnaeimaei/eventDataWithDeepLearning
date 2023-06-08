import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


##################################################################################
#query   Part 0 =




        create table `mimic-four-377221.P_NonEvents.HYT`    as
        SELECT distinct rowNum FROM `mimic-four-377221.P_NonEvents.K5`   ;




        alter table `mimic-four-377221.P_NonEvents.HYT` 
        ADD COLUMN icd_code_syn string  ;


        alter table `mimic-four-377221.P_NonEvents.HYT` 
        ADD COLUMN Value INTEGER  ;



##################################################################################
#query   Part 1 =

###  0



            create table `mimic-four-377221.P_NonEvents.TTTT_1`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_1`   
            set icd_code_syn  = "D01"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_1`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_1`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_1`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_1`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_1`    as (
            select 
            rowNum ,
            Value   as  D01 
            from `mimic-four-377221.P_NonEvents.UUUU_1`     );



###  1



            create table `mimic-four-377221.P_NonEvents.TTTT_2`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_2`   
            set icd_code_syn  = "D02"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_2`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_2`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_2`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_2`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_2`    as (
            select 
            rowNum ,
            Value   as  D02 
            from `mimic-four-377221.P_NonEvents.UUUU_2`     );



###  2



            create table `mimic-four-377221.P_NonEvents.TTTT_3`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_3`   
            set icd_code_syn  = "D03"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_3`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_3`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_3`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_3`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_3`    as (
            select 
            rowNum ,
            Value   as  D03 
            from `mimic-four-377221.P_NonEvents.UUUU_3`     );



###  3



            create table `mimic-four-377221.P_NonEvents.TTTT_4`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_4`   
            set icd_code_syn  = "D04"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_4`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_4`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_4`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_4`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_4`    as (
            select 
            rowNum ,
            Value   as  D04 
            from `mimic-four-377221.P_NonEvents.UUUU_4`     );



###  4



            create table `mimic-four-377221.P_NonEvents.TTTT_5`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_5`   
            set icd_code_syn  = "D05"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_5`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_5`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_5`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_5`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_5`    as (
            select 
            rowNum ,
            Value   as  D05 
            from `mimic-four-377221.P_NonEvents.UUUU_5`     );



###  5



            create table `mimic-four-377221.P_NonEvents.TTTT_6`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_6`   
            set icd_code_syn  = "D06"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_6`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_6`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_6`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_6`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_6`    as (
            select 
            rowNum ,
            Value   as  D06 
            from `mimic-four-377221.P_NonEvents.UUUU_6`     );



###  6



            create table `mimic-four-377221.P_NonEvents.TTTT_7`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_7`   
            set icd_code_syn  = "D07"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_7`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_7`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_7`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_7`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_7`    as (
            select 
            rowNum ,
            Value   as  D07 
            from `mimic-four-377221.P_NonEvents.UUUU_7`     );



###  7



            create table `mimic-four-377221.P_NonEvents.TTTT_8`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_8`   
            set icd_code_syn  = "D08"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_8`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_8`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_8`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_8`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_8`    as (
            select 
            rowNum ,
            Value   as  D08 
            from `mimic-four-377221.P_NonEvents.UUUU_8`     );



###  8



            create table `mimic-four-377221.P_NonEvents.TTTT_9`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_9`   
            set icd_code_syn  = "D09"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_9`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_9`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_9`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_9`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_9`    as (
            select 
            rowNum ,
            Value   as  D09 
            from `mimic-four-377221.P_NonEvents.UUUU_9`     );



###  9



            create table `mimic-four-377221.P_NonEvents.TTTT_10`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_10`   
            set icd_code_syn  = "D10"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_10`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_10`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_10`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_10`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_10`    as (
            select 
            rowNum ,
            Value   as  D10 
            from `mimic-four-377221.P_NonEvents.UUUU_10`     );



###  10



            create table `mimic-four-377221.P_NonEvents.TTTT_11`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_11`   
            set icd_code_syn  = "D11"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_11`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_11`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_11`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_11`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_11`    as (
            select 
            rowNum ,
            Value   as  D11 
            from `mimic-four-377221.P_NonEvents.UUUU_11`     );



###  11



            create table `mimic-four-377221.P_NonEvents.TTTT_12`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_12`   
            set icd_code_syn  = "D12"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_12`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_12`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_12`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_12`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_12`    as (
            select 
            rowNum ,
            Value   as  D12 
            from `mimic-four-377221.P_NonEvents.UUUU_12`     );



###  12



            create table `mimic-four-377221.P_NonEvents.TTTT_13`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_13`   
            set icd_code_syn  = "D13"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_13`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_13`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_13`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_13`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_13`    as (
            select 
            rowNum ,
            Value   as  D13 
            from `mimic-four-377221.P_NonEvents.UUUU_13`     );



###  13



            create table `mimic-four-377221.P_NonEvents.TTTT_14`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_14`   
            set icd_code_syn  = "D14"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_14`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_14`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_14`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_14`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_14`    as (
            select 
            rowNum ,
            Value   as  D14 
            from `mimic-four-377221.P_NonEvents.UUUU_14`     );



###  14



            create table `mimic-four-377221.P_NonEvents.TTTT_15`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_15`   
            set icd_code_syn  = "D15"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_15`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_15`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_15`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_15`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_15`    as (
            select 
            rowNum ,
            Value   as  D15 
            from `mimic-four-377221.P_NonEvents.UUUU_15`     );



###  15



            create table `mimic-four-377221.P_NonEvents.TTTT_16`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_16`   
            set icd_code_syn  = "D16"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_16`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_16`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_16`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_16`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_16`    as (
            select 
            rowNum ,
            Value   as  D16 
            from `mimic-four-377221.P_NonEvents.UUUU_16`     );



###  16



            create table `mimic-four-377221.P_NonEvents.TTTT_17`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_17`   
            set icd_code_syn  = "D17"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_17`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_17`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_17`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_17`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_17`    as (
            select 
            rowNum ,
            Value   as  D17 
            from `mimic-four-377221.P_NonEvents.UUUU_17`     );



###  17



            create table `mimic-four-377221.P_NonEvents.TTTT_18`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_18`   
            set icd_code_syn  = "D18"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_18`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_18`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_18`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_18`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_18`    as (
            select 
            rowNum ,
            Value   as  D18 
            from `mimic-four-377221.P_NonEvents.UUUU_18`     );



###  18



            create table `mimic-four-377221.P_NonEvents.TTTT_19`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_19`   
            set icd_code_syn  = "D19"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_19`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_19`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_19`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_19`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_19`    as (
            select 
            rowNum ,
            Value   as  D19 
            from `mimic-four-377221.P_NonEvents.UUUU_19`     );



###  19



            create table `mimic-four-377221.P_NonEvents.TTTT_20`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_20`   
            set icd_code_syn  = "D20"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_20`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_20`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_20`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_20`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_20`    as (
            select 
            rowNum ,
            Value   as  D20 
            from `mimic-four-377221.P_NonEvents.UUUU_20`     );



###  20



            create table `mimic-four-377221.P_NonEvents.TTTT_21`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_21`   
            set icd_code_syn  = "D21"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_21`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_21`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_21`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_21`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_21`    as (
            select 
            rowNum ,
            Value   as  D21 
            from `mimic-four-377221.P_NonEvents.UUUU_21`     );



###  21



            create table `mimic-four-377221.P_NonEvents.TTTT_22`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_22`   
            set icd_code_syn  = "D22"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_22`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_22`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_22`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_22`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_22`    as (
            select 
            rowNum ,
            Value   as  D22 
            from `mimic-four-377221.P_NonEvents.UUUU_22`     );



###  22



            create table `mimic-four-377221.P_NonEvents.TTTT_23`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_23`   
            set icd_code_syn  = "D23"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_23`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_23`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_23`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_23`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_23`    as (
            select 
            rowNum ,
            Value   as  D23 
            from `mimic-four-377221.P_NonEvents.UUUU_23`     );



###  23



            create table `mimic-four-377221.P_NonEvents.TTTT_24`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_24`   
            set icd_code_syn  = "D24"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_24`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_24`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_24`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_24`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_24`    as (
            select 
            rowNum ,
            Value   as  D24 
            from `mimic-four-377221.P_NonEvents.UUUU_24`     );



###  24



            create table `mimic-four-377221.P_NonEvents.TTTT_25`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_25`   
            set icd_code_syn  = "D25"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_25`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_25`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_25`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_25`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_25`    as (
            select 
            rowNum ,
            Value   as  D25 
            from `mimic-four-377221.P_NonEvents.UUUU_25`     );



###  25



            create table `mimic-four-377221.P_NonEvents.TTTT_26`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_26`   
            set icd_code_syn  = "D26"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_26`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_26`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_26`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_26`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_26`    as (
            select 
            rowNum ,
            Value   as  D26 
            from `mimic-four-377221.P_NonEvents.UUUU_26`     );



###  26



            create table `mimic-four-377221.P_NonEvents.TTTT_27`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_27`   
            set icd_code_syn  = "D27"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_27`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_27`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_27`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_27`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_27`    as (
            select 
            rowNum ,
            Value   as  D27 
            from `mimic-four-377221.P_NonEvents.UUUU_27`     );



###  27



            create table `mimic-four-377221.P_NonEvents.TTTT_28`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_28`   
            set icd_code_syn  = "D28"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_28`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_28`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_28`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_28`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_28`    as (
            select 
            rowNum ,
            Value   as  D28 
            from `mimic-four-377221.P_NonEvents.UUUU_28`     );



###  28



            create table `mimic-four-377221.P_NonEvents.TTTT_29`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_29`   
            set icd_code_syn  = "D29"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_29`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_29`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_29`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_29`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_29`    as (
            select 
            rowNum ,
            Value   as  D29 
            from `mimic-four-377221.P_NonEvents.UUUU_29`     );



###  29



            create table `mimic-four-377221.P_NonEvents.TTTT_30`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_30`   
            set icd_code_syn  = "D30"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_30`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_30`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_30`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_30`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_30`    as (
            select 
            rowNum ,
            Value   as  D30 
            from `mimic-four-377221.P_NonEvents.UUUU_30`     );



###  30



            create table `mimic-four-377221.P_NonEvents.TTTT_31`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_31`   
            set icd_code_syn  = "D31"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_31`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_31`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_31`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_31`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_31`    as (
            select 
            rowNum ,
            Value   as  D31 
            from `mimic-four-377221.P_NonEvents.UUUU_31`     );



###  31



            create table `mimic-four-377221.P_NonEvents.TTTT_32`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_32`   
            set icd_code_syn  = "D32"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_32`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_32`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_32`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_32`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_32`    as (
            select 
            rowNum ,
            Value   as  D32 
            from `mimic-four-377221.P_NonEvents.UUUU_32`     );



###  32



            create table `mimic-four-377221.P_NonEvents.TTTT_33`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_33`   
            set icd_code_syn  = "D33"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_33`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_33`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_33`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_33`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_33`    as (
            select 
            rowNum ,
            Value   as  D33 
            from `mimic-four-377221.P_NonEvents.UUUU_33`     );



###  33



            create table `mimic-four-377221.P_NonEvents.TTTT_34`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_34`   
            set icd_code_syn  = "D34"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_34`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_34`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_34`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_34`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_34`    as (
            select 
            rowNum ,
            Value   as  D34 
            from `mimic-four-377221.P_NonEvents.UUUU_34`     );



###  34



            create table `mimic-four-377221.P_NonEvents.TTTT_35`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_35`   
            set icd_code_syn  = "D35"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_35`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_35`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_35`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_35`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_35`    as (
            select 
            rowNum ,
            Value   as  D35 
            from `mimic-four-377221.P_NonEvents.UUUU_35`     );



###  35



            create table `mimic-four-377221.P_NonEvents.TTTT_36`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_36`   
            set icd_code_syn  = "D36"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_36`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_36`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_36`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_36`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_36`    as (
            select 
            rowNum ,
            Value   as  D36 
            from `mimic-four-377221.P_NonEvents.UUUU_36`     );



###  36



            create table `mimic-four-377221.P_NonEvents.TTTT_37`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_37`   
            set icd_code_syn  = "D37"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_37`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_37`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_37`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_37`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_37`    as (
            select 
            rowNum ,
            Value   as  D37 
            from `mimic-four-377221.P_NonEvents.UUUU_37`     );



###  37



            create table `mimic-four-377221.P_NonEvents.TTTT_38`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_38`   
            set icd_code_syn  = "D38"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_38`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_38`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_38`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_38`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_38`    as (
            select 
            rowNum ,
            Value   as  D38 
            from `mimic-four-377221.P_NonEvents.UUUU_38`     );



###  38



            create table `mimic-four-377221.P_NonEvents.TTTT_39`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_39`   
            set icd_code_syn  = "D39"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_39`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_39`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_39`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_39`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_39`    as (
            select 
            rowNum ,
            Value   as  D39 
            from `mimic-four-377221.P_NonEvents.UUUU_39`     );



###  39



            create table `mimic-four-377221.P_NonEvents.TTTT_40`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_40`   
            set icd_code_syn  = "D40"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_40`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_40`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_40`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_40`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_40`    as (
            select 
            rowNum ,
            Value   as  D40 
            from `mimic-four-377221.P_NonEvents.UUUU_40`     );



###  40



            create table `mimic-four-377221.P_NonEvents.TTTT_41`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_41`   
            set icd_code_syn  = "D41"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_41`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_41`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_41`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_41`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_41`    as (
            select 
            rowNum ,
            Value   as  D41 
            from `mimic-four-377221.P_NonEvents.UUUU_41`     );



###  41



            create table `mimic-four-377221.P_NonEvents.TTTT_42`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_42`   
            set icd_code_syn  = "D42"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_42`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_42`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_42`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_42`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_42`    as (
            select 
            rowNum ,
            Value   as  D42 
            from `mimic-four-377221.P_NonEvents.UUUU_42`     );



###  42



            create table `mimic-four-377221.P_NonEvents.TTTT_43`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_43`   
            set icd_code_syn  = "D43"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_43`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_43`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_43`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_43`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_43`    as (
            select 
            rowNum ,
            Value   as  D43 
            from `mimic-four-377221.P_NonEvents.UUUU_43`     );



###  43



            create table `mimic-four-377221.P_NonEvents.TTTT_44`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_44`   
            set icd_code_syn  = "D44"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_44`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_44`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_44`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_44`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_44`    as (
            select 
            rowNum ,
            Value   as  D44 
            from `mimic-four-377221.P_NonEvents.UUUU_44`     );



###  44



            create table `mimic-four-377221.P_NonEvents.TTTT_45`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_45`   
            set icd_code_syn  = "D45"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_45`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_45`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_45`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_45`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_45`    as (
            select 
            rowNum ,
            Value   as  D45 
            from `mimic-four-377221.P_NonEvents.UUUU_45`     );



###  45



            create table `mimic-four-377221.P_NonEvents.TTTT_46`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_46`   
            set icd_code_syn  = "D46"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_46`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_46`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_46`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_46`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_46`    as (
            select 
            rowNum ,
            Value   as  D46 
            from `mimic-four-377221.P_NonEvents.UUUU_46`     );



###  46



            create table `mimic-four-377221.P_NonEvents.TTTT_47`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_47`   
            set icd_code_syn  = "D47"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_47`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_47`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_47`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_47`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_47`    as (
            select 
            rowNum ,
            Value   as  D47 
            from `mimic-four-377221.P_NonEvents.UUUU_47`     );



###  47



            create table `mimic-four-377221.P_NonEvents.TTTT_48`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_48`   
            set icd_code_syn  = "D48"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_48`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_48`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_48`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_48`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_48`    as (
            select 
            rowNum ,
            Value   as  D48 
            from `mimic-four-377221.P_NonEvents.UUUU_48`     );



###  48



            create table `mimic-four-377221.P_NonEvents.TTTT_49`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_49`   
            set icd_code_syn  = "D49"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_49`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_49`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_49`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_49`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_49`    as (
            select 
            rowNum ,
            Value   as  D49 
            from `mimic-four-377221.P_NonEvents.UUUU_49`     );



###  49



            create table `mimic-four-377221.P_NonEvents.TTTT_50`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_50`   
            set icd_code_syn  = "D50"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_50`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_50`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_50`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_50`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_50`    as (
            select 
            rowNum ,
            Value   as  D50 
            from `mimic-four-377221.P_NonEvents.UUUU_50`     );



###  50



            create table `mimic-four-377221.P_NonEvents.TTTT_51`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_51`   
            set icd_code_syn  = "D51"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_51`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_51`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_51`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_51`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_51`    as (
            select 
            rowNum ,
            Value   as  D51 
            from `mimic-four-377221.P_NonEvents.UUUU_51`     );



###  51



            create table `mimic-four-377221.P_NonEvents.TTTT_52`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_52`   
            set icd_code_syn  = "D52"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_52`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_52`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_52`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_52`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_52`    as (
            select 
            rowNum ,
            Value   as  D52 
            from `mimic-four-377221.P_NonEvents.UUUU_52`     );



###  52



            create table `mimic-four-377221.P_NonEvents.TTTT_53`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_53`   
            set icd_code_syn  = "D53"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_53`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_53`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_53`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_53`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_53`    as (
            select 
            rowNum ,
            Value   as  D53 
            from `mimic-four-377221.P_NonEvents.UUUU_53`     );



###  53



            create table `mimic-four-377221.P_NonEvents.TTTT_54`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_54`   
            set icd_code_syn  = "D54"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_54`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_54`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_54`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_54`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_54`    as (
            select 
            rowNum ,
            Value   as  D54 
            from `mimic-four-377221.P_NonEvents.UUUU_54`     );



###  54



            create table `mimic-four-377221.P_NonEvents.TTTT_55`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_55`   
            set icd_code_syn  = "D55"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_55`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_55`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_55`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_55`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_55`    as (
            select 
            rowNum ,
            Value   as  D55 
            from `mimic-four-377221.P_NonEvents.UUUU_55`     );



###  55



            create table `mimic-four-377221.P_NonEvents.TTTT_56`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_56`   
            set icd_code_syn  = "D56"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_56`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_56`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_56`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_56`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_56`    as (
            select 
            rowNum ,
            Value   as  D56 
            from `mimic-four-377221.P_NonEvents.UUUU_56`     );



###  56



            create table `mimic-four-377221.P_NonEvents.TTTT_57`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_57`   
            set icd_code_syn  = "D57"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_57`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_57`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_57`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_57`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_57`    as (
            select 
            rowNum ,
            Value   as  D57 
            from `mimic-four-377221.P_NonEvents.UUUU_57`     );



###  57



            create table `mimic-four-377221.P_NonEvents.TTTT_58`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_58`   
            set icd_code_syn  = "D58"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_58`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_58`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_58`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_58`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_58`    as (
            select 
            rowNum ,
            Value   as  D58 
            from `mimic-four-377221.P_NonEvents.UUUU_58`     );



###  58



            create table `mimic-four-377221.P_NonEvents.TTTT_59`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_59`   
            set icd_code_syn  = "D59"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_59`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_59`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_59`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_59`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_59`    as (
            select 
            rowNum ,
            Value   as  D59 
            from `mimic-four-377221.P_NonEvents.UUUU_59`     );



###  59



            create table `mimic-four-377221.P_NonEvents.TTTT_60`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_60`   
            set icd_code_syn  = "D60"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_60`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_60`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_60`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_60`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_60`    as (
            select 
            rowNum ,
            Value   as  D60 
            from `mimic-four-377221.P_NonEvents.UUUU_60`     );



###  60



            create table `mimic-four-377221.P_NonEvents.TTTT_61`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_61`   
            set icd_code_syn  = "D61"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_61`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_61`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_61`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_61`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_61`    as (
            select 
            rowNum ,
            Value   as  D61 
            from `mimic-four-377221.P_NonEvents.UUUU_61`     );



###  61



            create table `mimic-four-377221.P_NonEvents.TTTT_62`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_62`   
            set icd_code_syn  = "D62"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_62`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_62`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_62`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_62`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_62`    as (
            select 
            rowNum ,
            Value   as  D62 
            from `mimic-four-377221.P_NonEvents.UUUU_62`     );



###  62



            create table `mimic-four-377221.P_NonEvents.TTTT_63`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_63`   
            set icd_code_syn  = "D63"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_63`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_63`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_63`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_63`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_63`    as (
            select 
            rowNum ,
            Value   as  D63 
            from `mimic-four-377221.P_NonEvents.UUUU_63`     );



###  63



            create table `mimic-four-377221.P_NonEvents.TTTT_64`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_64`   
            set icd_code_syn  = "D64"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_64`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_64`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_64`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_64`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_64`    as (
            select 
            rowNum ,
            Value   as  D64 
            from `mimic-four-377221.P_NonEvents.UUUU_64`     );



###  64



            create table `mimic-four-377221.P_NonEvents.TTTT_65`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_65`   
            set icd_code_syn  = "D65"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_65`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_65`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_65`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_65`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_65`    as (
            select 
            rowNum ,
            Value   as  D65 
            from `mimic-four-377221.P_NonEvents.UUUU_65`     );



###  65



            create table `mimic-four-377221.P_NonEvents.TTTT_66`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_66`   
            set icd_code_syn  = "D66"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_66`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_66`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_66`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_66`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_66`    as (
            select 
            rowNum ,
            Value   as  D66 
            from `mimic-four-377221.P_NonEvents.UUUU_66`     );



###  66



            create table `mimic-four-377221.P_NonEvents.TTTT_67`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_67`   
            set icd_code_syn  = "D67"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_67`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_67`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_67`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_67`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_67`    as (
            select 
            rowNum ,
            Value   as  D67 
            from `mimic-four-377221.P_NonEvents.UUUU_67`     );



###  67



            create table `mimic-four-377221.P_NonEvents.TTTT_68`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_68`   
            set icd_code_syn  = "D68"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_68`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_68`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_68`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_68`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_68`    as (
            select 
            rowNum ,
            Value   as  D68 
            from `mimic-four-377221.P_NonEvents.UUUU_68`     );



###  68



            create table `mimic-four-377221.P_NonEvents.TTTT_69`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_69`   
            set icd_code_syn  = "D69"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_69`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_69`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_69`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_69`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_69`    as (
            select 
            rowNum ,
            Value   as  D69 
            from `mimic-four-377221.P_NonEvents.UUUU_69`     );



###  69



            create table `mimic-four-377221.P_NonEvents.TTTT_70`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_70`   
            set icd_code_syn  = "D70"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_70`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_70`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_70`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_70`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_70`    as (
            select 
            rowNum ,
            Value   as  D70 
            from `mimic-four-377221.P_NonEvents.UUUU_70`     );



###  70



            create table `mimic-four-377221.P_NonEvents.TTTT_71`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_71`   
            set icd_code_syn  = "D71"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_71`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_71`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_71`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_71`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_71`    as (
            select 
            rowNum ,
            Value   as  D71 
            from `mimic-four-377221.P_NonEvents.UUUU_71`     );



###  71



            create table `mimic-four-377221.P_NonEvents.TTTT_72`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_72`   
            set icd_code_syn  = "D72"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_72`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_72`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_72`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_72`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_72`    as (
            select 
            rowNum ,
            Value   as  D72 
            from `mimic-four-377221.P_NonEvents.UUUU_72`     );



###  72



            create table `mimic-four-377221.P_NonEvents.TTTT_73`    as
            SELECT * from `mimic-four-377221.P_NonEvents.HYT`    ;


            update `mimic-four-377221.P_NonEvents.TTTT_73`   
            set icd_code_syn  = "D73"
            where icd_code_syn  is null  ;

            create table `mimic-four-377221.P_NonEvents.UUUU_73`    as (
            select 
            a.rowNum ,
            a.icd_code_syn ,
            a.Value ,
            b.Value   as  Value_2
            from `mimic-four-377221.P_NonEvents.TTTT_73`    a 
            left join `mimic-four-377221.P_NonEvents.K5`    b
            on
            a.rowNum =b.rowNum 
            and
            a.icd_code_syn =b.icd_code_syn ) ;

            update `mimic-four-377221.P_NonEvents.UUUU_73`  
            set Value  = Value_2
            where Value  is null  ;

            update `mimic-four-377221.P_NonEvents.UUUU_73`  
            set Value  = 0
            where Value  is null  ;

            create table `mimic-four-377221.P_NonEvents.VVVV_73`    as (
            select 
            rowNum ,
            Value   as  D73 
            from `mimic-four-377221.P_NonEvents.UUUU_73`     );



##################################################################################
#query   Part 3 =


        create table `mimic-four-377221.P_NonEvents.K6`     as
        SELECT
        KKKK_1.rowNum,
        KKKK_1.D01, 
        KKKK_2.D02, 
        KKKK_3.D03, 
        KKKK_4.D04, 
        KKKK_5.D05, 
        KKKK_6.D06, 
        KKKK_7.D07, 
        KKKK_8.D08, 
        KKKK_9.D09, 
        KKKK_10.D10, 
        KKKK_11.D11, 
        KKKK_12.D12, 
        KKKK_13.D13, 
        KKKK_14.D14, 
        KKKK_15.D15, 
        KKKK_16.D16, 
        KKKK_17.D17, 
        KKKK_18.D18, 
        KKKK_19.D19, 
        KKKK_20.D20, 
        KKKK_21.D21, 
        KKKK_22.D22, 
        KKKK_23.D23, 
        KKKK_24.D24, 
        KKKK_25.D25, 
        KKKK_26.D26, 
        KKKK_27.D27, 
        KKKK_28.D28, 
        KKKK_29.D29, 
        KKKK_30.D30, 
        KKKK_31.D31, 
        KKKK_32.D32, 
        KKKK_33.D33, 
        KKKK_34.D34, 
        KKKK_35.D35, 
        KKKK_36.D36, 
        KKKK_37.D37, 
        KKKK_38.D38, 
        KKKK_39.D39, 
        KKKK_40.D40, 
        KKKK_41.D41, 
        KKKK_42.D42, 
        KKKK_43.D43, 
        KKKK_44.D44, 
        KKKK_45.D45, 
        KKKK_46.D46, 
        KKKK_47.D47, 
        KKKK_48.D48, 
        KKKK_49.D49, 
        KKKK_50.D50, 
        KKKK_51.D51, 
        KKKK_52.D52, 
        KKKK_53.D53, 
        KKKK_54.D54, 
        KKKK_55.D55, 
        KKKK_56.D56, 
        KKKK_57.D57, 
        KKKK_58.D58, 
        KKKK_59.D59, 
        KKKK_60.D60, 
        KKKK_61.D61, 
        KKKK_62.D62, 
        KKKK_63.D63, 
        KKKK_64.D64, 
        KKKK_65.D65, 
        KKKK_66.D66, 
        KKKK_67.D67, 
        KKKK_68.D68, 
        KKKK_69.D69, 
        KKKK_70.D70, 
        KKKK_71.D71, 
        KKKK_72.D72, 
        KKKK_73.D73 

        from `mimic-four-377221.P_NonEvents.VVVV_1`  as KKKK_1

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_2`  as KKKK_2
        on
        KKKK_1.rowNum=KKKK_2.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_3`  as KKKK_3
        on
        KKKK_1.rowNum=KKKK_3.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_4`  as KKKK_4
        on
        KKKK_1.rowNum=KKKK_4.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_5`  as KKKK_5
        on
        KKKK_1.rowNum=KKKK_5.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_6`  as KKKK_6
        on
        KKKK_1.rowNum=KKKK_6.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_7`  as KKKK_7
        on
        KKKK_1.rowNum=KKKK_7.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_8`  as KKKK_8
        on
        KKKK_1.rowNum=KKKK_8.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_9`  as KKKK_9
        on
        KKKK_1.rowNum=KKKK_9.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_10`  as KKKK_10
        on
        KKKK_1.rowNum=KKKK_10.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_11`  as KKKK_11
        on
        KKKK_1.rowNum=KKKK_11.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_12`  as KKKK_12
        on
        KKKK_1.rowNum=KKKK_12.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_13`  as KKKK_13
        on
        KKKK_1.rowNum=KKKK_13.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_14`  as KKKK_14
        on
        KKKK_1.rowNum=KKKK_14.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_15`  as KKKK_15
        on
        KKKK_1.rowNum=KKKK_15.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_16`  as KKKK_16
        on
        KKKK_1.rowNum=KKKK_16.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_17`  as KKKK_17
        on
        KKKK_1.rowNum=KKKK_17.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_18`  as KKKK_18
        on
        KKKK_1.rowNum=KKKK_18.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_19`  as KKKK_19
        on
        KKKK_1.rowNum=KKKK_19.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_20`  as KKKK_20
        on
        KKKK_1.rowNum=KKKK_20.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_21`  as KKKK_21
        on
        KKKK_1.rowNum=KKKK_21.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_22`  as KKKK_22
        on
        KKKK_1.rowNum=KKKK_22.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_23`  as KKKK_23
        on
        KKKK_1.rowNum=KKKK_23.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_24`  as KKKK_24
        on
        KKKK_1.rowNum=KKKK_24.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_25`  as KKKK_25
        on
        KKKK_1.rowNum=KKKK_25.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_26`  as KKKK_26
        on
        KKKK_1.rowNum=KKKK_26.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_27`  as KKKK_27
        on
        KKKK_1.rowNum=KKKK_27.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_28`  as KKKK_28
        on
        KKKK_1.rowNum=KKKK_28.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_29`  as KKKK_29
        on
        KKKK_1.rowNum=KKKK_29.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_30`  as KKKK_30
        on
        KKKK_1.rowNum=KKKK_30.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_31`  as KKKK_31
        on
        KKKK_1.rowNum=KKKK_31.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_32`  as KKKK_32
        on
        KKKK_1.rowNum=KKKK_32.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_33`  as KKKK_33
        on
        KKKK_1.rowNum=KKKK_33.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_34`  as KKKK_34
        on
        KKKK_1.rowNum=KKKK_34.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_35`  as KKKK_35
        on
        KKKK_1.rowNum=KKKK_35.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_36`  as KKKK_36
        on
        KKKK_1.rowNum=KKKK_36.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_37`  as KKKK_37
        on
        KKKK_1.rowNum=KKKK_37.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_38`  as KKKK_38
        on
        KKKK_1.rowNum=KKKK_38.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_39`  as KKKK_39
        on
        KKKK_1.rowNum=KKKK_39.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_40`  as KKKK_40
        on
        KKKK_1.rowNum=KKKK_40.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_41`  as KKKK_41
        on
        KKKK_1.rowNum=KKKK_41.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_42`  as KKKK_42
        on
        KKKK_1.rowNum=KKKK_42.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_43`  as KKKK_43
        on
        KKKK_1.rowNum=KKKK_43.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_44`  as KKKK_44
        on
        KKKK_1.rowNum=KKKK_44.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_45`  as KKKK_45
        on
        KKKK_1.rowNum=KKKK_45.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_46`  as KKKK_46
        on
        KKKK_1.rowNum=KKKK_46.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_47`  as KKKK_47
        on
        KKKK_1.rowNum=KKKK_47.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_48`  as KKKK_48
        on
        KKKK_1.rowNum=KKKK_48.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_49`  as KKKK_49
        on
        KKKK_1.rowNum=KKKK_49.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_50`  as KKKK_50
        on
        KKKK_1.rowNum=KKKK_50.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_51`  as KKKK_51
        on
        KKKK_1.rowNum=KKKK_51.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_52`  as KKKK_52
        on
        KKKK_1.rowNum=KKKK_52.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_53`  as KKKK_53
        on
        KKKK_1.rowNum=KKKK_53.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_54`  as KKKK_54
        on
        KKKK_1.rowNum=KKKK_54.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_55`  as KKKK_55
        on
        KKKK_1.rowNum=KKKK_55.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_56`  as KKKK_56
        on
        KKKK_1.rowNum=KKKK_56.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_57`  as KKKK_57
        on
        KKKK_1.rowNum=KKKK_57.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_58`  as KKKK_58
        on
        KKKK_1.rowNum=KKKK_58.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_59`  as KKKK_59
        on
        KKKK_1.rowNum=KKKK_59.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_60`  as KKKK_60
        on
        KKKK_1.rowNum=KKKK_60.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_61`  as KKKK_61
        on
        KKKK_1.rowNum=KKKK_61.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_62`  as KKKK_62
        on
        KKKK_1.rowNum=KKKK_62.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_63`  as KKKK_63
        on
        KKKK_1.rowNum=KKKK_63.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_64`  as KKKK_64
        on
        KKKK_1.rowNum=KKKK_64.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_65`  as KKKK_65
        on
        KKKK_1.rowNum=KKKK_65.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_66`  as KKKK_66
        on
        KKKK_1.rowNum=KKKK_66.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_67`  as KKKK_67
        on
        KKKK_1.rowNum=KKKK_67.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_68`  as KKKK_68
        on
        KKKK_1.rowNum=KKKK_68.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_69`  as KKKK_69
        on
        KKKK_1.rowNum=KKKK_69.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_70`  as KKKK_70
        on
        KKKK_1.rowNum=KKKK_70.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_71`  as KKKK_71
        on
        KKKK_1.rowNum=KKKK_71.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_72`  as KKKK_72
        on
        KKKK_1.rowNum=KKKK_72.rowNum

        left join 
        `mimic-four-377221.P_NonEvents.VVVV_73`  as KKKK_73
        on
        KKKK_1.rowNum=KKKK_73.rowNum

##################################################################################
#query   Part 4 =


    ;
                    drop table  `mimic-four-377221.P_NonEvents.HYT`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_1`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_2`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_3`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_4`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_5`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_6`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_7`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_8`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_9`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_10`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_11`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_12`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_13`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_14`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_15`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_16`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_17`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_18`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_19`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_20`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_21`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_22`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_23`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_24`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_25`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_26`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_27`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_28`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_29`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_30`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_31`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_32`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_33`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_34`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_35`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_36`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_37`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_38`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_39`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_40`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_41`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_42`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_43`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_44`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_45`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_46`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_47`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_48`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_49`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_50`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_51`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_52`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_53`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_54`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_55`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_56`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_57`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_58`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_59`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_60`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_61`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_62`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_63`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_64`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_65`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_66`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_67`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_68`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_69`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_70`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_71`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_72`  ;


                        drop table  `mimic-four-377221.P_NonEvents.TTTT_73`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_1`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_2`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_3`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_4`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_5`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_6`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_7`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_8`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_9`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_10`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_11`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_12`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_13`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_14`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_15`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_16`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_17`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_18`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_19`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_20`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_21`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_22`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_23`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_24`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_25`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_26`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_27`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_28`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_29`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_30`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_31`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_32`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_33`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_34`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_35`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_36`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_37`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_38`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_39`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_40`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_41`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_42`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_43`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_44`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_45`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_46`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_47`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_48`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_49`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_50`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_51`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_52`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_53`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_54`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_55`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_56`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_57`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_58`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_59`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_60`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_61`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_62`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_63`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_64`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_65`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_66`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_67`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_68`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_69`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_70`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_71`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_72`  ;


                        drop table  `mimic-four-377221.P_NonEvents.UUUU_73`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_1`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_2`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_3`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_4`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_5`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_6`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_7`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_8`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_9`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_10`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_11`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_12`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_13`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_14`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_15`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_16`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_17`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_18`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_19`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_20`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_21`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_22`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_23`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_24`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_25`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_26`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_27`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_28`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_29`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_30`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_31`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_32`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_33`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_34`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_35`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_36`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_37`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_38`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_39`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_40`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_41`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_42`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_43`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_44`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_45`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_46`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_47`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_48`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_49`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_50`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_51`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_52`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_53`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_54`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_55`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_56`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_57`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_58`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_59`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_60`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_61`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_62`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_63`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_64`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_65`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_66`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_67`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_68`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_69`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_70`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_71`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_72`  ;


                        drop table  `mimic-four-377221.P_NonEvents.VVVV_73`  ;






'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
