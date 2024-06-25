from django.shortcuts import render
import requests
# Create your views here.
from bs4 import BeautifulSoup
from datetime import datetime

def extrair_dados_html(html, tag, atributo=None, valor_atributo=None):
    # Analisa o HTML com BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Procura a tag e os atributos desejados
    if atributo and valor_atributo:
        elementos = soup.find_all(tag, {atributo: valor_atributo})
    else:
        elementos = soup.find_all(tag)

    # Extrai o texto dos elementos encontrados
    dados = [elemento.text for elemento in elementos]

    return dados
hh={"Host": "en.onlinesoccermanager.com",
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:127.0) Gecko/20100101 Firefox/127.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
"Referer": "https://en.onlinesoccermanager.com/Career",
"Cookie": '''DefaultCultureCode=en-GB; CultureCode=en-GB; personalizedAdsAskAmount=1; personalizedAdsEnabled=true; personalizedAdsSettingLastAskedTimestamp=1701893527; _ga_1FLYTGXM8V=GS1.1.1719311743.27.1.1719311792.0.0.0; _ga=GA1.1.183631601.1701893528; HasLoggedInBefore=true; __gads=ID=341229a30eb98820:T=1701893546:RT=1719311760:S=ALNI_MaIL53HJ5wndp8AI0z_Id3YmsNdQg; __gpi=UID=00000ce405de8788:T=1701893546:RT=1719311760:S=ALNI_MZYp7FuPqwdenmnqcguo4tS_aUr2w; consumableRewardModalViewedTimestamp=1701893561; __eoi=ID=8b8a4869d8d3c684:T=1708436588:RT=1719311760:S=AA-AfjbBO0rI4BW6n8PUQQadbRTz; FCCDCF=%5Bnull%2Cnull%2Cnull%2C%5B%22CP6RzMAP6RzMAEsACBENAoEoAP_gAEPgABpYINJD7D7FbSFCwHpzaLsAMAhHRsCAQoQAAASBAmABQAKQIAQCgkAQFASgBAACAAAAICZBIQAECAAACUAAQAAAAAAEAAAAAAAIIAAAgAEAAAAIAAACAAAAEAAIAAAAEAAAmAgAAIIACAAAhAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAQOhQD2F2K2kKFkPCmQWYAQBCijYEAhQAAAAkCBIAAgAUgQAgFIIAgAIFAAAAAAAAAQEgCQAAQABAAAIACgAAAAAAIAAAAAAAQQAAAAAIAAAAAAAAEAAAAAAAQAAAAIAABEhCAAQQAEAAAAAAAQAAAAAAAAAAABAAA%22%2C%222~2072.70.89.93.108.122.149.196.2253.2299.259.2357.311.313.323.2373.338.358.2415.415.449.2506.2526.486.494.495.2568.2571.2575.540.574.2624.609.2677.864.981.1029.1048.1051.1095.1097.1126.1201.1205.1211.1276.1301.1344.1365.1415.1423.1449.1451.1570.1577.1598.1651.1716.1735.1753.1765.1870.1878.1889.1958~dv.%22%2C%222D7681C3-9260-49D1-98A1-C5DEDE8B2765%22%5D%5D; battleIntroShown=true; isFromGdprOptInCountry=true; isPrivacyNoticeAccepted=true; __cf_bm=QOysevD4j47Vbarym6oArVNU8qQ2JJhaOHD4_jsrSrY-1719311742-1.0.1.1-r_YDovQIDo0DmtFMuYkschtjfJ0s_OpaNtL5IoHWd8bNLjnJR4kUX_119gnKNqSx3HWHL0bGzAMZW__CjHal6w; bugsnagSession={"id":"clxu9tj6l000028bxfpl2akjy","startedAt":"2024-06-25T10:35:42.814Z","events":{"handled":0,"unhandled":0}}; access_token=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjcwMDEyMzMzOCIsImh0dHA6Ly9zY2hlbWFzLnhtbHNvYXAub3JnL3dzLzIwMDUvMDUvaWRlbnRpdHkvY2xhaW1zL25hbWUiOiJDRVJRVUVJUkFfQjM3NzAiLCJ3b3JsZCI6IjEiLCJuYmYiOjE3MTkzMTE3NTUsImV4cCI6MTcxOTMxMjk1NSwiaXNzIjoiT1NNLkF1dGhlbnRpY2F0aW9uIn0.uPJPdMak5-qjOi96fcIJ5es0PxHPEfz9VaaGu3q3qQc; refresh_token=eyJhbGciOiJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzA0L3htbGRzaWctbW9yZSNobWFjLXNoYTI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc1MDk4ODM4NiIsInRva2VuIjoiOGRkZDE1ODMtZWRmMS00ZjUyLTlkYjgtOTNkMTA4ZjdlNGYwIiwibmJmIjoxNzE5MzExNzU1LCJleHAiOjE3MTk5MTY1NTUsImlzcyI6Ik9TTS5BdXRoZW50aWNhdGlvbiJ9.BuXpB7RJXg8bmTVVWpMngtNV0YrOTYURJ03ReLQ6Fgw; stayLoggedIn=true; forum_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6IkNFUlFVRUlSQV9CMzc3MCIsImlkIjoiNzAwMTIzMzM4IiwiYXZhdGFyVXJsIjoiaHR0cHM6Ly9hc3NldHMub25saW5lc29jY2VybWFuYWdlci5jb20vQXZhdGFycy9Vc2Vycy8xMjkuanBnIiwibGFuZ3VhZ2Vjb2RlIjoiZW4iLCJuYmYiOjE3MTkzMTE3NTUsImV4cCI6MTcxOTkxNjU1NSwiaWF0IjoxNzE5MzExNzU1fQ.9vp970xTzOX1QpEGM60x-Iz7NhaKktgnCPf9x4ZYejI; session=%7B%22userId%22%3A700123338%2C%22login%22%3A%22CERQUEIRA_B3770%22%2C%22leagueId%22%3A0%2C%22teamId%22%3A0%2C%22leagueTypeId%22%3A0%2C%22leagueTypeName%22%3A%22%22%2C%22teamName%22%3A%22%22%2C%22slotIndex%22%3A0%2C%22serverDownForCurrentSlotIndex%22%3Afalse%2C%22hasMultipleSlots%22%3Atrue%2C%22hasInvites%22%3Atrue%2C%22hasBossCoinWallet%22%3Atrue%2C%22isReservedForFantasyLeague%22%3Afalse%2C%22leagueTheme%22%3A0%2C%22appTheme%22%3A3%2C%22leagueMode%22%3A0%7D; StatsSend=true; FCNEC=%5B%5B%22AKsRol9puoZyKc-hnRwNl-N-YELf6xsMy5zv6U2qDwtslXFD1LvCSIvl-ML9hjE-WtvNKHMsPhw0fE_jFVyHZKKW2-RB_ZJtuBhgZPIkGHHQK90kZ5Z6XUnPQIDLgKEiG3TDrpFiyycJPDaWW0hkFL5munbTa-jMYQ%3D%3D%22%5D%5D''',
}
# Exemplo de uso
html = BeautifulSoup(requests.get('https://en.onlinesoccermanager.com/Crew/', headers=hh).text,'html.parser').find('table',attrs={'id':'crew-member-table'}).encode_contents().decode('utf-8')
tag = 'span'
atributo = 'class'
valor_atributo = 'semi-bold'


def remove(ocor,a):
    while ocor in a:
        a.remove(ocor)
    return a

resultado =remove("\n\n",extrair_dados_html(html, tag, atributo, valor_atributo))

pnt=resultado[1::3]

while '-' in pnt:
    pnt.remove('-')

while len(pnt)<24:
    pnt.append('0')

name=resultado[::3]

while len(name)<24:
    name.append('')

dic_pnt=dict()
for i,j in zip(pnt,name):
    dic_pnt[j]=i

print(dic_pnt)
data_hj=datetime.strftime(datetime.now(),"%d %B %Y")
if data_hj[0:2]=="1 ":
    with open('pnts_acad.txt','w',encoding='utf-8') as art:
        art.write(str(pnt))
with open('pnts_acad.txt', 'r', encoding='utf-8') as ard:
    pnts=dict(ard.read())

pts=[]
for k in name:
    pts.append((int(dic_pnt[k]))-(int(pnts[k])))


order=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

dic=dict()
for h,k,l in zip(order,pts,name):
    dic[h] = [l,k,'not available yet', data_hj]

sorted_items = sorted(dic.items(), key=lambda x: x[1][1], reverse=True)
dic = {i + 1: item for i, (key, item) in enumerate(sorted_items)}

data_1=dic.get(1, [])
data_2=dic.get(2, [])
data_3=dic.get(3, [])
data_4=dic.get(4, [])
data_5=dic.get(5, [])
data_6=dic.get(6, [])
data_7=dic.get(7, [])
data_8=dic.get(8, [])
data_9=dic.get(9, [])
data_10=dic.get(10, [])
data_11=dic.get(11, [])
data_12=dic.get(12, [])
data_13=dic.get(13, [])
data_14=dic.get(14, [])
data_15=dic.get(15, [])
data_16=dic.get(16, [])
data_17=dic.get(17, [])
data_18=dic.get(18, [])
data_19=dic.get(19, [])
data_20=dic.get(20, [])
data_21=dic.get(21, [])
data_22=dic.get(22, [])
data_23=dic.get(23, [])
data_24=dic.get(24, [])

def index(request):
	return render(request, "webap/index.html", {"data_1": data_1, "data_2": data_2, "data_3": data_3, "data_4": data_4, "data_5": data_5, "data_6": data_6, "data_7": data_7, "data_8": data_8, "data_9": data_9, "data_10": data_10, "data_11": data_11, "data_12": data_12, "data_13": data_13, "data_14": data_14, "data_15": data_15, "data_16": data_16, "data_17": data_17, "data_18": data_18, "data_19": data_19, "data_20": data_20, "data_21": data_21, "data_22": data_22, "data_23": data_23, "data_24": data_24})
# Create your views here.
