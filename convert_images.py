import os
import nibabel as nib
from matplotlib import pyplot as plt

input_dir = 'imagesTr'
output_dir = 'imagesPNG'

image_position = 21

filenames = [
    'la_003',
    'la_004',
    'la_005',
    'la_007',
    'la_009',
    'la_010',
    'la_011',
    'la_014',
    'la_016',
    'la_017',
    'la_018',
    'la_019',
    'la_020',
    'la_021',
    'la_022',
    'la_023',
    'la_024',
    'la_026',
    'la_029',
    'la_030',
]

for filename in filenames:
    filename_path = os.path.join(input_dir, filename + '.nii')
    img = nib.load(filename_path)
    img_fdata = img.get_fdata()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    output_file = os.path.join(output_dir, filename + '.png')
    plt.imsave(output_file, img_fdata[:, :, image_position])
