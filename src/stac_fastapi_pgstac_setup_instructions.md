
# STAC FastAPI PGStac Setup Instructions

### 1. Clone the `stac-fastapi-pgstac` Repository

First, open your WSL command window and navigate to the desired location where you want to clone the repository.

```bash
cd /path/to/your/location
sudo git clone https://github.com/stac-utils/stac-fastapi-pgstac
```

### 2. Update `docker-compose.yml`

In the `docker-compose.yml` file, update the configuration to use environment variables for the PostgreSQL-related values. 

If you encounter issues saving or editing files in WSL, use the following command to change ownership of the folder (replace `myuser` and `/path/to/folder` with your username and path):

```bash
sudo chown -R myuser /path/to/folder
```

Make sure the ports are consistent across services.

#### Example `docker-compose.yml` Updates

```yaml
app:
  environment:
    - POSTGRES_USER=${POSTGRES_USER}
    - POSTGRES_PASS=${POSTGRES_PASSWORD}
    - POSTGRES_DBNAME=${POSTGRES_DB}

database:
  environment:
    - POSTGRES_USER=${POSTGRES_USER}
    - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
    - POSTGRES_DB=${POSTGRES_DB}
    - PGUSER=${POSTGRES_USER}
    - PGPASSWORD=${POSTGRES_PASSWORD}
    - PGDATABASE=${POSTGRES_DB}
```

### 3. Create the `.env` File

In the root directory of the cloned repository, create a `.env` file with the following content:

```bash
POSTGRES_DB=stacdb
POSTGRES_USER=gis
POSTGRES_PASSWORD=password
STAC_API_URL=http://localhost:8082
STAC_API_TITLE=STAC API
STAC_API_DESCRIPTION=A STAC API powered by FastAPI and pgstac
PGSTAC_SCHEMA=public
PGSTAC_DB_CONN=postgresql://gis:password@db:5432/stac
```

### 4. Build and Run the Docker Containers

Once the `docker-compose.yml` and `.env` files are set up, return to the WSL command window and navigate to the location of the cloned repository.

```bash
cd /path/to/repo/stac-fastapi-pgstac
docker compose build
docker compose up -d
```

Check if the API is running by navigating to the URL specified in the `.env` file (`http://localhost:8082`). It should display a JSON-formatted page.

### 5. Load STAC Catalog and Items into PostgreSQL

Now that the API is running, you can load your STAC catalog and items into the PostgreSQL database using `pypgstac`.

First, activate a virtual environment that contains `pypgstac`:

```bash
mamba activate stac_tools
```

Then, export the necessary environment variables:

```bash
export PGHOST=localhost
export PGPORT=5439
export PGUSER=gis
export PGPASSWORD=password
export PGDATABASE=stacdb
```

Navigate to the directory where your STAC NDJSON files are stored, or provide the full path to the files, and load them:

```bash
pypgstac load collections stac_collection.ndjson
pypgstac load items stac_dem_combined.ndjson
```

### 6. Connect to STAC API in QGIS

Finally, open QGIS and install the STAC Browser plugin. Create a new connection with the URL specified in your `.env` file. Test the connection and fetch the available collections!

Happy STAC-ing!
