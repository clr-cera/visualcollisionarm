import flycapture2

bus = PyCapture2.BusManager()
numCams = bus.getNumOfCameras()
camera = PyCapture2.Camera()
uid = bus.getCameraFromIndex(0)
camera.connect(uid)
camera.startCapture()

