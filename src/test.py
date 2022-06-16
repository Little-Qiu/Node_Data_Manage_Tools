

from osgeo import gdal;
from osgeo import ogr;
import sys;

# print(gdal.__version__)

gdal.SetConfigOption( "GDAL_FILENAME_IS_UTF8", "YES")
gdal.SetConfigOption( "SHAPE_ENCODING", "GBk")

driver = ogr.GetDriverByName('ESRI Shapefile')
# shp文件路径
file_name = 'D:/03_Work/03_航天智慧/03_CIG_data_work/01_data_guangzhou_huangpu/03_shp/GRID_COMMUNITY_GEO.shp'
# Open方法第二个参数0表示只读
data_source = driver.Open(file_name, 0)

if data_source is None:
    print("文件【%s】无法打开", file_name)
    sys.exit(-1)

layer = data_source.GetLayer(0)
for feature in layer:
	# 要素字段名集合
	keys = feature.keys()
	for key in keys:
		# 要素字段值
		value = feature.GetField(key)
		print("{}-->{}".format(key, value))
	# 图形字段
	# geometry = feature.geometry()
	print("-----------")
del data_source