#hi my name is Abhijeet singh i made this simple curl-counter hope you will like it


import math
import cv2
import mediapipe as mp


mppose=mp.solutions.pose
pose=mppose.Pose()



mpdraw=mp.solutions.drawing_utils


up=0
down=0
count=0
cap=cv2.VideoCapture(0)


def draw(img,x,y,radius=2,color=(0,0,255),thick=(2)):

    
    ih,iw,ic=img.shape

    cx=int(x*iw)
    cy=int(y*ih)
    cv2.circle(img,(cx,cy),radius,color,thick)

    return cx,cy


while True:
    ok,frame=cap.read()
    rgb=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    result=(pose.process(rgb))
    if (result.pose_landmarks):
        x1,y1=draw(frame,(result.pose_landmarks.landmark[12].x),(result.pose_landmarks.landmark[12].y),radius=8,thick=-1)
        draw(frame,(result.pose_landmarks.landmark[12].x),(result.pose_landmarks.landmark[12].y),radius=18,color=(0,255,255))


        x2,y2=draw(frame,(result.pose_landmarks.landmark[14].x),(result.pose_landmarks.landmark[14].y),radius=8,thick=-1)
        draw(frame,(result.pose_landmarks.landmark[14].x),(result.pose_landmarks.landmark[14].y),radius=18,color=(0,255,255))

        x3,y3=draw(frame,(result.pose_landmarks.landmark[16].x),(result.pose_landmarks.landmark[16].y),radius=8,thick=-1)
        draw(frame,(result.pose_landmarks.landmark[16].x),(result.pose_landmarks.landmark[16].y),radius=18,color=(0,255,255))

        cv2.line(frame,(x1,y1),(x2,y2),(255,255,255),2)
        cv2.line(frame,(x2,y2),(x3,y3),(255,255,255),2)


        lower_arm=(math.degrees

              (math.atan2((y2-y3),(x3-x2))))
        upper_arm=(math.degrees(math.atan2((y2-y1),(x2-x1))))

        cv2.ellipse(frame,(x2,y2),(50,50),(0),(-90),(-lower_arm),(255,255,255),3)



        cv2.putText(frame,f'{upper_arm-lower_arm:.0f}',(x2+50,y2),cv2.FONT_HERSHEY_DUPLEX,1.5,(255,255,255),3)

        if (upper_arm-lower_arm)>150:
            down=down+1
        if down and (upper_arm-lower_arm)<45:
            up=up+1

        if up and down:
            count=count+1

            up=0
            down=0

        rx1=70
        ry1=90
        ry2=110
        rx2=max(int(270-((upper_arm-lower_arm))),80)
        
        cv2.rectangle(frame,(rx1,ry1),(rx2,ry2),(0,255,255),-1)
        cv2.rectangle(frame,(rx1,ry1),(rx2,ry2),(0,0,0),1)

        cv2.putText(frame,f'count:-{count}',(50,50),cv2.FONT_HERSHEY_DUPLEX,1.5,(0,0,255),3)
        cv2.putText(frame,f'strength',(50,150),cv2.FONT_HERSHEY_DUPLEX,1,(0,0,255),2)


    
    cv2.imshow("frame",frame)

    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()
