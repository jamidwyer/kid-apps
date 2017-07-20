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

subs = ['enoughtrumpspam', 'miami', 'miamiheraldauto', 'political_revolution', 'worldnews', 'bluemidterm2018', 'politicaltweets', 'technology', 'impeach_trump', 'autotldr', 'esist', 'indepthstories', 'keepournetfree', 'democrats', 'thehillauto', 'democracy', 'waexauto', 'unremovable', 'badgovnofreedom', 'thenewcoldwar', 'politicalvideo', 'autonewspaper', 'chapotraphouse', 'sandersforpresident', 'environment', 'keep_track', 'liberal', 'women', 'cornbreadliberals', 'greed', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'goodlongposts', 'theconstitution', 'reddit.com', 'wayofthebern', 'climate', 'cnet_all_rss', 'pancakepalpatine', 'nottheonion', 'skydtech', 'PoliticalVideos', 'huffpoauto', 'geprnotes', 'UMukhasimAutoNews', 'trussiagate']

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.top('month'):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            if re.search("balart", submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://dos.myflorida.com/elections/for-voters/voter-registration/register-to-vote-or-update-your-information/) \n\n"
                "[**Alina Valdes**](http://alinavaldesforcongress.com/) is running against Mario Diaz-Balart. \n\n"
                "[Donate](https://secure.actblue.com/contribute/page/alina-valdes-1) | [Facebook](https://www.facebook.com/alinavaldesforcongress/) | [Twitter](https://twitter.com/DrAlinaValdes) \n\n"
                "Valdes supports Medicare for all, public schools. \n\n\n "

                "Map of Florida District 25: https://www.govtrack.us/congress/members/FL/25 \n\n"

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
