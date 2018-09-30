import cv2
import os
import gc
 
def video_output_od(pathIn, pathOut,videoPath):

 
    cap = cv2.VideoCapture(videoPath)
    count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)
    imageSize=cv2.imread(pathIn+'det_frame'+str(0)+'.jpg')
    y=imageSize.shape[0]
    x=imageSize.shape[1]
    print(fps)
    frame_count=os.listdir(pathIn)
    frame_count=len(frame_count)
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    video = cv2.VideoWriter(pathOut,fourcc,fps,(x,y))


    for j in range(0,frame_count):
        a=cv2.imread(pathIn+'det_frame'+str(j)+'.jpg')
        video.write(a)
        print('Write frame ' + str(j))
        a=None
        del a
        gc.collect()

    cv2.destroyAllWindows()
    video.release()
 

 
def main():
    video_output_od('/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/user/destination_data/', '/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/user/od_output.avi', '/media/mayur/2ef007f3-505d-4f8d-98f8-efe8bfc991c5/ReviewIt/ReviewIt/webapp/media/user/video')

if __name__ == '__main__':
    main()