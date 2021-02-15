from neo4j import GraphDatabase
from pandas import DataFrame
import os
import pathlib

class Neo4jConnection:
    
    def __init__(self, uri, user, pwd):
        self.__uri = uri
        self.__user = user
        self.__pwd = pwd
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__pwd))
        except Exception as e:
            print("Failed to create the driver:", e)
        
    def close(self):
        if self.__driver is not None:
            self.__driver.close()
        
    def query(self, query, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try: 
            session = self.__driver.session(database=db) if db is not None else self.__driver.session() 
            response = list(session.run(query))
        except Exception as e:
            print("Query failed:", e)
        finally: 
            if session is not None:
                session.close()
        return response

if __name__ == '__main__':
    user=input("Please give the user name:")
    pwd=input("Password:")
    db=input("Database name:")
    uri="bolt://localhost:7687"

    conn = Neo4jConnection(uri, user, pwd)

    query_string = '''
    MATCH (n)
    WHERE NOT n:Metagraph AND size(labels(n))>0
    WITH labels(n) as LABELS, keys(n) as KEYS
    MERGE (m:Metagraph:NodeType {labels: LABELS})
    SET m.properties =
    CASE m.properties
        WHEN NULL THEN KEYS
        ELSE apoc.coll.union(m.properties, KEYS)
    END
    '''
    conn.query(query_string, db)

    query_string = '''
    MATCH (n)-[r]->(m)
    WHERE NOT n:Metagraph AND NOT m:Metagraph
    WITH labels(n) as start_labels, type(r) as rel_type, keys(r) as rel_keys, labels(m) as end_labels
    MERGE (a:Metagraph:NodeType {labels: start_labels})
    MERGE (b:Metagraph:NodeType {labels: end_labels})
    MERGE (rel:Metagraph:RelType {type:rel_type})
    MERGE (a)<-[:StartNodeType]-(rel)-[:EndNodeType]->(b)
    SET rel.properties =
    CASE
        WHEN rel.properties IS NULL AND rel_keys IS NULL THEN []
        WHEN rel.properties IS NULL AND rel_keys IS NOT NULL THEN rel_keys
        WHEN rel.properties IS NOT NULL AND rel_keys IS NULL THEN rel.properties
        WHEN rel.properties IS NOT NULL AND rel_keys IS NOT NULL THEN apoc.coll.union(rel.properties, rel_keys)
    END
    '''
    conn.query(query_string, db)

    query_string = '''
    CALL apoc.meta.schema() YIELD value as schemaMap
    UNWIND keys(schemaMap) as label
    WITH label, schemaMap[label] as data
    WHERE data.type = "node"
    UNWIND keys(data.properties) as property
    WITH label, property, data.properties[property] as propData
    RETURN label,
    property,
    propData.type as type,
    propData.indexed as isIndexed,
    propData.unique as uniqueConstraint,
    propData.existence as existenceConstraint
    '''
    dtf_data = DataFrame([dict(_) for _ in conn.query(query_string, db)])

    dtf_data.to_csv(path_or_buf=open(os.path.join(pathlib.Path().absolute(), 'metadata.csv'), 'w'),index=False)

    print('The metadata are generated in \'metadata.csv\'')
    conn.close()