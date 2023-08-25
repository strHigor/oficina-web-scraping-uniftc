import os
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime


sessao = requests.session()
anuncios_obtidos = []

def iniciar_scraper():
    procurar()
    if anuncios_obtidos:
        extrair()


def procurar():
    pass


def extrair():
    pass
                        
                
def corrigir_valor_monetario(valor_original):
    valor_original = valor_original.replace('Â', '').replace('\xa0', ' ')
    valor_corrigido = valor_original.encode('iso-8859-1').decode('utf-8')
    return valor_corrigido.replace("R$ ", "").replace(".", "").replace(",", ".")


iniciar_scraper()