import os
import subprocess

from flask import Flask, render_template, jsonify
import netifaces as ni
import RPi.GPIO as GPIO

app = Flask(__name__)

ip = ni.ifaddresses('wlan0')[ni.AF_INET][0]['addr']

# GPIO setup
motorkiri1 = 22
motorkiri2 = 27
motorkanan1 = 23
motorkanan2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(motorkiri1, GPIO.OUT)
GPIO.setup(motorkiri2, GPIO.OUT)
GPIO.setup(motorkanan1, GPIO.OUT)
GPIO.setup(motorkanan2, GPIO.OUT)

# Jalankan mjpg-streamer hanya sekali (hindari duplikat saat Flask debug reload)
if os.environ.get('WERKZEUG_RUN_MAIN') != 'true':
    subprocess.Popen([
        "mjpg_streamer",
        "-i", "input_uvc.so -r 320x240 -d /dev/video0 -f 60 -q 20",
        "-o", "output_http.so -p 8080 -w /usr/local/share/mjpg-streamer/www"
    ])


@app.route('/')
def index():
    return render_template('mobildankamera.html', ip=ip)


@app.route('/maju')
def maju():
    GPIO.output(motorkiri1, GPIO.HIGH)
    GPIO.output(motorkiri2, GPIO.LOW)
    GPIO.output(motorkanan1, GPIO.LOW)
    GPIO.output(motorkanan2, GPIO.HIGH)
    return jsonify(status="ok")


@app.route('/kiri')
def kiri():
    GPIO.output(motorkiri1, GPIO.LOW)
    GPIO.output(motorkiri2, GPIO.HIGH)
    GPIO.output(motorkanan1, GPIO.LOW)
    GPIO.output(motorkanan2, GPIO.HIGH)
    return jsonify(status="ok")


@app.route('/kanan')
def kanan():
    GPIO.output(motorkiri1, GPIO.HIGH)
    GPIO.output(motorkiri2, GPIO.LOW)
    GPIO.output(motorkanan1, GPIO.HIGH)
    GPIO.output(motorkanan2, GPIO.LOW)
    return jsonify(status="ok")


@app.route('/mundur')
def mundur():
    GPIO.output(motorkiri1, GPIO.LOW)
    GPIO.output(motorkiri2, GPIO.HIGH)
    GPIO.output(motorkanan1, GPIO.HIGH)
    GPIO.output(motorkanan2, GPIO.LOW)
    return jsonify(status="ok")


@app.route('/berhenti')
def berhenti():
    GPIO.output(motorkiri1, GPIO.LOW)
    GPIO.output(motorkiri2, GPIO.LOW)
    GPIO.output(motorkanan1, GPIO.LOW)
    GPIO.output(motorkanan2, GPIO.LOW)
    return jsonify(status="ok")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
