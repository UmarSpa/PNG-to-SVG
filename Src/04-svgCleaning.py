import os
import tools as myTools
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', type=str, default='./temp/03/', help='Input directory.')
parser.add_argument('--outDir', type=str, default='./temp/04/', help='Output directory.')
args = parser.parse_args()

if not os.path.exists(args.outDir):
    os.makedirs(args.outDir)

dataList = myTools.folder2files(args.inDir, format='.svg')
myTools.removeAStyle(dataList, args.outDir, attrRem="style", valRem="stroke:#01017f; fill:none;")
