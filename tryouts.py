from tensorflow.python.client import device_lib
import os

if len(device_lib.list_local_devices()) == 0:
    print('error no gpu, proceeding further')
else:
    print('Found GPU', len(device_lib.list_local_devices()))


os.system("shutdown /s /t 1")