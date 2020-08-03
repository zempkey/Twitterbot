"""Currently replies with a random bird picture and it's respective fact
to a tweet on authenticated users homepage. It is called whenever a
post uses the word bird. Just needs to be adjusted to scan and post
on other profiles. It also runs kinda slow."""

import tweepy
import random
import json

# _____ BEFORE ______
# def OAuth(path_to_cred_file):
#     try:
#         with open(path_to_cred_file, encoding='utf-8') as json_file:
#             creds = (json.load(json_file))
#         auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
#         auth.set_access_token(creds['access_token'], creds['access_token_secret'])
#         return auth
#     except tweepy.TweepError as e:
#         return e.reason, 'They done blocked Ya!'


# def bird_fct_maker(): 
#     # create list of media id lists (each containing one id)
#     mourn = [api.media_upload('Mourning_Dove.jpg').media_id] 
#     osprey = [api.media_upload('Osprey.jpg').media_id]
#     rivoli = [api.media_upload('Rivoli\'s_Hummingbird.jpg').media_id]
#     scaled = [api.media_upload('Scaled_Quail.jpg').media_id]
#     whip = [api.media_upload('whip-poor-will.jpg').media_id]
#     media_ids = [scaled, mourn, whip, rivoli, osprey]

#     # iterate over text file and produce a list of fact strings
#     fact_strings = []
#     with open('arizona_bird_facts.txt') as fact_sheet:
#         for line in fact_sheet.readlines():
#             fact, bib = line.split(',')
#             fact_strings.append(fact)
#     return fact_strings, media_ids

# def fact_zipper():
#     # random list element generator
#     fact_list, media_list = bird_fct_maker()
#     numb = random.randint(0, 4)
#     fact = fact_list[numb]
#     image = media_list[numb]
#     return fact, image

# if __name__ == '__main__': 
#     path = "C:/Users/Workin'/Documents/Docs/TBot_AuthKeys.json"
#     oath = OAuth(path)
#     api = tweepy.API(oauth)
#     for s in tweepy.Cursor(api.user_timeline).items():
#         s_txt = s.text
#         s_id = s.id
#         if ' bird' in s_txt:
#             print('Got em')
#             fct, img = fact_zipper()
#             # api.update_status(fct, media_ids=img, in_reply_to_status_id=s_id)

# Original code is preserved above for reference.


def OAuth(path_to_cred_file):
    try:
        with open(path_to_cred_file, encoding='utf-8') as json_file:
            creds = (json.load(json_file))
        auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
        auth.set_access_token(creds['access_token'], creds['access_token_secret'])
        return auth
    except tweepy.TweepError as e:
        return e.reason, 'They done blocked Ya!'


def bird_fct_maker(api):
    """
    create list of media id lists (each containing one id)
        params:  api - a Tweepy api object
        returns: list of fact strings and media_ids as a tuple
    """ 
    mourn = [api.media_upload('Mourning_Dove.jpg').media_id] #
    osprey = [api.media_upload('Osprey.jpg').media_id]
    rivoli = [api.media_upload('Rivoli\'s_Hummingbird.jpg').media_id]
    scaled = [api.media_upload('Scaled_Quail.jpg').media_id]
    whip = [api.media_upload('whip-poor-will.jpg').media_id]
    media_ids = [scaled, mourn, whip, rivoli, osprey]

    # iterate over text file and produce a list of fact strings
    fact_strings = []
    with open('arizona_bird_facts.txt') as fact_sheet:
        for line in fact_sheet.readlines():
            fact, bib = line.split(',')
            fact_strings.append(fact)
    return fact_strings, media_ids


def fact_zipper(fact_list, media_list):
    # random list element generator    
    numb = random.randint(0, 4)
    fact = fact_list[numb]
    image = media_list[numb]
    return fact, image


if __name__ == '__main__': 
    path = "C:/Users/Workin'/Documents/Docs/TBot_AuthKeys.json"
    oauth = OAuth(path)
    api = tweepy.API(oauth) 
    for s in tweepy.Cursor(api.user_timeline).items():
        s_txt = s.text
        s_id = s.id
        if ' bird' in s_txt:
            print('Got em')
            fact_list, media_list = bird_fct_maker(api)
            fct, img = fact_zipper(fact_list, media_list) # takes fact_list and media list as argument
            api.update_status(fct, media_ids=img, in_reply_to_status_id=s_id)
    
