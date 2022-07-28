import os
import nibabel as nib
from matplotlib import pyplot as plt

filename = os.path.join('imagesTr', 'la_003.nii')
img = nib.load(filename)

print(img.shape)

img_fdata = img.get_fdata()

plt.imsave('test.png', img_fdata[:,:,21])
