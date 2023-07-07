## Defining lists to populate dictionary
filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg" ]
pet_labels = ["beagle", "beagle", "skunk"]
classifier_labels = ["walker hound, walker foxhound", "beagle",
                     "skunk, polecat, wood pussy"]
pet_label_is_dog = [1, 1, 0]
classifier_label_is_dog = [1, 1, 0]

## Defining empty dictionary
results_dic = dict()

## Populates empty dictionary with both labels &indicates if they match (idx 2)
for idx in range (0, len(filenames), 1):
    # If first time key is assigned initialize the list with pet &
    # classifier labels
    if filenames[idx] not in results_dic:
        results_dic[filenames[idx]] = [ pet_labels[idx], classifier_labels[idx] ]

    # Determine if pet_labels matches classifier_labels using in operator
    # - so if pet label is 'in' classifier label it's a match
    # ALSO since Key already exists because labels were added, append
    # value to end of list for idx 2
    # if pet image label was FOUND then there is a match
    if pet_labels[idx] in classifier_labels[idx]:
        results_dic[filenames[idx]].append(1)

    # if pet image label was NOT found then there is no match
    else:
        results_dic[filenames[idx]].append(0)

## Populates dictionary with whether or not labels indicate a dog image (idx 3&4)
for idx in range (0, len(filenames), 1):
    # Key already exists, extend values to end of list for idx 3 & 4
    results_dic[filenames[idx]].extend([pet_label_is_dog[idx],
                                       classifier_label_is_dog[idx]])

## Iterates through the list to print the results for each filename
for key in results_dic:
    print("\nFilename=", key, "\npet_image Label=", results_dic[key][0],
          "\nClassifier Label=", results_dic[key][1], "\nmatch=",
          results_dic[key][2], "\nImage is dog=", results_dic[key][3],
          "\nClassifier is dog=", results_dic[key][4])

    # Provides classifications of the results
    if sum(results_dic[key][2:]) == 3:
        print("*Breed Match*")
    if sum(results_dic[key][3:]) == 2:
        print("*Is-a-Dog Match*")
    if sum(results_dic[key][3:]) == 0 and results_dic[key][2] == 1:
        print("*NOT-a-Dog Match*")



# lst = ['me']
# lst.extend(['awesume', 'attractive'])
# print(lst)

# t = True
# if t == 1:
#     print("1 is the same as True")


# with open("dognames.txt") as f:
#     dog_breeds = f.read().split(',')
# dog_breeds = [breed.strip().split('\n') for breed in dog_breeds]
# dog_breeds = [breed for breeds in dog_breeds for breed in breeds]
# print(dog_breeds, len(dog_breeds))
# print(True + True + True)


# x = ["apple", "banana", "cherry"]
# y = ["google", "microsoft", "apple"]
#
# # z = x.intersection(y)
# print(len(set(x).intersection(set(y))) != 0)


# x = "hi how are you"
# y = "Mostafa, hi how are you"
# print(x in y)
