import cv2
import dropbox
import time
import random
Start_time=time.time()
def Take_snapshot():
    number=random.randint(0,1000)
    #initializing cv2
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        #readint he frames while the camera is on
        ret,frame=videoCaptureObject.read()
        image_name="Pic"+str(number)+".png"
        cv2.imwrite(image_name,frame)
        Start_time=time.time
        result=False
        return image_name
    
    print("Image has been taken and sent to the police")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
def UploadFile(image_name):
    access_token='MbyVoWJ-1kgAAAAAAAAAARvXRiJc3xojTv8-9YYttejxkMc01-ayPQQ9xslubGt5'
    file=image_name
    file_from=file
    file_to="/CloudStorageTest/"+(image_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded to the database of the police")
def main():
    while(True):
        if((time.time()-Start_time)>=15):
            name=Take_snapshot()
            UploadFile(name)
main()