# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 13:47:53 2024

@author: Dharshu
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def plot_tone_curves(im1,im2,im3,im4,im5,im6,im7,im8):
    h1 = cv2.calcHist([im1],[0],None,[256],[10,250]).flatten()  
    h2 = cv2.calcHist([im2],[0],None,[256],[10,250]).flatten()
    h3 = cv2.calcHist([im3],[0],None,[256],[10,250]).flatten()
    h4 = cv2.calcHist([im4],[0],None,[256],[10,250]).flatten()
    h5 = cv2.calcHist([im5],[0],None,[256],[10,250]).flatten()
    h6 = cv2.calcHist([im6],[0],None,[256],[10,250]).flatten()
    h7 = cv2.calcHist([im7],[0],None,[256],[10,250]).flatten()
    h8 = cv2.calcHist([im8],[0],None,[256],[10,250]).flatten()
    
    plt.figure(figsize=(24,16))
    
    plt.subplot(4,1,1)
    plt.plot(h1,color="blue", lw = 3)
    plt.title("X-ray Original",fontsize=30,loc='right')
    plt.xlabel('Pixel Intensity',fontsize=15)
    plt.ylabel("Frequency",fontsize=15)
    plt.legend(fontsize=15)

    
    plt.subplot(4,1,2)
    plt.plot(h2,color="red", lw = 3)
    plt.title("DRR Style",fontsize=30,loc='right')
    plt.xlabel('Pixel Intensity',fontsize=15)
    plt.ylabel("Frequency",fontsize=15)
    plt.legend(fontsize=15)
    
    plt.subplot(4,1,3)
    plt.plot(h3,color="black", lw = 3)
    plt.title("OP 300",fontsize=30,loc='right')
    plt.xlabel('Pixel Intensity',fontsize=15)
    plt.ylabel("Frequency",fontsize=15)
    plt.legend(fontsize=15)
    
    plt.subplot(4,1,4)
    plt.plot(h4,color="black", lw = 3)
    plt.title("OP 700",fontsize=30,loc='right')
    plt.xlabel('Pixel Intensity',fontsize=15)
    plt.ylabel("Frequency",fontsize=15)
    plt.legend(fontsize=15)
    
    '''
    plt.subplot(8,1,5)
    plt.plot(h5,color="black")
    plt.title("OP 700")
    plt.xlabel('Pixel Intensity')
    plt.ylabel("Frequency")
    
    plt.subplot(8,1,6)
    plt.plot(h6,color="black")
    plt.title("OP 1000")
    plt.xlabel('Pixel Intensity')
    plt.ylabel("Frequency")
    
    plt.subplot(8,1,7)
    plt.plot(h7,color="black")
    plt.title("OP 1500")
    plt.xlabel('Pixel Intensity')
    plt.ylabel("Frequency")
    
    plt.subplot(8,1,8)
    plt.plot(h8,color="black")
    plt.title("OP 2000")
    plt.xlabel('Pixel Intensity')
    plt.ylabel("Frequency")
    '''
    plt.tight_layout()
    plt.show()


    
    
im1 = cv2.imread("C:/Dharshu/College/FYP/Data/testSET55LP.jpg")
im2 = cv2.imread("C:\\Users\\Dharshu\\Downloads\\DRR (1).png")

im2.resize((500,800,3))
im3 = cv2.imread("C:\\Users\\Dharshu\\Downloads\\op300 (1).png")
im4 = cv2.imread("C:\\Users\\Dharshu\\Downloads\\op700 (1).png")
im5 = cv2.imread("C:\\Users\\Dharshu\\Downloads\\op700.png")
im6 = cv2.imread("C:\\Users\\Dharshu\\Downloads\\op1000.png")
im7 = cv2.imread("C:\\Users\\Dharshu\\Downloads\\op1500.png")
im8 = cv2.imread("C:\\Users\\Dharshu\\Downloads\\op2000.png")

plot_tone_curves(im1,im2,im3,im4,im5,im6,im7,im8)