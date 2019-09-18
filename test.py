#!/usr/bin/env python3
from requests import get
import logging

def reqs(seller_id, offset, limit):
    url = 'https://api.mercadolibre.com/sites/MLA/search?seller_id={seller_id}&offset={offset}&limit={limit}'.format(seller_id=seller_id, offset=offset, limit=limit)
    response = get(url)
    return response.json()

def req_items(seller_id): 
    offset= 0
    rjson = reqs(seller_id=seller_id, offset=offset, limit=50)
    items = rjson['results']
    while rjson['paging']['total'] > offset+50:
        offset +=50
        limit = rjson['paging']['total'] - offset
        if limit >=50:
            limit = 50
        rjson = reqs(seller_id, offset, limit)
        items = items+rjson['results']
    return items

def req_cat_name(cat_id):
    url = 'https://api.mercadolibre.com/categories/{cat_id}'.format(cat_id=cat_id)
    response = get(url).json()
    return response['name']

def logg_item(seller_id):
    items = req_items(seller_id)
    logging.basicConfig(level=logging.INFO,
                    format='%(message)s',
                    filename='test_log.log',
                    filemode='w')
    for item in items:
        cat_name = req_cat_name(item['category_id'])
        logging.info(item['id'] +' , '+ item['title']+' , '+ item['category_id']+' , '+ cat_name)

seller_id = 81644614
logg_item(seller_id)