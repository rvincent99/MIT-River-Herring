import os
import sys

folder_path = sys.argv[1]
label_path = os.path.join(folder_path, "labels")
image_path = os.path.join(folder_path, "images")

total = 0
not_background = 0
nothing = set()
for name in os.listdir(label_path):
    # Open file
    total += 1
    with open(os.path.join(label_path, name)) as f:
        if os.path.getsize(os.path.join(label_path, name)) == 0:
            file = name.split(".txt")
            nothing.add(file[0])
        else:
            not_background += 1

bkg_desired = int(0.25*not_background)
bkg_count = total - not_background
delete_bkg = bkg_count - bkg_desired
count = 0

for empty in nothing:
    if count >= delete_bkg:
        break
    else:
        count += 1
        empty_label = empty + ".txt"
        empty_img = empty + ".jpg"
        print(empty)
        os.remove(os.path.join(image_path, empty_img))
        os.remove(os.path.join(label_path, empty_label))




        
 
    