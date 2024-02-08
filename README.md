# Installation

Simple install with docker

1. Create a typesense-data directory

```bash
mkdir $(pwd)/typesense-data
```

2. Load documents

Create a data directory

```bash
mkdir $(pwd)/data
```

Put the documents.jsonl file from teams into the newly created directory

3. Run the build command
```bash
docker-compose up -d --build
```

You will now have two docker containers running, the app and typesense.

4. Load documents

Then run the following command to load the documents.jsonl into the typesense service.
```bash
docker-compose exec app python scripts/import_documents.py
```

You should now be able to visit the dashboard at
```
http://localhost:8501
```
