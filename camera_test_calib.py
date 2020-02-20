#from __future__ import print_function
import numpy as np
import cv2
#import glob
import os
import os.path
import pickle
import winsound

calibrationImagesNo=30
CalibrationSquareDim = 0.036 #meters
checkorBoardSize=(9,6)
duration = 1000  # millisecond
freq = 1000
CROP_WIDTH = 960

#linux users please comment this out and give a defined dump_loc
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
dump_loc=(desktop+"\objp.txt")

#camera stuff
cam = cv2.  VideoCapture(0)
#cam.set(cv2.CAP_PROP_FPS, 120)

#cam.set(cv2.CAP_PROP_FRAME_WIDTH, (640*2))
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
s,orignal = cam.read()
height, width, channels = orignal.shape
print(width)
print(height)

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((checkorBoardSize[1]*checkorBoardSize[0],3), np.float32)
objp[:,:2] = np.mgrid[0:checkorBoardSize[0],0:checkorBoardSize[1]].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

while(1):
    x=0
    print("Do you want to calibrate?")
    print(dump_loc)
    chk_cond=input("If no please check file path given above(y/n)")

    if((chk_cond=="y" )or (chk_cond=="Y")):
        x=0
        break

    elif((chk_cond=="n") or (chk_cond=="N")):
        if(os.path.exists(dump_loc)):
            x=100

            s,orignal = cam.read()

            ##cropping
            img=orignal

            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

            with open((desktop+"\objp.txt"), "rb") as fp:   # Unpickling
                objpoints = pickle.load(fp)
                imgpoints = pickle.load(fp)

            break
        else:
            print("File not found at: "+dump_loc)


    else:
        print("Input Not recognised try again")



#cv2.namedWindow("Pre_show",cv2.WINDOW_NORMAL)
#cv2.namedWindow("img", cv2.WINDOW_NORMAL)
#cv2.resizeWindow('Pre_show', 640,600)
#cv2.resizeWindow('img', 640,600)

while(x<calibrationImagesNo):

    s,orignal = cam.read()

    ##cropping
    img=orignal

    cv2.imshow('Pre_show',img)


    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray,checkorBoardSize,corners=None,flags=cv2.CALIB_CB_ADAPTIVE_THRESH+cv2.CALIB_CB_NORMALIZE_IMAGE)


# If found, add object points, image points (after refining them)
    if ret == True:
        winsound.Beep(freq, duration)
        x=x+1
        print("Matched "+str(x))
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, checkorBoardSize, corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(1000)


        print("Restarting")
        if(x>=calibrationImagesNo):
            chk_cond=input("Do you want to save the calibration data(y/n)")

            if((chk_cond=="y" )or (chk_cond=="Y")):
                print("Dumping data to" + dump_loc)
                with open(dump_loc, "wb") as fp:   #Pickling
                   pickle.dump(objpoints, fp)
                   pickle.dump(imgpoints,fp)




    if cv2.waitKey(1) & 0xFF == ord('w'):
        cv2.destroyAllWindows()
        print("Calibration Cancled")
        exit()
        break
print("Calibrating")

ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)#,flags=cv2.CALIB_USE_EXTRINSIC_GUESS+cv2.CALIB_FIX_K3)
h,  w = img.shape[:2]
newcameramtx, roi=cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))

while(1):
    s,orignal = cam.read()
    #img=orignal[0:height,0:int(width/2)]
    img=orignal
    #img=cropHorizontal(img)

    # undistort
    dst = cv2.undistort(img, mtx, dist, None, newcameramtx)

    # crop the image
    x,y,w,h = roi
    dst = dst[y:y+h, x:x+w]
    cv2.imshow('calibresult',dst)
    cv2.imshow('orignal',img)

    if cv2.waitKey(1) & 0xFF == ord('w'):
        cv2.imwrite('calibresult.png',dst)
        cv2.imwrite('orignal.png',img)
        cv2.destroyAllWindows()

        break
mean_error = 0
print(roi)
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    mean_error += error

print ("total error: ", mean_error/len(objpoints))
