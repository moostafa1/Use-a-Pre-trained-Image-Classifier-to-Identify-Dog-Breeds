from torchvision.transforms import RandomHorizontalFlip
from PIL import Image
from re import compile, search, match
from os import listdir



def horizontal_flip(img_path, save_name):
    img = Image.open(img_path)
    transform = RandomHorizontalFlip(p=1)
    img_transformed = transform(img)
    img_transformed.save(save_name)
    print(f"image {img_path} is flipped horizontally and saved as {save_name}")




# horizontal_flip("uploaded_images/Dog_01.jpg", "uploaded_images/Dog_02.jpg")




def join_lst_to_str(lst, prev_element, next_element):
    start = lst.index(prev_element)
    end = lst.index(next_element)
    #print(start, end)
    return ' '.join(lst[start + 1: end])


# s = "Real:                     beagle is nice  Classifier:             labrador retriever".split()
# s.append(" ")
# print(s)
# print(join_lst_to_str(s, "Real:", "Classifier:"))
# print(join_lst_to_str(s, "Classifier:", " "))





def extract_labels(example, pattern1, pattern2):
    ptrn = compile(f"{pattern1}:\s+[a-z]+\s+{pattern2}:\s+[a-z]+.+")
    srch = ptrn.search(example)
    if srch != None:
        result = srch.group().split()
        result.append(" ")
        real_label = join_lst_to_str(result, pattern1+':', pattern2+':')
        predected_label = join_lst_to_str(result, pattern2+':', " ")

        #print(real_label, predected_label)
        return real_label, predected_label



# s = "Real:                     beagle   Classifier:                         beagle"
# s = "Real:                     beagle   Classifier:             labrador retriever"
# s1 = "Real:                      chair   Classifier:          studio couch, day bed"
# s2 = "Real:                      chair   Classifier:                   barber chair"
# s3 = "Real:                      chair   Classifier:          rocking chair, rocker"
# print(extract_labels(s1, "Real", "Classifier"))
# print(extract_labels(s2, "Real", "Classifier"))
# print(extract_labels(s3, "Real", "Classifier"))



def time_extraction(file):
    with open(file) as f:
        time = f.read().split('\n')[-2]
    #print(time)
    return f"{file.split('_')[0]}: {time[3:]}"



# print(time_extraction('vgg_uploaded-images.txt'))






def extract_it(file, img_name, pattern1, pattern2):
    model_name = file.split('_')[0]
    pattern = f"{img_name}:(\s+[A-Za-z]+:?)+.*"
    with open(file) as f:
        whole_file = f.read()
    #print(whole_file, type(whole_file))
    ptrn = compile(pattern)    #(f"'{pattern}': [0-9]+((.[0-9])?)*")   #(f"{pattern}: \d.\d+")
    srch = ptrn.search(whole_file)
    result = ""
    if srch != None:
        # result = srch.group().split('\n')[-2][55:].strip()
        result = srch.group().strip()
        #print(result)
        real_label, predected_label = extract_labels(result, pattern1, pattern2)
        str_to_add = f"model_name: {model_name}, real_label: {real_label}, predected_label: {predected_label}"
    else:
        str_to_add = f"model_name: {model_name} has no value for{img_name}"

    return str_to_add, f"classified correctly: {real_label in predected_label}"






def stats_extract(file):
    with open(file) as f:
        read_file = f.read().split('\n')
    return read_file[-14:-3]

# print(stats_extract("vgg_uploaded-images.txt"))












#files_lst = ['vgg_uploaded-images.txt', 'resnet_uploaded-images.txt', 'alexnet_uploaded-images.txt']
#imgs_lst = listdir("uploaded_images")
# img_1 = "Beagle_01.jpg"
# img_2 = "Beagle_02.jpg"
# img_3 = "Chair_01.jpg"
# img_4 = "Parrot_01.jpg"

files_lst = ['vgg_pet-images.txt', 'resnet_pet-images.txt', 'alexnet_pet-images.txt']
imgs_lst = listdir("pet_images")

#
# str_to_add = []
# for img in imgs_lst:
#     under_line = (len(img)+5) * '-'
#     str_to_add.append(f"img: {img}\n{under_line}")
#     for file in files_lst:
#         str_to_add.append(extract_it(file, img, "Real", "Classifier"))
#     str_to_add.append('\n')
#
#
#
#
# model_time = []
# for file in files_lst:
#     model_time.append(time_extraction(file))
#
# print(model_time)


str_to_add = []
for file in files_lst:
    under_line = (len(file)+6) * '-'
    str_to_add.append(f"file: {file}\n{under_line}")
    str_to_add.append(time_extraction(file))
    str_to_add.extend(stats_extract(file))

    # for img in imgs_lst:
    #     str_to_add.append(f"img: {img}: " + str(extract_it(file, img, "Real", "Classifier")))
    #     #under_line = (len(img)+5) * '-'
    #     #str_to_add.append()
    str_to_add.append('\n')


#print(str_to_add)
for s in str_to_add:
    print(s)



def write_file(file, text_lst):
    with open(file, 'w') as f:
        for s in text_lst:
            f.write(s + '\n')






write_file("notice_from_useful_functions_pet.txt", str_to_add)


# print(f"{img_3}:")
# for file in files_lst:
#     extract_it(file, img_3, "Real", "Classifier")
