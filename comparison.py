#names.csv
#need results from landscan15_final_1.py and landscan20_final_1.py -- this is folder from line 96 and 219


STRR = "BF CD ZM AO ML MZ MW NG ZW BI ET GH SL SN TZ"
africa_prov_countries = STRR.split(" ")

STRR = "ZA GA GH GQ CI SN SZ CG BW NG CM NA KE TG BJ GM AO MR ZW SD GN ZM LR MZ LS TZ ML ET RW UG CD NE SS BI TD MW CF MG BF SL GW"
africa_countries = STRR.split(" ")

error = "1 6 21 89 7 72 4 3 39 36 15 15 52 29 13 12 6 3 5 18 7 5 9 11 29 21 6 2 6 1 12 9 2 1 2 5 25 4 10 43 10 15 19 12 5 16 22 11 6 19 6 11 3 15 33 30 6 5 21 34 2 35 23 1 25 1 20 8 11 9 14 20 23 19 26 24 24 19 9 50 1 20 20 7 15 45 22 50 29 8 0 7 14 34 14 22 52 22 24 25 7 1 10 3 5 12 1 5 21 7 12 3 6 3 1 3 1 1 1 5 37 16 18 10 8 33 24 22 19 19 6 0 19 26 27 2 39 7 8 0 0 3 15 35 21 8 20 32 37 40 11 13 47 34 48 7 31 6 38 46 42 31 0 24 1 8 26 4 13 5 23 29 11 19 44 12 35"
error = error.split(" ")
area = "17098242 9833517 551695 747 270467 726 9984670 1964375 108889 21041 283561 109884 22966 112492 130370 1138914 51100 74177 1285216 2166086 13943 27750 48310 10991 41543 912050 8515770 756102 2780400 214969 1098581 406752 163820 176215 103000 1030000 196722 1240192 11295 245857 36125 71740 111369 323802 242500 70273 505992 92090 446550 2381740 274222 238533 322463 56785 42916 357375 30528 2586 41285 83871 301318 163610 1759540 1267000 923768 112622 475650 28051 964 267668 450295 338145 312685 78867 49035 93028 20273 56594 77474 51197 61 13812 28748 1284000 622984 342000 2344858 1246700 824292 1221037 45227 64589 65300 207595 603628 33850 238391 110879 25713 783562 131957 1002000 1886068 619745 241551 26338 27834 945087 752618 390757 582000 30355 185180 9251 10400 438317 22072 89342 6020 2150000 117600 1104300 580000 118484 801590 17364 2724900 69700 86600 29743 1648195 17818 527968 23200 637657 587041 447400 488100 309500 741 11586 83600 2040 143100 199951 652090 796095 3287263 9596960 298 1564100 147181 38394 143998 65610 676578 513120 329847 1904569 331689 236800 181035 725 300000 5765 7741220 120538 99678 377915 14874 702 490 462840 28896 181 12189 18274"
area = area.split(" ")

prov_study_names ="BF-03 BF-01 BF-07 BF-11 BF-04 BF-05 BF-06 BF-08 BF-10 BF-02 BF-09 BF-12 BF-13 CD-KN CD-BC CD-EQ CD-NK CD-MA CD-SK CD-KA CD-KE ML-1 ML-2 ML-3 ML-4 ML-5 ML-BKO MZ-A MZ-P MZ-N MZ-Q MZ-T MZ-B MZ-S MZ-I MZ-G MZ-L MZ-MPM NG-PL NG-FC NG-BE NG-KO NG-KW NG-NA NG-NI NG-AD NG-BA NG-BO NG-GO NG-TA NG-YO NG-JI NG-KD NG-KN NG-KT NG-KE NG-SO NG-ZA NG-AB NG-AN NG-EB NG-EN NG-IM NG-EK NG-LA NG-OG NG-ON NG-OS NG-OY NG-AK NG-BY NG-CR NG-DE NG-ED NG-RI ZM-07 ZM-02 ZM-01 ZM-08 ZM-03 ZM-04 ZM-09 ZM-10 ZM-05 ZM-06 ZW-MC ZW-ME ZW-MW ZW-MN ZW-MS ZW-MI ZW-MV ZW-HA ZW-BU"
prov_study = "55.3 4.6 4.8 7.7 7.7 2 14.6 4.6 10.6 18.2 40.5 7.5 13.2 90 13.5 1.9 8.7 9 6.2 26.4 0.9 32.6 36.2 31 28.5 15.1 89.2 17.6 16.7 14.8 11.4 8.3 24.7 28 16 37.5 62.6 93.3 19.2 70 23 71.2 56.5 27.3 39.1 13.1 30.2 69.1 55.4 16.7 43.4 18.7 39.3 34.6 29.6 32.2 18.5 34.4 90.6 84.4 51.7 66.2 81.3 81.9 99.6 65.6 56.9 81.2 62.2 78.7 70.5 53 73.1 89.3 64.3 16.7 14.2 6.3 54 6.3 4.7 70.8 9.2 7 12.3 12.3 18.2 29.4 17.2 17.2 30.1 22.1 76.2 96.7"

prov_2015 = "87.7 55.1 81.3 96.7 65.5 54 38.3 82.4 88.2 90 80.3 97.5 48.1 95.6 58.1 69.6 57 80.2 75 51.4 79.1 85.5 99.8 96.6 42.6 68.5 39.7 50 95.4 20.4 3.4 67.1 87.3 88.5 66.5 36.1 21.9 79.6 35.2 21 36.5 27.5 38 23.5 6.5 21 33.6 51.8 33.3 15.9 24.8 35.8 100 100 99.9 100 100 100 99.8 100 99.7 100 100 47.6 69.8 43 61 43.8 60.8 15.5 34.1 39.9 91.5 29.3 6.6 25.6 47.4 19.4 26.3 30.6 55.9 4.5 4.4 5.6 5.5 1.2 12.2 5.1 8.2 16.7 11.8 69.6 7.1 3.3 2.2 9.8 7.7 1.5 6.3 2.2 3.8 2.2 1.8 2.6 7.3 4.3 3.4 77.6 46.7 36.5 48.4 31.7 84.3 99.6 46.8 30.7 40.9 40.8 26.6 46.4 26.4 44.1 14 59.7 63 59 74.4 44.2 54.5 2.1 10.3 3.7 3.5 10.1 4.5 1.6 2.4 1.8 16.4 6.4 5.7 2 0.9 5.4 99.9 78.9 86.2 95 99.8 99.6 97.3 95.9 98.5 97.5 99.4 99.6 98.6 95 99.1 99.4 99.8 99.7 98.5 99.4 86.6 99.6 95.4 92.9 87.7 99.6 97.8 48.9 98.3 81.2 93.4 98.9 39.2 64 53.6 6.6 29.7 7.4 4.6 6 18.7 20.1 90.5 14.6 0.7 2.1 7.9 10 9.2 7.4 29.1 0.9 1.2 31.1 22.6 18.4 16.9 13.5 18 13.7 38.3 75 99.8 64.7 57.3 69.6 83.5 92 87.7 77.6 82.3 69.4 69.8 78.8 93.3 81.9 70.9 83.2 77 59.9 65.2 46.7 71.5 70.3 98.6 90.5 98.2 95.3 96.4 89.4 95.2 95.7 94.1 93.9 92.8 91.6 80.7 80.9 72.2 50 70.3 77.8 85.7 78.7 82.9 90.5 93.8 21 8.2 9.4 24.7 5.3 9.6 4.4 99.8 98.9 99.5 99.6 91.2 90.9 96.3 72.6 97.8 60 81.1 86.6 78.3 92.8 91.8 96 96.7 99.4 92.8 99.8 96.2 93.5 98.2 99.2 99 97.2 99.6 100 99.8 99.2 98.9 99.5 99.4 99.6 99.4 99.2 99.5 99.5 99.6 99.7 99.5 99.2 99.3 99.7 99.9 99.9 98.8 99.9 99.8 100 17.3 26.6 30.6 43.3 28.6 11.8 19.5 28 6.8 6.6 25.5 4.5 2.1 0.4 3.2 2.1 7.7 3.1 2.7 3.1 0.5 2 0.8 0.1 0.7 7.9 8.4 4.1 14.9 12.5 44.7 1.3 4 5.9 3.3 6 6.1 5.4 4.2 4 7 7.9 13 3.7 7.4 2.7 6.9 40.2 11.7 16.9 31.6 35.4 33.2 31.9 14.2 90.3 21.2 19.9 17.9 12.1 10 27.2 27.3 17.3 42.8 69.3 94.8 73.1 87.1 54.3 42.6 44.4 67.9 60.1 31.6 48.5 74.9 61.5 89.9 59.7 38.3 59.4 9.6 11.1 30.9 24.7 48.8 35 74.3 79.4 75.6 81.9 73.6 73.5 6.4 10.1 9.6 39.2 11.2 8 31.6 69.6 22.9 67.1 51 20.3 37.4 17.1 14.4 39.2 63.9 61.2 17.4 45.9 21.9 38.7 38.9 33.2 30.3 18 36.4 90.6 88.7 46.2 72.1 81.8 82.1 99.7 64.3 57.5 80.9 65.8 78.4 69.3 52.8 77 88 64 94.6 90.6 97.5 77.8 95.4 98.3 68.4 91.3 73.1 81 97.5 92 90.7 98 81.8 82.7 89.1 93 82.7 97.7 88 77.3 98.5 69.8 94.4 91.6 79 85.5 99.1 97.9 93.7 92.5 84.4 95.1 77.7 84.3 83.2 84.3 74.8 53.3 85 16.8 20.1 20.4 11.3 71.4 97.7 69.9 59.8 21.1 46.2 50.6 49.9 67.2 30.6 22.4 50.7 57.3 33.5 29.4 9.4 7.7 12.3 60.2 80 91.7 83.4 100 98.3 99.5 19.8 6.7 12 8 39.4 29.6 27.6 6.1 4.2 10.4 27.6 7 9.7 14 75.9 19.4 8.8 11.7 13.2 17.5 3.4 3.6 14.7 7.1 18.5 35.4 82.5 22.9 28.6 68.5 58.2 85.2 76.3 65.5 97.2 49.2 70.7 84.6 64.6 90.5 73 66.8 25.9 27.5 39.5 25.2 11.4 10.7 26.6 10.9 88 93.2 85.3 78.1 63.2 44.1 63.3 91.3 74.6 95.4 81.9 79.3 99.4 68.5 88.4 70.8 98.7 69.1 43.1 14.9 6.7 5.5 7.3 54.8 5.3 72.2 12.2 9.4 12 15.6 11.8 16.8 25.5 12.4 13.1 24.3 20 76.5 96.3"
prov_2015_names = "AF-KAB AF-KAP AF-PAR AF-WAR AF-LOG AF-NAN AF-LAG AF-PAN AF-BGL AF-BAM AF-GHA AF-PKA AF-PIA AF-KHO AF-KNR AF-NUR AF-BDS AF-TAK AF-KDZ AF-SAM AF-BAL AF-SAR AF-GHO AF-DAY AF-URU AF-ZAB AF-KAN AF-JOW AF-FYB AF-HEL AF-BDG AF-HER AF-FRA AF-NIM AO-CAB AO-ZAI AO-UIG AO-LUA AO-CNO AO-CUS AO-MAL AO-LNO AO-BGU AO-HUA AO-BIE AO-MOX AO-CCU AO-NAM AO-HUI AO-CNN AO-LSU AO-BGO AM-AG AM-AR AM-AV AM-GR AM-LO AM-KT AM-SH AM-SU AM-VD AM-TV AM-ER BD-06 BD-10 BD-60 BD-27 BD-55 BD-54 BJ-AK BJ-DO BJ-AQ BJ-LI BJ-BO BJ-AL BJ-MO BJ-OU BJ-PL BJ-ZO BJ-CO BF-03 BF-01 BF-07 BF-11 BF-04 BF-05 BF-06 BF-08 BF-10 BF-02 BF-13 BI-BM BI-BB BI-BR BI-CA BI-CI BI-GI BI-KR BI-KY BI-KI BI-MA BI-MU BI-MY BI-MW BI-NG BI-RT BI-RY KH-1 KH-3 KH-4 KH-5 KH-6 KH-8 KH-12 KH-14 KH-15 KH-20 KH-17 KH-22 CM-ES CM-NO CM-AD CM-EN CM-CE CM-SU CM-OU CM-LT CM-NW CM-SW TD-CB TD-GR TD-HL TD-KA TD-LO TD-LR TD-MA TD-ME TD-MO TD-MC TD-OD TD-SA TD-TA TD-WF TD-BG CO-DC CO-LAG CO-CES CO-MAG CO-ATL CO-SAP CO-BOL CO-SUC CO-COR CO-NSA CO-SAN CO-BOY CO-CUN CO-MET CO-ANT CO-CAL CO-RIS CO-QUI CO-TOL CO-HUI CO-CAQ CO-VAC CO-CAU CO-NAR CO-CHO CO-ARA CO-CAS CO-GUA CO-VID CO-AMA CO-PUT CO-GUV CO-VAU CG-BZV CG-16 CG-2 CG-11 CG-12 CG-14 CG-15 CG-13 CG-7 CD-KN CD-BC CD-BN CD-EQ CD-OR CD-NK CD-MA CD-SK CD-KA CD-KE CD-KW ET-TI ET-AF ET-AM ET-OR ET-SO ET-BE ET-SN ET-GA ET-HA ET-AA ET-DD GA-6 GA-9 GA-7 GA-2 GA-1 GA-3 GA-8 GA-4 GA-5 GH-WP GH-AA GH-TV GH-EP GH-AH GH-BA GH-NP GH-UW GH-UE GH-CP GT-PE GT-GU GT-PR GT-SA GT-CM GT-ES GT-SR GT-SO GT-TO GT-QZ GT-SU GT-RE GT-SM GT-HU GT-QC GT-BV GT-AV GT-PE GT-IZ GT-ZA GT-CQ GT-JA GT-JU GN-C GN-B GN-FA GN-KA GN-KD GN-LA GN-MM GN-NZ IN-DL IN-HR IN-HP IN-PB IN-RJ IN-MP IN-CT IN-UP IN-UT IN-BR IN-JH IN-OR IN-AS IN-MN IN-ML IN-MZ IN-NL IN-SK IN-TR IN-GA IN-GJ IN-MH IN-KA IN-KL IN-TN IN-AN IN-CH IN-LD IN-PY IN-AP IN-TG JO-AM JO-BA JO-AZ JO-MD JO-IR JO-MA JO-JA JO-AJ JO-KA JO-AT JO-MN JO-AQ KG-GB KG-Y KG-J KG-N KG-B KG-T KG-C LS-B LS-C LS-D LS-A LS-E LS-F LS-G LS-H LS-J LS-K LR-MO LR-SI LR-GG LR-BM LR-CM LR-GP LR-MG LR-GB LR-RI LR-RG LR-GK LR-MY LR-LO LR-BG LR-NI MW-CT MW-KR MW-MZ MW-RU MW-NB MW-LK MW-DE MW-DO MW-KS MW-MC MW-SA MW-BA MW-CK MW-CR MW-MH MW-MG MW-MU MW-MW MW-NE MW-NS MW-PH MW-TH MW-BL MW-ZO MW-LI ML-1 ML-2 ML-3 ML-4 ML-5 ML-BKO MZ-A MZ-P MZ-N MZ-Q MZ-T MZ-B MZ-S MZ-I MZ-G MZ-L MZ-MPM MM-11 MM-12 MM-13 MM-14 MM-01 MM-05 MM-02 MM-03 MM-04 MM-15 MM-16 MM-06 MM-17 MM-07 MM-18 NA-OS NA-OW NA-ON NA-OT NA-KU NA-OH NA-OD NA-ER NA-KH NA-HA NA-KA NE-8 NE-3 NE-4 NE-5 NE-1 NE-6 NE-7 NE-2 NG-FC NG-BE NG-KO NG-KW NG-NA NG-NI NG-PL NG-AD NG-BA NG-BO NG-GO NG-TA NG-YO NG-JI NG-KD NG-KN NG-KT NG-KE NG-SO NG-ZA NG-AB NG-AN NG-EB NG-EN NG-IM NG-EK NG-LA NG-OG NG-ON NG-OS NG-OY NG-AK NG-BY NG-CR NG-DE NG-ED NG-RI PK-PB PK-SD PK-KP PK-BA PK-GB PK-IS PE-LOR PE-JUN PE-HUC PE-PAS PE-ARE PE-ANC PE-PIU PE-TUM PE-APU PE-CUS PE-MDD PE-MOQ PE-PUN PE-TAC PE-AYA PE-HUV PE-ICA PE-CAJ PE-LAM PE-LAL PE-SAM PE-UCA PE-LIM PH-00 PH-15 PH-01 PH-02 PH-03 PH-41 PH-05 PH-08 PH-07 PH-10 PH-14 PH-13 RW-03 RW-02 RW-04 RW-05 RW-01 SN-DK SN-TH SN-DB SN-KA SN-KL SN-LG SN-FK SN-ZG SN-SE SN-KD SN-MT SN-SL SN-KE SN-TC SL-E SL-N SL-S SL-W ZA-EC ZA-GT ZA-MP TJ-DU TJ-SU TJ-KT TZ-18 TZ-24 TZ-22 TZ-08 TZ-09 TZ-25 TZ-01 TZ-26 TZ-03 TZ-23 TZ-04 TZ-20 TZ-05 TZ-13 TZ-02 TZ-16 TZ-12 TZ-17 TZ-21 TZ-29 TZ-30 TZ-27 TZ-14 TZ-28 TZ-07 TZ-11 TZ-15 TZ-06 TZ-10 TL-AL TL-AN TL-BA TL-BO TL-CO TL-DI TL-ER TL-LI TL-LA TL-MF TL-MT TL-OE TL-VI TG-P TG-M TG-C TG-K TG-S UG-E UG-W UG-W YE-IB YE-AB YE-BA YE-TA YE-JA YE-HJ YE-HU YE-HD YE-DH YE-SH YE-SD YE-SN YE-AD YE-LA YE-MA YE-MW YE-MR YE-AM YE-RA ZM-07 ZM-01 ZM-03 ZM-05 ZM-08 ZM-04 ZM-09 ZM-06 ZM-10 ZM-02 ZW-MA ZW-MC ZW-ME ZW-MW ZW-MN ZW-MS ZW-MI ZW-MV ZW-HA ZW-BU"
prov_2020 = "58.6 83 76.9 86.9 65.4 87.9 91 76.5 20.4 36.3 42.9 87.1 24.8 23.6 33.9 48.5 25.2 34.4 32.7 59.1 4.8 8.8 5.4 9.9 7 7.2 5.1 8.8 18.1 4.8 42.4 27.5 43.3 17.9 56.2 65.6 79.4 84.4 56.5 98.4 44.9 22.2 27.2 27.7 10.2 21.1 31.6 40.1 80.8 98.8 72.2 87.2 97 83.6 88.5 84.8 67.9 67.8 56.5 43.4 87.3 97.7 38.9 29.5 50 45.1 27.5 33 21.2 99.9 99.6 99.5 99.7 98.1 98.4 98.8 91 99.6 96.3 94.3 97 92.6 98.1 91.9 98.2 98.5 99.3 98.2 100 97.6 97.8 99.1 99.6 99.3 97.6 99.8 99.8 99.9 99.5 99.6 99.3 52.1 6.3 11.3 8.6 16.8 5 7.9 11.3 4.3 3.1 7 19.9 13.1 2.9 4.8 38.9 51 56.5 48.6 18.6 92.3 12.5 18.8 25.4 25.8 21.7 44.3 53.8 95.6 23.3 18.1 87.2 11.4 13.9 31.5 16.3 13.5 27.3 31.7 26.2 47.8 78.7 97.4 77.3 41.3 58.7 75.9 59.3 52.2 41.1 42.7 36.4 47.1 45.3 20.7 31.2 27.8 63.7 55.4 46.5 34 34.5 36.9 91.1 83.9 25.3 64.3 54.5 59.5 98.9 92.5 54.7 78.7 76.2 74.7 48.8 53.4 72.9 72.6 81.8 94.8 87.4 94.9 85.9 100 97.3 99 96.4 97.3 96.9 96.9 86.7 89 93.7 91.5 86.3 82 88.5 33.9 43.4 42.7 38.2 89.1 8.2 64.9 11 13.5 7.8 98.5 100 99.2 34.3 44.1 39.1 28.9 15.1 95.3 23.8 56.5 25.3 19.8 11.6 15.8 11.9 62.2 12.3 76.9 18.9 12.8 23.2"
prov_2020_names = "BD-06 BD-10 BD-60 BD-27 BD-55 BD-54 BD-13 BD-34 BJ-AK BJ-DO BJ-AQ BJ-LI BJ-BO BJ-AL BJ-MO BJ-OU BJ-PL BJ-ZO BJ-CO BF-03 BF-01 BF-07 BF-11 BF-04 BF-05 BF-06 BF-08 BF-10 BF-02 BF-13 CM-ES CM-NO CM-AD CM-EN CM-CE CM-SU CM-OU CM-LT CM-NW CM-SW ET-TI ET-AF ET-AM ET-OR ET-SO ET-BE ET-SN ET-GA ET-HA ET-AA ET-DD GH-WP GH-AA GH-TV GH-EP GH-AH GH-BA GH-NP GH-UW GH-UE GH-CP GN-C GN-B GN-FA GN-KA GN-KD GN-LA GN-MM GN-NZ IN-DL IN-HR IN-HP IN-PB IN-RJ IN-MP IN-CT IN-UP IN-UT IN-BR IN-JH IN-OR IN-AS IN-MN IN-ML IN-MZ IN-NL IN-SK IN-TR IN-GA IN-GJ IN-MH IN-KA IN-KL IN-TN IN-AN IN-CH IN-LD IN-PY IN-AP IN-TG IN-JK LR-MO LR-SI LR-GG LR-BM LR-CM LR-GP LR-MG LR-GB LR-RI LR-RG LR-GK LR-MY LR-LO LR-BG LR-NI ML-1 ML-2 ML-3 ML-4 ML-5 ML-BKO MR-01 MR-02 MR-03 MR-04 MR-05 MR-06 MR-07 MR-08 MR-09 MR-10 MR-11 MZ-A MZ-P MZ-N MZ-Q MZ-T MZ-B MZ-S MZ-I MZ-G MZ-L MZ-MPM NG-FC NG-BE NG-KO NG-KW NG-NA NG-NI NG-PL NG-AD NG-BA NG-BO NG-GO NG-TA NG-YO NG-JI NG-KD NG-KN NG-KT NG-KE NG-SO NG-ZA NG-AB NG-AN NG-EB NG-EN NG-IM NG-EK NG-LA NG-OG NG-ON NG-OS NG-OY NG-AK NG-BY NG-CR NG-DE NG-ED NG-RI PK-PB PK-SD PK-KP PK-BA PK-GB PK-IS PH-00 PH-15 PH-01 PH-02 PH-03 PH-41 PH-05 PH-08 PH-07 PH-10 PH-14 PH-13 RW-03 RW-02 RW-04 RW-05 RW-01 SL-S SL-W SL-E SL-N SL-NW TJ-DU TJ-SU TJ-KT TG-P TG-M TG-C TG-K TG-S UG-102 UG-E UG-W UG-N ZM-07 ZM-01 ZM-03 ZM-05 ZM-08 ZM-04 ZM-09 ZM-06 ZM-10 ZM-02"

prov_2015 = prov_2015.split(" ")
prov_2015_names = prov_2015_names.split(" ")
prov_2020 = prov_2020.split(" ")
prov_2020_names = prov_2020_names.split(" ")

prov_2015_dict = {}
for i,j in zip(prov_2015_names, prov_2015):
    prov_2015_dict[i] = j
prov_2020_dict = {}
for i,j in zip(prov_2020_names, prov_2020):
    prov_2020_dict[i] = j

import csv

prov_study = prov_study.split(" ")
prov_study_names = prov_study_names.split(" ")
prov_study_dict = {}
for i,j in zip(prov_study_names, prov_study):
    prov_study_dict[i] = j

names = []
# opening the CSV file
with open('elec/census/names.csv', mode ='r')as file:
  # reading the CSV file
    csvFile = csv.reader(file)
  # displaying the contents of the CSV file
    for lines in csvFile:
        for i in lines:
            names.append(i)

area_dict = {}
for i,j in zip(names,error):
    area_dict[i] = j

area_dictf = {}
for i,j in zip(names,area):
    area_dictf[i] = j
area_dictf


areaf = {}
for i,j in area_dictf.items():
    for k,l in country_census_names.items():
        if i == k:
            areaf[l] = j
            
areaf


import matplotlib.pyplot as plt
import random
no_of_colors=41
color=["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(no_of_colors)]
    
together = {}
for i,j in zip(set(lst), color):
    together[i] = j
together

colors = []
for k in lst:
    for i,j in together.items():
        if i == k:
            colors.append(j)
            
len(colors)


plt.figure(figsize=(7,7),dpi=1000)
elec_2015 = {}

for i in glob.glob("elec/results/final_2015/*"):
    with open(f'{i}',"r") as file:
        jsonData = json.load(file)
        for key, value in jsonData.items():
            if (key[:2] in africa_countries):
                if key[:2] in elec_2015:
                    elec_2015[key[:2]] = [elec_2015[key[:2]][0] + value[0], elec_2015[key[:2]][1] + value[1]]
                else:
                    elec_2015[key[:2]] = value

for i,j in elec_2015.items():
    if j[0] != 0 and j[1] != 0:
        elec_2015[i] = round((j[0]/j[1])*100,1)
        
final = {}
for i,j in elec_2015.items():
    if type(j) == float:
        final[i] = j
final
        
census = {}
for i,j in country_2015_census.items():
    if i in final:
        census[i] = j
        
        
         
af_2015_prov2 = {}
af_2015_elec2 = {}
for key, value in sorted(final.items()):
    af_2015_elec2[key] = value
for key, value in sorted(census.items()): 
    af_2015_prov2[key] = value
af_elec, af_prov = [], []
for i,j in zip(af_2015_elec2.values(),af_2015_prov2.values()):
    af_elec.append(i)
    af_prov.append(float(j))

lst = []
for i in af_2015_prov2.keys():
    lst.append(i[:2])

af_elec, af_prov = [], []
for i,j in zip(af_2015_elec2.values(),af_2015_prov2.values()):
    af_elec.append(i)
    af_prov.append(float(j))
    


x = np.array(af_elec)
y = np.array(af_prov)


#use green as color for individual points
area_plot = {}
for i in areaf.keys():
    if i in africa_countries:
        area_plot[i] = areaf[i]

areap = {}
for key, value in sorted(area_plot.items()):
    areap[key] = int(value)/1000
b2 = [i for i in areap.values()]
        
plt.scatter(x, y,s=b2,c=colors)

full_lst = []
for i,j in country_census_names.items():
    for k in set(lst):
        if j == k:
            full_lst.append(i)

x = np.array(x).reshape((-1, 1))
y = np.array(y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
plt.rc('font', size=25) 
#plt.title(f"2015 sub-Saharan Africa: R\u00b2 = {round(r_sq,2)}")
plt.annotate("R\u00b2= {:.2f}".format(r_sq), (60, 90),color='blue')
plt.xlabel('Prediction')
plt.ylabel('Country Census')
plt.xlim(0,100) 
plt.ylim(0,100)
plt.plot((0,100),(0,100), 'k-', alpha=0.75, zorder=0)

markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in together.values()]
final = []
for i in together.keys():
    for j,k in country_census_names.items():
        if i == k:
            final.append(j)
plt.rcParams['legend.fontsize'] = 13
plt.legend(markers, final, numpoints=1,bbox_to_anchor=(1.1,1),ncol=2, markerscale=3)
plt.savefig("elec/sub_saharan_country_2015.pdf",bbox_inches="tight")
plt.show()


color = ['#00B7FF',
 '#004DFF',
 '#00FFFF',
 '#FF00FF',
 '#00FF00',
 '#C500FF',
 '#FFCA00',
 '#969600',
 '#B4A2FF',
 '#C20078',
 '#0000C1',
 '#FF8B00',
 '#FFC8FF',
 '#666666',
 '#FF0000',
 '#CCCCCC',
 '#009E8F',
 '#8200FF',
 '#960000',
 '#BBFF00',
 '#FFFF00',
 '#006F00']


 elec_2015 = {}
for i in glob.glob("1lmin_2020/*"):
    with open(f'{i}',"r") as file:
        jsonData = json.load(file)
        for key, value in jsonData.items():
            if key in prov_2020_names:
                if key in elec_2015:
                    elec_2015[key] = [elec_2015[key][0] + value[0], elec_2015[key][1] + value[1]]
                else:
                    elec_2015[key] = value

for i,j in elec_2015.items():
    if j[0] != 0 and j[1] != 0:
        elec_2015[i] = round((j[0]/j[1])*100,1)

final = {}
for i,j in elec_2015.items():
    if type(j) == float:
        final[i] = j
        
census = {}
for i,j in prov_2020_dict.items():
    if f"{i}" in final:
        census[f"{i}"] = j 
        
af_2015_prov2 = {}
af_2015_elec2 = {}
for key, value in sorted(final.items()):
    af_2015_elec2[key] = value
for key, value in sorted(census.items()): 
    af_2015_prov2[key] = value

    
lst = []
for i in af_2015_prov2.keys():
    lst.append(i[:2])
    
af_elec, af_prov = [], []
for i,j in zip(af_2015_elec2.values(),af_2015_prov2.values()):
    af_elec.append(i)
    af_prov.append(float(j))

x = np.array(af_elec)
y = np.array(af_prov)
  
together = {}
for i,j in zip(set(lst), color):
    together[i] = j

colors = []
for k in lst:
    for i,j in together.items():
        if i == k:
            colors.append(j)


area_plot = {}
for i in areaf.keys():
    if i in lst:
        area_plot[i] = areaf[i]

areap = {}
for key, value in sorted(area_plot.items()):
    if key == 'IN':
        areap[key] = int(value)/13000
    else:
        areap[key] = int(value)/4000

sizes = []
for k in lst:
    for i,j in areap.items():
        if i == k:
            sizes.append(j)

           
plt.figure(figsize=(7,7),dpi=1000)
#use green as color for individual points
plt.scatter(x, y,c=colors,s=sizes)


full_lst = []
for i,j in country_census_names.items():
    for k in set(lst):
        if j == k:
            full_lst.append(i)

x = np.array(x).reshape((-1, 1))
y = np.array(y)
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
#plt.title(f"2020 Global Provinces: R\u00b2 = {round(r_sq,1)}")
plt.annotate("R\u00b2= {:.2f}".format(r_sq), (6, 90),color='blue')
plt.xlabel('Prediction')
plt.ylabel('Province Census')
plt.xlim(-1,101) 
plt.ylim(-1,101)
plt.plot((0,100),(0,100), 'k-', alpha=0.75, zorder=0)

markers = [plt.Line2D([0,0],[0,0],color=color, marker='o', linestyle='') for color in together.values()]
final = []
for i in together.keys():
    for j,k in country_census_names.items():
        if i == k:
            final.append(j)
plt.rcParams['legend.fontsize'] = 15
plt.legend(markers, final, numpoints=1,bbox_to_anchor=(1.1,1),ncol=1, markerscale=3)
#plt.savefig("elec/global_province_2020.pdf",bbox_inches="tight")
plt.show()