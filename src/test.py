import ee
import wxee
import matplotlib.pyplot as plt

ee.Initialize()
wxee.Initialize()

geom = ee.Geometry.Point([12.371255943360984, 51.34689601157099])  # Leipzig Home
geom_region = geom.buffer(1000) # 1 km buffer

ic1 = ee.ImageCollection("MODIS/061/MOD09GQ") \
    .filterBounds(geom) \
    .filterDate("2020-10-21") \
    .map(lambda x: x.clipToBoundsAndScale(geom_region,scale=250))

ic2 = ee.ImageCollection("LANDSAT/LC09/C02/T1_L2") \
    .filterBounds(geom) \
    .filterDate("2020-10-21")

ic1.wx.to_tif(
    out_dir="data",
    file_per_band = True
)
ic2.wx.to_tif(
    out_dir="data",
    file_per_band = True
)
ic1xx = ic1.wx.to_xarray()
