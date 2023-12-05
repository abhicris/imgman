# Image solid color checker by Clement
# optimizations by Nathan 'jesterKing' Letwory
# experimented on by Jarek
from PIL import Image
import System
import os
import time
from System.Threading import Tasks as task


def IsImageAllSameColor(image_path, color):
    """Read image from path, then test each pixel against the 
    passed in color. Color is a list of color components
    with order [r, g, b, a]
    """

    if not os.path.exists(image_path): return
    
    # unpack the color, since we don't want to waste time on
    # lookups
    r, g, b, a = color
    
    # set up bitmap reading into array
    bmp = System.Drawing.Bitmap.FromFile(image_path)
    form = System.Drawing.Imaging.PixelFormat.Format32bppArgb
    mode = System.Drawing.Imaging.ImageLockMode.ReadOnly
    area = System.Drawing.Rectangle(0, 0, bmp.Width, bmp.Height)
    
    #number of bytes to skip in testing based on image dimensions
    skipstep= int((bmp.Width+bmp.Height)/1000)*2
    if skipstep == 0: skipstep=1
    print("Testing every" + str(skipstep) + " pixel")
    
    # and lock the data for specific format so we can copy for consumption
    data = bmp.LockBits(area, mode, form)
    
    # copy the image data to rgb_values array, so we can throw the bitmap away
    byte_count = (data.Stride) * data.Height
    rgb_values = System.Array.CreateInstance(System.Byte, byte_count)
    System.Runtime.InteropServices.Marshal.Copy(data.Scan0, rgb_values, 0, byte_count)
    # done with original bmp, unlock and release file handle
    bmp.UnlockBits(data)
    bmp.Dispose()
    
    # create a single-item list, so we can actually set it
    # it appears that using just same_color = True, then set
    # it in the worker doesn't work as expected. The list works
    # since it is really a reference, not a hard-copy of the value
    same_color = [True]
    
    # our worker takes an item from the input in i, one element
    # created by the xrange. The state we use to break the loop
    # as soon as we find a dissimilar color from what we want
    def Worker(i, state, unused):
        # we now test against the r,g,b,a variables in that order. Assuming
        # that alpha channel isn't what we're looking for we can put it last
        # so that any of r,g,b short-circuit. At best the r value is different
        # resulting in skipping of tests for g,b,and a. Worst case is only alpha
        # is different.
        # Also we no longer use any data structure to compare against to get rid
        # of any lookups
        if rgb_values[i+3] != a:
            same_color[0] = False
            state.Break()
    
    # do the work
    task.Parallel.ForEach(xrange(0, byte_count, 4 * skipstep), Worker)
    
    return same_color[0]

def TestImageForFullTransparency():
    image_path = "images/Tesla/Tesla_05.png"
    test_color = [0,0,0,0] # r, g, b, a - in this case really only a=0 matters

    start = time.time()
    result = IsImageAllSameColor(image_path, test_color)
    end = time.time()
    
    return result, end-start

r = TestImageForFullTransparency()
print(r)
