Chargement des données : 

Env: 
```bash
 BDD_PG='postgresql://USER:PASSWORD@HOST.postgres.database.azure.com/BDD?sslmode=require'
 BDD_LITE='sqlite:///test.sqlite'
```

Exécution appli, BDD SQLITE
```bash
 # SQLITE BDD
 BDD_URI=$BDD_LITE python3 hello_app/loadData.py
```

Exécution appli, BDD PROD PG Azure
```bash
 # PROD BDD
 BDD_URI=$BDD_PG python3 hello_app/loadData.py
```

client psql, BDD PROD PG Azure
```bash
 # PROD BDD
 psql $BDD_PG
```

client sqlite, BDD SQLITE
```bash
 # SQLITE BDD
 sqlite3 test.sqlite
```