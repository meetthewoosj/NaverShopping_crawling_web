import requests
from bs4 import BeautifulSoup
import json
import sys



headers = {
    'authority': 'search.shopping.naver.com',
    'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    'accept': 'application/json, text/plain, */*',
    'sec-ch-ua-mobile': '?0',
    'logic': 'PART',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'sec-fetch-dest': 'empty',
    'referer': 'https://search.shopping.naver.com/search/all?query=%EC%95%9E%EC%B9%98%EB%A7%88&cat_id=&frm=NVSHATC',
    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': 'NNB=P5XE2VS37U2F4; NRTK=ag#all_gr#1_ma#-2_si#0_en#0_sp#0; ASID=d36c4d9d00000170ba46d77300000048; AD_SHP_BID=3; MM_NEW=1; NFS=2; MM_NOW_COACH=1; _ga_4BKHBFKFK0=GS1.1.1622941158.4.1.1622942820.60; _ga_7VKFYR6RV1=GS1.1.1625706689.17.0.1625706694.55; _ga_1BVHGNLQKG=GS1.1.1630112220.2.1.1630112240.0; nid_inf=45700487; NID_AUT=pfUUAmBbKA3eoKsG7jkgKYwBCmMu35LfO6EUrMNXarpGOmKmDFlgV7FDuGJwbPcl; NID_JKL=uVcubDtW1r9H+2wjqTa52Pujtdy4unhy377y/8JElRI=; _ga=GA1.2.592713173.1580652471; nx_ssl=2; _shopboxeventlog=false; NID_SES=AAABedmjUVXjmL4gy+ydT+bDnWfELVxCj5rKoq3t8XIGNtOORNygYgR/W9IKR1kW7G5tigyI+M2L+fv7H0XVZGJoWuEVlyyPeFEuBisfQ6Ba95uchAiuc0vM/tpVJPw9EG36iPfgUnmiWbqqOnOLXOxJ+iy/4868wTgQtUEb8kBlvJ/ytZECcsFnmyztFGcfhuLVpG3G7X1b3vjOtcXSJC2RPLR0s9lkGXqBEdv+crIc+lJxgYNFXZ2lNcjwtrFQewtDCJY6WcIyVTUYQfrkuhJVdcEwQJf+96ilGYm55qpdsJdPjk7wGbW+2wLYqZQEHPsSfNX/T0fhYg1SQOW2F111DWqD0VuN8QViDUj0MgwgGi4iC51Fmm5axP33ivdWItprIsHG6QVAKLk1rUzPm57RF8nx6pb/u9jG2wf8mTvnEAUFRIq2ynokmER+puuj+uFn04qekZXFdB7XwpykhX5bRLkVDj8GNLhbQRZpGgcEWYwup7NaZeFeMZbzU+bbkt1SMg==; page_uid=hghe9wp0Jy0ssab+zM4ssssssiN-171378; sus_val=yI3Iog73ymvrJ37eTY6Veikl; spage_uid=hghe9wp0Jy0ssab%2BzM4ssssssiN-171378; ncpa=1154320|kt5shlnc|2677eb48cd8fea3256af7388decc1868f343afdd|s_334402acb8f31|6031d27f97817a77ec12e845456f67524d1cf7c7:195260|kt5shvog|192dcf422403ba64bd5b4a96489b2f069007291c|s_4fab9635a0b66dff|6a3ab9d8ebfe410b4b6017228f9bd772cc4f6a11:95694|kt8nxwhs|2f3ef224c295b1eb044f9ead0863e3dc4dd4bbae|null|b5e3019f1de2924f7b6eb81e7c613f4fc68ed128',
}



pgidx = 1
pridx = 0

productfound = False

#productname = input('상품명을 입력하세요: ')
productname = sys.argv[1]
#print(productname)

#searchname = input('검색할 키워드를 입력하세요: ')
searchname = sys.argv[2]
#print(searchname)

while pgidx < 1000:
    params = (
        ('sort', 'rel'),
        ('pagingIndex', pgidx),
        ('pagingSize', '40'),
        ('viewType', 'list'),
        ('productSet', 'total'),
        ('deliveryFee', ''),
        ('deliveryTypeValue', ''),
        ('frm', 'NVSHATC'),
        ('query', searchname),
        ('origQuery', searchname),
        ('iq', ''),
        ('eq', ''),
        ('xq', ''),
    )

    response = requests.get('https://search.shopping.naver.com/api/search/all', headers=headers, params=params)
    result_dict = json.loads(response.text)
    product_data = result_dict['shoppingResult']['products']

    for i in product_data:
        try:
            product = i['productTitle']
            price = i['price']
            # print(product, price)
            smart_farm_data = {
                'product': product,
                'price': price
                }
            pridx = pridx + 1
            #print(pridx, smart_farm_data)
            if product == productname:
                #print(pgidx)
                #print(pridx)
                idx = pridx - 40*pgidx + 40
                print(pgidx, "|", idx)

                productfound = True
                break
        except:
            pass

    if productfound:
        break

    pgidx = pgidx + 1
    #print('next page', pgidx)

    html_text = pgidx
