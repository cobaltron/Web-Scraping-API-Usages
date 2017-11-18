#import multithread
import os
import win32file
def locate_usb():
    drive_list = []
    drivebits=win32file.GetLogicalDrives()
    for d in range(1,26):
        mask=1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname='%c:\\' % chr(ord('A')+d)
            t=win32file.GetDriveType(drname)
            drive_list.append(drname)
    return drive_list

print 'Any specific drive?'
drive=str(raw_input())
print 'search string(with/without extension)'
s=str(raw_input())
di=locate_usb()
if drive=='none':
    for i in di:

        for root, dirs, files in os.walk(i):
            for file in files:
                #if file.endswith("exam.mp4"):
                if s in file:
                    print(os.path.join(root, file))
