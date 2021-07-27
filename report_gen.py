import pandas as pd
import math as mt
from reportlab.pdfgen import canvas

# Classe do dataframe
df = pd.read_csv('test.csv')
identifier = df['identificador'].astype('int')
age = df['idade'].astype('int')
revenue = df['receita'].astype('float')
date = pd.to_datetime(df['data'])
rate = df['nota'].astype('int')
pdfs = []
dfYear = date.dt.year
dfMonth = date.dt.month
dfWeek = date.dt.dayofweek

# Quantidade de clientes for faixa de idade
youngAdult = sum(age.values <= 29)
adult = sum((age.values >= 30) & (age.values < 50))
seniorAdult = sum((age.values >= 50) & (age.values < 70))
senior = sum(age.values > 70)
# Idade para ser usada no pie
ages_range = [youngAdult, adult, seniorAdult, senior]

# Constantes do relatório
point = 1
inch = 72
# Nome do arquivo com o relatório em texto
filename = "teste/texto.pdf"


# Funções para relatório
# Clientes ativos total
def count_active_clientes():
    sac_value = identifier.count()
    return sac_value


# Clientes idade média total
def age_medium():
    am = mt.trunc(sum(age) / age.count())
    return am


# Clientes por satisfação, mínima, média, máxima
def clients_rate():
    crMin = round(min(rate))
    crAvg = round(sum(rate) / rate.count())
    crMax = round(max(rate))
    return crMin, crAvg, crMax


# Ticket médio total
def active_clients_by_revenue():
    acbr = "{:.2f}".format(sum(revenue) / count_active_clientes())
    return float(acbr)


# Ticket médio total por faixa de idade
def avg_ticket_by_age(ageRangeSum):
    if ageRangeSum != 0:
        return float("{:.2f}".format(active_clients_by_revenue() / ageRangeSum))
    else:
        return print('Não existe cliente com essa idade para gerar ticket médio')


# Relatório com as informações dos clientes
def report():
    texto = f'''
    O gráfico acima apresenta as correlações entre os dados,elas podem ser positivas, negativas 
    ou neutras. As variáveis que estão dentro da escala de 1 a 0,7 (+ ou -)e na tonalidade laranja 
    no caso das positivas, e roxo escuro no caso das negativas, possuem uma forte correlação.
    Já as variáveis que estão entre 0,7 a 0,5 (+ ou -) e na tonalidade avermelhada no caso das 
    positivas e roxo médio no caso das negativas, possuem correlação moderada; as variáveis que 
    possuem escala de 0,5 a 0,25 e (+ ou -) possuem baixa;e por fim as variáveis com coeficiente 
    próximo a 0 (+ ou -) e com tonalidade vermelha não possuem correlação.
    
    
    Há um total de {count_active_clientes()} clientes ativos, com a média de idade em {age_medium()}
    As avaliações de seus clientes seguem a média de {clients_rate()[1]} com o mínimo de {clients_rate()[0]} e máximo de {clients_rate()[2]}


    O ticket médio total é de {active_clients_by_revenue()}, quando separados por faixa etária, são {avg_ticket_by_age(youngAdult)} 
    para jovens (18-29) com {youngAdult} clientes nessa faixa etária, {avg_ticket_by_age(adult)} para adultos (30-49) com {adult}, 
    para adultos seniores (50-69) {avg_ticket_by_age(seniorAdult)} com {seniorAdult} e para seniores de {avg_ticket_by_age(senior)} 
    com {senior} clientes.
    '''
    return texto


def make_pdf_file(archive):
    c = canvas.Canvas(archive, pagesize=(8.5 * inch, 11 * inch))
    c.setFont("Helvetica", 12 * point)
    v = 10 * inch
    for subtline in (report()).split('\n'):
        c.drawString(1 * inch, v, subtline)
        v -= 12 * point
    c.showPage()
    c.save()


if __name__ == '__main__':
    make_pdf_file(filename)
