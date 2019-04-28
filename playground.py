from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
es.index(index='my_index', doc_type='my_index', id=1, body={'text': 'this is a test'})
es.index(index='my_index', doc_type='my_index', id=2, body={'text': 'a second test'})
es.search(index='my_index', body={'query': {'match': {'text': 'this test'}}})

import pprint

pp = pprint.PrettyPrinter(indent=4)
results = es.search(index='my_index', body={'query': {'match': {'text': 'a second test'}}})
pp.pprint(results)

es.indices.delete('my_index')
