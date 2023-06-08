import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            






        create table `mimic-four-377221.E6_BloodGas.HYT`    as
        SELECT distinct rowNum FROM `mimic-four-377221.E6_BloodGas.bgA6`   ;




        alter table `mimic-four-377221.E6_BloodGas.HYT` 
        ADD COLUMN Label_Syn string  ;


        alter table `mimic-four-377221.E6_BloodGas.HYT` 
        ADD COLUMN Value_Int INTEGER  ;



##################################################################################
#query   Part 1 =

###  0



            create table `mimic-four-377221.E6_BloodGas.TTTT_1`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_1`   
            set Label_Syn  = "Item1"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_1`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_1`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_1`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_1`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_1`    as (
            select 
            rowNum ,
            Value_Int   as  Item1 
            from `mimic-four-377221.E6_BloodGas.UUUU_1`     );



###  1



            create table `mimic-four-377221.E6_BloodGas.TTTT_2`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_2`   
            set Label_Syn  = "Item2"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_2`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_2`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_2`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_2`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_2`    as (
            select 
            rowNum ,
            Value_Int   as  Item2 
            from `mimic-four-377221.E6_BloodGas.UUUU_2`     );



###  2



            create table `mimic-four-377221.E6_BloodGas.TTTT_3`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_3`   
            set Label_Syn  = "Item3"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_3`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_3`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_3`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_3`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_3`    as (
            select 
            rowNum ,
            Value_Int   as  Item3 
            from `mimic-four-377221.E6_BloodGas.UUUU_3`     );



###  3



            create table `mimic-four-377221.E6_BloodGas.TTTT_4`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_4`   
            set Label_Syn  = "Item4"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_4`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_4`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_4`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_4`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_4`    as (
            select 
            rowNum ,
            Value_Int   as  Item4 
            from `mimic-four-377221.E6_BloodGas.UUUU_4`     );



###  4



            create table `mimic-four-377221.E6_BloodGas.TTTT_5`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_5`   
            set Label_Syn  = "Item5"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_5`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_5`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_5`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_5`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_5`    as (
            select 
            rowNum ,
            Value_Int   as  Item5 
            from `mimic-four-377221.E6_BloodGas.UUUU_5`     );



###  5



            create table `mimic-four-377221.E6_BloodGas.TTTT_6`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_6`   
            set Label_Syn  = "Item6"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_6`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_6`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_6`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_6`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_6`    as (
            select 
            rowNum ,
            Value_Int   as  Item6 
            from `mimic-four-377221.E6_BloodGas.UUUU_6`     );



###  6



            create table `mimic-four-377221.E6_BloodGas.TTTT_7`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_7`   
            set Label_Syn  = "Item7"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_7`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_7`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_7`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_7`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_7`    as (
            select 
            rowNum ,
            Value_Int   as  Item7 
            from `mimic-four-377221.E6_BloodGas.UUUU_7`     );



###  7



            create table `mimic-four-377221.E6_BloodGas.TTTT_8`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_8`   
            set Label_Syn  = "Item8"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_8`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_8`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_8`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_8`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_8`    as (
            select 
            rowNum ,
            Value_Int   as  Item8 
            from `mimic-four-377221.E6_BloodGas.UUUU_8`     );



###  8



            create table `mimic-four-377221.E6_BloodGas.TTTT_9`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_9`   
            set Label_Syn  = "Item9"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_9`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_9`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_9`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_9`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_9`    as (
            select 
            rowNum ,
            Value_Int   as  Item9 
            from `mimic-four-377221.E6_BloodGas.UUUU_9`     );



###  9



            create table `mimic-four-377221.E6_BloodGas.TTTT_10`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_10`   
            set Label_Syn  = "Item10"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_10`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_10`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_10`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_10`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_10`    as (
            select 
            rowNum ,
            Value_Int   as  Item10 
            from `mimic-four-377221.E6_BloodGas.UUUU_10`     );



###  10



            create table `mimic-four-377221.E6_BloodGas.TTTT_11`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_11`   
            set Label_Syn  = "Item11"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_11`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_11`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_11`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_11`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_11`    as (
            select 
            rowNum ,
            Value_Int   as  Item11 
            from `mimic-four-377221.E6_BloodGas.UUUU_11`     );



###  11



            create table `mimic-four-377221.E6_BloodGas.TTTT_12`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_12`   
            set Label_Syn  = "Item12"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_12`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_12`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_12`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_12`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_12`    as (
            select 
            rowNum ,
            Value_Int   as  Item12 
            from `mimic-four-377221.E6_BloodGas.UUUU_12`     );



###  12



            create table `mimic-four-377221.E6_BloodGas.TTTT_13`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_13`   
            set Label_Syn  = "Item13"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_13`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_13`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_13`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_13`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_13`    as (
            select 
            rowNum ,
            Value_Int   as  Item13 
            from `mimic-four-377221.E6_BloodGas.UUUU_13`     );



###  13



            create table `mimic-four-377221.E6_BloodGas.TTTT_14`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_14`   
            set Label_Syn  = "Item14"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_14`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_14`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_14`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_14`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_14`    as (
            select 
            rowNum ,
            Value_Int   as  Item14 
            from `mimic-four-377221.E6_BloodGas.UUUU_14`     );



###  14



            create table `mimic-four-377221.E6_BloodGas.TTTT_15`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_15`   
            set Label_Syn  = "Item15"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_15`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_15`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_15`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_15`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_15`    as (
            select 
            rowNum ,
            Value_Int   as  Item15 
            from `mimic-four-377221.E6_BloodGas.UUUU_15`     );



###  15



            create table `mimic-four-377221.E6_BloodGas.TTTT_16`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_16`   
            set Label_Syn  = "Item16"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_16`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_16`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_16`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_16`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_16`    as (
            select 
            rowNum ,
            Value_Int   as  Item16 
            from `mimic-four-377221.E6_BloodGas.UUUU_16`     );



###  16



            create table `mimic-four-377221.E6_BloodGas.TTTT_17`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_17`   
            set Label_Syn  = "Item17"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_17`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_17`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_17`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_17`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_17`    as (
            select 
            rowNum ,
            Value_Int   as  Item17 
            from `mimic-four-377221.E6_BloodGas.UUUU_17`     );



###  17



            create table `mimic-four-377221.E6_BloodGas.TTTT_18`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_18`   
            set Label_Syn  = "Item18"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_18`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_18`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_18`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_18`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_18`    as (
            select 
            rowNum ,
            Value_Int   as  Item18 
            from `mimic-four-377221.E6_BloodGas.UUUU_18`     );



###  18



            create table `mimic-four-377221.E6_BloodGas.TTTT_19`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_19`   
            set Label_Syn  = "Item19"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_19`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_19`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_19`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_19`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_19`    as (
            select 
            rowNum ,
            Value_Int   as  Item19 
            from `mimic-four-377221.E6_BloodGas.UUUU_19`     );



###  19



            create table `mimic-four-377221.E6_BloodGas.TTTT_20`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_20`   
            set Label_Syn  = "Item20"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_20`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_20`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_20`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_20`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_20`    as (
            select 
            rowNum ,
            Value_Int   as  Item20 
            from `mimic-four-377221.E6_BloodGas.UUUU_20`     );



###  20



            create table `mimic-four-377221.E6_BloodGas.TTTT_21`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_21`   
            set Label_Syn  = "Item21"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_21`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_21`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_21`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_21`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_21`    as (
            select 
            rowNum ,
            Value_Int   as  Item21 
            from `mimic-four-377221.E6_BloodGas.UUUU_21`     );



###  21



            create table `mimic-four-377221.E6_BloodGas.TTTT_22`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_22`   
            set Label_Syn  = "Item22"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_22`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_22`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_22`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_22`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_22`    as (
            select 
            rowNum ,
            Value_Int   as  Item22 
            from `mimic-four-377221.E6_BloodGas.UUUU_22`     );



###  22



            create table `mimic-four-377221.E6_BloodGas.TTTT_23`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_23`   
            set Label_Syn  = "Item23"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_23`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_23`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_23`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_23`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_23`    as (
            select 
            rowNum ,
            Value_Int   as  Item23 
            from `mimic-four-377221.E6_BloodGas.UUUU_23`     );



###  23



            create table `mimic-four-377221.E6_BloodGas.TTTT_24`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_24`   
            set Label_Syn  = "Item24"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_24`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_24`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_24`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_24`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_24`    as (
            select 
            rowNum ,
            Value_Int   as  Item24 
            from `mimic-four-377221.E6_BloodGas.UUUU_24`     );



###  24



            create table `mimic-four-377221.E6_BloodGas.TTTT_25`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_25`   
            set Label_Syn  = "Item25"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_25`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_25`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_25`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_25`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_25`    as (
            select 
            rowNum ,
            Value_Int   as  Item25 
            from `mimic-four-377221.E6_BloodGas.UUUU_25`     );



###  25



            create table `mimic-four-377221.E6_BloodGas.TTTT_26`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_26`   
            set Label_Syn  = "Item26"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_26`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_26`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_26`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_26`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_26`    as (
            select 
            rowNum ,
            Value_Int   as  Item26 
            from `mimic-four-377221.E6_BloodGas.UUUU_26`     );



###  26



            create table `mimic-four-377221.E6_BloodGas.TTTT_27`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_27`   
            set Label_Syn  = "Item27"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_27`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_27`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_27`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_27`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_27`    as (
            select 
            rowNum ,
            Value_Int   as  Item27 
            from `mimic-four-377221.E6_BloodGas.UUUU_27`     );



###  27



            create table `mimic-four-377221.E6_BloodGas.TTTT_28`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_28`   
            set Label_Syn  = "Item28"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_28`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_28`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_28`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_28`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_28`    as (
            select 
            rowNum ,
            Value_Int   as  Item28 
            from `mimic-four-377221.E6_BloodGas.UUUU_28`     );



###  28



            create table `mimic-four-377221.E6_BloodGas.TTTT_29`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_29`   
            set Label_Syn  = "Item29"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_29`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_29`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_29`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_29`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_29`    as (
            select 
            rowNum ,
            Value_Int   as  Item29 
            from `mimic-four-377221.E6_BloodGas.UUUU_29`     );



###  29



            create table `mimic-four-377221.E6_BloodGas.TTTT_30`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_30`   
            set Label_Syn  = "Item30"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_30`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_30`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_30`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_30`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_30`    as (
            select 
            rowNum ,
            Value_Int   as  Item30 
            from `mimic-four-377221.E6_BloodGas.UUUU_30`     );



###  30



            create table `mimic-four-377221.E6_BloodGas.TTTT_31`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_31`   
            set Label_Syn  = "Item31"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_31`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_31`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_31`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_31`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_31`    as (
            select 
            rowNum ,
            Value_Int   as  Item31 
            from `mimic-four-377221.E6_BloodGas.UUUU_31`     );



###  31



            create table `mimic-four-377221.E6_BloodGas.TTTT_32`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_32`   
            set Label_Syn  = "Item32"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_32`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_32`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_32`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_32`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_32`    as (
            select 
            rowNum ,
            Value_Int   as  Item32 
            from `mimic-four-377221.E6_BloodGas.UUUU_32`     );



###  32



            create table `mimic-four-377221.E6_BloodGas.TTTT_33`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_33`   
            set Label_Syn  = "Item33"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_33`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_33`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_33`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_33`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_33`    as (
            select 
            rowNum ,
            Value_Int   as  Item33 
            from `mimic-four-377221.E6_BloodGas.UUUU_33`     );



###  33



            create table `mimic-four-377221.E6_BloodGas.TTTT_34`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_34`   
            set Label_Syn  = "Item34"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_34`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_34`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_34`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_34`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_34`    as (
            select 
            rowNum ,
            Value_Int   as  Item34 
            from `mimic-four-377221.E6_BloodGas.UUUU_34`     );



###  34



            create table `mimic-four-377221.E6_BloodGas.TTTT_35`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_35`   
            set Label_Syn  = "Item35"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_35`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_35`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_35`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_35`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_35`    as (
            select 
            rowNum ,
            Value_Int   as  Item35 
            from `mimic-four-377221.E6_BloodGas.UUUU_35`     );



###  35



            create table `mimic-four-377221.E6_BloodGas.TTTT_36`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_36`   
            set Label_Syn  = "Item36"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_36`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_36`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_36`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_36`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_36`    as (
            select 
            rowNum ,
            Value_Int   as  Item36 
            from `mimic-four-377221.E6_BloodGas.UUUU_36`     );



###  36



            create table `mimic-four-377221.E6_BloodGas.TTTT_37`    as
            SELECT * from `mimic-four-377221.E6_BloodGas.HYT`    ;


            update `mimic-four-377221.E6_BloodGas.TTTT_37`   
            set Label_Syn  = "Item37"
            where Label_Syn  is null  ;

            create table `mimic-four-377221.E6_BloodGas.UUUU_37`    as (
            select 
            a.rowNum ,
            a.Label_Syn ,
            a.Value_Int ,
            b.Value_Int   as  Value_2
            from `mimic-four-377221.E6_BloodGas.TTTT_37`    a 
            left join `mimic-four-377221.E6_BloodGas.bgA6`    b
            on
            a.rowNum =b.rowNum 
            and
            a.Label_Syn =b.Label_Syn ) ;

            update `mimic-four-377221.E6_BloodGas.UUUU_37`  
            set Value_Int  = Value_2
            where Value_Int  is null  ;

            update `mimic-four-377221.E6_BloodGas.UUUU_37`  
            set Value_Int  = 9999
            where Value_Int  is null  ;

            create table `mimic-four-377221.E6_BloodGas.VVVV_37`    as (
            select 
            rowNum ,
            Value_Int   as  Item37 
            from `mimic-four-377221.E6_BloodGas.UUUU_37`     );



##################################################################################
#query   Part 3 =


        create table `mimic-four-377221.E6_BloodGas.bgA7`     as
        SELECT
        KKKK_1.rowNum,
        KKKK_1.Item1, 
        KKKK_2.Item2, 
        KKKK_3.Item3, 
        KKKK_4.Item4, 
        KKKK_5.Item5, 
        KKKK_6.Item6, 
        KKKK_7.Item7, 
        KKKK_8.Item8, 
        KKKK_9.Item9, 
        KKKK_10.Item10, 
        KKKK_11.Item11, 
        KKKK_12.Item12, 
        KKKK_13.Item13, 
        KKKK_14.Item14, 
        KKKK_15.Item15, 
        KKKK_16.Item16, 
        KKKK_17.Item17, 
        KKKK_18.Item18, 
        KKKK_19.Item19, 
        KKKK_20.Item20, 
        KKKK_21.Item21, 
        KKKK_22.Item22, 
        KKKK_23.Item23, 
        KKKK_24.Item24, 
        KKKK_25.Item25, 
        KKKK_26.Item26, 
        KKKK_27.Item27, 
        KKKK_28.Item28, 
        KKKK_29.Item29, 
        KKKK_30.Item30, 
        KKKK_31.Item31, 
        KKKK_32.Item32, 
        KKKK_33.Item33, 
        KKKK_34.Item34, 
        KKKK_35.Item35, 
        KKKK_36.Item36, 
        KKKK_37.Item37 

        from `mimic-four-377221.E6_BloodGas.VVVV_1`  as KKKK_1

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_2`  as KKKK_2
        on
        KKKK_1.rowNum=KKKK_2.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_3`  as KKKK_3
        on
        KKKK_1.rowNum=KKKK_3.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_4`  as KKKK_4
        on
        KKKK_1.rowNum=KKKK_4.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_5`  as KKKK_5
        on
        KKKK_1.rowNum=KKKK_5.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_6`  as KKKK_6
        on
        KKKK_1.rowNum=KKKK_6.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_7`  as KKKK_7
        on
        KKKK_1.rowNum=KKKK_7.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_8`  as KKKK_8
        on
        KKKK_1.rowNum=KKKK_8.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_9`  as KKKK_9
        on
        KKKK_1.rowNum=KKKK_9.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_10`  as KKKK_10
        on
        KKKK_1.rowNum=KKKK_10.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_11`  as KKKK_11
        on
        KKKK_1.rowNum=KKKK_11.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_12`  as KKKK_12
        on
        KKKK_1.rowNum=KKKK_12.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_13`  as KKKK_13
        on
        KKKK_1.rowNum=KKKK_13.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_14`  as KKKK_14
        on
        KKKK_1.rowNum=KKKK_14.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_15`  as KKKK_15
        on
        KKKK_1.rowNum=KKKK_15.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_16`  as KKKK_16
        on
        KKKK_1.rowNum=KKKK_16.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_17`  as KKKK_17
        on
        KKKK_1.rowNum=KKKK_17.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_18`  as KKKK_18
        on
        KKKK_1.rowNum=KKKK_18.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_19`  as KKKK_19
        on
        KKKK_1.rowNum=KKKK_19.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_20`  as KKKK_20
        on
        KKKK_1.rowNum=KKKK_20.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_21`  as KKKK_21
        on
        KKKK_1.rowNum=KKKK_21.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_22`  as KKKK_22
        on
        KKKK_1.rowNum=KKKK_22.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_23`  as KKKK_23
        on
        KKKK_1.rowNum=KKKK_23.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_24`  as KKKK_24
        on
        KKKK_1.rowNum=KKKK_24.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_25`  as KKKK_25
        on
        KKKK_1.rowNum=KKKK_25.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_26`  as KKKK_26
        on
        KKKK_1.rowNum=KKKK_26.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_27`  as KKKK_27
        on
        KKKK_1.rowNum=KKKK_27.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_28`  as KKKK_28
        on
        KKKK_1.rowNum=KKKK_28.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_29`  as KKKK_29
        on
        KKKK_1.rowNum=KKKK_29.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_30`  as KKKK_30
        on
        KKKK_1.rowNum=KKKK_30.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_31`  as KKKK_31
        on
        KKKK_1.rowNum=KKKK_31.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_32`  as KKKK_32
        on
        KKKK_1.rowNum=KKKK_32.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_33`  as KKKK_33
        on
        KKKK_1.rowNum=KKKK_33.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_34`  as KKKK_34
        on
        KKKK_1.rowNum=KKKK_34.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_35`  as KKKK_35
        on
        KKKK_1.rowNum=KKKK_35.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_36`  as KKKK_36
        on
        KKKK_1.rowNum=KKKK_36.rowNum

        left join 
        `mimic-four-377221.E6_BloodGas.VVVV_37`  as KKKK_37
        on
        KKKK_1.rowNum=KKKK_37.rowNum

##################################################################################
#query   Part 4 =


    ;
                    drop table  `mimic-four-377221.E6_BloodGas.HYT`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_1`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_2`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_3`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_4`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_5`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_6`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_7`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_8`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_9`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_10`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_11`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_12`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_13`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_14`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_15`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_16`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_17`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_18`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_19`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_20`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_21`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_22`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_23`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_24`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_25`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_26`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_27`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_28`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_29`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_30`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_31`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_32`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_33`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_34`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_35`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_36`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.TTTT_37`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_1`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_2`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_3`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_4`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_5`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_6`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_7`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_8`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_9`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_10`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_11`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_12`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_13`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_14`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_15`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_16`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_17`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_18`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_19`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_20`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_21`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_22`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_23`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_24`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_25`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_26`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_27`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_28`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_29`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_30`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_31`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_32`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_33`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_34`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_35`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_36`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.UUUU_37`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_1`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_2`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_3`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_4`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_5`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_6`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_7`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_8`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_9`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_10`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_11`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_12`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_13`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_14`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_15`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_16`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_17`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_18`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_19`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_20`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_21`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_22`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_23`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_24`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_25`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_26`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_27`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_28`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_29`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_30`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_31`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_32`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_33`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_34`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_35`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_36`  ;


                        drop table  `mimic-four-377221.E6_BloodGas.VVVV_37`  ;








'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
