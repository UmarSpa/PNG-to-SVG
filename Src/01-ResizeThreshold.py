import os
import tools as myTools
import cv2
import matplotlib.pylab as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--inDir', type=str, default='../Input', help='Input directory.')
parser.add_argument('--outDir', type=str, default='./temp/01', help='Output directory.')
parser.add_argument('--ResizeFlag', type=bool, default=True, help='Output directory.')
parser.add_argument('--ResizeH', type=int, default=300, help='Height.')
parser.add_argument('--ResizeW', type=int, default=300, help='Width.')
args = parser.parse_args()

if not os.path.exists(args.outDir):
    os.makedirs(args.outDir)

dataList = myTools.folder2files(args.inDir, format='.png')

for imgFile in dataList:
    img = cv2.imread(imgFile)
    img = (img-img.min())/(img.max()-img.min())
    if args.ResizeFlag == True:
        img = cv2.resize(img,(args.ResizeH,args.ResizeW), interpolation=cv2.INTER_LINEAR)
    img = img > 0.5
    plt.imsave(args.outDir + '/' + imgFile.split('/')[-1].split('.')[0] + ".png", img.astype("float32"))