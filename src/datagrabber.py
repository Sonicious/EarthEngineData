from pystac_client import Client
import ee, geemap, eemont
import wxee

ee.Initialize()
wxee.Initialize()

client = Client.open("https://earthengine-stac.storage.googleapis.com/catalog/catalog.json")
print(f"{client.title}: {client.description}")

geom = ee.Geometry.Point([10.434102660958201, 51.08111585538142])  # Hainich

l9 = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2") \
    .filterBounds(geom) \
    .filterDate("2022-01-01","2022-02-01")
l9_scaled = l9.scaleAndOffset()
Map = geemap.Map()
Map.addLayer(l9_scaled.first(), {
             "bands": ["SR_B4", "SR_B3", "SR_B2"], "min": 0, "max": 0.3})
Map.centerObject(l9_scaled.first())

