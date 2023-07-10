import cv2
import os

class TrimVideo:
    
    def video_edit(input_path='F:\\AI\\UnMute\\Dataset\\Videos\\'):
        obj = file_name(input_path)
        total_folders_list = next(obj)
        
        for i in total_folders_list:
            
            input_video_path,files = next(obj)
#             print(input_video_path,files)

            for file in files:
#                 print(input_video_path+'\\'+file)
                cap = cv2.VideoCapture(input_video_path+'\\'+file)
                
                if not os.path.exists(input_video_path + '\\Output\\'):
                    os.mkdir(input_video_path + '\\Output\\')
                
                output_video_path = input_video_path + '\\Output\\' + file
                print(output_video_path)
                fps = cap.get(cv2.CAP_PROP_FPS)
                frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
                frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
                fourcc = cv2.VideoWriter_fourcc(*"mp4v")
                out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
                No_frames_count =0

                while True:
                    ret, current_frame = cap.read()

                    if not ret:
                        break
                    No_frames_count+=1
                    if No_frames_count == int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) // 2 + 10 :
                        break
                    out.write(current_frame)
                out.release()
        
        
    def file_name(path):
        parent_dir = os.walk(path)
        total_parent_directories = next(parent_dir)[1]
        yield total_parent_directories
        
        for i in range(len(total_parent_directories)):
            sub_dir,sub_sub,files = next(parent_dir)
            yield sub_dir,files
        
        
    