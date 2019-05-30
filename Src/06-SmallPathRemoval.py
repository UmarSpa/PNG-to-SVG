import os
import tools as myTools
from svg.path import parse_path
from xml.dom import minidom
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', type=str, default='./input', help='Input directory.')
parser.add_argument('--outDir', type=str, default='./output/', help='Output directory.')
parser.add_argument('--minLen', type=int, default=10, help='Output directory.')
args = parser.parse_args()

if not os.path.exists(args.outDir):
    os.makedirs(args.outDir)

dataList = myTools.folder2files(args.inDir, format='.svg')

for svgFileName in dataList:

    svgFile = minidom.parse(svgFileName)
    pathList = svgFile.getElementsByTagName("path")

    parent = pathList[0].parentNode

    for pathIdx, pathEle in enumerate(pathList):
        mypath  = parse_path(pathEle.attributes["d"].value)
        if mypath.length() < args.minLen:
            parent.removeChild(pathEle)

    with open(args.outDir + '/' + svgFileName.split('/')[-1], "w") as f:
        f.write(svgFile.toxml())
