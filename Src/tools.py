"""
Author: Muhammad Umar Riaz
"""

import os
from xml.dom import minidom
import glob
import xml.etree.ElementTree as ET

def get_path_strings(svgfile):

  """
  This function gets the list of paths from svgFile
  It needs: import xml.etree.ElementTree as ET
  """
  tree = ET.parse(svgfile)
  p = []
  for elem in tree.iter():
    if elem.attrib.has_key('d'):
      p.append(elem.attrib['d'])
  return p

def folder2files(dataDir, format='.png'):
    """
    Function: It creates a list of all the files present in all the
              subfolders of dataDir.
    Input:
        dataDir: folder path containing the subfolders where the
                 files of interest are present.
    Output:
        dataList: list of files in the subfolders of dataDir.
    N.B.: It needs import os.
    """
    dataList = []
    for dirName, subdirList, fileList in os.walk(dataDir):
      dataList = dataList + sorted(glob.glob(dirName + '/*' + format))
    return dataList

def removeAStyle(svgFiles, desDir, attrRem, valRem):
    """
    it removes all the paths containg the attribute (attrRem) with value (valRem)
    """
    for svgFileName in svgFiles:
        svgFile = minidom.parse(svgFileName)
        pathList = svgFile.getElementsByTagName("path")

        for pathIdx, pathEle in enumerate(pathList):
            if pathEle.attributes[attrRem].value == valRem:
                parent = pathEle.parentNode
                parent.removeChild(pathEle)

        with open(desDir + '/' + svgFileName.split('/')[-1], "w") as f:
            f.write(svgFile.toxml())

def svg1M1Path(svgFiles, desDir):
    """
    creates one path for each M.
    """
    for svgFileName in svgFiles:
        svgFile = minidom.parse(svgFileName)
        pathList = svgFile.getElementsByTagName("path")

        for pathIdx, pathEle in enumerate(pathList):

            if len(pathEle.attributes["d"].value.split("M")) > 2:
                pathStyle = pathEle.attributes["style"].value

                parent = pathEle.parentNode
                parent.removeChild(pathEle)

                for pathVal in pathEle.attributes["d"].value.split("M")[1:]:
                    newPath = svgFile.createElement("path")
                    newPath.setAttribute("d",u"M"+str(pathVal))
                    newPath.setAttribute("style", pathStyle)
                    parent.appendChild(newPath)

        with open(desDir + '/' + svgFileName.split('/')[-1], "w") as f:
            f.write(svgFile.toxml())