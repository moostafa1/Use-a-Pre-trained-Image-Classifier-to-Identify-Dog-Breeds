#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Mostafa Noaman
# DATE CREATED: 5/7/2023
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir
from re import findall


# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#


#
# def extract_it(img, pattern = "([A-Za-z]+_)+"):      # [^?!.]?
#     ptrn = re.compile(pattern)
#     srch = ptrn.search(img)
#     result = srch.group()[:-1].lower().split('_')
#     result = " ".join(result)
#
#     return result
#





def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    pet_labels = [[findall("([A-Za-z_]+)", img)[0].lower().replace("_", " ").strip()] for img in listdir(image_dir) if not img.startswith(".")]
    pet_img_name = [img for img in listdir(image_dir) if not img.startswith(".")]
    return dict(zip(pet_img_name, pet_labels))
    # image_label_dic = {}
    # for img in listdir(image_dir):
    #     if img[0] != '.':
    #         image_label_dic[img] = [extract_it(img)]
    # return image_label_dic





if __name__ == "__main__":
    path = "pet_images/"
    image_label_dic = get_pet_labels(path)
    for i in image_label_dic:
        print(f"{i}: {image_label_dic[i]}")
    print(type(image_label_dic))
