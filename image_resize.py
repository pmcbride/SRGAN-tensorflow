from PIL import Image
import scipy.misc as sic
import os
from multiprocessing import Pool

# Define the pool function
def downscale(name):
    new_name = dirname + "_" + name.split('\\')[-1].split('.')[0]
    #print(name)
    with Image.open(name) as im:
        w, h = im.size
        w_new = int(w / scale)
        h_new = int(h / scale)
        im_new = im.resize((w_new, h_new), Image.NEAREST)
        save_name_HR = os.path.join(output_dir_HR, dirname + "_" + name.split('\\')[-1].split('.')[0])
        save_name_LR = os.path.join(output_dir_LR, dirname + "_" + name.split('\\')[-1].split('.')[0])
        im.save(save_name_HR + '.png', format='png')
        im_new.save(save_name_LR + '.png', format='png')
        print("Saved file: {}".format(new_name))

# Define the input and output image directories
dirs = ["test"]
for dirname in dirs:
    input_dir = "./data/" + dirname
    output_dir_HR = './data/train_HR'
    output_dir_LR = './data/train_LR'
    scale = 4

    if not os.path.exists(output_dir_HR):
        os.mkdir(output_dir_HR)

    if not os.path.exists(output_dir_LR):
        os.mkdir(output_dir_LR)

    image_list = os.listdir(input_dir)
    if os.path.exists(os.path.join(input_dir,'.ipynb_checkpoints')):
        image_list.remove('.ipynb_checkpoints')
    image_list = [os.path.join(input_dir, _) for _ in image_list]

    for name in image_list:
        downscale(name)

