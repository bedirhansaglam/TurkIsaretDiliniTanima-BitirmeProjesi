# -*- coding: utf-8 -*-
"""
Created on Mon Dec 04 10:54:10 2017

@author: Bedirhan
"""

import Leap,sys,thread,time
from Leap import CircleGesture,KeyTapGesture,ScreenTapGesture,SwipeGesture
import time
import DataBase
from DataBase import connect
from DataBase import addTable

class LeapMotionListener(Leap.Listener):
    finger_names=['Thumbs','Index','Middle','Ring','Pinky']
    bone_names=['Metacarpal','Proximal','Intermediate','Distal']
    state_names=['STATE_INVALID','STATE_START','STATE_UPDATE','STATE_END']
    
    def on_init(self,controller):
        print "Yuklendi"
    
    
    def on_connect(self,controller):
        self.i=0
        print "Leap Motion Baglandi"
        self.cnx=connect("root","","127.0.0.1","leap_data_new")
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);
        
    def on_disconnect(self,controller):
        print "Leap Motion baglantisi kesildi"
    
    
    def on_frame(self,controller):
        self.i+=1
        frame=controller.frame()
        cursor=self.cnx.cursor()
        data=[]
        for i in range (0,391):
            data.append(0)
        etiket=1
        
        now_data=[]


        for i,hand in enumerate(frame.hands):
            handTypedata=0 if hand.is_left else 1
            normal= hand.palm_normal
            direction=hand.direction
            arm=hand.arm
            
            now_data=str(hand.palm_position.x),str(hand.palm_position.y) ,\
            str(hand.palm_position.z),str(direction.pitch* Leap.RAD_TO_DEG),\
            str(normal.roll*Leap.RAD_TO_DEG),str(direction.yaw*Leap.RAD_TO_DEG) , \
            str(arm.direction.x),str(arm.direction.y),str(arm.direction.z) ,\
            str(arm.wrist_position.x),\
            str(arm.wrist_position.y),str(arm.wrist_position.z), \
            str(arm.elbow_position.x),str(arm.elbow_position.y),\
            str(arm.elbow_position.z), 

            for finger in hand.fingers:
                for b in range(0,4):
                    bone=finger.bone(b)
                    now_data+=str(bone.prev_joint.x),str(bone.prev_joint.y),\
                    str(bone.prev_joint.z), \
                    str(bone.next_joint.x) , str(bone.next_joint.y), \
                    str(bone.next_joint.z) , \
                    str(bone.direction.x) , str(bone.direction.y) , \
                    str(bone.direction.z),
            
            
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

        data[390]=etiket
        
        if data[389]==0 and data[0]==0: #el verisi yoksa kayıt etme
            pass
        else:
            if self.i<11:
                print (str(data))
                addTable(cursor,data)
#        time.sleep(0.5)    
        
        
            


#def datadoldur(self):
    
def main():
    
    listener=LeapMotionListener()
    controller=Leap.Controller()
    
    controller.add_listener(listener)
    
    print "Press enter to quit"
    
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__== "__main__":
    main()