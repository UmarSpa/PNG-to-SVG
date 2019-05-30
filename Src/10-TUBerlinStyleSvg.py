import os
import tools as myTools
from xml.dom import minidom
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', type=str, default='./input', help='Input directory.')
parser.add_argument('--outDir', type=str, default='./output/', help='Output directory.')
parser.add_argument('--refSVG', type=str, default='./Ref-svg.svg', help='Output directory.')
parser.add_argument('--imgSize', type=int, default=800, help='Output svg size.')
parser.add_argument('--strokeWidth', type=float, default=1.8481, help='stroke width.')
args = parser.parse_args()

if not os.path.exists(args.outDir):
    os.makedirs(args.outDir)

dataList = myTools.folder2files(args.inDir, format='.svg')

for svgFileName in dataList:

    refFile = minidom.parse(args.refSVG)
    refSvgEle = refFile.getElementsByTagName("svg")[0]
    refSvgEle.attributes['viewBox'].value = u'0 0 ' + str(args.imgSize) + ' ' + str(args.imgSize)
    refG2Ele = refSvgEle.getElementsByTagName("g")[1]
    refG2Ele.attributes['transform'].value = u'translate(0,0) scale(0.0) translate(0,0)'
    refG1Ele = refSvgEle.getElementsByTagName("g")[0]
    refG1Ele.attributes['stroke-width'].value = str(args.strokeWidth)

    refPathList = refFile.getElementsByTagName("path")
    parent = refPathList[0].parentNode
    for pathIdx, pathEle in enumerate(refPathList):
        parent.removeChild(pathEle)

    svgFile = minidom.parse(svgFileName)
    inputHeight = int(svgFile.getElementsByTagName("svg")[0].attributes['width'].value)
    refG2Ele.attributes['transform'].value = u'translate(0,0) scale(' + str("{0:.3f}".format(args.imgSize / float(inputHeight))) +') translate(0,0)'
    pathList = svgFile.getElementsByTagName("path")

    for pathIdx, pathEle in enumerate(pathList):
        pathList[pathIdx].removeAttribute("style")
        parent.appendChild(pathList[pathIdx])

    with open(args.outDir + '/' + svgFileName.split('/')[-1], "w") as f:
        dom_string = refFile.toprettyxml(indent='\r')
        dom_string = os.linesep.join([s for s in dom_string.splitlines() if s.strip()])
        f.write(dom_string)
