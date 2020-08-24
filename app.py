import csv
from bs4 import BeautifulSoup
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()
pagina = http.request('GET', 'https://receita.economia.gov.br/orientacao/tributaria/cadastros/cadastro-de-imoveis-rurais-cafir/introducao')

sopa = BeautifulSoup(pagina.data, "lxml")
#print(sopa)

cla = sopa.find("div", {"id":'content-core'})
links = cla.find_all('a')
conteudo = sopa.find_all('b')
len(linkas)
with open('testecsv.csv', 'a', newline='', encoding='utf-8') as file:
    for link in links:
        a = str(link.get_text()).replace(',',' ').replace('[','').replace(']','').replace("", '').replace('\n', '')
        b = str(link.get('href'))
        #c = str(conteudos.contents).replace(',',' ').replace('[','').replace(']','').replace("", '').replace('\n', '').replace("'", '')


        #aa = a.replace(',',' ')
        #bb = b.replace(',', ' ')
        writer = csv.writer(file)
        #writer.writerow(["perguntas", "respostas"])
        #aa = a.getTexto
        try:
            writer.writerow([a, b]) 
        except:
            pass 

'''
aa = a.replace(',',' ')
bb = b.replace(',', ' ')

with open('chatbots.csv', 'a', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    #writer.writerow(["perguntas", "respostas"])
    writer.writerow([aa, bb])   
'''

