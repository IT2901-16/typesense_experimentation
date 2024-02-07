# Installation

Simple install with docker

1. Create a typesense-data directory

```bash
mkdir $(pwd)/typesense-data
```
2. Run the build command
```bash
docker-compose up -d --build
```

You will now have two docker containers running, the app and typesense.

3. Load documents

Put the documents.jsonl file from teams into `data/`

To load all the documents into typesense, run
```bash
docker-compose exec app python import_documents.py
```

You should now be able to visit the dashboard at
```
http://localhost:8501
```