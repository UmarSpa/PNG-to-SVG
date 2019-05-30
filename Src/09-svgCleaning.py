import os
import tools as myTools
from xml.dom import minidom
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', type=str, default='./input', help='Input directory.')
parser.add_argument('--outDir', type=str, default='./output/', help='Output directory.')
args = parser.parse_args()

if not os.path.exists(args.outDir):
    os.makedirs(args.outDir)

dataList = myTools.folder2files(args.inDir, format='.svg')

for svgFileName in dataList:
    svgFile = minidom.parse(svgFileName)
    with open(args.outDir + '/' + svgFileName.split('/')[-1], "w") as f:
        dom_string = svgFile.toprettyxml(indent='\r')
        dom_string = os.linesep.join([s for s in dom_string.splitlines() if s.strip()])
        f.write(dom_string)
