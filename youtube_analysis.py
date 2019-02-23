#!/usr/bin/python

from apiclient.discovery import build
from apiclient.errors import HttpError
import argparse

import json
import pymongo 
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
import re
import pprint

# Connecting to mongodb
client = MongoClient()
db = client.youtube_db
youtube_col = db.youtube_col
# football collections
youtube_col_glasgow = db.youtube_col_glasgow
youtube_col_london = db.youtube_col_london
youtube_col_sf_soc = db.youtube_col_sf_soc
youtube_col_la_soc = db.youtube_col_la_soc
youtube_col_man_fb = db.youtube_col_man_fb
youtube_col_liv_fb = db.youtube_col_liv_fb
youtube_col_ed_fb = db.youtube_col_ed_fb
# basketball collections
youtube_col_glasgow_bb = db.youtube_col_glasgow_bb
youtube_col_london_bb = db.youtube_col_london_bb
youtube_col_sf = db.youtube_col_sf
youtube_col_la = db.youtube_col_la
# Cursor gets data from data collection
# Football 
gl_fb_cursor = youtube_col_glasgow.find()
ld_fb_cursor = youtube_col_london.find()
man_fb_cursor = youtube_col_man_fb.find()
liv_fb_cursor = youtube_col_liv_fb.find()
ed_fb_cursor = youtube_col_ed_fb.find()


gl_bb_cursor = youtube_col_glasgow_bb.find()
ld_bb_cursor = youtube_col_london_bb.find()

la_bb_cursor = youtube_col_la.find()
sf_bb_cursor = youtube_col_sf.find()

la_soc_cursor = youtube_col_la_soc.find()
sf_soc_cursor = youtube_col_sf_soc.find()



class DataAnalysis():

    def __init__(self):
        
        #setting arrays that 
        n_list = [1.0, 2.0, 3.0]
        n_array = np.array(n_list)
        
        # column 0 is views, 1 is likes, 2 is comments
   
        

  

    def calculateMean(self):

        man_fb = np.zeros((50,3))
        liv_fb = np.zeros((50,3))
        ed_fb  = np.zeros((50,3))
        london_fb = np.zeros((50,3))
        glasgow_fb = np.zeros((50,3))
        i=0

        for document in gl_fb_cursor:
            glasgow_fb[i,0] = int(document['VideoCount'])
            glasgow_fb[i,1] = int(document['Likes'])
            glasgow_fb[i,2] = int(document['CommentCount'])
            i+=1
        
        i=0
        for document in ld_fb_cursor:
            london_fb[i,0] = int(document['VideoCount'])
            london_fb[i,1] = int(document['Likes'])
            london_fb[i,2] = int(document['CommentCount'])
            i+=1
        i=0
        for document in man_fb_cursor:
            man_fb[i,0] = int(document['VideoCount'])
            man_fb[i,1] = int(document['Likes'])
            man_fb[i,2] = int(document['CommentCount'])
            i+=1
        i=0
        for document in liv_fb_cursor:
            liv_fb[i,0] = int(document['VideoCount'])
            liv_fb[i,1] = int(document['Likes'])
            liv_fb[i,2] = int(document['CommentCount'])
            i+=1
        i=0
        for document in ed_fb_cursor:
            ed_fb[i,0] = int(document['VideoCount'])
            ed_fb[i,1] = int(document['Likes'])
            ed_fb[i,2] = int(document['CommentCount'])
            i+=1
        
        self.mean_edfb = np.mean(ed_fb, axis = 0)
        self.mean_livfb = np.mean(liv_fb, axis = 0)
        self.mean_manfb = np.mean(man_fb, axis = 0)
        self.mean_ldfb = np.mean(london_fb, axis = 0)
        self.mean_gfb = np.mean(glasgow_fb, axis = 0)
        
 
    def plotViewsUK(self):
        
        fig = plt.figure()
        axes = plt.subplot(1,1,1)
        barWidth=0.50
        
        r1 = 1
        r2 = [1 + barWidth]
        r3 = [1.5 +barWidth]
        r4 = [2 +barWidth]
        r5 = [2.5 +barWidth]
        
        axes.get_xaxis().set_visible(False)
        plt.bar(r1, self.mean_edfb[0], color='red', width=barWidth, edgecolor='white', label='Edinburgh')
        plt.bar(r2, self.mean_livfb[0], color='yellow', width=barWidth, edgecolor='white', label='Liverpool')
        plt.bar(r3, self.mean_manfb[0], color='blue', width=barWidth, edgecolor='white', label='Manchester')
        plt.bar(r4, self.mean_gfb[0], color='green', width=barWidth, edgecolor='white', label='Glasgow Views')

        plt.legend()
        axes.set_title('Mean Number of Football Video Views per City')
        axes.set_ylabel('View Count')
        axes.set_xlabel('City')
        plt.show()
        
    def plotLikesUK(self):
        fig = plt.figure()
        axes = plt.subplot(1,1,1)
        barWidth=0.50
        
        r1 = 1
        r2 = [1 + barWidth]
        r3 = [1.5 +barWidth]
        r4 = [2 +barWidth]
        r5 = [2.5 +barWidth]
        
        plt.bar(r1, self.mean_edfb[1], color='red', width=barWidth, edgecolor='white', label='Edinburgh')
        plt.bar(r2, self.mean_livfb[1], color='yellow', width=barWidth, edgecolor='white', label='Liverpool')
        plt.bar(r3, self.mean_manfb[1], color='blue', width=barWidth, edgecolor='white', label='Manchester')
        plt.bar(r4, self.mean_gfb[1], color='green', width=barWidth, edgecolor='white', label='Glasgow')
        axes.get_xaxis().set_visible(False)

        plt.legend()
        axes.set_title('Mean Number of Football Video Likes per City')
        axes.set_ylabel('View Count')
        axes.set_xlabel('City')
        plt.tight_layout()
        plt.show()
        
    def plotCommentsUK(self):
        fig = plt.figure()
        axes = plt.subplot(1,1,1)
        barWidth=0.50
        
        r1 = 1
        r2 = [1 + barWidth]
        r3 = [1.5 +barWidth]
        r4 = [2 +barWidth]
        r5 = [2.5 +barWidth]
        
        plt.bar(r1, self.mean_edfb[2], color='red', width=barWidth, edgecolor='white', label='Edinburgh')
        plt.bar(r2, self.mean_livfb[2], color='yellow', width=barWidth, edgecolor='white', label='Liverpool')
        plt.bar(r3, self.mean_manfb[2], color='blue', width=barWidth, edgecolor='white', label='Manchester')
        plt.bar(r4, self.mean_gfb[2], color='green', width=barWidth, edgecolor='white', label='Glasgow')
        axes.get_xaxis().set_visible(False)

        
        
        plt.legend()
        axes.set_title('Mean Number of Football Video Comments per City')
        axes.set_ylabel('View Count')
        axes.set_xlabel('City)')
        plt.tight_layout()
        plt.show()
        
        
if __name__ == "__main__":
    
    print('-----')
    analysis = DataAnalysis()
    analysis.calculateMean()
    analysis.plotViewsUK()
    analysis.plotLikesUK()
    analysis.plotCommentsUK()

    
    

    


