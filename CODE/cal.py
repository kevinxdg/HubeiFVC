#coding=utf-8

from commol import *
import os
import arcpy
import arcpy

os.chdir(data_processing_dir)
#arcpy.env.workspace = r'D:\Workspace\Data\HBProject\Workfiles\HBProject.gdb'  # 设置本代码的工作文件
arcpy.CheckOutExtension('Spatial')
arcpy.CheckOutExtension("ImageAnalyst")  # 检查许可
arcpy.env.outputCoordinateSystem = arcpy.SpatialReference("WGS 1984 UTM Zone 49N")
arcpy.env.overwriteOutput = True
#arcpy.env.extent = "MAXOF"

ras_fvc_2000 = arcpy.Raster(file_fvc_2000)
ras_fvc_2020 = arcpy.Raster(file_fvc_2020)
ras_landuse_2000 = arcpy.Raster(file_landuse_2000)
ras_landuse_2020 = arcpy.Raster(file_landuse_2020)

transmat_landuse = ras_landuse_2000 * 10 + ras_landuse_2020

ras_fvc_diff = ras_fvc_2020 - ras_fvc_2000

# 提取 FVC 变化正值像素
ras_pos_diff = arcpy.ia.Con(ras_fvc_diff,1,0,"VALUE > 0")
#posFVCRate.save(posFVCrate_file)
#print(posFVCrate_file + ' saved.')

# 提取 FVC 变化率负值像素
ras_neg_diff = arcpy.ia.Con(ras_fvc_diff,1,0,"VALUE < 0")

#negFVCRate = arcpy.ia.Con(FVCRate,1,0, "VALUE <= 0")
#negFVCRate.save(negFVCrate_file)
#print(negFVCrate_file + ' saved.')



