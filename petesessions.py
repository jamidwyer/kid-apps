#!/usr/bin/python
import praw
import pdb
import re
import os


# Create the Reddit instance
reddit = praw.Reddit('bot1')

# and login
#reddit.login(REDDIT_USERNAME, REDDIT_PASS)

# Have we run this code before? If not, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If we have run the code before, load the list of posts we have replied to
else:
    # Read the file into a list and remove any empty values
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

subs = ['enoughtrumpspam', 'houstonchronauto', 'houston', 'texas', 'thenewsrightnow', 'political_revolution', 'bluemidterm2018', 'california_politics', 'politicaltweets', 'technology', 'autotldr', 'esist', 'keepournetfree', 'democrats', 'thehillauto', 'democracy', 'waexauto', 'unremovable', 'badgovnofreedom', 'thenewcoldwar', 'politicalvideo', 'autonewspaper', 'chapotraphouse', 'sandersforpresident', 'environment', 'keep_track', 'liberal', 'women', 'cornbreadliberals', 'greed', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'politicalrevolutionca', 'goodlongposts', 'theconstitution', 'reddit.com', 'wayofthebern', 'climate', 'cnet_all_rss', 'pancakepalpatine', 'nottheonion', 'skydtech', 'PoliticalVideos', 'huffpoauto']

# Get the top 100 values from our subreddit
subreddit = reddit.subreddit('indivisibleguide')
for submission in subreddit.hot(limit=500):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("pete sessions", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Colin Allred is running against Pete Sessions. \n\n Campaign site: https://www.colinallred.com/ \n\n Register to vote: http://www.votetexas.gov/register-to-vote/ \n\n Donate: https://secure.actblue.com/contribute/page/colinallred/ \n\n Facebook: https://www.facebook.com/ColinAllredTX/ \n\n Twitter: https://twitter.com/colinallredtx \n\n Allred wants grandparents with expired driver's licenses to be able to vote, supports universal pre-K, and thinks the money Sessions would spend on a border wall could be used better.\n\n I'm a bot and I'm learning. Let me know if I can do better.")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
