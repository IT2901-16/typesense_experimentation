import typesense


def create_collection(client):
    try:
        client.collections['routines'].delete()
    except Exception as e:
        pass
    client.collections.create({
        "name": "routines",
        "fields": [
        {"name": "Dokument-ID", "type": "string"},
        {"name": "Dokumentnavn", "type": "string"},
        {"name": "Søkeord", "type": "string"},
        {"name": "Sist endret av", "type": "string"},
        {"name": "Revisjonsansvarlig", "type": "string"},
        {"name": "Dokumentansvarlig", "type": "string"},
        {"name": "Dokumentansvarlig dokument", "type": "string"},
        {"name": "Godkjenner dokument", "type": "string"},
        {"name": "Godkjenner", "type": "string"},
        {"name": "Revisjonsansvarlig dokument", "type": "string"},
        ],
    })


def import_documents(client):
    with open('data/documents.jsonl') as jsonl_file:
        client.collections['routines'].documents.import_(jsonl_file.read().encode('utf-8'), {'action': 'create'})
        print("Import successful!")

def main():
    client = typesense.Client({
    'api_key': 'xyz',
    'nodes': [{
        'host': 'typesense',
        'port': '8108',
        'protocol': 'http'
    }],
    'connection_timeout_seconds': 500
    })
    create_collection(client)
    import_documents(client)

if __name__ == "__main__":
    main()
