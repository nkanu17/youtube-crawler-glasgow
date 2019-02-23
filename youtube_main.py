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
glasgow_fb = youtube_col_glasgow.find()
london_fb = youtube_col_london.find()
glasgow_bb = youtube_col_glasgow_bb.find()
london_bb = youtube_col_london_bb.find()
la_bb = youtube_col_la.find()
sf_bb = youtube_col_sf.find()
la_soc = youtube_col_la_soc.find()
sf_soc = youtube_col_sf_soc.find()


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = "AIzaSyAKjTwDRYcWBLByznOSoHvXFsEItFadpcw"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
                                            q=options.q,
                                            type="video",
                                            location=options.location,
                                            locationRadius=options.location_radius,
                                            part="id,snippet",
                                            maxResults=options.max_results
                                            ).execute()

    search_videos = []

    # Merge video ids
    for search_result in search_response.get("items", []):
        search_videos.append(search_result["id"]["videoId"])
        video_ids = ",".join(search_videos)

    # Call the videos.list method to retrieve location details for each video.
    video_response = youtube.videos().list(
                                            id=video_ids,
                                            part='snippet, statistics, recordingDetails'
                                            ).execute()

    videos = []

    # Add each result to the list, and then display the list of matching videos.
    for video_result in video_response.get("items", []):
        
        
        dictionary = {
            #'id' : video_result["id"].encode("utf-8),
            'Title': (video_result["snippet"]["title"]).encode("utf-8"),
            #'Likes' : str((video_result["statistics"]["likeCount"]).encode("utf-8")),
            'Likes' : video_result["statistics"]["likeCount"],

            'VideoCount' : video_result["statistics"]["viewCount"],
            'DislikeCount' : video_result["statistics"]["dislikeCount"],
            'FavoriteCount' : video_result["statistics"]["favoriteCount"],
            'CommentCount' : video_result["statistics"]["commentCount"]
            }
        
        print(dictionary)
        try:
            #youtube_col_london.insert(dictionary) 
            #youtube_col_glasgow.insert(dictionary)
            
            #youtube_col_london_bb.insert(dictionary)
            #youtube_col_glasgow_bb.insert(dictionary)
            #youtube_col_sf_soc.insert(dictionary)
            #youtube_col_la_soc.insert(dictionary)
            #youtube_col_sf.insert(dictionary) 
            #youtube_col_la.insert(dictionary)
            #youtube_col_man_fb.insert(dictionary)
            #youtube_col_liv_fb.insert(dictionary)
            youtube_col_ed_fb.insert(dictionary)
            
            
            
        except:
            print("mongo error")
            pass
            
        
        videos.append("%s, (%s,%s)" % (video_result["snippet"]["title"],
                                  video_result["recordingDetails"]["location"]["latitude"],
                                  video_result["recordingDetails"]["location"]["longitude"]))

def meanLikes():
    
    for document in glasgow_cursor:
        pass
    
def meanComments():
    pass

def meanViews():
    pass
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='youtube')
    parser.add_argument("--q", help="Search term", default="football")
    #parser.add_argument("--location", help="Location", default="51.5074,-0.1278")  #london
    #parser.add_argument("--location", help="Location", default="55.8642, -4.2518") #glasgow
    #parser.add_argument("--location", help="Location", default="34.0522, -118.2437") #la
    #parser.add_argument("--location", help="Location", default="37.7749, -122.4194") #sf
    #parser.add_argument("--location", help="Location", default="53.4808, -2.2426") #manchester
    #parser.add_argument("--location", help="Location", default="53.4084, -2.9916") #liverpool
    parser.add_argument("--location", help="Location", default="55.9533, -3.1883") #edinburgh
    parser.add_argument("--location-radius", help="Location radius", default="10km")
    parser.add_argument("--max-results", help="Max results", default=50)
    args = parser.parse_args()
    youtube_search(args)
