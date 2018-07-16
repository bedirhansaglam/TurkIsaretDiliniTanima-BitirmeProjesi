# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 10:54:10 2017

@author: Bedirhan
"""

import Leap,sys,thread,time
import time
from sklearn.externals import joblib
import numpy as np

import cv2, Leap, math, ctypes

def convert_distortion_maps(image):

    distortion_length = image.distortion_width * image.distortion_height
    xmap = np.zeros(distortion_length/2, dtype=np.float32)
    ymap = np.zeros(distortion_length/2, dtype=np.float32)

    for i in range(0, distortion_length, 2):
        xmap[distortion_length/2 - i/2 - 1] = image.distortion[i] * image.width
        ymap[distortion_length/2 - i/2 - 1] = image.distortion[i + 1] * image.height

    xmap = np.reshape(xmap, (image.distortion_height, image.distortion_width/2))
    ymap = np.reshape(ymap, (image.distortion_height, image.distortion_width/2))

    #resize the distortion map to equal desired destination image size
    resized_xmap = cv2.resize(xmap,
                              (image.width, image.height),
                              0, 0,
                              cv2.INTER_LINEAR)
    resized_ymap = cv2.resize(ymap,
                              (image.width, image.height),
                              0, 0,
                              cv2.INTER_LINEAR)

    #Use faster fixed point maps
    coordinate_map, interpolation_coefficients = cv2.convertMaps(resized_xmap,
                                                                 resized_ymap,
                                                                 cv2.CV_32FC1,
                                                                 nninterpolation = False)

    return coordinate_map, interpolation_coefficients

def undistort(image, coordinate_map, coefficient_map, width, height):
    destination = np.empty((width, height), dtype = np.ubyte)

    #wrap image data in numpy array
    i_address = int(image.data_pointer)
    ctype_array_def = ctypes.c_ubyte * image.height * image.width
    # as ctypes array
    as_ctype_array = ctype_array_def.from_address(i_address)
    # as numpy array
    as_numpy_array = np.ctypeslib.as_array(as_ctype_array)
    img = np.reshape(as_numpy_array, (image.height, image.width))

    #remap image to destination
    destination = cv2.remap(img,
                            coordinate_map,
                            coefficient_map,
                            interpolation = cv2.INTER_LINEAR)

    #resize output to desired destination size
    destination = cv2.resize(destination,
                             (width, height),
                             0, 0,
                             cv2.INTER_LINEAR)
    return destination

def run(controller):
    maps_initialized = False
    while(True):
        frame = controller.frame()
        image = frame.images[0]
        if image.is_valid:
            if not maps_initialized:
                left_coordinates, left_coefficients = convert_distortion_maps(frame.images[0])
                right_coordinates, right_coefficients = convert_distortion_maps(frame.images[1])
                maps_initialized = True

            undistorted_left = undistort(image, left_coordinates, left_coefficients, 400, 400)
            undistorted_right = undistort(image, right_coordinates, right_coefficients, 400, 400)

            #display images
            cv2.imshow('Left Camera', undistorted_left)
            cv2.imshow('Right Camera', undistorted_right)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

class LeapMotionListener(Leap.Listener):
    finger_names=['Thumbs','Index','Middle','Ring','Pinky']
    bone_names=['Metacarpal','Proximal','Intermediate','Distal']
    state_names=['STATE_INVALID','STATE_START','STATE_UPDATE','STATE_END']
    
    def on_init(self,controller):
        print "Yuklendi"
    
    
    def on_connect(self,controller):
        print "Leap Motion Baglandi"
        self.clf=joblib.load('./models/RandomForestModel.pkl')
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_disconnect(self,controller):
        print "Leap Motion baglantisi kesildi"
    
    
    def on_frame(self,controller):
        frame=controller.frame()
        data=[]
        for i in range (0,390):
            data.append(0)
        
        now_data=[]


        for i,hand in enumerate(frame.hands):
            handTypedata=0 if hand.is_left else 1
            normal= hand.palm_normal
            direction=hand.direction
            arm=hand.arm
            
            now_data=str(hand.palm_position.x),str(hand.palm_position.y) , str(hand.palm_position.z),\
            str(direction.pitch* Leap.RAD_TO_DEG),str(normal.roll*Leap.RAD_TO_DEG),str(direction.yaw*Leap.RAD_TO_DEG) , \
            str(arm.direction.x),str(arm.direction.y),str(arm.direction.z) ,\
            str(arm.wrist_position.x),str(arm.wrist_position.y),str(arm.wrist_position.z), \
            str(arm.elbow_position.x),str(arm.elbow_position.y),str(arm.elbow_position.z), 

            for finger in hand.fingers:
                for b in range(0,4):
                    bone=finger.bone(b)
                    now_data+=str(bone.prev_joint.x),str(bone.prev_joint.y),str(bone.prev_joint.z), \
                    str(bone.next_joint.x) , str(bone.next_joint.y), str(bone.next_joint.z) , \
                    str(bone.direction.x) , str(bone.direction.y) , str(bone.direction.z),
            
            
            if(handTypedata==0 and i==0):#"1.el ve sol"  b
                for x in range(0,195):
                    data[x]=now_data[x]
                for y in range (195,390):
                    data[y]=0
                         
            elif (handTypedata==1 and i==0): #1.el ve sag  a
                for x in range(0,195):
                    data[x]=0
                for y in range (195,390):
                    data[y]=now_data[y-195]
                    
            elif (handTypedata==0 and i==1): # 2.el ve sol ccc
                for x in range(0,195):
                    data[x]=now_data[x]
                    
            elif (handTypedata==1 and i==1): #2.el ve sag ccc
                for y in range (195,390):
                    data[y]=now_data[y-195]


        if data[389]==0 and data[0]==0:
            pass
        else:
            data=np.array(data).reshape(-1,1).T
            result=self.clf.predict(data)
            lbl_text=""
            if result==1:
                lbl_text+="A"
            elif result==2:
                lbl_text+="B"
            elif result==3:
                lbl_text+="C"
            elif result==4:
                lbl_text+="Ç"
            elif result==5:
                lbl_text+="D"
            elif result==6:
                lbl_text+="E"
            elif result==7:
                lbl_text+="F"
            elif result==8:
                lbl_text+="G"
            elif result==9:
                lbl_text+="Ğ"
            elif result==10:
                lbl_text+="H"
            elif result==11:
                lbl_text+="I"
            elif result==12:
                lbl_text+="İ"
            elif result==13:
                lbl_text+="J"
            elif result==14:
                lbl_text+="K"
            elif result==15:
                lbl_text+="L"
            elif result==16:
                lbl_text+="M"
            elif result==17:
                lbl_text+="N"
            elif result==18:
                lbl_text+="O"
            elif result==19:
                lbl_text+="Ö"
            elif result==20:
                lbl_text+="P"
            elif result==21:
                lbl_text+="R"
            elif result==22:
                lbl_text+="S"
            elif result==23:
                lbl_text+="Ş"
            elif result==24:
                lbl_text+="T"
            elif result==25:
                lbl_text+="U"
            elif result==26:
                lbl_text+="Ü"
            elif result==27:
                lbl_text+="V"
            elif result==28:
                lbl_text+="Y"
            elif result==29:
                lbl_text+="Z"
            print(lbl_text)
        time.sleep(1)    

    
def main():
    listener=LeapMotionListener()
    controller=Leap.Controller()
    controller.set_policy_flags(Leap.Controller.POLICY_IMAGES)
    controller.add_listener(listener)
    print "Press enter to quit"
    try:
        run(controller)
    except KeyboardInterrupt:
        sys.exit(0)
    
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)
        
    



if __name__== "__main__":
    main()