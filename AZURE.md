
# Environnements

```bash
 BDD_PG='postgresql://USER:PASSWORD@HOST.postgres.database.azure.com/BDD?sslmode=require'
 BDD_LITE='sqlite:///test.sqlite'
```

# Load Data

Load data, BDD SQLITE
```bash
 # SQLITE BDD
 BDD_URI=$BDD_LITE python3 hello_app/loadData.py
```

Load data, BDD PROD PG Azure
```bash
 # PROD BDD
 BDD_URI=$BDD_PG python3 hello_app/loadData.py
```

# Appli

lien appli Azure : [p2w23web](https://p2w23web.azurewebsites.net)

```bash
 # PROD BDD
 BDD_URI=$BDD_PG python3 hello_app/views.py
```

# Clients BDD

BDD PROD PG Azure
```bash
 # PROD BDD
 psql $BDD_PG
```

BDD SQLITE
```bash
 # SQLITE BDD
 sqlite3 test.sqlite
```