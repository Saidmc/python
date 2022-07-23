from numpy import NaN
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

sFILE = 'scraperAmazon/articulos.csv'
sFIELD_LINKS = 'Link'
sFIELD_PRICES = 'Price'
sCODEERROR_FILECSV = 'No se pudo leer el archivo'
sTAG_CSS = 'span'
sHTML_PARSER = 'html.parser'

sHTML_PRODUCT_TITLE = 'a-size-large product-title-word-break'
sHTML_PRICE_WHOLE = 'a-price-whole'
sHTML_PRICE_FRACTION = 'a-price-fraction'
sHTML_SAVINGS_PORCENTAGE = 'a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage'

sHEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}


def webScraper(_urls, _prices, _df_file_cols):

    df_validator = pd.DataFrame(columns=_df_file_cols)
    iCont = 0
    
    for item in _urls:
        response = requests.get(item, headers=sHEADERS)
        html = response.text
        #print(html)

        soup = BeautifulSoup(html, sHTML_PARSER)

        title = soup.find(sTAG_CSS, id=sHTML_PRODUCT_TITLE).text.strip()
        whole_price = soup.find(sTAG_CSS, class_=sHTML_PRICE_WHOLE).text
        fraction_price = soup.find(sTAG_CSS, class_=sHTML_PRICE_FRACTION).text
        percentTXT = soup.find(sTAG_CSS, class_=sHTML_SAVINGS_PORCENTAGE)
        if percentTXT is None:
            savings_percentage = ''
        else:
            savings_percentage = percentTXT.text
        final_price = whole_price + fraction_price

        fFinalPrice = float(final_price.replace(',', ''))
        fRegPrice = float(_prices[iCont].replace(',', ''))

        if fFinalPrice < fRegPrice:
            print(f'El precio bajó {fRegPrice - fFinalPrice} pesos')
        
        df_validator.loc[len(df_validator.index)] = [item, title, final_price, savings_percentage]
        iCont += 1

    return df_validator




os.system('cls')

try:
    df_file_cols = pd.read_csv(sFILE, nrows=1, sep='|').columns.tolist()
    df_file = pd.read_csv(sFILE, sep='|')

except:
    print(f'{sCODEERROR_FILECSV} "{sFILE}"')

urls = list(df_file[sFIELD_LINKS])
prices = list(df_file[sFIELD_PRICES])

df_validator_resp = webScraper(urls, prices, df_file_cols)

#Imprimimos resultados
print('*'*150)
print(df_file)
print('*'*150)
print(df_validator_resp)


