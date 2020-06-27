import cv2
import numpy as np
import imutils
import winsound
import time

x, y, h, w = (207, 127, 246, 246)

def lenI(liste):
     ret = 0
     try:
          len(liste[0])
     except:
          return len(liste)
     finally:
          for i in range(0,len(liste)):
               ret += len(liste[i])
          return ret

def xybul(a):
     if(a == 1 or a == 2 or a == 3):
          return [int(x+h/3*(a-1)),int(y),int(x+h/3*a),int(y+h/3)]
     elif(a == 4 or a == 5 or a == 6):
          return [int(x+h/3*(a-4)),int(y+h/3),int(x+h/3*(a-3)),int(y+h/3*2)]
     elif(a == 7 or a == 8 or a == 9):
          return [int(x+h/3*(a-7)),int(y+h/3*2),int(x+h/3*(a-6)),int(y+h)]

def cube_control(cube_list):
     for a in range(0,len(cube_list)):
          for i in range(0,len(cube_list)):
               if(cube_list[a][i] != '?'):
                    return True
               else:
                    return False
               
cube_state = None

def cube_scan(lower_color,upper_color,color,boxFrame,cube_state):
     global nFrame
     mask = cv2.inRange(hsv,lower_color,upper_color)

     cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
     cnts = imutils.grab_contours(cnts)

     for c in cnts:
          area = cv2.contourArea(c)
          if area > 5000:
               cv2.drawContours(boxFrame,[c],-1,(0,255,0), 3)

               M = cv2.moments(c)
               cx = int(M["m10"]/ M["m00"])
               cy = int(M["m01"]/ M["m00"])
               
               if(35 <= cy <= 45): #Üst Satır
                    if(35 <= cx <= 45):
                         cube_state[0][0] = str(color[0])
                    if(65 <= cx <= 75):
                         cube_state[0][1] = str(color[0])
                    if(100 <= cx <= 110):
                         cube_state[0][2] = str(color[0])

               elif(65 <= cy <= 75): #Orta Satır
                    if(35 <= cx <= 45):
                         cube_state[1][0] = str(color[0])
                    if(65 <= cx <= 75):
                         cube_state[1][1] = str(color[0])
                    if(100 <= cx <= 110):
                         cube_state[1][2] = str(color[0])          

               elif(100 <= cy <= 110): #Alt Satır
                    if(35 <= cx <= 45):
                         cube_state[2][0] = str(color[0])
                    if(65 <= cx <= 75):
                         cube_state[2][1] = str(color[0])
                    if(100 <= cx <= 110):
                         cube_state[2][2] = str(color[0])         
               
               
               cv2.circle(boxFrame,(cx,cy),7,(255,255,255),-1)
               #cv2.putText(boxFrame, color, (cx-20, cy-20), cv2.FONT_HERSHEY_COMPLEX,2.5,(255,255,255), 3)

def getColor(char):
    m = {'r': (255,0,0), 'o':(255,128,0), 'b':(0,0,255),
         'g':(0,255,0), 'w':(255,255,255), 'y':(255,255,0),
         '?':(128,128,128)}
    return tuple(list(m[char.lower()])[::-1])

def draw_cube(cube_state):
    global nFrame
    for i in range(3):
        for j in range(3):
            if cube_state != None:
                cv2.rectangle(nFrame, (10+40*j, 10+40*i),
                                   (40+40*j, 40+40*i), getColor(cube_state[i][j]), 3)
                cv2.putText(nFrame, cube_state[i][j], (17+40*j, 32+40*i),
                                 cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                 getColor(cube_state[i][j]), 1)
            else:
                cv2.rectangle(nFrame, (10+40*j, 10+40*i),
                                   (40+40*j, 40+40*i), (128,128,128), 3)
                cv2.putText(nFrame, '?', (17+40*j, 32+40*i),
                                 cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                                 (128,128,128), 1)


cap= cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)



while True:
     _,frame= cap.read()
     nFrame = frame
     
     frameList = []
     #üst sol frame
     frame1 = frame[y:220,x:350]
     #üst orta frame
     frame2 = frame[y:220,x+50:400]
     #üst sağ frame
     frame3 = frame[y:220,x+100:450]
     #orta sol frame
     frame4 = frame[y+50:300,x:300]
     #orta orta frame
     frame5 = frame[y+50:300,x+50:400]
     #orta sağ frame
     frame6 = frame[y+50:300,x+100:450]
     #alt sol frame
     frame7 = frame[y+100:400,x:300]
     #alt orta frame
     frame8 = frame[y+100:400,x+50:400]
     #alt sağ frame
     frame9 = frame[y+100:400,x+100:450]
     
     for i in range(1,10):
          exec("frameList.append(frame" + str(i) + ")")

     
     #Ana Kare
     #cv2.rectangle(nFrame, (x, y), (x + w, y + h), (0, 0 , 255), 4)

     for i in range(1,10):
         cv2.rectangle(nFrame, (xybul(i)[0], xybul(i)[1]), (xybul(i)[2],xybul(i)[3]), (0,0 , 255), 3)
         

     #Renk Paleti
     
          #Sarı
     lower_yellow = np.array([25,50,50],dtype=np.uint8)
     upper_yellow = np.array([32,255,255],dtype=np.uint8)
          #Yeşil
     lower_green = np.array([40,40,40],dtype=np.uint8)
     upper_green = np.array([70,255,255],dtype=np.uint8)

          #Kırmızı
     lower_red = np.array([170,120,70],dtype=np.uint8)
     upper_red = np.array([180,255,255],dtype=np.uint8)
          #Mavi
     lower_blue = np.array([94, 80, 2],dtype=np.uint8) 
     upper_blue = np.array([121,255,255],dtype=np.uint8)
          #Turuncu
     lower_orange = np.array([5,50,50],dtype=np.uint8)
     upper_orange = np.array([15, 255, 255],dtype=np.uint8)

     lower_white = np.array([0,0,0],dtype=np.uint8)
     upper_white = np.array([0,0,255],dtype=np.uint8)
     
     im = np.zeros((640,480,3), dtype=np.uint8)
     cube_state = [['?','?','?'],['?','?','?'],['?','?','?']]
     
     #cube_state = [[None,None,None],[None,None,None],[None,None,None]]
     for i in range(1,10):
          hsv = cv2.cvtColor(frameList[i-1], cv2.COLOR_BGR2HSV)
          cube_scan(lower_yellow,upper_yellow,"Yellow",frameList[i-1],cube_state)
          cube_scan(lower_green,upper_green,"Green",frameList[i-1],cube_state)
          cube_scan(lower_red,upper_red,"Red",frameList[i-1],cube_state)
          cube_scan(lower_blue,upper_blue,"Blue",frameList[i-1],cube_state)
          cube_scan(lower_orange,upper_orange,"Orange",frameList[i-1],cube_state)
          cube_scan(lower_white,upper_white,"White",frameList[i-1],cube_state)

     if(lenI(cube_state) == 9):
          draw_cube(cube_state)
     if(cube_control(cube_state)):
          print(cube_state)


     cv2.imshow("Cube Scan",nFrame)
     k = cv2.waitKey(5)
     if k == 27:
         break

cap.release()
cv2.destroyAllWindows()

