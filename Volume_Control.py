import cv2
import mediapipe as mp
import math
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands = 1,static_image_mode = False, min_detection_confidence = 0.4, min_tracking_confidence = 0.5)


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)


volume = interface.QueryInterface(IAudioEndpointVolume)

vol_range=volume.GetVolumeRange()

print(vol_range)

min_vol = vol_range[0]
max_vol = vol_range[1]

smoothed_vol = min_vol


cap = cv2.VideoCapture(0)
vol=0
vol_bar = 400
vol_per = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break
    else:
        frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)
        
        if results.multi_hand_landmarks:
            for handlmn in results.multi_hand_landmarks:
                
                thumb_tip = handlmn.landmark[4]
                index_tip = handlmn.landmark[8]
                
                h,w,c = frame.shape
                
                thumb_pos = int(thumb_tip.x *w),int(thumb_tip.y*h)
                index_pos = int(index_tip.x*w), int(index_tip.y*h)
                
                middle_pos = int(thumb_pos[0]+index_pos[0])//2,int(thumb_pos[1]+index_pos[1])//2
                
                cv2.circle(frame,thumb_pos,9,(0,255,255),cv2.FILLED)
                cv2.circle(frame,index_pos,9,(0,255,255),cv2.FILLED)
                cv2.line(frame, thumb_pos,index_pos,(127,0,255),4)
                cv2.circle(frame,middle_pos,8,(51,255,51),cv2.FILLED)
                
                distance = math.hypot(thumb_pos[0]-index_pos[0],thumb_pos[1]-index_pos[1])

                if distance<16:
                    cv2.circle(frame,middle_pos,8,(51,51,255),cv2.FILLED)
                
                
                vol = np.interp(distance,[17,137],[min_vol,max_vol])
                vol_bar = np.interp(distance,[17,137],[400,60])
                vol_per = np.interp(distance,[17,137],[0,100])
                
                smoothed_vol = int(0.8 * smoothed_vol + 0.2 * vol)
                
                volume.SetMasterVolumeLevel(smoothed_vol, None)
                
                
        cv2.rectangle(frame,(20,60),(60,400),(0,255,0),2)        
        cv2.rectangle(frame,(20,int(vol_bar)),(60,400),(0,255,0),-1)        
        cv2.putText(frame,f'{int(vol_per)}%',(20,50),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,0),1)       
        cv2.imshow("Volume Control",frame)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()