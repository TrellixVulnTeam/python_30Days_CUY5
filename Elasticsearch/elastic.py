from elasticsearch import Elasticsearch

# create an instance of elasticsearch and assign it to port 9200
ES_HOST = {"host": "localhost", "port": 9200}
es = Elasticsearch(hosts=[ES_HOST])


def create_index(index_name):
    """Functionality to create index."""
    resp = es.indices.create(index=index_name)
    print(resp)


def document_add(index_name, doc_type, doc, doc_id=None):
    """Funtion to add a document by providing index_name,
    document type, document contents as doc and document id."""
    resp = es.index(index=index_name, doc_type=doc_type, body=doc, id=doc_id)
    print(resp)


def document_view(index_name, doc_type, doc_id):
    """Function to view document."""
    resp = es.get(index=index_name, doc_type=doc_type, id=doc_id)
    document = resp["_source"]
    print(document)


def document_update(index_name, doc_type, doc_id, doc=None, new=None):
    """Function to edit a document either updating existing fields or adding a new field."""
    if doc:
        resp = es.index(index=index_name, doc_type=doc_type,
                        id=doc_id, body=doc)
        print(resp)
    else:
        resp = es.update(index=index_name, doc_type=doc_type,
                         id=doc_id, body={"doc": new})


def document_delete(index_name, doc_type, doc_id):
    """Function to delete a specific document."""
    resp = es.delete(index=index_name, doc_type=doc_type, id=doc_id)
    print(resp)


def delete_index(index_name):
    """Delete an index by specifying the index name"""
    resp = es.indices.delete(index=index_name)
    print(resp)


    import tutorial
    tutorial.create_index('novels')
    tutorial.document_add('novels', 'authors', {'name':'Sidney Sheldon'}, 1)
    tutorial.document_view(index_name='novels', doc_type='authors', doc_id=1)


import pandas as pd
tables = pd.read_html("https://www.yelp.com/search?cflt=restaurants&find_loc=Newport%20Beach")
print(tables[0])

class Python:
    name="Tahir"
    age=23
    country="Pakistan"
    def abc(self):
        return(self.name,self.age,self.country)
inst = Python()
x,y,z = inst.abc()