
# Loading STAC JSONs to a pgstac PostgreSQL Database via Command Line

This guide details how to bulk load STAC JSON data into a pgstac PostgreSQL database using the command line.

## 1. Create Bulk Loading NDJSONs

- Use the `create_ndjson.ipynb` script to generate NDJSON files for all items.
- The script extracts JSON data from the specified location. The catalog line must be removed, and the collection line should be saved to a separate JSON file.
- Move the combined `item.ndjson` and the collection JSON file to another directory for easy access later.<br>
<br>**the create_ndjson notebook should be modified to only compile the items and not the collection and catalog** 
### Example NDJSON 

The resulting NDJSON for the items might look like this, with one:

```json
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o020_xli1m_utm10_2018_cog", "properties": {"datetime": "2024-07-04T15:43:22.851051Z"}, "geometry": {"type": "Polygon", "coordinates": [[[555893.0, 5661307.0], [555893.0, 5672410.0], [567624.0, 5672410.0], [567624.0, 5661307.0], [555893.0, 5661307.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o020_xli1m_utm10_2018_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o020_xli1m_utm10_2018_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [555893.0, 5661307.0, 567624.0, 5672410.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o019_xli1m_utm10_2018_2_cog", "properties": {"datetime": "2024-07-04T15:43:22.167823Z"}, "geometry": {"type": "Polygon", "coordinates": [[[541951.0, 5661212.0], [541951.0, 5670352.0], [556016.0, 5670352.0], [556016.0, 5661212.0], [541951.0, 5661212.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o019_xli1m_utm10_2018_2_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o019_xli1m_utm10_2018_2_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [541951.0, 5661212.0, 556016.0, 5670352.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o029_xli1m_utm10_2019_cog", "properties": {"datetime": "2024-07-04T15:43:23.297861Z"}, "geometry": {"type": "Polygon", "coordinates": [[[542485.0, 5672237.0], [542485.0, 5683491.0], [555894.0, 5683491.0], [555894.0, 5672237.0], [542485.0, 5672237.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o029_xli1m_utm10_2019_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o029_xli1m_utm10_2019_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [542485.0, 5672237.0, 555894.0, 5683491.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o030_xli1m_utm10_2018_cog", "properties": {"datetime": "2024-07-04T15:43:23.544498Z"}, "geometry": {"type": "Polygon", "coordinates": [[[555803.0, 5672369.0], [555803.0, 5681181.0], [559397.0, 5681181.0], [559397.0, 5672369.0], [555803.0, 5672369.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o030_xli1m_utm10_2018_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o030_xli1m_utm10_2018_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [555803.0, 5672369.0, 559397.0, 5681181.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o018_xli1m_utm10_2018_cog", "properties": {"datetime": "2024-07-04T15:43:21.937492Z"}, "geometry": {"type": "Polygon", "coordinates": [[[533696.0, 5666237.0], [533696.0, 5672238.0], [541953.0, 5672238.0], [541953.0, 5666237.0], [533696.0, 5666237.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o018_xli1m_utm10_2018_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o018_xli1m_utm10_2018_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [533696.0, 5666237.0, 541953.0, 5672238.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o019_xli1m_utm10_2018_cog", "properties": {"datetime": "2024-07-04T15:43:22.395401Z"}, "geometry": {"type": "Polygon", "coordinates": [[[541919.0, 5663231.0], [541919.0, 5672371.0], [555994.0, 5672371.0], [555994.0, 5663231.0], [541919.0, 5663231.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o019_xli1m_utm10_2018_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o019_xli1m_utm10_2018_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [541919.0, 5663231.0, 555994.0, 5672371.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o028_xli1m_utm10_2018_cog", "properties": {"datetime": "2024-07-04T15:43:23.065555Z"}, "geometry": {"type": "Polygon", "coordinates": [[[535246.0, 5672186.0], [535246.0, 5678033.0], [541921.0, 5678033.0], [541921.0, 5672186.0], [535246.0, 5672186.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o028_xli1m_utm10_2018_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o028_xli1m_utm10_2018_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [535246.0, 5672186.0, 541921.0, 5678033.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o018_xli1m_utm10_2018_2_cog", "properties": {"datetime": "2024-07-04T15:43:21.719944Z"}, "geometry": {"type": "Polygon", "coordinates": [[[539056.0, 5663025.0], [539056.0, 5668306.0], [541996.0, 5668306.0], [541996.0, 5663025.0], [539056.0, 5663025.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o018_xli1m_utm10_2018_2_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o018_xli1m_utm10_2018_2_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [539056.0, 5663025.0, 541996.0, 5668306.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
{"type": "Feature", "stac_version": "1.0.0", "id": "bc_092o020_xli1m_utm10_2018_2_cog", "properties": {"datetime": "2024-07-04T15:43:22.609228Z"}, "geometry": {"type": "Polygon", "coordinates": [[[555992.0, 5661249.0], [555992.0, 5663233.0], [561120.0, 5663233.0], [561120.0, 5661249.0], [555992.0, 5661249.0]]]}, "links": [{"rel": "root", "href": "../DEM_Test.json", "type": "application/json"}, {"rel": "collection", "href": "../COG-DEM-Test/collection.json", "type": "application/json", "title": "BC-DEM"}, {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}], "assets": {"bc_092o020_xli1m_utm10_2018_2_cog": {"href": "https://nrs.objectstore.gov.bc.ca/cloudgistest/STAC_DEM/Data/bc_092o020_xli1m_utm10_2018_2_cog.tif", "type": "image/tiff; application=geotiff; profile=cloud-optimized"}}, "bbox": [555992.0, 5661249.0, 561120.0, 5663233.0], "stac_extensions": [], "collection": "COG-DEM-Test"}
```

### Example Collection JSON

The collection JSON might look like this:

```json
{
    "type": "Collection",
    "id": "COG-DEM-Test",
    "stac_version": "1.0.0",
    "description": "Digital Elevation Models for the interior of British Columbia",
    "links": [
        {"rel": "root", "href": "../DEM_Test.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o018_xli1m_utm10_2018_2_cog/bc_092o018_xli1m_utm10_2018_2_cog.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o018_xli1m_utm10_2018_cog/bc_092o018_xli1m_utm10_2018_cog.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o019_xli1m_utm10_2018_2_cog/bc_092o019_xli1m_utm10_2018_2_cog.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o019_xli1m_utm10_2018_cog/bc_092o019_xli1m_utm10_2018_cog.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o020_xli1m_utm10_2018_2_cog/bc_092o020_xli1m_utm10_2018_2_cog.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o020_xli1m_utm10_2018_cog/bc_092o020_xli1m_utm10_2018_cog.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o028_xli1m_utm10_2018_cog/bc_092o028_xli1m_utm10_2018_cog.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o029_xli1m_utm10_2019_cog/bc_092o029_xli1m_utm10_2019_cog.json", "type": "application/json"},
        {"rel": "item", "href": "../bc_092o030_xli1m_utm10_2018_cog/bc_092o030_xli1m_utm10_2018_cog.json", "type": "application/json"},
        {"rel": "parent", "href": "../DEM_Test.json", "type": "application/json"}
    ],
    "title": "BC-DEM",
    "extent": {
        "spatial": {"bbox": [[533696.0, 5661212.0, 567624.0, 5683491.0]]},
        "temporal": {"interval": [["2024-07-04T15:43:21.719944Z", "2024-07-04T15:43:21.937492Z"]]}
    },
    "license": "Apache-2.0"
}
```

## 2. Setting Up the PostgreSQL Database

- if you do not have a postgres database with the pgstac extension enabled you will need to create a new database named `PgstacDB` since it's specified in the [pgstac source code](https://github.com/stac-utils/pgstac/blob/main/src/pypgstac/python/pypgstac/load.py#L150).
- Directions on setting the PgstacDB can be found here: [pgstac setup wsl](https://github.com/GrahamMacGregorBCGov/BC_Webmap_Lidar_STAC/blob/main/src/pgstac/pgstac_setup_wsl.md)
- if you do not know the password for the `pgstac_admin` user, change it to a new password:
  ```sql
  ALTER USER pgstac_admin WITH PASSWORD 'new_password';
  ```

### Logging into PostgreSQL via WSL

1. Check the status of the PostgreSQL service:
   ```bash
   sudo service postgresql status
   ```
2. Start the PostgreSQL service if it's not running:
   ```bash
   sudo service postgresql start
   ```
3. Log in to the `PgstacDB` database:
   ```bash
   psql -h localhost -p 5432 -U pgstac_admin -d PgstacDB
   ```
4. once verified database works exit the database: 
   ``` bash
      \q
   ```

### Setting Environment Variables

Set the necessary environment variables (ensure no spaces on either side of `=`):

```bash
export PGHOST=localhost
export PGPORT=5432
export PGUSER=pgstac_admin
export PGPASSWORD=new_password
export PGDATABASE=PgstacDB
```

To verify the environment variables are set correctly:

```bash
echo $PGHOST $PGPORT $PGUSER $PGPASSWORD $PGDATABASE
```

## 3. Loading Collections and Items

- Activate the Python environment with `pypgstac`:
  ```bash
  mamba activate stac_tools
  ```
- Navigate to the directory containing the NDJSON files:
  ```bash
  cd /STAC_LiDAR/ndjson
  ```

### Loading Collections

- Collections need to be loaded separately and before the items. Use the following command to load a collection NDJSON file:
  ```bash
  pypgstac load collections 'stac_collection.ndjson'
  ```

### Loading Items

- After loading the collections, load the items using:
  ```bash
  pypgstac load items 'stac_dem_combined.ndjson'
  ```

- If there are potential conflicts (e.g., duplicates), refer to the documentation for resolving them.

### Success?

If everything is configured correctly, the items should be successfully loaded into the `pgstac` database, and you will find the jsons under the tables pgstac.collections and pgstac.items
