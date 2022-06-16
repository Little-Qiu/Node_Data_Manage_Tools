
from osgeo import gdal;
from osgeo import ogr;
import sys;

# print(gdal.__version__)

gdal.SetConfigOption( "GDAL_FILENAME_IS_UTF8", "YES")
gdal.SetConfigOption( "SHAPE_ENCODING", "GBk")

gdal.SetConfigOption("PGEO_DRIVER_TEMPLATE", "DRIVER=Microsoft Access Driver (*.mdb, *.accdb);DBQ=%s")
gdal.SetConfigOption("MDB_DRIVER_TEMPLATE", "DRIVER=Microsoft Access Driver (*.mdb, *.accdb);DBQ=%s")

ogr.RegisterAll()
file_name = 'D:/03_Work/03_航天智慧/03_CIG_data_work/GD_HP_GRID_20210425UP.mdb'
data_source = ogr.Open(file_name,0)
if data_source is None:
    print("文件【%s】无法打开", file_name)
    sys.exit(-1)
