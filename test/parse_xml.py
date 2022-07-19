#!/usr/bin/env python 
# -*- coding: utf-8 -*-
'''
Time    : 2022/05/12 12:32
Author  : zhuchunjin
Email   : chunjin.zhu@taurentech.net
File    : parse_xml.py
Software: PyCharm
'''
import re
import time

import requests
import xlsxwriter
from bs4 import BeautifulSoup
base_url="https://www.labsci.com.cn/category_82.html"
all_product=[]
workbook = xlsxwriter.Workbook('demo2.xlsx')  # 创建一个excel文件
worksheet = workbook.add_worksheet(u'sheet1')  # 在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
for i in range(1440,12468):
    headers={
            "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
            # "Connection": "keep-alive",
            # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            # "Host": "www.labsci.com.cn",
            # "Origin": "https://www.labsci.com.cn",
            # "Referer": "https://www.labsci.com.cn/category_82.html",
            # "X-MicrosoftAjax":"Delta=true",
            "Cookie":"_ga=GA1.3.195865237.1652268530; _gid=GA1.3.1153911878.1652268530; meil10aglfdd5kyy50m0evcaCusID=; ASP.NET_SessionId=cji50pldlgnasdaqjmopg4o0; Hm_lvt_572e7d0a5b68f27810baffb7df9d5de0=1652268527,1652328021; Hm_lvt_1aec78342987aa3b28bbe45e87d2ea9e=1652268527,1652328021; Hm_lvt_f393f799160e5db67bd58d97a70c7e70=1652268527,1652328021; yzmcodes=17+16=?; cji50pldlgnasdaqjmopg4o0CusID=30311; cji50pldlgnasdaqjmopg4o0LoginID=19916939864; cji50pldlgnasdaqjmopg4o0CusName=19916939864; cji50pldlgnasdaqjmopg4o0Email=; cji50pldlgnasdaqjmopg4o0Tel=; cji50pldlgnasdaqjmopg4o0TypeID=1; cji50pldlgnasdaqjmopg4o0CusNo=; Apweb=APUSNAME=Oz9wjbn8tNWUkW3Dn7o20g==&APUSPASS=AIa8yn1hpjciN7UziiJeAw==; __session:sessionID:=https:; Hm_lpvt_f393f799160e5db67bd58d97a70c7e70=1652346443; Hm_lpvt_572e7d0a5b68f27810baffb7df9d5de0=1652348096; Hm_lpvt_1aec78342987aa3b28bbe45e87d2ea9e=1652348099"}
    s = requests.session()
    s.headers = headers
    rest= s.get(base_url)
    # rest=requests.get(base_url,headers=headers,timeout=(3,7))
    VIEWSTATE=re.findall(r'<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(.*?)" />',rest.text,re.I)
    EVENTVALIDATION=re.findall(r'<input type="hidden" name="__EVENTVALIDATION" id="__EVENTVALIDATION" value="(.*?)" />',rest.text,re.I)
    values={}
    print(i,rest.headers)
    if 'Set-Cookie' in rest.headers.keys():
        headers['Cookie']=rest.headers['Set-Cookie']
    values['__EVENTTARGET']="dtListPag$ctl0%d$btnPageNum"%i
    values['ScriptManager']='UpdatePanel1|dtListPag$ctl0%d$btnPageNum'%i
    values['__EVENTARGUMENT']=''
    values['__VIEWSTATE']=VIEWSTATE[0]
    values['__VIEWSTATEGENERATOR']='654AF4A5'
    values['__VIEWSTATEENCRYPTED']=''
    values['__EVENTVALIDATION']=EVENTVALIDATION[0]
    values['txtSear']=''
    values['txtHidd']=''
    values['txtAuto']=''
    values['txtShowType']=0
    values['gridview$ctl02$lblNewPrice1']: 855.00
    values['gridview$ctl02$txtTrnQty']: 1
    values['gridview$ctl03$lblNewPrice1']: 1020.00
    values['gridview$ctl03$txtTrnQty']: 1
    values['gridview$ctl04$lblNewPrice1']: 1074.00
    values['gridview$ctl04$txtTrnQty']: 1
    values['gridview$ctl05$lblNewPrice1']: 570.00
    values['gridview$ctl05$txtTrnQty']: 1
    values['gridview$ctl06$lblNewPrice1']: 736.00
    values['gridview$ctl06$txtTrnQty']: 1
    values['gridview$ctl07$lblNewPrice1']: 500.00
    values['gridview$ctl07$txtTrnQty']: 1
    values['gridview$ctl08$lblNewPrice1']: 1101.00
    values['gridview$ctl08$txtTrnQty']: 1
    values['gridview$ctl09$lblNewPrice1']: 588.00
    values['gridview$ctl09$txtTrnQty']: 1
    values['gridview$ctl10$lblNewPrice1']: 800.00
    values['gridview$ctl10$txtTrnQty']: 1
    values['gridview$ctl11$lblNewPrice1']: 1187.00
    values['gridview$ctl11$txtTrnQty']: 1
    values['gridview$ctl12$lblNewPrice1']: 1009.00
    values['gridview$ctl12$txtTrnQty']: 1
    values['gridview$ctl13$lblNewPrice1']: 1202.25
    values['gridview$ctl13$txtTrnQty']: 1
    values['gridview$ctl14$lblNewPrice1']: 0.00
    values['gridview$ctl14$txtTrnQty']: 1
    values['gridview$ctl15$lblNewPrice1']: 463.00
    values['gridview$ctl15$txtTrnQty']: 1
    values['gridview$ctl16$lblNewPrice1']: 268.00
    values['gridview$ctl16$txtTrnQty']: 1
    values['gridview$ctl17$lblNewPrice1']: 601.00
    values['gridview$ctl17$txtTrnQty']: 1
    values['gridview$ctl18$lblNewPrice1']: 1086.00
    values['gridview$ctl18$txtTrnQty']: 1
    values['gridview$ctl19$lblNewPrice1']: 589.00
    values['gridview$ctl19$txtTrnQty']: 1
    values['gridview$ctl20$lblNewPrice1']: 478.00
    values['gridview$ctl20$txtTrnQty']: 1
    values['gridview$ctl21$lblNewPrice1']: 138.00
    values['gridview$ctl21$txtTrnQty']: 1
    values['gridview$ctl22$lblNewPrice1']: 268.00
    values['gridview$ctl22$txtTrnQty']: 1
    values['gridview$ctl23$lblNewPrice1']: 792.75
    values['gridview$ctl23$txtTrnQty']: 1
    values['gridview$ctl24$lblNewPrice1']: 364.00
    values['gridview$ctl24$txtTrnQty']: 1
    values['gridview$ctl25$lblNewPrice1']: 882.00
    values['gridview$ctl25$txtTrnQty']: 1
    values['gridview$ctl26$lblNewPrice1']: 268.00
    values['gridview$ctl26$txtTrnQty']: 1
    values['gridview$ctl27$lblNewPrice1']: 226.00
    values['gridview$ctl27$txtTrnQty']: 1
    values['gridview$ctl28$lblNewPrice1']: 324.00
    values['gridview$ctl28$txtTrnQty']: 1
    values['gridview$ctl29$lblNewPrice1']: 121.00
    values['gridview$ctl29$txtTrnQty']: 1
    values['txtToPageNum']=i+1
    # values['txtUserID']='19916939864'
    # values['txtPassWord']='zcj319319'
    # values['IfChoose2']='on'
    values['__ASYNCPOST']='true'
    ret=requests.post(base_url,data=values,headers=headers)
    soup=BeautifulSoup(ret.text,'lxml')

    # print(ret.content.decode('utf-8'))
    product_id=[]
    product_name=[]
    product_url=[]
    price_list=[]
    product_style=[]
    product_brand=[]
    i=1
    for ui in soup.find_all('span'):
        ret='lblPrice' in str(ui)
        if ret:
            price_list.append(ui.string)
        if 'title' in ui.attrs.keys():
            if i % 2 == 0:
                product_style.append(ui.attrs['title'])
            else:
                product_brand.append(ui.attrs['title'])
            i+=1
    i=1
    for ui in soup.find_all('a'):
        # 提取商品编号和商品名称
        if 'href' and 'style' and 'id' in ui.attrs.keys() and 'onclick' not in ui.attrs.keys() and 'target' in ui.attrs.keys():
            if i%2==0:
                product_name.append(ui.attrs["title"])
            else:
                product_id.append(ui.attrs['title'])
                product_url.append('https://www.labsci.com.cn/'+ui.attrs['href'])
            i+=1
    product_list=[]
    product_detail={"product_id":"","product_name":"","product_brand":"","product_style":"","product_list":"","product_url":""}

    with open("product.txt", "a") as file:
        for i in range(28):
            file.write("%s#%s#%s#%s#%s#%s\n"%(product_id[i],product_name[i],product_brand[i],product_style[i],price_list[i],product_url[i]))
            # product_detail["product_id"]=product_id[i]
            # product_detail["product_name"]=product_name[i]
            # product_detail["product_brand"]=product_brand[i]
            # product_detail["product_style"]=product_style[i]
            # product_detail["product_list"]=price_list[i]
            # product_detail["product_url"]=product_url[i]
            # product_list.append(product_detail.copy())
    # all_product.append(product_list)
    # time.sleep(1)
# detail=["product_id","product_name","product_brand","product_style","product_list","product_url"]
# for item in range(len(all_product)):
#     for elem in all_product[item]:
#         print(elem)
#         for i in range(6):
#             worksheet.write(item, i, elem[detail[i]])
# workbook.close()
# except Exception as e:
#     print(e)
    # detail = ["product_id", "product_name", "product_brand", "product_style", "product_list", "product_url"]
    # for row in range(len(all_product)):
    #     for i in range(5):
    #         print(all_product[row])
    #         # worksheet.write(row, i, all_product[row][detail[i]])
    # workbook.close()