# Camera Claibration opencv 
This script uses 9*6 checkerboard to generate calibration data and saves it using pickle so that it can be used to calibrate the camera. It also displays your calibrated images at the end
This script uses live feed to detect corners.

 <ul>
  <li>Change value of "checkorBoardSize" to your checkerboard size</li>
  <li>Change calue of "dump_loc" to change the location where you save your calibration data</li>
  <li>To change the number of images used to complete calibration change "calibrationImagesNo"</li>
  <li>It is recommended that you use more than 50 images for calibration</li>
</ul> 

