from django.shortcuts import render
from bs4 import BeautifulSoup

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
html='''
<body><section class="wrapper">
    <!-- Row title -->
    <main class="row title">
      <ul>
        <li>Posição</li>
        <li>Treinador</li>
        <li>Pontos</li>
        <li>ΔP</li>
        <li>last update</li>
      </ul>
    </main>
    <!-- Row 1 -->
    <article class="row first">
      <ul>
        <li><a>1º</a></li>

        <li class="q">Guitta76</li>

        <li class="q">95</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>Obs:</li>
      </ul>
    </article>
    <!-- Row 2 -->
    <article class="row first">
      <ul>
        <li><a>2º</a></li>

        <li class="q">FaCarreira</li>

        <li class="q">92</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 3 -->
    <article class="row first">
      <ul>
        <li><a>3º</a></li>

        <li>TiburcioFC</li>

        <li>65</li>

        <li>not available yet</li>

        <li>Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 4 -->
    <article class="row scnd">
      <ul>
        <li><a>4º</a></li>

        <li class="q">Davide da Silva Costa</li>

        <li class="q">62</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 5 -->
    <article class="row scnd">
      <ul>
        <li><a>5º</a></li>

        <li class="q">tbc111</li>

        <li class="q">49</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 6 -->
    <article class="row scnd">
      <ul>
        <li><a>6º</a></li>

        <li class="q">Defected66</li>

        <li class="q">46</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 7 -->
    <article class="row scnd">
      <ul>
        <li><a>7º</a></li>

        <li class="q">hilarioSilva</li>

        <li class="q">41</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 8 -->
    <article class="row mid">
      <ul>
        <li><a>8º</a></li>

        <li class="q">Paulinho Terror1906</li>

        <li class="q">41</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 9 -->
    <article class="row mid">
      <ul>
        <li><a>9º</a></li>

        <li class="q">Davide Oliveira 89</li>

        <li class="q">38</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>10º</a></li>

        <li class="q">JNPires</li>

        <li class="q">33</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>11º</a></li>

        <li class="q">nunobarbosa86</li>

        <li class="q">31</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>12º</a></li>

        <li class="q">EmanuelJLC</li>

        <li class="q">28</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>13º</a></li>

        <li class="q">Pepe_31</li>

        <li class="q">25</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>14º</a></li>

        <li class="q">Mtx9900</li>

        <li class="q">17</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>15º</a></li>

        <li class="q">perfilariam</li>

        <li class="q">7</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>16º</a></li>

        <li class="q">n.jorge</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>17º</a></li>

        <li class="q">Tiago.21</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>18º</a></li>

        <li class="q">rafaelraf665</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>19º</a></li>

        <li class="q">PutoFananBoy</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>20º</a></li>

        <li class="q">Champion38866</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>21º</a></li>

        <li class="q">PinOkaS</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row end">
      <ul>
        <li><a>22º</a></li>

        <li class="q">sequeira5</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row end">
      <ul>
        <li><a>23º</a></li>

        <li class="q">Cláudia Inês</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row end">
      <ul>
        <li><a>24º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h46</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
  </section>

</body>
'''
html_academy='''
<body><section class="wrapper">
    <!-- Row title -->
    <main class="row title">
      <ul>
        <li>Posição</li>
        <li>Treinador</li>
        <li>Pontos</li>
        <li>ΔP</li>
        <li>last update</li>
      </ul>
    </main>
    <!-- Row 1 -->
    <article class="row first">
      <ul>
        <li><a>1º</a></li>

        <li class="q">CERQUEIRA_B3770</li>

        <li class="q">11</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>Obs:</li>
      </ul>
    </article>
    <!-- Row 2 -->
    <article class="row first">
      <ul>
        <li><a>2º</a></li>

        <li class="q">Ze Lion2002</li>

        <li class="q">8</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 3 -->
    <article class="row first">
      <ul>
        <li><a>3º</a></li>

        <li>Jota500</li>

        <li>7</li>

        <li>not available yet</li>

        <li>Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 4 -->
    <article class="row scnd">
      <ul>
        <li><a>4º</a></li>

        <li class="q">Pedro Te1xe1r4</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 5 -->
    <article class="row scnd">
      <ul>
        <li><a>5º</a></li>

        <li class="q">estrico_1</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 6 -->
    <article class="row scnd">
      <ul>
        <li><a>6º</a></li>

        <li class="q">Mr Botelho</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 7 -->
    <article class="row scnd">
      <ul>
        <li><a>7º</a></li>

        <li class="q">GomesSporting</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 8 -->
    <article class="row mid">
      <ul>
        <li><a>8º</a></li>

        <li class="q">m7spkkk</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <!-- Row 9 -->
    <article class="row mid">
      <ul>
        <li><a>9º</a></li>

        <li class="q">Tuta1994</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>10º</a></li>

        <li class="q">jemika</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>11º</a></li>

        <li class="q">vitorino_986</li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>12º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>13º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>14º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row mid">
      <ul>
        <li><a>15º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>16º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>17º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>18º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>19º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>20º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row last">
      <ul>
        <li><a>21º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row end">
      <ul>
        <li><a>22º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row end">
      <ul>
        <li><a>23º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
    <article class="row end">
      <ul>
        <li><a>24º</a></li>

        <li class="q"></li>

        <li class="q">0</li>

        <li class="q">not available yet</li>

        <li class="q">Sept 11 22h47</li>

      </ul>
      <ul class="more-content">
        <li>obs:</li>
      </ul>
    </article>
  </section>

</body>
'''
tag='li'
atributo='class'
valor='q'
result=extrair_dados_html(html, tag, atributo, valor)[::4]
result_academy=extrair_dados_html(html_academy, tag, atributo, valor)[::4]
while len(result)<24:
    result.append('')
while len(result_academy)<24:
    result_academy.append('')
data_1_academy=result_academy[0]
data_2_academy=result_academy[1]
data_3_academy=result_academy[2]
data_4_academy=result_academy[3]
data_5_academy=result_academy[4]
data_6_academy=result_academy[5]
data_7_academy=result_academy[6]
data_8_academy=result_academy[7]
data_9_academy=result_academy[8]
data_10_academy=result_academy[9]
data_11_academy=result_academy[10]
data_12_academy=result_academy[11]
data_13_academy=result_academy[12]
data_14_academy=result_academy[13]
data_15_academy=result_academy[14]
data_16_academy=result_academy[15]
data_17_academy=result_academy[16]
data_18_academy=result_academy[17]
data_19_academy=result_academy[18]
data_20_academy=result_academy[19]
data_21_academy=result_academy[20]
data_22_academy=result_academy[21]
data_23_academy=result_academy[22]
data_24_academy=result_academy[23]

data_1=result[0]
data_2=result[1]
data_3=result[2]
data_4=result[3]
data_5=result[4]
data_6=result[5]
data_7=result[6]
data_8=result[7]
data_9=result[8]
data_10=result[9]
data_11=result[10]
data_12=result[11]
data_13=result[12]
data_14=result[13]
data_15=result[14]
data_16=result[15]
data_17=result[16]
data_18=result[17]
data_19=result[18]
data_20=result[19]
data_21=result[20]
data_22=result[21]
data_23=result[22]
data_24=result[23]

# Create your views here.
def index(request):
	return render(request, "cbr/index.html", {"data_1": data_1, "data_2": data_2, "data_3": data_3, "data_4": data_4, "data_5": data_5, "data_6": data_6, "data_7": data_7, "data_8": data_8, "data_9": data_9, "data_10": data_10, "data_11": data_11, "data_12": data_12, "data_13": data_13, "data_14": data_14, "data_15": data_15, "data_16": data_16, "data_17": data_17, "data_18": data_18, "data_19": data_19, "data_20": data_20, "data_21": data_21, "data_22": data_22, "data_23": data_23, "data_24": data_24, "data_1_academy": data_1_academy, "data_2_academy": data_2_academy, "data_3_academy": data_3_academy, "data_4_academy": data_4_academy, "data_5_academy": data_5_academy, "data_6_academy": data_6_academy, "data_7_academy": data_7_academy, "data_8_academy": data_8_academy, "data_9_academy": data_9_academy, "data_10_academy": data_10_academy, "data_11_academy": data_11_academy, "data_12_academy": data_12_academy, "data_13_academy": data_13_academy, "data_14_academy": data_14_academy, "data_15_academy": data_15_academy, "data_16_academy": data_16_academy, "data_17_academy": data_17_academy, "data_18_academy": data_18_academy, "data_19_academy": data_19_academy, "data_20_academy": data_20_academy, "data_21_academy": data_21_academy, "data_22_academy": data_22_academy, "data_23_academy": data_23_academy, "data_24_academy": data_24_academy})
