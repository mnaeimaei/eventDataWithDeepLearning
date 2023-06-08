
list1=['K002', 'K003', 'K004', 'K005', 'K006', 'K007', 'K008', 'K009', 'K010', 'K011', 'K012', 'K013', 'K014', 'K015', 'K016', 'K017', 'K018', 'K019', 'K020', 'K021', 'K022']
list2=['K001', 'K002', 'K003', 'K004', 'K005', 'K006', 'K007', 'K008', 'K009', 'K010', 'K011', 'K012', 'K013', 'K014', 'K015', 'K016', 'K017', 'K018', 'K019', 'K020', 'K021']


query2=""
for i,j in zip(list1,list2):
    New = i
    Old = j
    query1 = f'''            


    ################################################

    
    CREATE TABLE  `mimic-four-377221.R_TimeQ.{New}`   AS
    
        (
        select distinct
        a.subject_id,
        a.hadm_id,
        a.stay_id,
        a.transfer_id,
    
        a.min_Time as min_Time,
        b.min_Time as max_Time,
    
    
    
    
    
    
    
        from (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id=0 and transfer_id=0) a
        left join (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id<>0 and transfer_id<>0) b
        on
        a.subject_id=b.subject_id
        and
        a.hadm_id=b.hadm_id
    
        where
        (a.min_Time<b.min_Time and a.max_Time>b.max_Time and b.min_Time<>b.max_Time)
        )
    
    
        #########################################################################################################
    
    union distinct
    
    ##########################################################################
    
        (
        select distinct
        a.subject_id,
        a.hadm_id,
        a.stay_id,
        a.transfer_id,
    
        b.max_Time as min_Time,
        a.max_Time as  max_Time,
    
    
    
        from (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id=0 and transfer_id=0) a
        left join (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id<>0 and transfer_id<>0) b
        on
        a.subject_id=b.subject_id
        and
        a.hadm_id=b.hadm_id
    
        where
        (a.min_Time<b.min_Time and a.max_Time>b.max_Time and b.min_Time<>b.max_Time)
        
        )
    
            #########################################################################################################
    
    union distinct
    
    ##################################################################
    
    
    
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
    from (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id<>0 and transfer_id<>0) b
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
    from (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id<>0 and transfer_id<>0) b
    on
        a.subject_id=b.subject_id
        and
        a.hadm_id=b.hadm_id
    
        where
        (a.min_Time<b.min_Time and a.max_Time>b.max_Time and b.min_Time<>b.max_Time)
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
    
            #########################################################################################################
    
    union distinct
    
    ##################################################################
    
    #Different Column
    (
    select distinct
    a.subject_id,
    a.hadm_id,
    a.stay_id,
    a.transfer_id,
    a.min_Time,
    a.max_Time
    
    from (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id=0 and transfer_id=0) a
    left join (SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id<>0 and transfer_id<>0) b
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
    SELECT * FROM `mimic-four-377221.R_TimeQ.{Old}` where stay_id<>0 and transfer_id<>0
    )
    ;
    ################################################






    '''
    query2 = query2 + query1


print(query2)