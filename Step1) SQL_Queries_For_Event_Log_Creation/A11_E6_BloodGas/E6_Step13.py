import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


        CREATE   TABLE `mimic-four-377221.E6_BloodGas.bgA8`  AS
        SELECT   * FROM `mimic-four-377221.E6_BloodGas.bgA7` ;


##########################################################################
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item1  = 1  WHERE Item1<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item2  = 1  WHERE Item2<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item3  = 1  WHERE Item3<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item4  = 1  WHERE Item4<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item5  = 1  WHERE Item5<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item6  = 1  WHERE Item6<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item7  = 1  WHERE Item7<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item8  = 1  WHERE Item8<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item9  = 1  WHERE Item9<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item10  = 1  WHERE Item10<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item11  = 1  WHERE Item11<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item12  = 1  WHERE Item12<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item13  = 1  WHERE Item13<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item14  = 1  WHERE Item14<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item15  = 1  WHERE Item15<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item16  = 1  WHERE Item16<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item17  = 1  WHERE Item17<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item18  = 1  WHERE Item18<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item19  = 1  WHERE Item19<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item20  = 1  WHERE Item20<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item21  = 1  WHERE Item21<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item22  = 1  WHERE Item22<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item23  = 1  WHERE Item23<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item24  = 1  WHERE Item24<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item25  = 1  WHERE Item25<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item26  = 1  WHERE Item26<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item27  = 1  WHERE Item27<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item28  = 1  WHERE Item28<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item29  = 1  WHERE Item29<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item30  = 1  WHERE Item30<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item31  = 1  WHERE Item31<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item32  = 1  WHERE Item32<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item33  = 1  WHERE Item33<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item34  = 1  WHERE Item34<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item35  = 1  WHERE Item35<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item36  = 1  WHERE Item36<>9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item37  = 1  WHERE Item37<>9999 ;


#############################################################################################

UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item1  = 0  WHERE Item1=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item2  = 0  WHERE Item2=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item3  = 0  WHERE Item3=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item4  = 0  WHERE Item4=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item5  = 0  WHERE Item5=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item6  = 0  WHERE Item6=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item7  = 0  WHERE Item7=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item8  = 0  WHERE Item8=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item9  = 0  WHERE Item9=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item10  = 0  WHERE Item10=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item11  = 0  WHERE Item11=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item12  = 0  WHERE Item12=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item13  = 0  WHERE Item13=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item14  = 0  WHERE Item14=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item15  = 0  WHERE Item15=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item16  = 0  WHERE Item16=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item17  = 0  WHERE Item17=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item18  = 0  WHERE Item18=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item19  = 0  WHERE Item19=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item20  = 0  WHERE Item20=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item21  = 0  WHERE Item21=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item22  = 0  WHERE Item22=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item23  = 0  WHERE Item23=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item24  = 0  WHERE Item24=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item25  = 0  WHERE Item25=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item26  = 0  WHERE Item26=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item27  = 0  WHERE Item27=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item28  = 0  WHERE Item28=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item29  = 0  WHERE Item29=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item30  = 0  WHERE Item30=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item31  = 0  WHERE Item31=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item32  = 0  WHERE Item32=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item33  = 0  WHERE Item33=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item34  = 0  WHERE Item34=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item35  = 0  WHERE Item35=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item36  = 0  WHERE Item36=9999 ;
UPDATE `mimic-four-377221.E6_BloodGas.bgA8`   SET  Item37  = 0  WHERE Item37=9999 ;
,0

'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
