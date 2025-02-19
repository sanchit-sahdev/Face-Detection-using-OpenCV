import numpy as np
import cv2
import sys
import pickle

#-------------------------------------------------------------------------------------------------------

def page():

    
    cv2.destroyAllWindows()

    print ("     Computer Graphics and Image Processing Project     ")
    print ("\n")
    print ("        ********** Face Detection **********            ")
    print ("\n")
    print ("                            Made By:                    ")
    print ("                                    Sanchit Sahdev      ")
    print ("\n")
    print ("        **********    MAIN MENU   ***********           ")
    print ("\n")
    print ("Available Options:")
    print ("*** 1. Use webcam to detect face")
    print ("*** 2. Upload your own image")
    print ("*** 3. Exit Program")

    ch=input("Please enter your choice:")

    if ch=="1":
        WebVid()
    elif ch=="2":
        Upld()
    elif ch=="3":
        newch="no"
        newch=input("Are you sure you want to exit? (yes/no)")
        if newch=="yes":
            Bye()
        else:
            page()

#----------------------------------------------------------------------------------------------------------

def WebVid():
    print ("Searching for image...")

    face_cascade=cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    labels={"name": 1}
    with open("labels.pickle", 'rb') as f:
        firstlabels=pickle.load(f)
        labels={v:k for k,v in firstlabels.items()}

    cap=cv2.VideoCapture(0)

    while (True):
        
        ret, frame=cap.read()
    
        grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        faces=face_cascade.detectMultiScale(grey, scaleFactor=1.5, minNeighbors=5)
    
    
        for (x,y,w,h) in faces:

            #while True:
            NUMPY_img=np.array(grey, "uint8")
            print (NUMPY_img) #coordinates of the face

            color=(255, 0, 0)
            stroke=2
            width=x+w
            height=y+h

            roi_gray=grey[y:y+h, x:x+w]
            roi_color=frame[y:y+h, x:x+w]

            id_, conf=recognizer.predict(roi_gray)
            if conf>=45 and conf<=85:
                print(id_)
                print(labels[id_])
                font=cv2.FONT_HERSHEY_DUPLEX
                name=labels[id_]
                color=(0,0,255)
                stroke=2
                cv2.putText(frame, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)


            r=width//2
            cv2.rectangle(frame , (x, y), (width, height), color, stroke)

            if cv2.waitKey(1) & 0xFF==ord("a"):
                cv2.rectangle(frame , (x, y), (width, height), color, stroke)
                ch=input("Do you want to save this face?")
                if ch=="yes":
                    roi_color=frame[y:y+h, x:x+w]
                    img_item="DetectedFace.png"
                    cv2.imwrite(img_item, roi_color)

                    ch=input("Press M to go back to the Main Menu or press any other key to exit the program")
                    if ch=="m" or ch=="M":
                        page()
                        cap.release()
                        cv2.destroyAllWindows()
                    else:
                        cap.release()
                        cv2.destroyAllWindows()
                        sys.exit()
    
    
                        

        cv2.imshow("frame", frame)

        if cv2.waitKey(20) & 0xFF==ord("q"):
            print ("********** PAUSED **********")
            ch=input("Press M to go back to the Main Menu or press any other key to exit the program")
            if ch=="m" or ch=="M":
                page()
                cap.release()
                cv2.destroyAllWindows()
            else:
                cap.release()
                cv2.destroyAllWindows()
                sys.exit()
                Bye()
    
    cap.release()
    cv2.destroyAllWindows()

#--------------------------------------------------------------------------------------------------------------
    
def Upld():

    face_cascade=cv2.CascadeClassifier("cascades/data/haarcascade_frontalface_alt2.xml")

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("trainer.yml")

    labels={"name": 1}
    with open("labels.pickle", 'rb') as f:
        firstlabels=pickle.load(f)
        labels={v:k for k,v in firstlabels.items()}


    n=int(input("Enter the number of images you want to check:"))

    for i in range (0, n):

        path=input("Enter the location of the image:")

        img=cv2.imread(path)

        cv2.imshow("image", img)

        
        grey=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces=face_cascade.detectMultiScale(grey, scaleFactor=1.5, minNeighbors=5, minSize=(30, 30))

        for (x,y,w,h) in faces:
            rt=[x,y,w,h]

            print (rt)          
            color=(255, 0, 0)
            stroke=2
            width=x+w
            height=y+h

            roi_gray=grey[y:y+h, x:x+w]
            roi_color=img[y:y+h, x:x+w]

            id_, conf=recognizer.predict(roi_gray)
            if conf>=45 and conf<=85:
                print(id_)
                print(labels[id_])
                font=cv2.FONT_HERSHEY_DUPLEX
                name=labels[id_]
                color=(0,0,255)
                stroke=2
                cv2.putText(img, name, (x,y), font, 1, color, stroke, cv2.LINE_AA)

            cv2.rectangle(img , (x, y), (width, height), color, stroke)

            cv2.imshow("image", img)

            cv2.waitKey(0)

        print ("********** Faces have been found **********")

    
        z1=input("Press any key to check the next image:")
        
        
    print ("********** ALL DONE **********")

    ch=input("Press M to go back to the Main Menu or press any other key to exit the program")

    if ch=="m" or ch=="M":
        page()
        cv2.destroyAllWindows()
    else:

        cv2.destroyAllWindows()
        sys.exit()

#---------------------------------------------------------------------------------------------------------------------------
        

def Bye():
    rows=10
    n = 0
    for i in range(1, rows + 1):  
        for j in range (1, (rows - i) + 1): 
            print(end = " ") 

        while n != (2 * i - 1): 
            print("*", end = "") 
            n = n + 1
        n = 0

        print()  
  
    k = 1
    n = 1
    for i in range(1, rows): 

        for j in range (1, k + 1): 
            print(end = " ") 
        k = k + 1

        while n <= (2 * (rows - i) - 1): 
            print("*", end = "") 
            n = n + 1
        n = 1
        print() 


    print("  _  ")              
    print(" | |   ")            
    print(" | |__  _   _  ___ ")
    print(" | '_ \| | | |/ _ \ ")
    print(" | |_) | |_| |  __/")
    print(" |_.__/ \__, |\___|")
    print("         __/ |     ")
    print("        |___/  ")

        
    sys.exit()

#---------------------------------------------------------------------------------------------------------------------------


page()
















