import os
import tools as myTools
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', type=str, default='./input', help='Input directory.')
parser.add_argument('--outDir', type=str, default='./output/', help='Output directory.')
args = parser.parse_args()

if not os.path.exists(args.outDir):
    os.makedirs(args.outDir)

dataList = myTools.folder2files(args.inDir, format='.svg')
myTools.svg1M1Path(dataList, args.outDir)
