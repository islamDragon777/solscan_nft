import requests
import time
import threading
import random
import eel


def Proxi():
    with open('sosk5_2022-08-24_20-25-12.txt') as txt_file:
        txt = txt_file.read()
        txt_file.close()
    count = 0
    for prox in txt.split('\n'):
        t = prox.replace('"', '')
        proxy.append(prox)
        count += 1
    print('кол-во прокси:', len(proxy))

# 8seow37AXM8kotVqEL7Awhc3PuEXiqy2yGaV3WKeWLd
# GttVBwwTjApyVZfPjMagpvRidCjXaUQ9t1BD5vTYCC93
@eel.expose
def get_address(wallet):
    start_time = time.time()
    nft = ''
    URL = f'https://api.solscan.io/account/tokens?address={wallet}&price=1'
    response = requests.get(URL, headers=HEADERS[random.randint(0, 2)])
    print('response-1', response)
    slovar = response.json()
    #print(slovar['data'])
    try:
        for i in slovar['data']:
            try:
                if int(i["tokenAmount"]["amount"]) > 0:
                    if str(i['tokenIcon'])[-2:] == '20':
                        nft += f'<image src="{str(i["tokenIcon"])[:-2]}110"  height="110px" width="110px">'
                        token_address.append(i['tokenAddress'])
                    else:
                        nft += f'<img src="{i["tokenIcon"]}" height="110px" width="110px">'
                        token_address.append(i['tokenAddress'])
            except Exception as e:
                print(e)
                continue
        nft += '<br><br>'+str(time.time() - start_time )+'сек'
    except:
        print('не найдено')



    #print(nft)
    return nft




# def get_image(id):
#     for t in range(len(tokens) // count_thread):
#         try:
#             URL_1 = f'https://api.solscan.io/account?address={tokens[id]}'
#             response = requests.get(URL_1, headers=HEADERS[random.randint(0, 2)], proxies={'http': f'socks5://{proxy[random.randint(0, 147)]}'})
#             print('response-2', response)
#             slovar2 = response.json()
#             print(slovar2)
#             id += 1
#         except Exception as e:
#             print('error 1 -', e)
#             continue
#         try:
#             URL_2 = f"{slovar2['data']['metadata']['data']['uri']}"
#             response2 = requests.get(URL_2, headers=HEADERS[random.randint(0, 2)], proxies={'http': f'socks5://{proxy[random.randint(0, 147)]}'})
#             print('response-3', response2)
#             slovar3 = response2.json()
#             nft_image.append(slovar3['image'])
#             print('image -', slovar3['image'])
#         except Exception as e:
#             print('error 2 -', e)
#             continue


# def threads():
#     arg = 0
#     d = len(nft_image) // count_thread
#     print('d -', d)
#     for potok in range(count_thread):
#         print('arg -', arg)
#         t = threading.Thread(target=get_image, args=(arg,))
#         potoki.append(t)
#         t.start()
#         arg += d



def html(wallet):
    print(wallet)
    img = ['<img src="https://image1.solscan.io/?url=https://nftstorage.link/ipfs/bafybeigkhdrns3aszrj4ig5kibp3dzwwvaevt7hz5gxhn3lowsldohbvlq/359.jpeg&w=100" height="100px" width="100px">']

    return img

#document.getElementByid('ad').value;

# def html():
#     print(nft_image)
#     img_html = ''
#     for o in nft_image:
#         img_html += f'''<img src="{o}" alt="1" height="100px"
#                         width="100px">'''
#
#
#     txt = f'''<!DOCTYPE html>
#     <html lang="en">
#     <head>
#         <meta charset="UTF-8">
#         <meta http-equiv="X-UA-Compatible" content="IE=edge">
#         <meta name="viewport" content="width=device-width, initial-scale=1.0">
#         <title>ScanWallet</title>
#     </head>
#     <body>
#         <div>
#             {img_html}
#     </body>
#     </html>'''
#
#     f = open('web/text.html', 'w')
#     f.write(txt)
#     f.close()





if __name__ == '__main__':
    HEADERS = [{'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 YaBrowser/20.9.3.136 Yowser/2.5 Safari/537.36'},
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'},
               {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36'}]

    start_time = time.time()
    #eel.init('web')
    #eel.start('text.html')
    token_address = []
    tokens = nft_image = potoki = proxy = []
    #get_address()
    #html()
    eel.init('web')
    eel.start('sol.html')
    print(len(nft_image))
    print(time.time() - start_time)