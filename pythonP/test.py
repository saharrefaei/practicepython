# years = [2015, 2016, 2017, 2018, 2019, 2020]

# sales = [350000, 400000, 410000, 439000, 500000, 290000]


# Dictionary=dict(zip(years,sales))

# print(Dictionary)

#-------------

#     words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# dictionary ={}

# for i in words :
#     length = len(i)
#     dictionary[i] = length
    
#     print(dictionary)

#-------------

# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}
# sortedKey = sorted(d1.items())
# print(sortedKey)

# sortedlist = {}
# for key, value in sortedKey:
#     sortedlist[key]=value

#-------------

# d1 = {'x': 5, 'a': 3, 'c': 2, 'b': 0}

# for k in sorted(d1.keys()):
#     print(f'{k} -> {d1[k]}')

#-------------
# employees = {
#     'John': ('London', 4000, 28), 
#     'Maria':('Zagreb', 3800, 40), 
#     'Diana': ('NYC', 3500, 31)
#              }

# sortiation = sorted(employees.items() , key=lambda item:item [0] , reverse=True)
# print(sortiation)

#-------------
# COUNTRY = {
# "MX":"MEXICO",
# "RW":"RWANDA",
# "BI":"BURUNDI",
# "PR":"PUERTO RICO",
# "GM":"GAMBIA",
# "SR":"SURINAME",
# "KG":"KYRGYZSTAN",
# "GA":"GABON",
# "CK":"COOK ISLANDS",
# "VN":"VIET NAM",
# "UZ":"UZBEKISTAN",
# "BG":"BULGARIA",
# "JP":"JAPAN",
# "KP":"KOREA, DEMOCRATIC PEOPLE'S REPUBLIC OF",
# "PL":"POLAND",
# "BB":"BARBADOS",
# "CF":"CENTRAL AFRICAN REPUBLIC",
# "GI":"GIBRALTAR",
# "AE":"UNITED ARAB EMIRATES",
# "MY":"MALAYSIA",
# "KI":"KIRIBATI",
# "RU":"RUSSIAN FEDERATION",
# "MQ":"MARTINIQUE",
# "SB":"SOLOMON ISLANDS",
# "TL":"TIMOR-LESTE",
# "VI":"VIRGIN ISLANDS, U.S.",
# "FR":"FRANCE",
# "ZA":"SOUTH AFRICA",
# "NE":"NIGER",
# "IE":"IRELAND",
# "MG":"MADAGASCAR",
# "TC":"TURKS AND CAICOS ISLANDS",
# "BW":"BOTSWANA",
# "KY":"CAYMAN ISLANDS",
# "JO":"JORDAN",
# "MR":"MAURITANIA",
# "NI":"NICARAGUA",
# "KM":"COMOROS",
# "FK":"FALKLAND ISLANDS (MALVINAS)",
# "SH":"SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA",
# "PF":"FRENCH POLYNESIA",
# "DK":"DENMARK",
# "PT":"PORTUGAL",
# "NR":"NAURU",
# "DM":"DOMINICA",
# "GH":"GHANA",
# "GP":"GUADELOUPE",
# "CU":"CUBA",
# "GR":"GREECE",
# "AS":"AMERICAN SAMOA",
# "AI":"ANGUILLA",
# "LS":"LESOTHO",
# "TJ":"TAJIKISTAN",
# "AW":"ARUBA",
# "GY":"GUYANA",
# "LC":"SAINT LUCIA",
# "GG":"GUERNSEY",
# "TG":"TOGO",
# "OM":"OMAN",
# "NL":"NETHERLANDS",
# "MT":"MALTA",
# "MD":"MOLDOVA, REPUBLIC OF",
# "EC":"ECUADOR",
# "FM":"MICRONESIA, FEDERATED STATES OF",
# "CA":"CANADA",
# "TT":"TRINIDAD AND TOBAGO",
# "CN":"CHINA",
# "CM":"CAMEROON",
# "BD":"BANGLADESH",
# "LK":"SRI LANKA",
# "CO":"COLOMBIA",
# "LT":"LITHUANIA",
# "DJ":"DJIBOUTI",
# "CX":"CHRISTMAS ISLAND",
# "TF":"FRENCH SOUTHERN TERRITORIES",
# "TM":"TURKMENISTAN",
# "SC":"SEYCHELLES",
# "MK":"MACEDONIA, THE FORMER YUGOSLAV REPUBLIC OF",
# "TH":"THAILAND",
# "LA":"LAO PEOPLE'S DEMOCRATIC REPUBLIC",
# "BE":"BELGIUM",
# "UY":"URUGUAY",
# "MV":"MALDIVES",
# "SZ":"SWAZILAND",
# "MN":"MONGOLIA",
# "PK":"PAKISTAN",
# "BZ":"BELIZE",
# "AT":"AUSTRIA",
# "WF":"WALLIS AND FUTUNA",
# "GD":"GRENADA",
# "RO":"ROMANIA",
# "SJ":"SVALBARD AND JAN MAYEN",
# "CV":"CAPE VERDE",
# "UG":"UGANDA",
# "CR":"COSTA RICA",
# "HM":"HEARD ISLAND AND MCDONALD ISLANDS",
# "TN":"TUNISIA",
# "MC":"MONACO",
# "MP":"NORTHERN MARIANA ISLANDS",
# "SN":"SENEGAL",
# "PW":"PALAU",
# "VC":"SAINT VINCENT AND THE GRENADINES",
# "ST":"SAO TOME AND PRINCIPE",
# "DO":"DOMINICAN REPUBLIC",
# "EG":"EGYPT",
# "TZ":"TANZANIA, UNITED REPUBLIC OF",
# "SV":"EL SALVADOR",
# "TR":"TURKEY",
# "SG":"SINGAPORE",
# "UM":"UNITED STATES MINOR OUTLYING ISLANDS",
# "KR":"KOREA, REPUBLIC OF",
# "PG":"PAPUA NEW GUINEA",
# "GQ":"EQUATORIAL GUINEA",
# "US":"UNITED STATES",
# "BF":"BURKINA FASO",
# "AM":"ARMENIA",
# "TD":"CHAD",
# "NP":"NEPAL",
# "IT":"ITALY",
# "IO":"BRITISH INDIAN OCEAN TERRITORY",
# "ZW ":"ZIMBABWE",
# "HU":"HUNGARY",
# "BR":"BRAZIL",
# "IN":"INDIA",
# "PH":"PHILIPPINES",
# "TW":"TAIWAN, PROVINCE OF CHINA",
# "AO":"ANGOLA",
# "MH":"MARSHALL ISLANDS",
# "NO":"NORWAY",
# "JE":"JERSEY",
# "VU":"VANUATU",
# "EE":"ESTONIA",
# "AF":"AFGHANISTAN",
# "AX":"ALAND ISLANDS",
# "GN":"GUINEA",
# "FO":"FAROE ISLANDS",
# "SE":"SWEDEN",
# "SL":"SIERRA LEONE",
# "LB":"LEBANON",
# "MO":"MACAO",
# "IR":"IRAN, ISLAMIC REPUBLIC OF",
# "CG":"CONGO",
# "SM":"SAN MARINO",
# "NA":"NAMIBIA",
# "CI":"COTE D'IVOIRE",
# "GL":"GREENLAND",
# "VE":"VENEZUELA, BOLIVARIAN REPUBLIC OF",
# "VG":"VIRGIN ISLANDS, BRITISH",
# "BH":"BAHRAIN",
# "ZM":"ZAMBIA",
# "HR":"CROATIA",
# "MZ":"MOZAMBIQUE",
# "KW":"KUWAIT",
# "MA":"MOROCCO",
# "DZ":"ALGERIA",
# "AQ":"ANTARCTICA",
# "AU":"AUSTRALIA",
# "PN":"PITCAIRN",
# "QA":"QATAR",
# "AL":"ALBANIA",
# "BN":"BRUNEI DARUSSALAM",
# "NZ":"NEW ZEALAND",
# "SA":"SAUDI ARABIA",
# "RE":"REUNION",
# "HK":"HONG KONG",
# "CD":"CONGO, THE DEMOCRATIC REPUBLIC OF THE",
# "MW":"MALAWI",
# "CZ":"CZECH REPUBLIC",
# "DE":"GERMANY",
# "AD":"ANDORRA",
# "LU":"LUXEMBOURG",
# "CY":"CYPRUS",
# "TO":"TONGA",
# "FJ":"FIJI",
# "GT":"GUATEMALA",
# "LV":"LATVIA",
# "ES":"SPAIN",
# "SI":"SLOVENIA",
# "IM":"ISLE OF MAN",
# "BS":"BAHAMAS",
# "RS":"SERBIA",
# "WS":"SAMOA",
# "NC":"NEW CALEDONIA",
# "SY":"SYRIAN ARAB REPUBLIC",
# "MS":"MONTSERRAT",
# "GB":"UNITED KINGDOM",
# "PM":"SAINT PIERRE AND MIQUELON",
# "CL":"CHILE",
# "MF":"SAINT MARTIN",
# "SO":"SOMALIA",
# "BJ":"BENIN",
# "YE":"YEMEN",
# "TV":"TUVALU",
# "GE":"GEORGIA",
# "BM":"BERMUDA",
# "GS":"SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS",
# "AN":"NETHERLANDS ANTILLES",
# "BY":"BELARUS",
# "FI":"FINLAND",
# "BV":"BOUVET ISLAND",
# "LR":"LIBERIA",
# "KH":"CAMBODIA",
# "LY":"LIBYAN ARAB JAMAHIRIYA",
# "MU":"MAURITIUS",
# "GU":"GUAM",
# "ER":"ERITREA",
# "LI":"LIECHTENSTEIN",
# "SD":"SUDAN",
# "PA":"PANAMA",
# "IL":"ISRAEL",
# "EH":"WESTERN SAHARA",
# "KE":"KENYA",
# "CC":"COCOS (KEELING) ISLANDS",
# "IS":"ICELAND",
# "GF":"FRENCH GUIANA",
# "MM":"MYANMAR",
# "HT":"HAITI",
# "NF":"NORFOLK ISLAND",
# "ML":"MALI",
# "PY":"PARAGUAY",
# "KZ":"KAZAKHSTAN",
# "CH":"SWITZERLAND",
# "BA":"BOSNIA AND HERZEGOVINA",
# "BO":"BOLIVIA, PLURINATIONAL STATE OF",
# "UA":"UKRAINE",
# "BL":"SAINT BARTHELEMY",
# "AZ":"AZERBAIJAN",
# "BT":"BHUTAN",
# "VA":"HOLY SEE (VATICAN CITY STATE)",
# "PE":"PERU",
# "AR":"ARGENTINA",
# "TK":"TOKELAU",
# "AG":"ANTIGUA AND BARBUDA",
# "KN":"SAINT KITTS AND NEVIS",
# "PS":"PALESTINIAN TERRITORY, OCCUPIED",
# "ID":"INDONESIA",
# "GW":"GUINEA-BISSAU",
# "HN":"HONDURAS",
# "NG":"NIGERIA",
# "IQ":"IRAQ",
# "JM":"JAMAICA",
# "NU":"NIUE",
# "ET":"ETHIOPIA",
# "ME":"MONTENEGRO",
# "SK":"SLOVAKIA",
# "YT":"MAYOTTE"
# }
# lengths =[len(i) for i in COUNTRY.values()]

# max= [i for i in COUNTRY.values() if len(i) ==lengths ]
# print(print(max))

#---------------------

# years = [2015, 2016, 2017, 2018, 2019, 2020]

# sales = [350000, 400000, 410000, 439000, 500000, 290000]

# mix = dict(zip(years,sales))

# print(mix)

#---------------------
