import os
from google.cloud import bigquery

symPath = '../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''
            

            


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K002`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K001` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K003`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K002` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K004`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K003` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K005`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K004` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K006`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K005` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K007`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K006` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K008`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K007` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K009`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K008` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K010`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K009` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K011`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K010` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K012`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K011` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K013`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K012` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K014`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K013` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K015`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K014` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K016`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K015` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K017`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K016` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K018`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K017` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K019`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K018` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K020`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K019` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################

    CREATE TABLE  `mimic-four-377221.R_TimeL.K021`   AS

    (
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time as min_Time,
    b.min_Time as max_Time


    from (SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id

    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time and b.min_Time<>b.max_Time)    
    )


    #####################################################################################################
    union distinct
    (
    #####################################################################################################

    select 
    c.subject_id,
    c.hadm_id,
    c.stay_id,
    c.transfer_id,
    c.min_Time,
    c.max_Time,

    from
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id) c


    left join
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time,
    from (SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where
    (a.min_Time<b.min_Time and a.max_Time=b.max_Time  and b.min_Time<>b.max_Time)
    ) d


    on
    c.subject_id=d.subject_id
    and
    c.hadm_id=d.hadm_id
    and
    c.min_Time=d.min_Time
    and
    d.max_Time=d.max_Time
    where d.subject_id is null


    #####################################################################################################
    )
    union distinct
    #####################################################################################################
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time

    from (SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id<>0 and transfer_id<>0) b
    on
    a.subject_id=b.subject_id
    and
    a.hadm_id=b.hadm_id
    where b.subject_id is null
    )



    #####################################################################################################
    union distinct
    #####################################################################################################
    #left Table


    (
    SELECT * FROM `mimic-four-377221.R_TimeL.K020` where stay_id<>0 and transfer_id<>0
    )

    );
    ################################################

                


    ################################################


    




'''

QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)

for row in query_job.result():
    print(row)
