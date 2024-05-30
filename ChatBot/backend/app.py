from flask import Flask, render_template, Response
import cv2
import tensorflow as tf

app = Flask(__name__)

face_model = cv2.CascadeClassifier('C:/Users/HP/Desktop/data analysis/Python-Projects-for-Interviews/ChatBot/backend/models/face_model.xml')
object_model = tf.keras.models.load_model('C:/Users/HP/Desktop/data analysis/Python-Projects-for-Interviews/ChatBot/backend/models/object_model.h5')
behavior_model = tf.keras.models.load_model('C:/Users/HP/Desktop/data analysis/Python-Projects-for-Interviews/ChatBot/backend/models/behavior_model.h5')

def generate_frames():
    camera = cv2.VideoCapture('C:/Users/HP/Desktop/data analysis/Python-Projects-for-Interviews/ChatBot/frontend/video.mp4')  

    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_model.detectMultiScale(gray, 1.1, 4)

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            

            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)