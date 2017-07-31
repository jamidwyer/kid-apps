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

subs = ['modesto', 'orangecounty', 'california_politics', 'politicalrevolutionca', 'politicalcalifornia', '2018elections', 'indepthstories', 'democrats', 'chapotraphouse', 'bluemidterm2018', 'enoughtrumpspam', 'liberal', 'political_revolution', 'thehillauto', 'waexauto', 'unremovable', 'politicaltweets', 'thenewcoldwar', 'technology', 'autonewspaper', 'autotldr', 'esist', 'marchagainsttrump', 'politicalvideo', 'keepournetfree', 'goodlongposts', 'badgovnofreedom', 'good_cake', 'democracy', 'fcc', 'worldnews', 'nottheonion', 'wayofthebern', 'sandersforpresident', 'impeach_trump', 'fuckthealtright', 'environment', 'keep_track', 'PoliticalVideos', 'climate', 'cnet_all_rss', 'women', 'cornbreadliberals', 'greed', 'huffpoauto', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'trussiagate', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'skydtech']

# Get the top 100 values from our subreddit
subreddit = reddit.subreddit('california_politics')
for submission in subreddit.hot(limit=500):
    #print(submission.title)

    # If we haven't replied to this post before
    if submission.id not in posts_replied_to:

        # Do a case insensitive search
        if re.search("jeff denham", submission.title, re.IGNORECASE):
            # Reply to the post
            submission.reply("Dotty Nygard is running against Jeff Denham. \n\n Campaign site: https://www.dottynygardforcongress.com/ \n\n Register to vote: http://registertovote.ca.gov/ \n\n Donate: https://secure.actblue.com/contribute/page/dottyforcongress \n\n Facebook: https://www.facebook.com/DottyForCongressCD10/ \n\n Twitter: https://twitter.com/Dotty4Congress \n\n Nygard supports single-payer health care, renewable energy, campaign finance reform, net neutrality, and college affordability.\n\n I'm a bot and I'm learning. Let me know if I can do better.")
            print("Bot replying to : ", submission.title)

            # Store the current id into our list
            posts_replied_to.append(submission.id)

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
