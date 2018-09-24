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
