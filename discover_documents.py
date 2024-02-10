from connect import connect
from config import load_config

def get_docs_for_org(org):
    config = load_config()
    db_conn = connect(config)
    cursor = db_conn.cursor()
    cursor.execute("INSERT INTO documents (id, org, last_update) VALUES (%s, %s, %s)", (1, org, "2019-01-01"))
    cursor.execute("SELECT * FROM documents")
    print(cursor.fetchall())
    db_conn.commit()
if __name__ == "__main__":
    get_docs_for_org("orgn")
    
    
