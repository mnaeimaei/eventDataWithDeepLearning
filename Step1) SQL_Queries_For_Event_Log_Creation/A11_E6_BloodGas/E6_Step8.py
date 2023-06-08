import os
from google.cloud import bigquery
symPath='../gcKey/MIMIC_Google_Cloud.json'
Realpath = os.path.realpath(symPath)
print(Realpath)


os.environ['GOOGLE_APPLICATION_CREDENTIALS']=Realpath

client = bigquery.Client()

# Perform a query.
query1 = f'''            


    
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=14
            where Value="%";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=15
            where Value="-0.7 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=16
            where Value="-1 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=17
            where Value="-10 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=18
            where Value="-11 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=19
            where Value="-12 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=20
            where Value="-12.4 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=21
            where Value="-13 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=22
            where Value="-14 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=23
            where Value="-15 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=24
            where Value="-16 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=25
            where Value="-17 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=26
            where Value="-18 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=27
            where Value="-19 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=28
            where Value="-2 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=29
            where Value="-20 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=30
            where Value="-21 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=31
            where Value="-22 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=32
            where Value="-23 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=33
            where Value="-24 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=34
            where Value="-25 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=35
            where Value="-26 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=36
            where Value="-27 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=37
            where Value="-28 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=38
            where Value="-29 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=39
            where Value="-29.4 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=40
            where Value="-3 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=41
            where Value="-30 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=42
            where Value="-31 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=43
            where Value="-313 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=44
            where Value="-32 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=45
            where Value="-33 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=46
            where Value="-34 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=47
            where Value="-35 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=48
            where Value="-36 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=49
            where Value="-37 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=50
            where Value="-38 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=51
            where Value="-39 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=52
            where Value="-4 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=53
            where Value="-4.4 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=54
            where Value="-40 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=55
            where Value="-41 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=56
            where Value="-413 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=57
            where Value="-414 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=58
            where Value="-43 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=59
            where Value="-44 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=60
            where Value="-47 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=61
            where Value="-5 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=62
            where Value="-5.1 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=63
            where Value="-50 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=64
            where Value="-6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=65
            where Value="-6 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=66
            where Value="-6.3 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=67
            where Value="-7 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=68
            where Value="-8 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=69
            where Value="-9 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=70
            where Value="/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=71
            where Value="/0 .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=72
            where Value="/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=73
            where Value="/11.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=74
            where Value="/12.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=75
            where Value="/13.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=76
            where Value="/14.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=77
            where Value="/15.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=78
            where Value="/16.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=79
            where Value="/17.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=80
            where Value="/18.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=81
            where Value="/19.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=82
            where Value="/2 .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=83
            where Value="/20.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=84
            where Value="/21.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=85
            where Value="/22.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=86
            where Value="/23.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=87
            where Value="/24.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=88
            where Value="/25.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=89
            where Value="/26.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=90
            where Value="/27.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=91
            where Value="/28.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=92
            where Value="/29.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=93
            where Value="/30.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=94
            where Value="/31.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=95
            where Value="/32.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=96
            where Value="/33.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=97
            where Value="/34.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=98
            where Value="/35.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=99
            where Value="/36.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=100
            where Value="/37.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=101
            where Value="/38.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=102
            where Value="/39.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=103
            where Value="/4 .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=104
            where Value="/40.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=105
            where Value="/41.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=106
            where Value="/42.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=107
            where Value="/44.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=108
            where Value="/45.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=109
            where Value="/5 .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=110
            where Value="/50.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=111
            where Value="/6 .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=112
            where Value="/7 .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=113
            where Value="/8 .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=114
            where Value="/9 .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=115
            where Value="0";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=116
            where Value="0 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=117
            where Value="0 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=118
            where Value="0 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=119
            where Value="0.12 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=120
            where Value="0.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=121
            where Value="0.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=122
            where Value="0.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=123
            where Value="0.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=124
            where Value="0.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=125
            where Value="0.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=126
            where Value="0.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=127
            where Value="0.59 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=128
            where Value="0.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=129
            where Value="0.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=130
            where Value="0.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=131
            where Value="0.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=132
            where Value="0.76 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=133
            where Value="0.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=134
            where Value="0.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=135
            where Value="0.83 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=136
            where Value="0.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=137
            where Value="0.9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=138
            where Value="0.95 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=139
            where Value="0.99 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=140
            where Value="0/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=141
            where Value="0/11.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=142
            where Value="0/12.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=143
            where Value="0/13.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=144
            where Value="0/14.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=145
            where Value="0/15.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=146
            where Value="0/16.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=147
            where Value="0/17.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=148
            where Value="0/18.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=149
            where Value="0/19.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=150
            where Value="0/20.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=151
            where Value="0/21.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=152
            where Value="0/22.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=153
            where Value="0/23.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=154
            where Value="0/24.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=155
            where Value="0/25.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=156
            where Value="0/26.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=157
            where Value="0/28.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=158
            where Value="0/30.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=159
            where Value="0/32.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=160
            where Value="0/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=161
            where Value="0/9.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=162
            where Value="1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=163
            where Value="1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=164
            where Value="1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=165
            where Value="1 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=166
            where Value="1.04 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=167
            where Value="1.07 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=168
            where Value="1.09 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=169
            where Value="1.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=170
            where Value="1.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=171
            where Value="1.12 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=172
            where Value="1.19 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=173
            where Value="1.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=174
            where Value="1.23 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=175
            where Value="1.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=176
            where Value="1.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=177
            where Value="1.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=178
            where Value="1.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=179
            where Value="1.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=180
            where Value="1.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=181
            where Value="1.68 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=182
            where Value="1.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=183
            where Value="1.72 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=184
            where Value="1.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=185
            where Value="1.9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=186
            where Value="10";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=187
            where Value="10 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=188
            where Value="10 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=189
            where Value="10 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=190
            where Value="10.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=191
            where Value="10.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=192
            where Value="10.2 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=193
            where Value="10.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=194
            where Value="10.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=195
            where Value="10.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=196
            where Value="10.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=197
            where Value="10.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=198
            where Value="10.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=199
            where Value="10.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=200
            where Value="10.9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=201
            where Value="10/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=202
            where Value="10/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=203
            where Value="10/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=204
            where Value="10/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=205
            where Value="10/12.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=206
            where Value="10/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=207
            where Value="10/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=208
            where Value="10/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=209
            where Value="10/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=210
            where Value="10/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=211
            where Value="10/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=212
            where Value="100";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=213
            where Value="100 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=214
            where Value="100 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=215
            where Value="100 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=216
            where Value="1000";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=217
            where Value="1009";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=218
            where Value="101 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=219
            where Value="101 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=220
            where Value="1012";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=221
            where Value="102";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=222
            where Value="102 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=223
            where Value="103 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=224
            where Value="104 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=225
            where Value="1044";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=226
            where Value="105 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=227
            where Value="106 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=228
            where Value="106 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=229
            where Value="107 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=230
            where Value="108 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=231
            where Value="109 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=232
            where Value="11";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=233
            where Value="11 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=234
            where Value="11 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=235
            where Value="11 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=236
            where Value="11.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=237
            where Value="11.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=238
            where Value="11.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=239
            where Value="11.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=240
            where Value="11.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=241
            where Value="11.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=242
            where Value="11.9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=243
            where Value="11/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=244
            where Value="110 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=245
            where Value="1100";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=246
            where Value="1109";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=247
            where Value="112 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=248
            where Value="113 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=249
            where Value="114 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=250
            where Value="115 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=251
            where Value="116";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=252
            where Value="116 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=253
            where Value="118";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=254
            where Value="118 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=255
            where Value="1180";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=256
            where Value="119 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=257
            where Value="12";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=258
            where Value="12 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=259
            where Value="12 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=260
            where Value="12 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=261
            where Value="12.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=262
            where Value="12.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=263
            where Value="12.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=264
            where Value="12.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=265
            where Value="12.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=266
            where Value="12.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=267
            where Value="12.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=268
            where Value="12.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=269
            where Value="12/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=270
            where Value="12/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=271
            where Value="12/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=272
            where Value="12/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=273
            where Value="12/12.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=274
            where Value="12/13.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=275
            where Value="12/14.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=276
            where Value="12/16.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=277
            where Value="12/17.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=278
            where Value="12/18.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=279
            where Value="12/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=280
            where Value="12/20.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=281
            where Value="12/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=282
            where Value="12/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=283
            where Value="12/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=284
            where Value="12/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=285
            where Value="12/7.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=286
            where Value="12/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=287
            where Value="120";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=288
            where Value="120 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=289
            where Value="1200";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=290
            where Value="121 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=291
            where Value="121 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=292
            where Value="122 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=293
            where Value="123";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=294
            where Value="123 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=295
            where Value="124 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=296
            where Value="125";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=297
            where Value="125 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=298
            where Value="126 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=299
            where Value="127 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=300
            where Value="128 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=301
            where Value="129 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=302
            where Value="13";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=303
            where Value="13 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=304
            where Value="13 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=305
            where Value="13 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=306
            where Value="13.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=307
            where Value="13.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=308
            where Value="13.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=309
            where Value="13.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=310
            where Value="13.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=311
            where Value="13/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=312
            where Value="130";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=313
            where Value="130 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=314
            where Value="131 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=315
            where Value="132";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=316
            where Value="132 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=317
            where Value="133 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=318
            where Value="134 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=319
            where Value="135 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=320
            where Value="135 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=321
            where Value="136 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=322
            where Value="137 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=323
            where Value="138 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=324
            where Value="14";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=325
            where Value="14 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=326
            where Value="14 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=327
            where Value="14 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=328
            where Value="14.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=329
            where Value="14.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=330
            where Value="14.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=331
            where Value="14/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=332
            where Value="14/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=333
            where Value="14/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=334
            where Value="14/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=335
            where Value="14/12.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=336
            where Value="14/14.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=337
            where Value="14/15.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=338
            where Value="14/16.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=339
            where Value="14/17.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=340
            where Value="14/18.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=341
            where Value="14/19.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=342
            where Value="14/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=343
            where Value="14/20.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=344
            where Value="14/22.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=345
            where Value="14/24.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=346
            where Value="14/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=347
            where Value="14/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=348
            where Value="14/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=349
            where Value="14/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=350
            where Value="14/7.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=351
            where Value="14/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=352
            where Value="14/9.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=353
            where Value="140";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=354
            where Value="140 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=355
            where Value="1400";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=356
            where Value="141 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=357
            where Value="142 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=358
            where Value="143 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=359
            where Value="144";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=360
            where Value="144 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=361
            where Value="145 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=362
            where Value="146 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=363
            where Value="147 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=364
            where Value="147 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=365
            where Value="148 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=366
            where Value="149 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=367
            where Value="15";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=368
            where Value="15 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=369
            where Value="15 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=370
            where Value="15 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=371
            where Value="15.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=372
            where Value="15.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=373
            where Value="15.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=374
            where Value="15.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=375
            where Value="15/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=376
            where Value="15/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=377
            where Value="15/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=378
            where Value="15/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=379
            where Value="15/15.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=380
            where Value="15/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=381
            where Value="15/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=382
            where Value="15/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=383
            where Value="15/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=384
            where Value="15/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=385
            where Value="15/7.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=386
            where Value="15/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=387
            where Value="150";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=388
            where Value="150 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=389
            where Value="1500";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=390
            where Value="151 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=391
            where Value="152 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=392
            where Value="153 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=393
            where Value="154";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=394
            where Value="154 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=395
            where Value="155 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=396
            where Value="156 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=397
            where Value="1566";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=398
            where Value="157 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=399
            where Value="158 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=400
            where Value="159 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=401
            where Value="16";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=402
            where Value="16 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=403
            where Value="16 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=404
            where Value="16 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=405
            where Value="16.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=406
            where Value="16.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=407
            where Value="16.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=408
            where Value="16.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=409
            where Value="16.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=410
            where Value="16/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=411
            where Value="16/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=412
            where Value="16/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=413
            where Value="16/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=414
            where Value="16/11.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=415
            where Value="16/12.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=416
            where Value="16/14.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=417
            where Value="16/15.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=418
            where Value="16/16.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=419
            where Value="16/17.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=420
            where Value="16/18.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=421
            where Value="16/19.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=422
            where Value="16/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=423
            where Value="16/20.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=424
            where Value="16/22.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=425
            where Value="16/25.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=426
            where Value="16/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=427
            where Value="16/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=428
            where Value="16/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=429
            where Value="16/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=430
            where Value="16/7.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=431
            where Value="16/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=432
            where Value="16/9.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=433
            where Value="160";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=434
            where Value="160 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=435
            where Value="161 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=436
            where Value="162 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=437
            where Value="163 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=438
            where Value="164 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=439
            where Value="165 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=440
            where Value="166 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=441
            where Value="167 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=442
            where Value="168 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=443
            where Value="169 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=444
            where Value="17";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=445
            where Value="17 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=446
            where Value="17 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=447
            where Value="17 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=448
            where Value="17.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=449
            where Value="17/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=450
            where Value="17/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=451
            where Value="17/17.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=452
            where Value="170";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=453
            where Value="170 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=454
            where Value="171 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=455
            where Value="172 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=456
            where Value="173 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=457
            where Value="174 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=458
            where Value="175";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=459
            where Value="175 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=460
            where Value="176 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=461
            where Value="177 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=462
            where Value="178";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=463
            where Value="178 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=464
            where Value="179 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=465
            where Value="18";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=466
            where Value="18 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=467
            where Value="18 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=468
            where Value="18 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=469
            where Value="18.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=470
            where Value="18.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=471
            where Value="18.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=472
            where Value="18/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=473
            where Value="18/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=474
            where Value="18/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=475
            where Value="18/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=476
            where Value="18/12.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=477
            where Value="18/18.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=478
            where Value="18/19.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=479
            where Value="18/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=480
            where Value="18/20.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=481
            where Value="18/21.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=482
            where Value="18/22.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=483
            where Value="18/23.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=484
            where Value="18/24.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=485
            where Value="18/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=486
            where Value="18/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=487
            where Value="18/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=488
            where Value="18/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=489
            where Value="18/7.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=490
            where Value="18/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=491
            where Value="18/9.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=492
            where Value="180";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=493
            where Value="180 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=494
            where Value="1800";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=495
            where Value="181 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=496
            where Value="182 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=497
            where Value="183 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=498
            where Value="184";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=499
            where Value="184 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=500
            where Value="185";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=501
            where Value="185 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=502
            where Value="186 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=503
            where Value="187";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=504
            where Value="187 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=505
            where Value="188 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=506
            where Value="188 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=507
            where Value="189";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=508
            where Value="189 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=509
            where Value="19";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=510
            where Value="19 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=511
            where Value="19 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=512
            where Value="19.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=513
            where Value="19.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=514
            where Value="19.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=515
            where Value="19.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=516
            where Value="19/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=517
            where Value="19/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=518
            where Value="190";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=519
            where Value="190 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=520
            where Value="191";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=521
            where Value="191 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=522
            where Value="192 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=523
            where Value="193 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=524
            where Value="194 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=525
            where Value="195 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=526
            where Value="196 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=527
            where Value="196 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=528
            where Value="197 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=529
            where Value="198";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=530
            where Value="198 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=531
            where Value="198 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=532
            where Value="199 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=533
            where Value="2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=534
            where Value="2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=535
            where Value="2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=536
            where Value="2 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=537
            where Value="2.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=538
            where Value="2.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=539
            where Value="2.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=540
            where Value="2.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=541
            where Value="2.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=542
            where Value="2.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=543
            where Value="2.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=544
            where Value="2.7 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=545
            where Value="2/ .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=546
            where Value="20";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=547
            where Value="20 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=548
            where Value="20 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=549
            where Value="20 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=550
            where Value="20.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=551
            where Value="20.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=552
            where Value="20.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=553
            where Value="20/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=554
            where Value="20/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=555
            where Value="20/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=556
            where Value="20/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=557
            where Value="20/11.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=558
            where Value="20/12.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=559
            where Value="20/15.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=560
            where Value="20/16.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=561
            where Value="20/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=562
            where Value="20/20.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=563
            where Value="20/21.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=564
            where Value="20/22.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=565
            where Value="20/23.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=566
            where Value="20/24.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=567
            where Value="20/28.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=568
            where Value="20/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=569
            where Value="20/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=570
            where Value="20/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=571
            where Value="20/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=572
            where Value="20/7.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=573
            where Value="20/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=574
            where Value="20/9.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=575
            where Value="200";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=576
            where Value="200 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=577
            where Value="201 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=578
            where Value="202 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=579
            where Value="203 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=580
            where Value="204 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=581
            where Value="205";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=582
            where Value="205 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=583
            where Value="206";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=584
            where Value="206 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=585
            where Value="207";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=586
            where Value="207 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=587
            where Value="208 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=588
            where Value="209 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=589
            where Value="21";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=590
            where Value="21 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=591
            where Value="21 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=592
            where Value="21 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=593
            where Value="21.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=594
            where Value="21.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=595
            where Value="21.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=596
            where Value="21.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=597
            where Value="21.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=598
            where Value="21/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=599
            where Value="21/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=600
            where Value="210";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=601
            where Value="210 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=602
            where Value="211";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=603
            where Value="211 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=604
            where Value="212 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=605
            where Value="213";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=606
            where Value="213 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=607
            where Value="214";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=608
            where Value="214 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=609
            where Value="215";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=610
            where Value="215 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=611
            where Value="216 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=612
            where Value="217";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=613
            where Value="217 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=614
            where Value="218";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=615
            where Value="218 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=616
            where Value="219 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=617
            where Value="22";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=618
            where Value="22 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=619
            where Value="22 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=620
            where Value="22 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=621
            where Value="22.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=622
            where Value="22.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=623
            where Value="22.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=624
            where Value="22.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=625
            where Value="22/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=626
            where Value="22/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=627
            where Value="22/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=628
            where Value="22/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=629
            where Value="22/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=630
            where Value="22/22.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=631
            where Value="22/23.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=632
            where Value="22/24.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=633
            where Value="22/25.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=634
            where Value="22/26.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=635
            where Value="22/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=636
            where Value="22/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=637
            where Value="22/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=638
            where Value="22/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=639
            where Value="22/7.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=640
            where Value="22/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=641
            where Value="220";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=642
            where Value="220 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=643
            where Value="221 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=644
            where Value="222 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=645
            where Value="223";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=646
            where Value="223 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=647
            where Value="224";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=648
            where Value="224 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=649
            where Value="225";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=650
            where Value="225 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=651
            where Value="226";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=652
            where Value="226 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=653
            where Value="227";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=654
            where Value="227 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=655
            where Value="228 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=656
            where Value="229 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=657
            where Value="23";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=658
            where Value="23 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=659
            where Value="23 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=660
            where Value="23 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=661
            where Value="23.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=662
            where Value="23.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=663
            where Value="23.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=664
            where Value="23.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=665
            where Value="23.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=666
            where Value="23/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=667
            where Value="23/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=668
            where Value="230";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=669
            where Value="230 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=670
            where Value="231";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=671
            where Value="231 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=672
            where Value="232 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=673
            where Value="232 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=674
            where Value="233";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=675
            where Value="233 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=676
            where Value="234";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=677
            where Value="234 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=678
            where Value="234 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=679
            where Value="235";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=680
            where Value="235 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=681
            where Value="236 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=682
            where Value="237 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=683
            where Value="238";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=684
            where Value="238 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=685
            where Value="239 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=686
            where Value="24";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=687
            where Value="24 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=688
            where Value="24 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=689
            where Value="24 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=690
            where Value="24.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=691
            where Value="24.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=692
            where Value="24.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=693
            where Value="24.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=694
            where Value="24.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=695
            where Value="24.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=696
            where Value="24.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=697
            where Value="24.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=698
            where Value="24.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=699
            where Value="24/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=700
            where Value="24/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=701
            where Value="24/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=702
            where Value="24/10.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=703
            where Value="24/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=704
            where Value="24/24.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=705
            where Value="24/26.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=706
            where Value="24/27.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=707
            where Value="24/28.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=708
            where Value="24/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=709
            where Value="24/30.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=710
            where Value="24/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=711
            where Value="24/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=712
            where Value="24/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=713
            where Value="24/7.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=714
            where Value="24/8.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=715
            where Value="240";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=716
            where Value="240 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=717
            where Value="241";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=718
            where Value="241 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=719
            where Value="242";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=720
            where Value="242 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=721
            where Value="243";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=722
            where Value="243 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=723
            where Value="244 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=724
            where Value="245";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=725
            where Value="245 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=726
            where Value="246";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=727
            where Value="246 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=728
            where Value="247";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=729
            where Value="247 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=730
            where Value="248";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=731
            where Value="248 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=732
            where Value="249 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=733
            where Value="25";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=734
            where Value="25 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=735
            where Value="25 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=736
            where Value="25 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=737
            where Value="25.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=738
            where Value="25.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=739
            where Value="25.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=740
            where Value="25.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=741
            where Value="25.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=742
            where Value="25.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=743
            where Value="25/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=744
            where Value="25/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=745
            where Value="25/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=746
            where Value="25/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=747
            where Value="25/25.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=748
            where Value="25/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=749
            where Value="25/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=750
            where Value="25/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=751
            where Value="250";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=752
            where Value="250 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=753
            where Value="251";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=754
            where Value="251 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=755
            where Value="252";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=756
            where Value="252 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=757
            where Value="253";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=758
            where Value="253 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=759
            where Value="254";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=760
            where Value="254 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=761
            where Value="255";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=762
            where Value="255 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=763
            where Value="256";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=764
            where Value="256 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=765
            where Value="257 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=766
            where Value="258 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=767
            where Value="259";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=768
            where Value="259 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=769
            where Value="26";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=770
            where Value="26 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=771
            where Value="26 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=772
            where Value="26 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=773
            where Value="26.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=774
            where Value="26.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=775
            where Value="26.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=776
            where Value="26.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=777
            where Value="26.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=778
            where Value="26.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=779
            where Value="26.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=780
            where Value="26.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=781
            where Value="26.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=782
            where Value="26/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=783
            where Value="26/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=784
            where Value="26/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=785
            where Value="26/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=786
            where Value="26/26.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=787
            where Value="26/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=788
            where Value="26/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=789
            where Value="26/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=790
            where Value="26/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=791
            where Value="260";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=792
            where Value="260 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=793
            where Value="261";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=794
            where Value="261 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=795
            where Value="262 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=796
            where Value="263";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=797
            where Value="263 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=798
            where Value="264 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=799
            where Value="265";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=800
            where Value="265 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=801
            where Value="266";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=802
            where Value="266 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=803
            where Value="267";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=804
            where Value="267 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=805
            where Value="268";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=806
            where Value="268 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=807
            where Value="269";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=808
            where Value="269 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=809
            where Value="27";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=810
            where Value="27 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=811
            where Value="27 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=812
            where Value="27 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=813
            where Value="27.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=814
            where Value="27.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=815
            where Value="27.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=816
            where Value="27.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=817
            where Value="27.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=818
            where Value="27.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=819
            where Value="27.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=820
            where Value="27.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=821
            where Value="27.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=822
            where Value="27/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=823
            where Value="27/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=824
            where Value="270";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=825
            where Value="270 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=826
            where Value="271";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=827
            where Value="271 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=828
            where Value="272";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=829
            where Value="272 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=830
            where Value="273 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=831
            where Value="274";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=832
            where Value="274 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=833
            where Value="275";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=834
            where Value="275 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=835
            where Value="276";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=836
            where Value="276 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=837
            where Value="277";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=838
            where Value="277 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=839
            where Value="278";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=840
            where Value="278 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=841
            where Value="279";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=842
            where Value="279 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=843
            where Value="28";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=844
            where Value="28 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=845
            where Value="28 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=846
            where Value="28 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=847
            where Value="28.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=848
            where Value="28.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=849
            where Value="28.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=850
            where Value="28.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=851
            where Value="28.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=852
            where Value="28.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=853
            where Value="28/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=854
            where Value="28/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=855
            where Value="28/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=856
            where Value="28/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=857
            where Value="28/28.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=858
            where Value="28/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=859
            where Value="28/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=860
            where Value="28/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=861
            where Value="28/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=862
            where Value="280";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=863
            where Value="280 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=864
            where Value="281";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=865
            where Value="281 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=866
            where Value="282";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=867
            where Value="282 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=868
            where Value="283";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=869
            where Value="283 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=870
            where Value="284";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=871
            where Value="284 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=872
            where Value="285";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=873
            where Value="285 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=874
            where Value="286";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=875
            where Value="286 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=876
            where Value="287";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=877
            where Value="287 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=878
            where Value="288";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=879
            where Value="288 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=880
            where Value="288 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=881
            where Value="289";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=882
            where Value="289 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=883
            where Value="29";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=884
            where Value="29 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=885
            where Value="29 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=886
            where Value="29.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=887
            where Value="29.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=888
            where Value="29.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=889
            where Value="29.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=890
            where Value="29.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=891
            where Value="29.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=892
            where Value="29.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=893
            where Value="29.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=894
            where Value="29.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=895
            where Value="29.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=896
            where Value="29.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=897
            where Value="29/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=898
            where Value="290";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=899
            where Value="290 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=900
            where Value="291";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=901
            where Value="291 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=902
            where Value="291 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=903
            where Value="292";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=904
            where Value="292 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=905
            where Value="293";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=906
            where Value="293 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=907
            where Value="294";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=908
            where Value="294 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=909
            where Value="294 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=910
            where Value="295";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=911
            where Value="295 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=912
            where Value="296";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=913
            where Value="296 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=914
            where Value="297";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=915
            where Value="297 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=916
            where Value="298";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=917
            where Value="298 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=918
            where Value="299";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=919
            where Value="299 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=920
            where Value="3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=921
            where Value="3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=922
            where Value="3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=923
            where Value="3 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=924
            where Value="3 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=925
            where Value="3 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=926
            where Value="3.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=927
            where Value="3.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=928
            where Value="30";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=929
            where Value="30 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=930
            where Value="30 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=931
            where Value="30 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=932
            where Value="30 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=933
            where Value="30.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=934
            where Value="30.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=935
            where Value="30.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=936
            where Value="30.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=937
            where Value="30.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=938
            where Value="30.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=939
            where Value="30.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=940
            where Value="30.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=941
            where Value="30.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=942
            where Value="30.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=943
            where Value="30.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=944
            where Value="30/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=945
            where Value="30/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=946
            where Value="30/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=947
            where Value="30/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=948
            where Value="30/3.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=949
            where Value="30/30.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=950
            where Value="30/32.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=951
            where Value="30/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=952
            where Value="30/5.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=953
            where Value="30/6.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=954
            where Value="300";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=955
            where Value="300 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=956
            where Value="301";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=957
            where Value="301 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=958
            where Value="302";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=959
            where Value="302 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=960
            where Value="303";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=961
            where Value="303 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=962
            where Value="304";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=963
            where Value="304 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=964
            where Value="305";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=965
            where Value="305 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=966
            where Value="306";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=967
            where Value="306 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=968
            where Value="307";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=969
            where Value="307 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=970
            where Value="308";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=971
            where Value="308 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=972
            where Value="309";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=973
            where Value="309 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=974
            where Value="31";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=975
            where Value="31 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=976
            where Value="31 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=977
            where Value="31 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=978
            where Value="31.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=979
            where Value="31.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=980
            where Value="31.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=981
            where Value="31.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=982
            where Value="31.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=983
            where Value="31.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=984
            where Value="31.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=985
            where Value="31.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=986
            where Value="31.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=987
            where Value="31.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=988
            where Value="31.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=989
            where Value="31.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=990
            where Value="31.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=991
            where Value="31.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=992
            where Value="31.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=993
            where Value="31.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=994
            where Value="31.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=995
            where Value="31.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=996
            where Value="31/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=997
            where Value="310";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=998
            where Value="310 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=999
            where Value="311";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1000
            where Value="311 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1001
            where Value="3110";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1002
            where Value="312";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1003
            where Value="312 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1004
            where Value="313";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1005
            where Value="313 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1006
            where Value="314 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1007
            where Value="315";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1008
            where Value="315 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1009
            where Value="316";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1010
            where Value="316 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1011
            where Value="317";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1012
            where Value="317 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1013
            where Value="318";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1014
            where Value="318 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1015
            where Value="319";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1016
            where Value="319 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1017
            where Value="32";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1018
            where Value="32 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1019
            where Value="32 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1020
            where Value="32 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1021
            where Value="32.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1022
            where Value="32.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1023
            where Value="32.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1024
            where Value="32.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1025
            where Value="32.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1026
            where Value="32.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1027
            where Value="32.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1028
            where Value="32.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1029
            where Value="32.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1030
            where Value="32.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1031
            where Value="32.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1032
            where Value="32.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1033
            where Value="32.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1034
            where Value="32.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1035
            where Value="32.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1036
            where Value="32.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1037
            where Value="32.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1038
            where Value="32/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1039
            where Value="32/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1040
            where Value="32/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1041
            where Value="32/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1042
            where Value="32/32.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1043
            where Value="32/4.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1044
            where Value="320";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1045
            where Value="320 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1046
            where Value="321";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1047
            where Value="321 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1048
            where Value="322";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1049
            where Value="322 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1050
            where Value="323";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1051
            where Value="323 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1052
            where Value="324";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1053
            where Value="324 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1054
            where Value="325";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1055
            where Value="325 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1056
            where Value="326";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1057
            where Value="326 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1058
            where Value="327";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1059
            where Value="327 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1060
            where Value="328";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1061
            where Value="328 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1062
            where Value="329";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1063
            where Value="329 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1064
            where Value="33";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1065
            where Value="33 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1066
            where Value="33 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1067
            where Value="33.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1068
            where Value="33.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1069
            where Value="33.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1070
            where Value="33.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1071
            where Value="33.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1072
            where Value="33.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1073
            where Value="33.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1074
            where Value="33.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1075
            where Value="33.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1076
            where Value="33.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1077
            where Value="33.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1078
            where Value="33.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1079
            where Value="33.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1080
            where Value="33.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1081
            where Value="33.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1082
            where Value="33.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1083
            where Value="33/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1084
            where Value="33/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1085
            where Value="330";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1086
            where Value="330 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1087
            where Value="331";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1088
            where Value="331 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1089
            where Value="332";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1090
            where Value="332 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1091
            where Value="333";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1092
            where Value="333 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1093
            where Value="334";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1094
            where Value="334 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1095
            where Value="335";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1096
            where Value="335 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1097
            where Value="336";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1098
            where Value="336 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1099
            where Value="337";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1100
            where Value="337 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1101
            where Value="338";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1102
            where Value="338 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1103
            where Value="339";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1104
            where Value="339 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1105
            where Value="34";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1106
            where Value="34 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1107
            where Value="34 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1108
            where Value="34 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1109
            where Value="34.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1110
            where Value="34.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1111
            where Value="34.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1112
            where Value="34.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1113
            where Value="34.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1114
            where Value="34.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1115
            where Value="34.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1116
            where Value="34.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1117
            where Value="34.5 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1118
            where Value="34.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1119
            where Value="34.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1120
            where Value="34.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1121
            where Value="34.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1122
            where Value="34.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1123
            where Value="34.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1124
            where Value="34.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1125
            where Value="34/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1126
            where Value="34/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1127
            where Value="34/1.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1128
            where Value="34/2.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1129
            where Value="34/34.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1130
            where Value="340";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1131
            where Value="340 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1132
            where Value="341";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1133
            where Value="341 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1134
            where Value="342";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1135
            where Value="342 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1136
            where Value="343";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1137
            where Value="343 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1138
            where Value="344";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1139
            where Value="344 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1140
            where Value="345";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1141
            where Value="345 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1142
            where Value="346";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1143
            where Value="346 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1144
            where Value="347";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1145
            where Value="347 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1146
            where Value="348";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1147
            where Value="348 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1148
            where Value="349";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1149
            where Value="349 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1150
            where Value="35";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1151
            where Value="35 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1152
            where Value="35 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1153
            where Value="35 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1154
            where Value="35.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1155
            where Value="35.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1156
            where Value="35.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1157
            where Value="35.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1158
            where Value="35.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1159
            where Value="35.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1160
            where Value="35.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1161
            where Value="35.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1162
            where Value="35.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1163
            where Value="35.6 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1164
            where Value="35.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1165
            where Value="35.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1166
            where Value="35.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1167
            where Value="35.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1168
            where Value="35/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1169
            where Value="35/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1170
            where Value="350";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1171
            where Value="350 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1172
            where Value="351";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1173
            where Value="351 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1174
            where Value="352";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1175
            where Value="352 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1176
            where Value="353";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1177
            where Value="353 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1178
            where Value="354";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1179
            where Value="354 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1180
            where Value="355";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1181
            where Value="355 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1182
            where Value="356";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1183
            where Value="356 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1184
            where Value="357";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1185
            where Value="357 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1186
            where Value="358";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1187
            where Value="358 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1188
            where Value="359";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1189
            where Value="359 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1190
            where Value="36";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1191
            where Value="36 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1192
            where Value="36 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1193
            where Value="36 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1194
            where Value="36.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1195
            where Value="36.1 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1196
            where Value="36.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1197
            where Value="36.2 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1198
            where Value="36.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1199
            where Value="36.3 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1200
            where Value="36.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1201
            where Value="36.4 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1202
            where Value="36.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1203
            where Value="36.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1204
            where Value="36.5 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1205
            where Value="36.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1206
            where Value="36.6 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1207
            where Value="36.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1208
            where Value="36.7 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1209
            where Value="36.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1210
            where Value="36.8 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1211
            where Value="36.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1212
            where Value="36.9 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1213
            where Value="36/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1214
            where Value="36/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1215
            where Value="360";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1216
            where Value="360 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1217
            where Value="361";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1218
            where Value="361 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1219
            where Value="362";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1220
            where Value="362 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1221
            where Value="363";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1222
            where Value="363 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1223
            where Value="364";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1224
            where Value="364 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1225
            where Value="365";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1226
            where Value="365 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1227
            where Value="366";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1228
            where Value="366 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1229
            where Value="367";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1230
            where Value="367 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1231
            where Value="368";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1232
            where Value="368 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1233
            where Value="369";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1234
            where Value="369 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1235
            where Value="37";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1236
            where Value="37 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1237
            where Value="37 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1238
            where Value="37 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1239
            where Value="37.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1240
            where Value="37.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1241
            where Value="37.1 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1242
            where Value="37.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1243
            where Value="37.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1244
            where Value="37.2 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1245
            where Value="37.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1246
            where Value="37.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1247
            where Value="37.3 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1248
            where Value="37.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1249
            where Value="37.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1250
            where Value="37.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1251
            where Value="37.5 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1252
            where Value="37.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1253
            where Value="37.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1254
            where Value="37.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1255
            where Value="37.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1256
            where Value="37.7 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1257
            where Value="37.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1258
            where Value="37.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1259
            where Value="37.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1260
            where Value="370";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1261
            where Value="370 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1262
            where Value="371";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1263
            where Value="371 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1264
            where Value="372";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1265
            where Value="372 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1266
            where Value="373";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1267
            where Value="373 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1268
            where Value="374";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1269
            where Value="374 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1270
            where Value="375";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1271
            where Value="375 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1272
            where Value="376";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1273
            where Value="376 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1274
            where Value="377";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1275
            where Value="377 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1276
            where Value="378";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1277
            where Value="378 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1278
            where Value="379";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1279
            where Value="379 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1280
            where Value="38";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1281
            where Value="38 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1282
            where Value="38 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1283
            where Value="38 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1284
            where Value="38.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1285
            where Value="38.1 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1286
            where Value="38.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1287
            where Value="38.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1288
            where Value="38.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1289
            where Value="38.3 C";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1290
            where Value="38.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1291
            where Value="38.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1292
            where Value="38.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1293
            where Value="38.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1294
            where Value="38.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1295
            where Value="38.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1296
            where Value="38.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1297
            where Value="38.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1298
            where Value="38.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1299
            where Value="38/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1300
            where Value="380";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1301
            where Value="380 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1302
            where Value="381";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1303
            where Value="381 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1304
            where Value="382";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1305
            where Value="382 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1306
            where Value="383";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1307
            where Value="383 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1308
            where Value="384";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1309
            where Value="384 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1310
            where Value="385";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1311
            where Value="385 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1312
            where Value="386";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1313
            where Value="386 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1314
            where Value="387";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1315
            where Value="387 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1316
            where Value="388";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1317
            where Value="388 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1318
            where Value="389";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1319
            where Value="389 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1320
            where Value="39";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1321
            where Value="39 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1322
            where Value="39 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1323
            where Value="39 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1324
            where Value="39.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1325
            where Value="39.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1326
            where Value="39.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1327
            where Value="39.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1328
            where Value="39.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1329
            where Value="39.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1330
            where Value="39.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1331
            where Value="39.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1332
            where Value="39.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1333
            where Value="39.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1334
            where Value="39.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1335
            where Value="39/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1336
            where Value="390";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1337
            where Value="390 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1338
            where Value="391";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1339
            where Value="391 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1340
            where Value="392";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1341
            where Value="392 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1342
            where Value="393";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1343
            where Value="393 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1344
            where Value="394";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1345
            where Value="394 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1346
            where Value="395";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1347
            where Value="395 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1348
            where Value="396";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1349
            where Value="396 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1350
            where Value="397";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1351
            where Value="397 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1352
            where Value="398";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1353
            where Value="398 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1354
            where Value="399";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1355
            where Value="399 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1356
            where Value="4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1357
            where Value="4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1358
            where Value="4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1359
            where Value="4 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1360
            where Value="4.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1361
            where Value="4.27 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1362
            where Value="4.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1363
            where Value="4.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1364
            where Value="4.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1365
            where Value="4.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1366
            where Value="4.86 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1367
            where Value="4.9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1368
            where Value="40";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1369
            where Value="40 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1370
            where Value="40 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1371
            where Value="40 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1372
            where Value="40.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1373
            where Value="40.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1374
            where Value="40.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1375
            where Value="40.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1376
            where Value="40.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1377
            where Value="40.4";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1378
            where Value="40.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1379
            where Value="40.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1380
            where Value="40.6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1381
            where Value="40.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1382
            where Value="40.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1383
            where Value="40.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1384
            where Value="40.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1385
            where Value="40.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1386
            where Value="40.9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1387
            where Value="40.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1388
            where Value="40/.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1389
            where Value="400";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1390
            where Value="400 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1391
            where Value="400 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1392
            where Value="401";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1393
            where Value="401 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1394
            where Value="402";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1395
            where Value="402 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1396
            where Value="403";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1397
            where Value="403 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1398
            where Value="404";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1399
            where Value="404 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1400
            where Value="405";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1401
            where Value="405 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1402
            where Value="406";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1403
            where Value="406 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1404
            where Value="407";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1405
            where Value="407 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1406
            where Value="408";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1407
            where Value="408 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1408
            where Value="409";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1409
            where Value="409 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1410
            where Value="41";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1411
            where Value="41 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1412
            where Value="41 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1413
            where Value="41.1";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1414
            where Value="41.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1415
            where Value="41.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1416
            where Value="41.3";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1417
            where Value="41.5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1418
            where Value="41.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1419
            where Value="41.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1420
            where Value="410";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1421
            where Value="410 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1422
            where Value="411";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1423
            where Value="411 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1424
            where Value="412";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1425
            where Value="412 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1426
            where Value="413";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1427
            where Value="413 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1428
            where Value="414";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1429
            where Value="414 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1430
            where Value="4140";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1431
            where Value="415";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1432
            where Value="415 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1433
            where Value="416";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1434
            where Value="416 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1435
            where Value="417";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1436
            where Value="417 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1437
            where Value="418";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1438
            where Value="418 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1439
            where Value="419";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1440
            where Value="419 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1441
            where Value="42";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1442
            where Value="42 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1443
            where Value="42 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1444
            where Value="42 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1445
            where Value="42.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1446
            where Value="42.8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1447
            where Value="420";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1448
            where Value="420 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1449
            where Value="421";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1450
            where Value="421 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1451
            where Value="422";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1452
            where Value="422 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1453
            where Value="423";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1454
            where Value="423 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1455
            where Value="424";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1456
            where Value="424 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1457
            where Value="425";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1458
            where Value="425 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1459
            where Value="426";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1460
            where Value="426 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1461
            where Value="427";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1462
            where Value="427 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1463
            where Value="428";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1464
            where Value="428 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1465
            where Value="429";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1466
            where Value="429 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1467
            where Value="43";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1468
            where Value="43 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1469
            where Value="43 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1470
            where Value="43 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1471
            where Value="43.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1472
            where Value="43.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1473
            where Value="430";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1474
            where Value="430 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1475
            where Value="431";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1476
            where Value="431 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1477
            where Value="432";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1478
            where Value="432 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1479
            where Value="433";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1480
            where Value="433 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1481
            where Value="434";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1482
            where Value="434 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1483
            where Value="435";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1484
            where Value="435 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1485
            where Value="436";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1486
            where Value="436 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1487
            where Value="437";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1488
            where Value="437 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1489
            where Value="438";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1490
            where Value="438 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1491
            where Value="439";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1492
            where Value="439 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1493
            where Value="44";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1494
            where Value="44 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1495
            where Value="44 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1496
            where Value="44 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1497
            where Value="44 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1498
            where Value="44.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1499
            where Value="44.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1500
            where Value="440";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1501
            where Value="440 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1502
            where Value="441";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1503
            where Value="441 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1504
            where Value="442";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1505
            where Value="442 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1506
            where Value="443";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1507
            where Value="443 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1508
            where Value="444";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1509
            where Value="444 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1510
            where Value="445";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1511
            where Value="445 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1512
            where Value="446";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1513
            where Value="446 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1514
            where Value="447";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1515
            where Value="447 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1516
            where Value="448";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1517
            where Value="448 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1518
            where Value="449";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1519
            where Value="449 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1520
            where Value="45";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1521
            where Value="45 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1522
            where Value="45 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1523
            where Value="45 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1524
            where Value="45.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1525
            where Value="45.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1526
            where Value="45.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1527
            where Value="450";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1528
            where Value="450 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1529
            where Value="451";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1530
            where Value="451 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1531
            where Value="4510";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1532
            where Value="452";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1533
            where Value="452 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1534
            where Value="453";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1535
            where Value="453 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1536
            where Value="454";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1537
            where Value="454 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1538
            where Value="455";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1539
            where Value="455 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1540
            where Value="456";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1541
            where Value="456 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1542
            where Value="457";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1543
            where Value="457 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1544
            where Value="458";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1545
            where Value="458 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1546
            where Value="459";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1547
            where Value="459 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1548
            where Value="46";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1549
            where Value="46 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1550
            where Value="46 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1551
            where Value="46.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1552
            where Value="460";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1553
            where Value="460 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1554
            where Value="460 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1555
            where Value="461";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1556
            where Value="461 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1557
            where Value="462";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1558
            where Value="462 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1559
            where Value="463";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1560
            where Value="463 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1561
            where Value="464";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1562
            where Value="464 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1563
            where Value="465";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1564
            where Value="465 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1565
            where Value="466";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1566
            where Value="466 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1567
            where Value="467";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1568
            where Value="467 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1569
            where Value="468";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1570
            where Value="468 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1571
            where Value="469";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1572
            where Value="469 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1573
            where Value="47";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1574
            where Value="47 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1575
            where Value="47 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1576
            where Value="47.7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1577
            where Value="47.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1578
            where Value="470";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1579
            where Value="470 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1580
            where Value="471";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1581
            where Value="471 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1582
            where Value="472";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1583
            where Value="472 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1584
            where Value="473";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1585
            where Value="473 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1586
            where Value="474";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1587
            where Value="474 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1588
            where Value="475";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1589
            where Value="475 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1590
            where Value="476";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1591
            where Value="476 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1592
            where Value="477";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1593
            where Value="477 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1594
            where Value="478";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1595
            where Value="478 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1596
            where Value="479";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1597
            where Value="479 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1598
            where Value="48";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1599
            where Value="48 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1600
            where Value="48.2";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1601
            where Value="48.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1602
            where Value="48.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1603
            where Value="480";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1604
            where Value="480 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1605
            where Value="481";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1606
            where Value="481 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1607
            where Value="482";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1608
            where Value="482 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1609
            where Value="483";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1610
            where Value="483 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1611
            where Value="484";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1612
            where Value="484 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1613
            where Value="485";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1614
            where Value="485 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1615
            where Value="486";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1616
            where Value="486 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1617
            where Value="487";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1618
            where Value="487 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1619
            where Value="4870";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1620
            where Value="488";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1621
            where Value="488 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1622
            where Value="4880";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1623
            where Value="489";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1624
            where Value="489 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1625
            where Value="49";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1626
            where Value="49 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1627
            where Value="49 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1628
            where Value="49 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1629
            where Value="49.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1630
            where Value="490";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1631
            where Value="490 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1632
            where Value="491";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1633
            where Value="491 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1634
            where Value="492";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1635
            where Value="492 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1636
            where Value="493";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1637
            where Value="493 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1638
            where Value="494";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1639
            where Value="494 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1640
            where Value="495";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1641
            where Value="495 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1642
            where Value="496";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1643
            where Value="496 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1644
            where Value="497";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1645
            where Value="497 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1646
            where Value="498";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1647
            where Value="498 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1648
            where Value="499";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1649
            where Value="499 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1650
            where Value="5";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1651
            where Value="5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1652
            where Value="5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1653
            where Value="5 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1654
            where Value="5 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1655
            where Value="5.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1656
            where Value="5.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1657
            where Value="5.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1658
            where Value="5.5 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1659
            where Value="5.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1660
            where Value="5.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1661
            where Value="5.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1662
            where Value="5.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1663
            where Value="5.9 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1664
            where Value="5/ .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1665
            where Value="50";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1666
            where Value="50 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1667
            where Value="50 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1668
            where Value="50 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1669
            where Value="50 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1670
            where Value="500";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1671
            where Value="500 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1672
            where Value="5000";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1673
            where Value="501";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1674
            where Value="501 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1675
            where Value="502";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1676
            where Value="502 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1677
            where Value="503";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1678
            where Value="503 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1679
            where Value="504";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1680
            where Value="504 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1681
            where Value="505";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1682
            where Value="505 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1683
            where Value="506";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1684
            where Value="506 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1685
            where Value="507";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1686
            where Value="507 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1687
            where Value="508";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1688
            where Value="508 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1689
            where Value="509";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1690
            where Value="509 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1691
            where Value="51";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1692
            where Value="51 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1693
            where Value="51 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1694
            where Value="510";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1695
            where Value="510 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1696
            where Value="5100";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1697
            where Value="511";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1698
            where Value="511 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1699
            where Value="512";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1700
            where Value="512 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1701
            where Value="513";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1702
            where Value="513 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1703
            where Value="514";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1704
            where Value="514 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1705
            where Value="515";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1706
            where Value="515 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1707
            where Value="516";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1708
            where Value="516 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1709
            where Value="517";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1710
            where Value="517 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1711
            where Value="518";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1712
            where Value="518 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1713
            where Value="519";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1714
            where Value="519 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1715
            where Value="52";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1716
            where Value="52 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1717
            where Value="52 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1718
            where Value="52 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1719
            where Value="520";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1720
            where Value="520 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1721
            where Value="521";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1722
            where Value="521 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1723
            where Value="522";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1724
            where Value="522 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1725
            where Value="523";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1726
            where Value="523 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1727
            where Value="524";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1728
            where Value="524 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1729
            where Value="525";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1730
            where Value="525 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1731
            where Value="526";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1732
            where Value="526 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1733
            where Value="527";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1734
            where Value="527 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1735
            where Value="528";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1736
            where Value="528 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1737
            where Value="529";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1738
            where Value="529 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1739
            where Value="53";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1740
            where Value="53 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1741
            where Value="53 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1742
            where Value="53.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1743
            where Value="530";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1744
            where Value="530 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1745
            where Value="531";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1746
            where Value="531 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1747
            where Value="532";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1748
            where Value="532 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1749
            where Value="533";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1750
            where Value="533 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1751
            where Value="534";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1752
            where Value="534 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1753
            where Value="535";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1754
            where Value="535 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1755
            where Value="536";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1756
            where Value="536 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1757
            where Value="537";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1758
            where Value="537 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1759
            where Value="538";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1760
            where Value="538 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1761
            where Value="539";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1762
            where Value="539 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1763
            where Value="54";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1764
            where Value="54 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1765
            where Value="54 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1766
            where Value="540";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1767
            where Value="540 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1768
            where Value="541";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1769
            where Value="541 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1770
            where Value="542";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1771
            where Value="542 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1772
            where Value="543";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1773
            where Value="543 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1774
            where Value="544";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1775
            where Value="544 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1776
            where Value="545";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1777
            where Value="545 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1778
            where Value="546";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1779
            where Value="546 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1780
            where Value="547";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1781
            where Value="547 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1782
            where Value="548";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1783
            where Value="548 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1784
            where Value="549";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1785
            where Value="549 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1786
            where Value="55";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1787
            where Value="55 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1788
            where Value="55 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1789
            where Value="55.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1790
            where Value="550";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1791
            where Value="550 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1792
            where Value="551";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1793
            where Value="551 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1794
            where Value="552";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1795
            where Value="552 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1796
            where Value="553 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1797
            where Value="554";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1798
            where Value="554 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1799
            where Value="555";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1800
            where Value="555 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1801
            where Value="556";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1802
            where Value="556 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1803
            where Value="557";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1804
            where Value="557 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1805
            where Value="558";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1806
            where Value="558 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1807
            where Value="559";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1808
            where Value="559 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1809
            where Value="56";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1810
            where Value="56 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1811
            where Value="56 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1812
            where Value="560";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1813
            where Value="560 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1814
            where Value="561";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1815
            where Value="561 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1816
            where Value="562";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1817
            where Value="562 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1818
            where Value="563";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1819
            where Value="563 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1820
            where Value="564";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1821
            where Value="564 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1822
            where Value="565";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1823
            where Value="565 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1824
            where Value="566";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1825
            where Value="566 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1826
            where Value="567";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1827
            where Value="567 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1828
            where Value="568";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1829
            where Value="568 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1830
            where Value="569";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1831
            where Value="569 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1832
            where Value="57";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1833
            where Value="57 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1834
            where Value="57 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1835
            where Value="570";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1836
            where Value="570 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1837
            where Value="571";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1838
            where Value="571 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1839
            where Value="572";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1840
            where Value="572 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1841
            where Value="573";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1842
            where Value="573 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1843
            where Value="574";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1844
            where Value="574 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1845
            where Value="575";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1846
            where Value="575 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1847
            where Value="576";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1848
            where Value="576 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1849
            where Value="577";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1850
            where Value="577 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1851
            where Value="578";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1852
            where Value="578 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1853
            where Value="579";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1854
            where Value="579 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1855
            where Value="58";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1856
            where Value="58 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1857
            where Value="58 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1858
            where Value="58 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1859
            where Value="58.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1860
            where Value="580";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1861
            where Value="580 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1862
            where Value="581";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1863
            where Value="581 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1864
            where Value="582";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1865
            where Value="582 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1866
            where Value="583";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1867
            where Value="583 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1868
            where Value="584";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1869
            where Value="584 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1870
            where Value="585";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1871
            where Value="585 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1872
            where Value="586";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1873
            where Value="586 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1874
            where Value="587";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1875
            where Value="587 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1876
            where Value="588";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1877
            where Value="588 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1878
            where Value="589";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1879
            where Value="589 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1880
            where Value="59";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1881
            where Value="59 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1882
            where Value="59 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1883
            where Value="59 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1884
            where Value="59 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1885
            where Value="590";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1886
            where Value="590 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1887
            where Value="591";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1888
            where Value="591 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1889
            where Value="592";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1890
            where Value="592 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1891
            where Value="593";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1892
            where Value="593 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1893
            where Value="594";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1894
            where Value="594 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1895
            where Value="595";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1896
            where Value="595 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1897
            where Value="596";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1898
            where Value="596 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1899
            where Value="597";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1900
            where Value="597 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1901
            where Value="598";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1902
            where Value="598 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1903
            where Value="599";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1904
            where Value="599 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1905
            where Value="6";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1906
            where Value="6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1907
            where Value="6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1908
            where Value="6 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1909
            where Value="6 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1910
            where Value="6 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1911
            where Value="6.02 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1912
            where Value="6.06 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1913
            where Value="6.07 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1914
            where Value="6.1 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1915
            where Value="6.11 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1916
            where Value="6.15 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1917
            where Value="6.16 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1918
            where Value="6.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1919
            where Value="6.2 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1920
            where Value="6.25 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1921
            where Value="6.27 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1922
            where Value="6.28 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1923
            where Value="6.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1924
            where Value="6.3 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1925
            where Value="6.31 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1926
            where Value="6.36 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1927
            where Value="6.37 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1928
            where Value="6.39 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1929
            where Value="6.4 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1930
            where Value="6.42 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1931
            where Value="6.43 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1932
            where Value="6.44 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1933
            where Value="6.45 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1934
            where Value="6.46 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1935
            where Value="6.47 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1936
            where Value="6.49 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1937
            where Value="6.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1938
            where Value="6.5 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1939
            where Value="6.51 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1940
            where Value="6.53 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1941
            where Value="6.54 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1942
            where Value="6.55 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1943
            where Value="6.56 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1944
            where Value="6.58 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1945
            where Value="6.59 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1946
            where Value="6.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1947
            where Value="6.6 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1948
            where Value="6.62 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1949
            where Value="6.64 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1950
            where Value="6.65 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1951
            where Value="6.66 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1952
            where Value="6.67 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1953
            where Value="6.68 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1954
            where Value="6.69 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1955
            where Value="6.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1956
            where Value="6.7 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1957
            where Value="6.71 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1958
            where Value="6.72 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1959
            where Value="6.73 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1960
            where Value="6.75 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1961
            where Value="6.76 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1962
            where Value="6.77 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1963
            where Value="6.78 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1964
            where Value="6.79 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1965
            where Value="6.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1966
            where Value="6.8 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1967
            where Value="6.81 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1968
            where Value="6.82 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1969
            where Value="6.83 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1970
            where Value="6.84 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1971
            where Value="6.85 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1972
            where Value="6.86 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1973
            where Value="6.87 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1974
            where Value="6.88 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1975
            where Value="6.89 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1976
            where Value="6.9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1977
            where Value="6.9 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1978
            where Value="6.91 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1979
            where Value="6.92 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1980
            where Value="6.93 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1981
            where Value="6.94 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1982
            where Value="6.95 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1983
            where Value="6.96 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1984
            where Value="6.964 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1985
            where Value="6.97 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1986
            where Value="6.98 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1987
            where Value="6.99 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1988
            where Value="6/ .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1989
            where Value="60";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1990
            where Value="60 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1991
            where Value="60 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1992
            where Value="60.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1993
            where Value="600";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1994
            where Value="600 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1995
            where Value="601";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1996
            where Value="601 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1997
            where Value="602";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1998
            where Value="602 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1999
            where Value="603";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2000
            where Value="603 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2001
            where Value="604";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2002
            where Value="604 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2003
            where Value="605";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2004
            where Value="605 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2005
            where Value="606";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2006
            where Value="606 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2007
            where Value="607";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2008
            where Value="607 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2009
            where Value="608";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2010
            where Value="608 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2011
            where Value="609";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2012
            where Value="609 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2013
            where Value="61";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2014
            where Value="61 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2015
            where Value="610";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2016
            where Value="610 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2017
            where Value="611";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2018
            where Value="611 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2019
            where Value="612";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2020
            where Value="612 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2021
            where Value="613";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2022
            where Value="613 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2023
            where Value="614";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2024
            where Value="614 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2025
            where Value="615";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2026
            where Value="615 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2027
            where Value="616";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2028
            where Value="616 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2029
            where Value="617";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2030
            where Value="617 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2031
            where Value="618";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2032
            where Value="618 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2033
            where Value="619";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2034
            where Value="619 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2035
            where Value="62";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2036
            where Value="62 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2037
            where Value="62 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2038
            where Value="620";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2039
            where Value="620 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2040
            where Value="621";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2041
            where Value="621 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2042
            where Value="622";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2043
            where Value="622 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2044
            where Value="623";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2045
            where Value="623 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2046
            where Value="624";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2047
            where Value="624 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2048
            where Value="625";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2049
            where Value="625 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2050
            where Value="626";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2051
            where Value="626 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2052
            where Value="627";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2053
            where Value="627 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2054
            where Value="628";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2055
            where Value="628 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2056
            where Value="629";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2057
            where Value="629 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2058
            where Value="63";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2059
            where Value="63 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2060
            where Value="63 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2061
            where Value="63 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2062
            where Value="63 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2063
            where Value="630";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2064
            where Value="630 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2065
            where Value="631";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2066
            where Value="631 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2067
            where Value="632";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2068
            where Value="632 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2069
            where Value="633";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2070
            where Value="633 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2071
            where Value="634";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2072
            where Value="634 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2073
            where Value="635";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2074
            where Value="635 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2075
            where Value="636";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2076
            where Value="636 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2077
            where Value="637 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2078
            where Value="638";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2079
            where Value="638 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2080
            where Value="639";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2081
            where Value="639 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2082
            where Value="64";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2083
            where Value="64 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2084
            where Value="64 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2085
            where Value="640";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2086
            where Value="640 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2087
            where Value="641";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2088
            where Value="641 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2089
            where Value="642";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2090
            where Value="642 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2091
            where Value="643";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2092
            where Value="643 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2093
            where Value="644";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2094
            where Value="644 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2095
            where Value="645";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2096
            where Value="645 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2097
            where Value="646";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2098
            where Value="646 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2099
            where Value="647";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2100
            where Value="647 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2101
            where Value="648";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2102
            where Value="648 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2103
            where Value="649";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2104
            where Value="649 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2105
            where Value="65";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2106
            where Value="65 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2107
            where Value="65 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2108
            where Value="650";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2109
            where Value="650 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2110
            where Value="651";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2111
            where Value="651 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2112
            where Value="652";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2113
            where Value="652 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2114
            where Value="653";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2115
            where Value="653 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2116
            where Value="654";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2117
            where Value="654 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2118
            where Value="655";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2119
            where Value="655 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2120
            where Value="656";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2121
            where Value="656 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2122
            where Value="657";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2123
            where Value="657 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2124
            where Value="658";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2125
            where Value="659";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2126
            where Value="659 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2127
            where Value="66";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2128
            where Value="66 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2129
            where Value="66 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2130
            where Value="66 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2131
            where Value="66.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2132
            where Value="660";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2133
            where Value="660 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2134
            where Value="661";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2135
            where Value="661 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2136
            where Value="662";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2137
            where Value="662 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2138
            where Value="663";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2139
            where Value="663 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2140
            where Value="664";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2141
            where Value="664 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2142
            where Value="665";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2143
            where Value="665 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2144
            where Value="666";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2145
            where Value="666 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2146
            where Value="667";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2147
            where Value="667 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2148
            where Value="668";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2149
            where Value="669";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2150
            where Value="669 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2151
            where Value="67";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2152
            where Value="67 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2153
            where Value="67 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2154
            where Value="67 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2155
            where Value="670";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2156
            where Value="670 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2157
            where Value="671";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2158
            where Value="672";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2159
            where Value="673";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2160
            where Value="674";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2161
            where Value="675";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2162
            where Value="675 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2163
            where Value="676";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2164
            where Value="677";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2165
            where Value="678";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2166
            where Value="68";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2167
            where Value="68 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2168
            where Value="68 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2169
            where Value="680";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2170
            where Value="681";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2171
            where Value="682";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2172
            where Value="683";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2173
            where Value="684";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2174
            where Value="684 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2175
            where Value="685";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2176
            where Value="686";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2177
            where Value="687";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2178
            where Value="687 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2179
            where Value="688";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2180
            where Value="688 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2181
            where Value="69";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2182
            where Value="69 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2183
            where Value="690";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2184
            where Value="691";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2185
            where Value="692";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2186
            where Value="693";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2187
            where Value="694";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2188
            where Value="695";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2189
            where Value="697";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2190
            where Value="698";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2191
            where Value="699";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2192
            where Value="7";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2193
            where Value="7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2194
            where Value="7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2195
            where Value="7 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2196
            where Value="7 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2197
            where Value="7.01 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2198
            where Value="7.02 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2199
            where Value="7.03 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2200
            where Value="7.04 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2201
            where Value="7.05 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2202
            where Value="7.06 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2203
            where Value="7.07 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2204
            where Value="7.08 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2205
            where Value="7.09 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2206
            where Value="7.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2207
            where Value="7.1 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2208
            where Value="7.11 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2209
            where Value="7.12 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2210
            where Value="7.13 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2211
            where Value="7.14 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2212
            where Value="7.15 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2213
            where Value="7.16 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2214
            where Value="7.17 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2215
            where Value="7.18 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2216
            where Value="7.19 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2217
            where Value="7.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2218
            where Value="7.2 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2219
            where Value="7.21 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2220
            where Value="7.22 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2221
            where Value="7.23 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2222
            where Value="7.24 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2223
            where Value="7.25 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2224
            where Value="7.26 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2225
            where Value="7.27 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2226
            where Value="7.28 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2227
            where Value="7.29 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2228
            where Value="7.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2229
            where Value="7.3 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2230
            where Value="7.31 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2231
            where Value="7.32 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2232
            where Value="7.33 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2233
            where Value="7.34 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2234
            where Value="7.35 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2235
            where Value="7.36 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2236
            where Value="7.37 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2237
            where Value="7.38 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2238
            where Value="7.39 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2239
            where Value="7.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2240
            where Value="7.4 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2241
            where Value="7.41 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2242
            where Value="7.42 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2243
            where Value="7.43 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2244
            where Value="7.44 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2245
            where Value="7.45 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2246
            where Value="7.46 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2247
            where Value="7.47 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2248
            where Value="7.48 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2249
            where Value="7.49 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2250
            where Value="7.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2251
            where Value="7.5 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2252
            where Value="7.51 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2253
            where Value="7.52 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2254
            where Value="7.53 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2255
            where Value="7.54 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2256
            where Value="7.55 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2257
            where Value="7.56 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2258
            where Value="7.57 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2259
            where Value="7.58 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2260
            where Value="7.59 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2261
            where Value="7.6 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2262
            where Value="7.61 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2263
            where Value="7.62 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2264
            where Value="7.63 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2265
            where Value="7.64 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2266
            where Value="7.65 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2267
            where Value="7.66 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2268
            where Value="7.67 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2269
            where Value="7.68 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2270
            where Value="7.69 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2271
            where Value="7.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2272
            where Value="7.7 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2273
            where Value="7.71 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2274
            where Value="7.72 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2275
            where Value="7.73 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2276
            where Value="7.74 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2277
            where Value="7.75 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2278
            where Value="7.76 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2279
            where Value="7.77 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2280
            where Value="7.78 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2281
            where Value="7.79 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2282
            where Value="7.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2283
            where Value="7.8 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2284
            where Value="7.81 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2285
            where Value="7.82 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2286
            where Value="7.83 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2287
            where Value="7.84 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2288
            where Value="7.85 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2289
            where Value="7.88 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2290
            where Value="7.89 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2291
            where Value="7.9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2292
            where Value="7.9 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2293
            where Value="7.91 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2294
            where Value="7.92 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2295
            where Value="7.93 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2296
            where Value="7.94 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2297
            where Value="7.95 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2298
            where Value="7.97 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2299
            where Value="7.98 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2300
            where Value="7.99 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2301
            where Value="7/ .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2302
            where Value="70";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2303
            where Value="70 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2304
            where Value="70 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2305
            where Value="70.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2306
            where Value="700";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2307
            where Value="7001";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2308
            where Value="701";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2309
            where Value="703";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2310
            where Value="703 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2311
            where Value="705";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2312
            where Value="706";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2313
            where Value="707";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2314
            where Value="707 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2315
            where Value="709";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2316
            where Value="709 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2317
            where Value="71";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2318
            where Value="71 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2319
            where Value="71 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2320
            where Value="710";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2321
            where Value="712";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2322
            where Value="713";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2323
            where Value="714";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2324
            where Value="715";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2325
            where Value="715 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2326
            where Value="716";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2327
            where Value="717";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2328
            where Value="718";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2329
            where Value="718 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2330
            where Value="719";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2331
            where Value="72";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2332
            where Value="72 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2333
            where Value="720";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2334
            where Value="720 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2335
            where Value="721";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2336
            where Value="721 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2337
            where Value="722";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2338
            where Value="723";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2339
            where Value="723 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2340
            where Value="725";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2341
            where Value="726";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2342
            where Value="726 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2343
            where Value="727";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2344
            where Value="728";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2345
            where Value="729";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2346
            where Value="73";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2347
            where Value="73 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2348
            where Value="730";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2349
            where Value="731 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2350
            where Value="735";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2351
            where Value="736";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2352
            where Value="737";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2353
            where Value="739";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2354
            where Value="74";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2355
            where Value="74 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2356
            where Value="74 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2357
            where Value="74.3 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2358
            where Value="740";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2359
            where Value="741";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2360
            where Value="743";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2361
            where Value="743 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2362
            where Value="744";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2363
            where Value="745";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2364
            where Value="746";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2365
            where Value="748";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2366
            where Value="749";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2367
            where Value="75";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2368
            where Value="75 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2369
            where Value="75 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2370
            where Value="750";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2371
            where Value="751";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2372
            where Value="752";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2373
            where Value="753";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2374
            where Value="755";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2375
            where Value="757";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2376
            where Value="758";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2377
            where Value="76";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2378
            where Value="76 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2379
            where Value="76.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2380
            where Value="760";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2381
            where Value="761";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2382
            where Value="762";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2383
            where Value="763";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2384
            where Value="764";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2385
            where Value="765";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2386
            where Value="766";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2387
            where Value="767";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2388
            where Value="768";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2389
            where Value="769";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2390
            where Value="77";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2391
            where Value="77 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2392
            where Value="77.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2393
            where Value="770";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2394
            where Value="772";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2395
            where Value="773";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2396
            where Value="774";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2397
            where Value="775";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2398
            where Value="78";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2399
            where Value="78 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2400
            where Value="780";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2401
            where Value="781";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2402
            where Value="784";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2403
            where Value="785";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2404
            where Value="786";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2405
            where Value="787";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2406
            where Value="79";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2407
            where Value="79 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2408
            where Value="79.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2409
            where Value="790";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2410
            where Value="794";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2411
            where Value="795";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2412
            where Value="798";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2413
            where Value="799";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2414
            where Value="8";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2415
            where Value="8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2416
            where Value="8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2417
            where Value="8 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2418
            where Value="8 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2419
            where Value="8.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2420
            where Value="8.14 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2421
            where Value="8.27 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2422
            where Value="8.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2423
            where Value="8.35 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2424
            where Value="8.36 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2425
            where Value="8.38 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2426
            where Value="8.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2427
            where Value="8.47 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2428
            where Value="8.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2429
            where Value="8.5 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2430
            where Value="8.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2431
            where Value="8.6 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2432
            where Value="8.67 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2433
            where Value="8.68 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2434
            where Value="8.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2435
            where Value="8.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2436
            where Value="8.9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2437
            where Value="8/ .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2438
            where Value="8/0.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2439
            where Value="80";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2440
            where Value="80 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2441
            where Value="80 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2442
            where Value="80 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2443
            where Value="800";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2444
            where Value="800 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2445
            where Value="803";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2446
            where Value="805";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2447
            where Value="806";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2448
            where Value="807";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2449
            where Value="809";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2450
            where Value="81";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2451
            where Value="81 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2452
            where Value="810";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2453
            where Value="813";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2454
            where Value="815";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2455
            where Value="816";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2456
            where Value="817";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2457
            where Value="818";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2458
            where Value="82";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2459
            where Value="82 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2460
            where Value="82.5 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2461
            where Value="82.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2462
            where Value="820";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2463
            where Value="822";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2464
            where Value="823";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2465
            where Value="825";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2466
            where Value="826";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2467
            where Value="827";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2468
            where Value="829";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2469
            where Value="83";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2470
            where Value="83 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2471
            where Value="83 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2472
            where Value="830";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2473
            where Value="834";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2474
            where Value="835";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2475
            where Value="838";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2476
            where Value="84";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2477
            where Value="84 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2478
            where Value="84 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2479
            where Value="840";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2480
            where Value="841";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2481
            where Value="843";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2482
            where Value="845";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2483
            where Value="847";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2484
            where Value="848";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2485
            where Value="85";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2486
            where Value="85 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2487
            where Value="85 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2488
            where Value="850";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2489
            where Value="851";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2490
            where Value="852";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2491
            where Value="853";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2492
            where Value="854";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2493
            where Value="856";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2494
            where Value="858";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2495
            where Value="86";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2496
            where Value="86 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2497
            where Value="86 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2498
            where Value="86 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2499
            where Value="860";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2500
            where Value="865";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2501
            where Value="866";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2502
            where Value="87";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2503
            where Value="87 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2504
            where Value="87 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2505
            where Value="870";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2506
            where Value="876";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2507
            where Value="88";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2508
            where Value="88 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2509
            where Value="88 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2510
            where Value="88 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2511
            where Value="88.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2512
            where Value="880";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2513
            where Value="885";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2514
            where Value="887";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2515
            where Value="888";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2516
            where Value="889";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2517
            where Value="89";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2518
            where Value="89 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2519
            where Value="89 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2520
            where Value="89 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2521
            where Value="890";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2522
            where Value="894";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2523
            where Value="895";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2524
            where Value="898";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2525
            where Value="899";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2526
            where Value="9";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2527
            where Value="9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2528
            where Value="9 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2529
            where Value="9 mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2530
            where Value="9.1 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2531
            where Value="9.2 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2532
            where Value="9.3 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2533
            where Value="9.38 units";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2534
            where Value="9.4 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2535
            where Value="9.6 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2536
            where Value="9.7 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2537
            where Value="9.8 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2538
            where Value="9/ .";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2539
            where Value="90";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2540
            where Value="90 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2541
            where Value="90 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2542
            where Value="90 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2543
            where Value="90.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2544
            where Value="900";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2545
            where Value="901 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2546
            where Value="906";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2547
            where Value="907";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2548
            where Value="909";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2549
            where Value="91";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2550
            where Value="91 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2551
            where Value="91 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2552
            where Value="91 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2553
            where Value="910";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2554
            where Value="919";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2555
            where Value="92";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2556
            where Value="92 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2557
            where Value="92 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2558
            where Value="92.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2559
            where Value="92.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2560
            where Value="920";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2561
            where Value="920 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2562
            where Value="922";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2563
            where Value="929";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2564
            where Value="93";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2565
            where Value="93 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2566
            where Value="93 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2567
            where Value="93 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2568
            where Value="930";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2569
            where Value="932 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2570
            where Value="935";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2571
            where Value="936";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2572
            where Value="936 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2573
            where Value="938";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2574
            where Value="94";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2575
            where Value="94 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2576
            where Value="94 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2577
            where Value="94.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2578
            where Value="94.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2579
            where Value="940";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2580
            where Value="941";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2581
            where Value="945";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2582
            where Value="95";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2583
            where Value="95 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2584
            where Value="95 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2585
            where Value="95 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2586
            where Value="95.2 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2587
            where Value="95.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2588
            where Value="95.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2589
            where Value="95.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2590
            where Value="950";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2591
            where Value="954";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2592
            where Value="96";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2593
            where Value="96 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2594
            where Value="96 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2595
            where Value="96.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2596
            where Value="96.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2597
            where Value="960";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2598
            where Value="962";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2599
            where Value="963";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2600
            where Value="963 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2601
            where Value="966";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2602
            where Value="967 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2603
            where Value="969 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2604
            where Value="97";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2605
            where Value="97 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2606
            where Value="97 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2607
            where Value="97 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2608
            where Value="97.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2609
            where Value="97.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2610
            where Value="97.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2611
            where Value="970";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2612
            where Value="98";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2613
            where Value="98 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2614
            where Value="98 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2615
            where Value="98 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2616
            where Value="98.1 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2617
            where Value="98.4 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2618
            where Value="98.8 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2619
            where Value="98.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2620
            where Value="980";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2621
            where Value="985";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2622
            where Value="985 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2623
            where Value="987 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2624
            where Value="989";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2625
            where Value="99";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2626
            where Value="99 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2627
            where Value="99 L/min";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2628
            where Value="99 mm Hg";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2629
            where Value="99.6 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2630
            where Value="99.7 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2631
            where Value="99.9 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2632
            where Value="998";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2633
            where Value="998 %";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2634
            where Value="999";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=2
            where Value="ART.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=3
            where Value="CENTRAL VENOUS.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=4
            where Value="CONTROLLED.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=5
            where Value="IMV.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=6
            where Value="INTUBATED.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=7
            where Value="MIX.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=8
            where Value="NOT INTUBATED.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=9
            where Value="NULL";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=10
            where Value="SPONTANEOUS.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=11
            where Value="VEN.";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=1
            where Value="abnormal";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=12
            where Value="mEq/L";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=0
            where Value="normal";
        
            update `mimic-four-377221.E6_BloodGas.bgA5`  
            set Value_Int=13
            where Value="units";
        
##################################################################################

 

    






'''


QUERY = (query1)

query_job = client.query(QUERY)  # API request
print(query_job)



for row in query_job.result():
    print(row)
