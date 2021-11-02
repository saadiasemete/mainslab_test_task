import json
import random
from datetime import datetime as dtm, timedelta as tmd

TIME_START = dtm.now()-tmd(hours = 48)

def get_random_time():
    return TIME_START+tmd(hours=random.randint(0,48))

subjects = ('a', 'b', 'c', 'd', 'e', 'a',)
to_emails = ['%s@example.com'%i for i in range(20)]

def generate_single_item(pk):
    return {
        'pk': pk,
        'model': 'api.SentMessageData',
        'fields': {
            'subject': random.choice(subjects),
            'to_email': random.choice(to_emails),
            'created_at': get_random_time().isoformat()
        }
    }

with open('data_seed.json', 'w', encoding='utf-8') as f:
    json.dump([generate_single_item(i) for i in range(10000)], f)