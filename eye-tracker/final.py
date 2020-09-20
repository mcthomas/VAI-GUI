import multiprocessing
import time
from pynput.keyboard import Key, Controller
import cv2
import numpy as np
import dlib
from math import hypot
global a
import speech_recognition as sr
import pyttsx3


keyboard = Controller()
def tab():
    while 1:
        print("tab")
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        time.sleep(3)
def blink():
    def midpoint(p1 ,p2):
        return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

    font = cv2.FONT_HERSHEY_PLAIN



    def get_blinking_ratio(eye_points, facial_landmarks):
        left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
        right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
        center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
        center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

        hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
        ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

        hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
        ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

        ratio = hor_line_lenght / ver_line_lenght
        return ratio


    i=0

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    a=0
    cap = cv2.VideoCapture(0)
    tic = time.time()

    while True:
        _, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
            #x, y = face.left(), face.top()
            #x1, y1 = face.right(), face.bottom()
            #cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

            landmarks = predictor(gray, face)
            left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
            right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
            blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
            #tok = time.time()
            #if tok-tic>3:
            #    a=0
            #    tic=tok

              #  print("boom")
            #print( "llk,",tok-tic)
            if blinking_ratio > 5.7:
                cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0))
                #print("blink", i)
                a=a+1
                i=i+1
            else:
                i=0

            if i==5:
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                a=0
                i=0
                print("ENTER")
                #print(a)
        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

r = sr.Recognizer()

def voice():

    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                if MyText == 'enter':
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                    print('enter')
                                
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occured")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=tab)
    p2 = multiprocessing.Process(target=blink)
    p3 = multiprocessing.Process(target=voice)
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("Done!")
