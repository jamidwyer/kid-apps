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

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=1000):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['john culberson', 'rep. culberson', 'congressman culberson', 'rep culberson']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("James Cargas is running against John Culberson. \n\n"
            "Campaign website: http://www.jamescargas.com/on-the-issues/ \n\n"
             "Register to vote: http://www.votetexas.gov/register-to-vote/ \n\n"
             "Donate: https://secure.actblue.com/contribute/page/james-cargas-1 \n\n"
             "Facebook: https://www.facebook.com/Cargas7/ \n\n"
             "Twitter: https://twitter.com/Cargas7 \n\n"
             "Cargas supports renewable energy, science, universal pre-K, public schools, affordable college, LGBTQ "
             "equality, background checks on every gun sale, and the Voting Rights Act. \n\n\n"

            "Map of Texas District 7: https://www.govtrack.us/congress/members/TX/7 \n\n "

            "^(I'm a bot and I'm learning. Let me know if I can do better. It's a lot of "
            "work to add all this info, but if you prefer a different candidate, let me know, and I'll add them.)")

        submission.reply(text)
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
