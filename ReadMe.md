# Vectorization of raster images: PNG to SVG
This code converts raster images (PNG) of sketches/edge-maps into vector representation (SVG). More importantly we use the same svg format as the one used in TUBerlin (a commonly used sketch dataset), where:
- shape and geometry of each stroke is represented by a 'path'.
- each 'path' is a sequence of segments defined by moveto (starting point of the stroke), lineto (straight line segment) and curveto (cubic Bézier curve segment).
- cubic Bézier segment is defined by a start point, an end point, and two control points.

The unique advantage of vector format SVG is that it can be resized to any dimension without loosing quality or detail of the image. Moreover it also conserves the information regarding the sequential order of strokes in sketches.

## Walk-through
Platform: linux-64
```bash
cd PNG-to-SVG
conda create --name PNG2SVG python=<3.9>
conda activate PNG2SVG
pip install opencv-python scipy matplotlib
bash ./install.sh
bash ./main.sh
```

## Explanation
Input: PNG files of any dimension.

**Resizing and thresholding**  
Often the raster sketch/edge-map images are in greyscale and of various sizes.
Here these two factors are normalized by:
1) resizing the input image to 500x500.
2) rescaling the values between 0 and 1, and then thresholding at 0.5 to get the binary output image.

**PNG to PPM**  
Png images are converted to ppm. Autotrace requires this format as input.

**PPM to SVG**  
Using Autotrace the rasterized images are converted to svg.

**SVG cleaning**  
Unnecessary paths are deleted.

**One path for each stroke**  
Svg file containing one path to represent the whole sketch/edge-map is broken down into one path for each stroke.

**Small path removal**  
We recommend to use this only for edge-maps. It removes unwanted grains (/very small sized segments) in the edge-maps.

**Longest path first**  
The longest stroke (/path) is moved at the first place in the sequential order in which strokes (/paths) are saved.

**Reorder path sequence**  
Starting from the first stroke, we compute the distance between its end point and the start points of all the other strokes. The stroke with the nearest start point is appended next in the ordered sequence of paths. In this way the jumps in between the two consecutive strokes are kept to minimum.

**SVG cleaning**  
Vacant spaces are removed, and one path is put in each line.

**TUBerlin format conversion**  
The format is changed to TUBerlin svg format:
- 'style' attribute is removed from the paths.
- sketch is scaled to 800x800, along with the addition of other attributes in the header, including 'preserveAspectRatio', 'viewBox', 'stroke', 'stroke-width' and 'transform'.

**SVG to PNG**  
SVG output is also converted to 256x256 PNG format.

Output: SVG (800x800) and PNG (256x256) format

N.B. All the intermediate files are deleted at the end of processing. If you wish to conserve these files just comment the last line (#rm -rf "./Src/temp") in main.sh file.
