import pandas as pd
# bibliotecas para plots
import seaborn as sb
import matplotlib.pyplot as mp
from PyPDF2 import PdfFileMerger as m

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
youngAdult = sum(age.values > 30)
adult = sum((age.values > 30) & (age.values < 50))
seniorAdult = sum((age.values > 50) & (age.values < 70))
senior = sum(age.values > 70)
# Idade para ser usada no pie
ages_range = [youngAdult, adult, seniorAdult, senior]

filename = "teste/texto.pdf"


# Funções de geração de gráficos
def bar_graph(horizontal, vertical, index, title=''):
    sb.set_color_codes("pastel")
    sb.barplot(data=df, x=horizontal, y=vertical)
    mp.title(title)
    mp.savefig(f'teste/{index}.pdf')
    mp.show()
    pdfs.append(f'teste/{index}.pdf')


def line_graph(horizontal, vertical, index, label='', title=''):
    sb.set_color_codes("pastel")
    sb.lineplot(data=df, x=horizontal, y=vertical, label=label, ci=None)
    mp.title(title)
    mp.savefig(f'teste/{index}.pdf')
    mp.show()
    pdfs.append(f'teste/{index}.pdf')


def displot_graph(horizontal, vertical, index, title=''):
    sb.set_theme(style="whitegrid")
    sb.scatterplot(data=df, x=horizontal, y=vertical)
    mp.title(title)
    mp.savefig(f'teste/{index}.pdf')
    mp.show()
    pdfs.append(f'teste/{index}.pdf')


def pie_graph(index, title=''):
    labels = 'Jovens (18-29)', 'Adultos (30-49)', 'Adultos sênior (50-69)', 'Sênior (70+)'
    sizes = [youngAdult, adult, seniorAdult, senior]

    fig1, ax1 = mp.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    mp.title(title)
    mp.savefig(f'teste/{index}.pdf')
    mp.show()
    pdfs.append(f'teste/{index}.pdf')


def corr_graph(index, title):
    sb.heatmap(df.corr(), annot=True, fmt=".1f", linewidths=.6)
    mp.title(title)
    mp.savefig(f'teste/{index}.pdf')
    mp.show()
    pdfs.append(f'teste/{index}.pdf')


def gen_pdf():
    pdfm = m()
    for pdf in pdfs:
        pdfm.append(pdf)
    pdfm.append(filename)
    pdfm.write('teste/relatorio.pdf')


def runner():
    pie_graph(1, 'Relação de faixa etária')  # Indicador de faixa etária em relação a base inteira
    line_graph(dfYear, rate, 2, 'Satisfação',
               'Satistação do cliente por ano')  # Indicador de satisfação do cliente por ano em linhas
    bar_graph(dfYear, revenue, 3, 'Receita por ano')  # Indicador de receita por ano em barras
    bar_graph(dfMonth, revenue, 4, 'Receita por mês')  # Indicador de receita por mes em barras
    bar_graph(dfWeek, revenue, 5, 'Receita por dia da semana')  # Indicador de receita por dia em barras
    displot_graph(age, revenue, 6, 'Receita por idade')  # Indicador de receita por faixa etária
    corr_graph(7, 'Gráfico de correlação')
    gen_pdf()
