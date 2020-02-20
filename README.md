# Camera Claibration opencv 
This script uses 9*6 checkerboard to generate calibration data and saves it using pickle so that it can be used to calibrate the camera. It also displays your calibrated images at the end
This script uses live feed to detect corners.

 <ul>
  <li>Change value of "checkorBoardSize" to your checkerboard size</li>
  <li>Change value of "dump_loc" to change the location where you save your calibration data</li>
  <li>To change the number of images used to complete calibration change "calibrationImagesNo"</li>
  <li>It is recommended that you use more than 50 images for calibration</li>
  <li>Linux users need to make a small change in the beggining of the code please chk the comments</li>
 
</ul> 

Please use idle to run this code it might not run using direct cmd prompt

## How to use
<ul>
  <li>Run script select correct option
  <li>The camera should start and display the image in a window
  <li>Stand infront of the camera with checkerboard
  <li>If the board is detected frame will freeze for a few seconds and will play a sound
  <li>Do this on all sides of the frame
  <li>Repeat the no of times that you selected
  <li>When the calibration is done a new window will appear with the corrected frame
  <li>The parameters will be saved using pickle on the desktop or the place where you selected
 </ul>
 
 Requirments:
<ul>
  <li>Python-OpenCV(I tested it on CV2 version 3.4.x i havent tested it with cv2 version 4.0.x)
  <li>Numpy
  <li>Pickle
</ul>

Note: pip installations should work here no need to compile from source
Note:If you arent getting good results then play with the flags in:

[ln 135] ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None,flags=cv2.CALIB_USE_EXTRINSIC_GUESS+cv2.CALIB_FIX_K3)

depending upon the type of error you may need to use a different combination

