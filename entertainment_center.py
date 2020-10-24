# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 02:01:58 2020

@author: asumo
"""

import movie_files as media
import index

#toy_story=media.Movie("Toy Story","Toys Come to Life","Toy StoryPostal Link","Toy Story Youtube Link")
the_invisible_man=media.Movie(
    
    "THE INVISIBLE MAN",
    "Cecilia’s (Elisabeth Moss) sanity begins to unravel as she desperately tries to prove she is being hunted by someone only she can see.",
    "https://cdn.moviestillsdb.com/storage/posters/86/1051906_100.jpg",
    "https://www.youtube.com/watch?v=WO_FJdiY9dA",
    ) 


#print("Title :",toy_story.title)
#print("Story_Info :",toy_story.storyline)
#print("Postal Image :",toy_story.poster_image_url)
#toy_story.show_trailer()
    
avatar =media.Movie(
    "AVATAR",
    "A story about the alien of the planet",
    "https://cdn.moviestillsdb.com/storage/posters/5c/499549_100.jpg",
    "https://www.youtube.com/watch?v=6ziBFh3V1aM",
       )    
    
print("Title :",avatar.title)
print("Story_Info :",avatar.storyline)
print("Postal Image :",avatar.poster_image_url)
#print("Movie Trailor:",avatar.trailer_youtube_url)
#avatar.show_trailer()

forrest_gump =media.Movie(
    "FORREST GUMP",
    "Story: A poor, unemployed family play out a well-laid plan to secure jobs for themselves in a wealthy household, only to unleash a series of unexpected events",
    "https://cdn.moviestillsdb.com/storage/posters/88/109830_100.jpg",
    "https://www.youtube.com/watch?v=uPIEn0M8su0",
       )    


parasite =media.Movie(
    "PARASITE",
    "Forrest, a man with low IQ, recounts the early years of his life when he found himself in the middle of key historical events. All he wants now is to be reunited with his childhood sweetheart, Jenny",
    "https://cdn.moviestillsdb.com/storage/posters/dc/6751668_100.jpg",
    "https://www.youtube.com/watch?v=DxLY268mtx0",
       )    

movie_1917 =media.Movie(
    "1917",
    "Story: Two young British soldiers, Schofield (George MacKay) and Blake (Dean-Charles Chapman), are given an impossible task during World War I",
    "https://cdn.moviestillsdb.com/storage/posters/88/8579674_100.jpg",
    "https://www.youtube.com/watch?v=gZjQROMAh_s",
       )    


the_outpost =media.Movie(
    "THE OUTPOST",
    "Story: A handful of American soldiers take hundreds of Taliban terrorists head-on from the remote combat outpost, located deep in the Afghanistan valley. The Battle of Kamdesh became the bloodiest American engagement of the Afghanistan War in 2009 and one of the most heroic tales of bravery",
    "https://cdn.moviestillsdb.com/storage/posters/10/7612548_100.jpg",
    "https://www.youtube.com/watch?v=Kp9JghhGPao",
       )    


tenet  =media.Movie(
    "TENET",
    "Story: A time travelling protagonist rises to the occasion and risks his own life to stop the inevitable catastrophe that could be bigger than World War III and nuclear holocaust. Will he make it ‘back in time’ to save the world?",
    "https://cdn.moviestillsdb.com/storage/posters/f5/6723592_100.jpg",
    "https://www.youtube.com/watch?v=LdOM0x0XDMo",
       )    


little_women  =media.Movie(
    "LITTLE WOMEN",
    "STORY: Based on Loiusa May Alcott’s classic novel with the same name, Little Women is a timeless tale of love, life and ambitions.",
    "https://cdn.moviestillsdb.com/storage/posters/74/6853528_100.jpg",
    "https://www.youtube.com/watch?v=LdOM0x0XDMo",
       )    



richard_jewell =media.Movie(
    "RICHARD JEWELL",
    "STORY: A security guard becomes a hero after finding an explosive device, but soon comes under scrutiny by the FBI as a prime suspect.",
    "https://cdn.moviestillsdb.com/storage/posters/4f/3513548_100.jpg",
    "https://www.youtube.com/watch?v=gSMxBLlA8qY",
       )    







movies=[the_invisible_man,avatar,forrest_gump,parasite,movie_1917,the_outpost,tenet,little_women,richard_jewell]
index.open_movies_page(movies)