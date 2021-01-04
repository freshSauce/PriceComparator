import requests as r
from bs4 import BeautifulSoup
from re import sub, match
from flask import Flask, request, Response

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
app = Flask(__name__)
requestFormat = 'r.{0}("{1}", {2}=data, headers=headers)'


def openList(file):
    # Abre el documento con las páginas web scrapeables
    try:
        with open(file, 'r', newline='') as websites:
            weblist = websites.readlines()
            websites.close()
            websites = [web for web in (webs.strip().split()[1] for webs in weblist)]
            return websites
    except Exception as e:
        return f'Something went wrong, contact the script creator. \nError: {str(e)}'

def mipc(item):
    try:
        data = {
            'q':item
        }
        response = eval(requestFormat.format('get', f'{[web for web in openList("weblist.md") if "mipc" in web][0]}catalogsearch/result/', 'params'))
        if 'catalogsearch/result/' in response.url:
            # Si no reedirige a un item específico, se scrapea la data obteniendo el primer item
            item = str(BeautifulSoup(response.text, 'html.parser').findAll('li', attrs={'class':'item product product-item col'})[0])
            itemName = BeautifulSoup(item, 'html.parser').find('a', attrs={'class':'product-item-link'}).text
            link = BeautifulSoup(item, 'html.parser').find('a', attrs={'class':'product-item-link'})['href']
            price = BeautifulSoup(item, 'html.parser').find('span', attrs={'class':'price'}).text
            return {'link':link, 'price':price, 'name':itemName}
        else:
            # Si se obtiene un item especifico, scrapea la data del item
            item = str(BeautifulSoup(response.text, 'html.parser').find('div', attrs={'class':'product-info-main'}))
            price = BeautifulSoup(item, 'html.parser').find('span', attrs={'class':'price'}).text
            itemName = BeautifulSoup(item, 'html.parser').find('h1', attrs={'class':'name'}).text
            link = response.url
            return {'link':link, 'price':price, 'name':itemName}



    except:
        # En caso de no encontrar el item manda este error
        {'link':'https://mipc.com.mx', 'price':'', 'name':'Item no encontrado, prueba cambiando el nombre del item.'}



def cyberpuerta(item):
    try:
        data = {
            'cl': 'search',
            'searchparam':item
            }
        
        response = eval(requestFormat.format('get', f'{[web for web in openList("weblist.md") if "cyberpuerta" in web][0]}index.php', 'params'))
        if 'index.php' in response.url:
            item = str(BeautifulSoup(response.text, 'html.parser').find('div', attrs={'class':'emproduct_right'}))
            price = BeautifulSoup(item, 'html.parser').find('label', attrs={'class':'price'}).text.strip()
            itemName = BeautifulSoup(item, 'html.parser').find('a', attrs={'id':'searchList-1'})['title']
            link = BeautifulSoup(item, 'html.parser').find('a', attrs={'id':'searchList-1'})['href']
            return {'link':link, 'price':price, 'name':itemName}
        else:
            try:
                item = str(BeautifulSoup(response.text, 'html.parser').find('div', attrs={'class':'emproduct_right'}))
                price = BeautifulSoup(item, 'html.parser').find('label', attrs={'class':'price'}).text.strip()
                itemName = BeautifulSoup(item, 'html.parser').find('a', attrs={'id':'productList-1'})['title']
                link = BeautifulSoup(item, 'html.parser').find('a', attrs={'id':'productList-1'})['href']
                return {'link':link, 'price':price, 'name':itemName}

            except:
                # En caso de no encontrar el item manda este error
                {'link':'https://www.cyberpuerta.mx', 'price':'', 'name':'Item no encontrado, prueba cambiando el nombre del item.'}
    except Exception as e:
        # En caso de no encontrar el item manda este error
        return {'link':'https://www.cyberpuerta.mx', 'price':'', 'name':'Item no encontrado, prueba cambiando el nombre del item.'}




def ddtech(item):
    try:
        data = {
            'search':item,
            'buscar':''
        }
        response = eval(requestFormat.format('post', f'{[web for web in openList("weblist.md") if "ddtech" in web][0]}productos/buscar/', 'data'))
        if response.url != 'https://ddtech.mx/':
            item = str(BeautifulSoup(response.text, 'html.parser').find('div', attrs={'class':'item item-carousel col-sm-4 products-prev'}))
            price = BeautifulSoup(item, 'html.parser').find('span', attrs={'class':'price'}).text.strip()
            itemName = BeautifulSoup(item, 'html.parser').find('a')['title']
            link = BeautifulSoup(item, 'html.parser').find('a')['href']
            return {'link':link, 'price':price, 'name':itemName}
        else:
            # En caso de no encontrar el item manda este error
            return {'link':'https://ddtech.mx', 'price':'', 'name':'Item no encontrado, prueba cambiando el nombre del item.'}
    except:
        # En caso de no encontrar el item manda este error
        return {'link':'https://ddtech.mx', 'price':'', 'name':'Item no encontrado, prueba cambiando el nombre del item.'}

def priceGet(item):
    # Itera por las funciones obteniendo los resultados de cada una y poniendolos en na lista
    result = [func(item) for func in [mipc, cyberpuerta, ddtech]]
    full = []
    for i in result:
        # Se obtiene el formato de información que será regresado al usuario
        mainName = (
            f'MiPC: \n\n' if 'mipc' in i['link'] else 'CyberPuerta: \n\n' if 'cyberpuerta' in i['link'] else 'DDTech: \n\n'
        )
        info = (
            f'Nombre: {i["name"]}\n'
            f'Precio: {i["price"]}\n'
            f'Link: {i["link"]}\n'
            )

        full.append(mainName+info)
    # Empieza el chequeo del mejor precio haciendo una lista que retorna los precios si la longitud del precio es mayor a 1
    betterPrice = [i['price'] for i in [i for i in result] if len(i['price']) > 1]
    # Ordena los precios - CAMBIAR FORMA DE ORDENARLOS
    betterPrice.sort()
    betterPrice = (f"Mejor precio: {betterPrice[0]} \nLink: {[i['link'] for i in result if i['price'] == betterPrice[0]][0]}")
    return '\n'.join(full), betterPrice

def getlastMsg(msg):
    chat_id = msg['message']['chat']['id']
    text = msg['message']['text']
    return text,chat_id

                   
# Función del webhook
@app.route('/', methods=['POST', 'GET'])
def index():
    TGLink = 'https://api.telegram.org/bot<YOUR_BOT_API_KEY>/sendMessage'
    if request.method == 'POST':
        msg = request.get_json()

        lastmsg, chat_id = getlastMsg(msg)
        
        if lastmsg.split()[0] == '/start':
            start_message = '''
                <strong>¡Bienvenido al Comparador de Precios MX!</strong>
            
    El bot actualmente funciona con los siguientes sitios:

        - <a href="https://mipc.com.mx/">MiPC</a>
        - <a href="https://www.cyberpuerta.mx/">CyberPuerta</a>
        - <a href="https://ddtech.mx/">DDTech</a>

    Uso:

        /compare &lt;item_a_comparar&gt;

        O bien

        !compare &lt;item_a_comparar&gt;

Si conoces alguna página que deba ser agregada, o bien, ocurrió algun error con el bot, manda mensaje al <a href="tg://user?id=560110547">creador del bot</a>

            
            '''
            data = {
                'chat_id':chat_id,
                'text': start_message,
                'parse_mode':'HTML',
                'disable_web_page_preview':'true'
            }

            r.post(TGLink, data=data)

        elif bool(match(r'[!/]compare [\w\W]+', lastmsg)):
            try:
            
                lista, betterPrice = priceGet(' '.join(lastmsg.split()[1:]))
        
                data = {
                        'chat_id':chat_id,
                        'text': lista,
                        'disable_web_page_preview':'true'
                    }
                r.post(TGLink, data=data)
                data = {
                        'chat_id':chat_id,
                        'text': betterPrice,
                        'disable_web_page_preview':'true'
                    }
                r.post(TGLink, data=data)
                   
            except Exception as e:
                   data = {
                        'chat_id':chat_id,
                        'text':f'Something went wrong while scraping the data: {str(e)}, please, send this message and your input to the script creator.\n\nHubo un Error al obtener la información {str(e)}, por fabor, envía este mensaje y tu input al creador del script.',
                        'disable_web_page_preview':'true'
                    }
                   r.post(TGLink, data=data)
                   return Response('Ok', status=200)
        return Response('Ok', status=200)


    else:
        return '<h1>MÉTODO: GET</h1>' 


if __name__ == '__main__':
    app.run(debug=True)
