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

subs = ['politicalrevolutionca', 'california_politics', 'politicalcalifornia', 'bluemidterm2018', 'indepthstories', 'democrats', 'chapotraphouse', 'enoughtrumpspam', 'keepournetfree', 'politicalvideo', 'wayofthebern', 'impeach_trump', 'russialago', 'liberal', 'tytpolitics', 'political_revolution', 'thehillauto', 'cornbreadliberals', 'thenewcoldwar', 'esist', 'waexauto', 'unremovable', 'good_cake', 'technology', 'autonewspaper', 'sandersforpresident', 'autotldr', 'marchagainsttrump', 'goodlongposts', 'badgovnofreedom', 'libs', 'stupid_watergate', 'democracy', 'fcc', 'worldnews', 'nottheonion', 'breakingnews24hr', 'newsbotbot', 'fuckthealtright', 'environment', 'inthenews', 'hotandtrending', 'UMukhasimAutoNews', 'keep_track', 'PoliticalVideos', 'climate', 'cnet_all_rss', 'women', 'greed', 'huffpoauto', 'watchingcongress', 'restorethefourth', 'trussiagate', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'skydtech']

# Get the top 100 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit('california')
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            if re.search("valadao", submission.title, re.IGNORECASE):
                # Reply to the post
                submission.reply("Emilio Huerta is running against David Valadao. \n\n Campaign site: http://www.huertaforcongress.com/ \n\n Register to vote: http://registertovote.ca.gov/ \n\n I'm a bot and I'm learning. Let me know if I can do better.")
                print("Bot replying to : ", submission.title)

                # Store the current id into our list
                posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
