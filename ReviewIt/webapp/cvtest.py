import cv2
import os
import numpy as np
 
'''
def extractFrames(pathIn, pathOut):
    os.mkdir(pathOut)
 
    cap = cv2.VideoCapture(pathIn)
    count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
 
    while (cap.isOpened()):
 
        # Capture frame-by-frame
        ret, frame = cap.read()
 
        if ret == True:
            print('Read %d frame: ' % count, ret)
            cv2.imwrite(os.path.join(pathOut, "frame{:d}.jpg".format(count)), frame)  # save frame as JPEG file
            count += 1
        else:
            break
 
    # When everything done, release the capture
    print(fps)
    cap.release()
    cv2.destroyAllWindows()
 
'''

'''
img=[]
for i in range(0,200):
    img.append(cv2.imread('/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/4226376/frame_data/frame'+str(i)+'.jpg'))
'''
#height,width,layers=img[1].shape
import gc
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
video = cv2.VideoWriter('output.avi',fourcc, 60.0, (1920,1080))


for j in range(0,2000):
    a=cv2.imread('/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/4226376/frame_data/frame'+str(j)+'.jpg')
    video.write(a)
    print('Write ' + str(j))
    a=None
    del a
    gc.collect()

cv2.destroyAllWindows()
video.release()







'''
def main():
    extractFrames('/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/tests/test_video.mp4', '/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/tests/frame_data')

if __name__ == '__main__':
    main()
'''
