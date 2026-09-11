## System Requirements & Environment Setup
Run the following commands on your Raspberry Pi to verify and install all required system components, Python packages, and video streaming dependencies for system-wide execution.

### 1. Python Dependencies (`flask` & `RPi.GPIO`)
Verify that Python 3 and the required libraries are installed:

```bash
python3 -c "import flask, RPi.GPIO; print('Flask:', flask.__version__); print('GPIO:', RPi.GPIO.VERSION)"

```

- **Expected Output:** Displays installed version numbers without throwing an `ImportError`.
- **Installation:** If missing, install system-wide using `apt`:
  ```bash
  sudo apt update && sudo apt install -y python3-flask python3-rpi.gpio
  
  ```

### 2. Camera Device Detection
Verify that your USB webcam or Raspberry Pi camera module is recognized by the Linux kernel:

```bash
ls -l /dev/video0

```

- **Expected Output:** Returns device info similar to `crw-rw----+ 1 root video /dev/video0`.
- **Troubleshooting:** Reconnect the camera or enable the camera interface using `sudo raspi-config` under **Interface Options**.

### 3. Video Streamer (`mjpg-streamer`)
Check if the `mjpg_streamer` binary is compiled and available in your system `PATH`:

```bash
which mjpg_streamer

```

- **Expected Output:** Returns `/usr/local/bin/mjpg_streamer` or `/usr/bin/mjpg_streamer`.
- **Installation:** If missing, build and install `mjpg-streamer` from source:
  ```bash
  sudo apt update
  sudo apt install -y cmake libjpeg-dev gcc g++ git
  cd ~
  git clone https://github.com/jacksonliam/mjpg-streamer.git
  cd mjpg-streamer/mjpg-streamer-experimental
  make
  sudo make install
  
  ```