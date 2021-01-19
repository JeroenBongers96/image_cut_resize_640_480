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
        count_changed = 0
        count_not_changed = 0
        for (dir_path, dir_names, file_names) in os.walk(original_path):
            for img_name in file_names:
                src = cv2.imread( original_path + img_name, cv2.IMREAD_UNCHANGED)

                ratio_width, ratio_heigth = self.check_ratio(src)

                if ratio_width > 1 and ratio_heigth > 1 : 
                    cropped_img = self.cut_img(src, ratio_width, ratio_heigth)
                    resized_img = self.resize_img(cropped_img)
                    self.write_to_folder(img_name, resized_img)
                    count_changed += 1
                    print(count_changed)
                else:
                    count_not_changed += 1
                    print(count_not_changed)
            break  
        
        print("Number of images processed: {}".format(count_changed))
        print("Number of images not processed: {}".format(count_not_changed))

    def check_ratio(self, src):
        self.src_height, self.src_width, c = src.shape

        print(self.src_width)
        print(self.src_height)

        ratio_width = float(self.src_width) / float(self.desired_width)
        ratio_heigth = float(self.src_height) / float(self.desired_height)

        print("Ratio width: {}".format(ratio_width))
        print("Ratio height: {}".format(ratio_heigth))

        return(ratio_width, ratio_heigth)

    def cut_img(self, src, ratio_width, ratio_heigth):
        if ratio_width < ratio_heigth:
            new_width = int(self.desired_width*ratio_width)
            new_height = int(self.desired_height*ratio_width)

            diff_width = (self.src_width - new_width)/2
            diff_height = (self.src_height - new_height)/2

            cropped_image = src[diff_height:new_height, diff_width:new_width]

            print("cropped image for height ratio")

            print("New width: {}".format(new_width))
            print("New height: {}".format(new_height))
            print("diff width: {}".format(diff_width))
            print("diff height: {}".format(diff_height))
            
        elif ratio_heigth < ratio_width:
            new_width = int(self.desired_width*ratio_heigth)
            new_height = int(self.desired_height*ratio_heigth)

            diff_width = (self.src_width - new_width)/2
            diff_height = (self.src_height - new_height)/2

            cropped_image = src[diff_height:new_height, diff_width:new_width]
            print("cropped image for height ratio")

            print("New width: {}".format(new_width))
            print("New height: {}".format(new_height))
            print("diff width: {}".format(diff_width))
            print("diff height: {}".format(diff_height))

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