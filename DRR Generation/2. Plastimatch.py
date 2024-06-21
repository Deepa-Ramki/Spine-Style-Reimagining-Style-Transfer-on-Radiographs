import os
import cv2
import time
import numpy as np
import matplotlib.pyplot as plt
from subprocess import check_output as qx
try:
    from data_preprocessing.ctxray_utils import load_scan_mhda, save_scan_mhda
except:
    from ctxray_utils import load_scan_mhda, save_scan_mhda

import os
root_dir = os.path.dirname(os.path .realpath(__file__))

root_path = "C:/Dharshu/College/FYP/Code/PerX2CT-main/mhd_2/"
save_root_path = "C:\Dharshu\College\FYP\Code\PerX2CT-main\MHD_op-Vol2"
plasti_path = 'C:\\Program Files\\plastimatch 1.6.4\\bin\\'

# compute xray source center in world coordinate
def get_center(origin, size, spacing):
    origin = np.array(origin)
    size = np.array(size)
    spacing = np.array(spacing)
    center = origin + (size - 1) / 2 * spacing
    return center

# convert a ndarray to string
def array2string(ndarray):
    ret = ""
    for i in ndarray:
        ret = ret + str(i) + " "
    return ret[:-2]

# save a .pfm file as a .png file
def savepng(filename, j):
    #raw_data , scale = pfm.read(filename)
    print(filename)
    raw_data = cv2.imread(filename, cv2.IMREAD_UNCHANGED)
    print(raw_data)
    #import pdb;pdb.set_trace()
    max_value = raw_data.max()
    im = (raw_data / max_value * 255).astype(np.uint8)
    '''# PA view should do additional left-right flip
    if direction == 1:
        im = np.fliplr(im)
    '''
    savedir, _ = os.path.split(filename)
    outfile = os.path.join(savedir, "xray{}.png".format(j))
    # plt.imshow(im, cmap=plt.cm.gray)
    plt.imsave(outfile, im, cmap=plt.cm.gray)
    # plt.imsave saves an image with 32bit per pixel, but we only need one channel
    image = cv2.imread(outfile)
    gray = cv2.split(image)[0]
    cv2.imwrite(outfile, gray)
    
    

def make_input():
    files_list = os.listdir(root_path)

    start = time.time()
    for fileIndex, fileName in enumerate(files_list):
        t0 = time.time()
        print('Begin {}/{}: {}'.format(fileIndex + 1, len(files_list), fileName))
        saveDir = os.path.join(save_root_path, fileName)
        if not os.path.exists(saveDir):
            os.makedirs(saveDir)
        # savePath is the .mha file store location
        #if not os.path.exists(saveDir + '/10000.pfm'):
        try:
            savePath = os.path.join(os.path.join(root_path, fileName), '{}.mha'.format(fileName))
            ct_itk, ct_scan, ori_origin, ori_size, ori_spacing = load_scan_mhda(savePath)
        except:
            savePath = os.path.join(os.path.join(root_path, fileName), 'ct_file.mha')
            ct_itk, ct_scan, ori_origin, ori_size, ori_spacing = load_scan_mhda(savePath)
        # savePath = glob.glob(f"{saveDir}/*.mha")[0]

        # compute isocenter
        center = get_center(ori_origin, ori_size, ori_spacing)
        # map the .mha file value to (-1000, 1000)
        cmd_str = f'{plasti_path}plastimatch.exe adjust --input "{savePath}" --output "{saveDir}/out.mha" --pw-linear "0, -1000"'
        output = qx(cmd_str)
        # get virtual xray file
        
        a = 360
        N = 1
        j=0
        '''
        plastimatch usage
        -t : save format
        -g : sid sad [DistanceSourceToPatient]:541 
                     [DistanceSourceToDetector]:949.075012
        -N : angle interval
        -a : number of images
        -r : output image resolution
        -o : isocenter position
        -z : physical size of imager
        -I : input file in .mha format
        -O : output prefix
                
            
            '''
        cmd_str = f'{plasti_path}drr.exe -t pfm -N "{N}" -a "{a}" -g "700 949" -r "1024 1024" -o "{array2string(center)}" -z "700 700" -I "{saveDir}/out.mha" -O "{saveDir}/{j}"'
        # print(cmd_str)
        output = qx(cmd_str)
        for j in range(0, a):
            # plastimatch would add a 0000 suffix
            if j<100:
                if j <10:
                    pfmFile = saveDir + '/' + '0000{}'.format(j)+'.pfm'
                else:
                    pfmFile = saveDir + '/' + '000{}'.format(j)+'.pfm'
            else:
                pfmFile = saveDir + '/' + '00{}'.format(j)+'.pfm'
            
            
            print("j = " + str(j))
            savepng(pfmFile,j)    
            
        # remove the temp .mha file due to large size
        os.remove(saveDir + '/out.mha')
        t1 = time.time()
        print('End! Case time: {}'.format(t1 - t0))

    end = time.time()
    print('Finally! Total time: {}'.format(end - start))


if __name__ == '__main__':
    make_input()

