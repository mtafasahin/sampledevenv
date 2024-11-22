# my_elasticsearch_fdw/elasticsearch_fdw.py
import logging
from multicorn import ForeignDataWrapper
from multicorn.utils import log_to_postgres
from elasticsearch import Elasticsearch
import certifi

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class ElasticsearchFDW(ForeignDataWrapper):
    def __init__(self, options, columns):
        
        super(ElasticsearchFDW, self).__init__(options, columns)
        
        self.columns = columns
        self.index = options.get("index", None)
        self.doc_type = options.get("doc_type", None)
        self.host = options.get("host", "172.21.0.3")
        self.port = options.get("port", "9200")
        self.scheme = options.get("scheme", "http")
        self.source_fields = options.get("source_fields", "").split(",")
        self.es = Elasticsearch("https://elastic:pze1EGattlzdTkybW0dv@172.21.0.3:9200/",ca_certs=certifi.where(), verify_certs=False)
            
        

    def execute(self, quals, columns):
        query = self._build_query(quals)
        # try:
        result = self.es.search(index=self.index, body=query)
        for hit in result['hits']['hits']:
            # yield hit['_source']
            person = hit['_source']
            addresses = person.get('addresses', [])
            for address in addresses:
                row = {                    
                    'first_name': person.get('first_name'),
                    'last_name': person.get('last_name'),
                    'city': address.get('city'),
                    'street': address.get('street')
                }
                yield row
        # except Exception as e:
        #     log_to_postgres(f"Elasticsearch query failed: {str(e)}", level='ERROR')

    def _build_query(self, quals):
        
        query = {
            "_source": self.source_fields,
            "query": {
                "bool": {
                    "must": []
                }
            }
        }
        for qual in quals:
            query["query"]["bool"]["must"].append({
                "match": {
                    qual.field_name: qual.value
                }
            })
        
        return query
