import cv2
import os
import numpy as np

class ImageManipulator:
    def __init__(self):
        self.curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.desired_width = 640
        self.desired_height =  480
        self.dsize = (self.desired_width, self.desired_height)
        pass

    def transform_img(self):

        original_path = self.curr_dir + '/original_images/'
        self.dest_path = self.curr_dir + '/resized_images/'

        #Walk through folder
        count = 0
        for (dir_path, dir_names, file_names) in os.walk(original_path):
            for img_name in file_names:
                src = cv2.imread( original_path + img_name, cv2.IMREAD_UNCHANGED)
                cropped_img = self.cut_img(src)
                resized_img = self.resize_img(cropped_img)
                self.write_to_folder(img_name, resized_img)
                count += 1
                print(count)
            break        

    def cut_img(self, src):
        src_height, src_width, c = src.shape

        print(src_width)
        print(src_height)

        ratio_width = float(src_width) / float(self.desired_width)
        ratio_heigth = float(src_height) / float(self.desired_height)

        print("Ratio width: {}".format(ratio_width))
        print("Ratio height: {}".format(ratio_heigth))
        
        if ratio_width < ratio_heigth:
            cropped_image = src[0:(int(self.desired_width*ratio_width)), 0:(int(self.desired_height*ratio_width))]
            print("cropped image for height ratio")
        elif ratio_heigth < ratio_width:
            print(int(self.desired_width*ratio_heigth))
            print(int(self.desired_height*ratio_heigth))
            cropped_image = src[0:(int(self.desired_width*ratio_heigth)), 0:(int(self.desired_height*ratio_heigth))]
            print("cropped image for height ratio")
        else:
            cropped_image = src
            print("Cropping not needed")
        
        return cropped_image

    def resize_img(self, src):
        return cv2.resize(src, self.dsize)

    def write_to_folder(self, img_name, img):
        cv2.imwrite(self.dest_path + img_name, img)
    
    def show_img(self, src):
        cv2.imshow("img", src)
        cv2.waitKey(0)

if __name__ == "__main__":
    manipulator = ImageManipulator()
    manipulator.transform_img()