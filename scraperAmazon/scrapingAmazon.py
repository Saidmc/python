import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}
products = []
url = ['https://www.amazon.com.mx/dp/B092VNM4ZS/?coliid=I3U17DK3B1OVI3&colid=3BPNBLNZHNWA7&ref_=lv_ov_lig_dp_it&th=1', 
'https://www.amazon.com.mx/Ventilador-escape-Hon-Guan-311CFM/dp/B07VC4RLGY/ref=pd_sbs_sccl_1_8/141-1573229-5596346?pd_rd_w=2D6A3&content-id=amzn1.sym.74f47eb8-40ce-4a57-9ac6-f186b4804611&pf_rd_p=74f47eb8-40ce-4a57-9ac6-f186b4804611&pf_rd_r=E0C9443V862T7Y1TNEC6&pd_rd_wg=Wmrei&pd_rd_r=6c9047c0-8da1-4aa3-89c5-564852801a76&pd_rd_i=B07VC4RLGY&th=1', 
'https://www.amazon.com.mx/Ventilador-controlador-atenuaci%C3%B3n-apartamento-hidropon%C3%ADa/dp/B08CXG7Y1H/ref=psdc_11076224011_t1_B07VC4RLGY?th=1',
'https://www.amazon.com.mx/gp/product/B07JQM7C28/ref=ox_sc_saved_title_3?smid=A163F6BACEV7XG&th=1']
    
df = pd.DataFrame(columns=['Title', 'Price', 'Savings Percentage'])

for item in url:    
    response = requests.get(item, headers=headers)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.find("span", id="productTitle").text.strip()
    whole_price = soup.find("span", class_="a-price-whole").text
    fraction_price = soup.find("span", class_="a-price-fraction").text
    savings_percentage = soup.find("span", class_="savingsPercentage")
    final_price = whole_price + fraction_price

    df.loc[len(df.index)] = [title, final_price, savings_percentage]

print(df)