from bs4 import BeautifulSoup
import requests

URL = 'https://produto.mercadolivre.com.br/MLB-2024353694-pc-gamer-facil-ryzen-7-5700g-vega-8-ssd-480gb-16gb-ddr4-500w-_JM#position=9&search_layout=grid&type=item&tracking_id=8bf89ebb-b21c-4915-96d3-2fbba6817e50'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'}

site = requests.get(URL, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')

nome_produto1 = soup.find('h1', class_ = 'ui-pdp-title').get_text()

preço = soup.find('div', class_= 'ui-pdp-price__second-line').get_text().strip()

# ANTES DO PREÇO EM FORMA NUMÉRICA,TEM UMA ESCRITA INFORMANDO O PREÇO EM FORMA DE TEXTO,TEM QUE REMOVER ELA E DEIXAR APENAS O PREÇO EM FORMATO NUMÉRICO,USANDO A FUNÇAO STRIP PRA REMOVER

formato_preço = preço[13:18]

# TIRAR O PONTO,USANDO A FUNÇAO REPLACE

formato_preço = formato_preço.replace('.','')

# TRANSFORMAR EM UM NÚMERO REAL,POIS ELE ESTÁ COM UMA STRING

formato_preço=float(formato_preço)
 
 # SE O PREÇO FOR MENOR OU IGUAL AO PREÇO QUE DESEJO,QUERO QUE UM EMAIL SEJA ENVIADO ATÉ MIM

def enviar_email():
    import win32com.client as win32
    # CRIAR A INTEGRAÇÃO COM O OUTLOOK (APP DE EMAIL QUE UTLIZO NO WINDOWS)
    outlook = win32.Dispatch('outlook.application')
    # CRIAR O EMAIL
    email= outlook.CreateItem(0)
    # INFORMAÇÕES DO EMAIL
    email.To = 'webscrapingproduto1@gmail.com'
    # ASSUNTO DO EMAIL
    email.Subject = 'PREÇO PC GAMER RYZEN 7'
    # CORPO DO EMAIL
    email.HTMLBody = f'''
    <p>Olá !</p> 
    
    <p>Seu produto:</p>
    <p>{nome_produto1}</p>
    
    <p>ESTÁ COM O VALOR QUE VOCÊ DESEJA !</p>

    <p>Abs,</p>
    <p>Elizeu Freitas</p>
    '''
    email.Send()
    print('EMAIL ENVIADO COM SUCESSO !')

if (formato_preço <= 3150):
    enviar_email()

