import os
from datetime import datetime
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_elk.settings')

import django
django.setup()
from django.conf import settings
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch

class Command(BaseCommand):
    help = "Check Elastic connection"

    def handle(self, *args, **options):
        log_entry = "Checking Elastic connection"
        self.stdout.write(log_entry)

        es = Elasticsearch([settings.ELASTIC_ENDPOINT])
        doc = {
                'city': 'test',
                'population': '34',
                'timestamp': datetime.now()
            }
        res = es.index(index=settings.ELASTIC_INDEX_NAME, id=doc['city'], document=doc)
        log_entry = str(res)
        self.stdout.write(log_entry)

if __name__ == "__main__":
    pass