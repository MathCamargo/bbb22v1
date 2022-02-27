import tweepy as tw
import pandas as pd
from time import sleep
from os import environ

# Criando autorização para o BOT 
acess_token = environ['acess_token']
acess_token_secret = environ['acess_token_secret']
api_key = environ['api_key']
api_secret_key = environ['api_secret_key']
bearer_token = environ['bearer_token']
client = tw.Client(bearer_token=bearer_token, consumer_key=api_key, consumer_secret=api_secret_key, access_token=acess_token, access_token_secret=acess_token_secret, wait_on_rate_limit=False)

# Definindo nomes e apelidos, para melhor busca na internet
players = {'Laís': ['lais', 'laís'], 
'Luciano': ['luciano'], 
'Jessilane': ['jessilane', 'jessi'], 
'Eliezer': ['eliezer'], 
'Eslovênia': ['eslovênia', 'eslovenia', 'eslovaca'], 
'Lucas': ['lucas', 'barão da piscadinha', 'barao da piscadinha', 'piscadinha'], 
'Bárbara': ['bárbara', 'barbara'], 
'Arthur': ['arthur aguiar', 'arthur'], 
'Rodrigo': ['rodrigo'], 
'Natália': ['natália', 'natalia'], 
'Vinicius': ['vinicius', 'vyni'], 
'Pedro': ['pedro scooby', 'scooby'], 
'Brunna': ['brunna gonçalves', 'brunna', 'bruna'], 
'Paulo': ['paulo andré', 'paulo andre', 'pa', 'p.a'], 
'Maria': ['maria'], 
'Jade': ['jade', 'jade picon'], 
'Douglas': ['douglas silva', 'dg'], 
'Linna': ['lin', 'linn', 'linna'], 
'Tiago': ['tiago abravanel', 'thiago abravanel', 'neto do silvio santos'], 
'Naiara': ['naiara azevedo'],
'Gustavo': ['gustavo'],
'Larissa': ['larissa', 'lari']
}

# Definindo dict de notoriedade, para salvar as menções
notoriedade = {'Laís': 0, 'Luciano': 0, 'Jessilane': 0, 'Eliezer': 0, 
                'Eslovênia': 0, 'Lucas': 0, 'Bárbara': 0, 'Arthur': 0, 
                'Rodrigo': 0, 'Natália': 0, 'Vinicius': 0, 'Pedro': 0, 
                'Brunna': 0, 'Paulo': 0, 'Maria': 0, 'Jade': 0, 'Douglas': 0, 
                'Linna': 0, 'Tiago': 0, 'Naiara': 0, 'Gustavo': 0, 'Larissa': 0}

# Abrindo meu arquivo em PANDAS
df = pd.read_excel('notor.xlsx')

# Pesquisando e salvando dados na tabela 
while True:
    search = client.search_recent_tweets(query='#BBB22', max_results = 100)
    data = search.data
    for i in data:
        text = i.text
        if 'RT' in text:
            text = text[text.find(':')+2:]
        for k in players:
            if k in text:
                notoriedade[k] += 1
    for j in notoriedade:
        df.loc[df['Participante'] == j, 'Mencoes'] = df['Mencoes'] + notoriedade[j]
    df.to_excel('notor.xlsx', index=False, encoding='UTF-8')
    sleep(3600)