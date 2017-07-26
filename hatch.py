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

subs = ['enoughtrumpspam', 'unbubbledpolitics', 'sltribauto', 'deseretauto', 'utahpoliticians', 'thenewsrightnow', 'political_revolution', 'bluemidterm2018', 'technology', 'autotldr', 'esist', 'keepournetfree', 'democrats', 'thehillauto', 'democracy', 'waexauto', 'unremovable', 'badgovnofreedom', 'thenewcoldwar', 'politicalvideo', 'autonewspaper', 'chapotraphouse', 'sandersforpresident', 'environment', 'keep_track', 'liberal', 'women', 'cornbreadliberals', 'greed', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'politicalrevolutionca', 'goodlongposts', 'theconstitution', 'reddit.com', 'wayofthebern', 'climate', 'cnet_all_rss', 'pancakepalpatine', 'nottheonion', 'skydtech', 'PoliticalVideos', 'huffpoauto']

# Get the top 5 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.top('month'):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['orrin hatch', 'sen. hatch', 'senator hatch']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://secure.utah.gov/voterreg/index.html) \n\n"
        "[**Jenny Wilson**](http://wilsonforsenate.com/) is running against Orrin Hatch. \n\n "
        "[Donate](https://www.crowdpac.com/candidates/58d92c47d9e704560d2afff1/jenny-wilson) | "
        "[Facebook](https://www.facebook.com/WilsonForSenate/) | "
        "[Twitter](https://twitter.com/jennywilsonut) \n\n "

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
