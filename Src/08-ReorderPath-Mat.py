import os
import tools as myTools
from svg.path import parse_path
from xml.dom import minidom
from scipy.spatial import distance as DT
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
    pathList = svgFile.getElementsByTagName("path")
    parent = pathList[0].parentNode

    for pathIdx, pathEle in enumerate(pathList):
        parent.removeChild(pathEle)
    parent.appendChild(pathList[0])
    pathInsertedList = []
    pathInsertedList.append(0)

    for pathIdx, pathEle in enumerate(pathList[:-1]):
        pathCurves = parse_path(pathEle.attributes["d"].value)
        firstCurve = pathCurves[0]
        firstx = firstCurve.start.real
        firsty = firstCurve.start.imag

        lastCurve = pathCurves[-1]
        lastx = lastCurve.end.real
        lasty = lastCurve.end.imag

        distMin = 9999
        minNextPathId = 0

        for pathIdx2, pathEle2 in enumerate(pathList):
            pathCurves2 = parse_path(pathEle2.attributes["d"].value)
            firstCurve2 = pathCurves2[0]
            firstx2 = firstCurve2.start.real
            firsty2 = firstCurve2.start.imag

            lastCurve2 = pathCurves2[-1]
            lastx2 = lastCurve2.end.real
            lasty2 = lastCurve2.end.imag

            if (distMin > DT.euclidean((lastx,lasty),(firstx2, firsty2))) and (pathIdx2 not in pathInsertedList):
                distMin = DT.euclidean((lastx,lasty),(firstx2, firsty2))
                minNextPathId = pathIdx2

        parent.appendChild(pathList[minNextPathId])
        pathInsertedList.append(minNextPathId)

    with open(args.outDir + '/' + svgFileName.split('/')[-1], "w") as f:
        f.write(svgFile.toxml())
