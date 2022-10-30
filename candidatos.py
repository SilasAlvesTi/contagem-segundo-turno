from time import sleep
from datetime import datetime
import json

import requests
import pandas as pd

while True:
    
    print('----------------------------NOVA REQUISIÇÂO----------------------------------')
    print(f'----------------------------{datetime.now().time()}----------------------------------')

    data = requests.get(
        'https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json'
    )
    json_data = json.loads(data.content)
    
    df = pd.DataFrame(
        [
            [
                json_data['cand'][0]['vap'], 
                json_data['cand'][0]['pvap']
            ],
            [
                json_data['cand'][1]['vap'], 
                json_data['cand'][1]['pvap']
            ]
        ],
        index=[json_data['cand'][0]['nm'], json_data['cand'][1]['nm']],
        columns=['Total votos', 'Porcentagem Votos']
    )
    
    print(df)

    sleep(300)