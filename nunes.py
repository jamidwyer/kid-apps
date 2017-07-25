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

subs = ['california_politics', 'centralvalley', 'latimesauto', 'politicalrevolutionca', 'indepthstories', 'democrats', 'chapotraphouse', 'bluemidterm2018', 'enoughtrumpspam', 'liberal', 'political_revolution', 'keepournetfree', 'thehillauto', 'cornbreadliberals', 'esist', 'waexauto', 'unremovable', 'politicaltweets', 'thenewcoldwar', 'technology', 'autonewspaper', 'wayofthebern', 'sandersforpresident', 'autotldr', 'marchagainsttrump', 'politicalvideo', 'goodlongposts', 'badgovnofreedom', 'good_cake', 'democracy', 'fcc', 'netneutrality', 'worldnews', 'nottheonion', 'breakingnews24hr', 'newsbotbot', 'impeach_trump', 'fuckthealtright', 'environment', 'hotandtrending', 'keep_track', 'PoliticalVideos', 'climate', 'nofilternews', 'russialago', 'cnet_all_rss', 'women', 'cnnauto', 'huffpoauto', 'greed', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'stupid_watergate', 'trussiagate', '538auto', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'datauncensored', 'skydtech']

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=1000):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['devin nunes', 'rep. nunes', 'congressman nunes', 'rep nunes']
            for term in terms:
                 search(term, submission);

def search(term, submission):
            if re.search(term, submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://registertovote.ca.gov/) \n\n"
                    "[**Andrew Janz**](http://andrewjanzforcongress.org/) is running against Devin Nunes. \n\n"
                    "[Donate](https://secure.actblue.com/contribute/page/andrew-janz) | "
                    "[Facebook](https://www.facebook.com/andrewjanzforcongress/) | "
                    "[Twitter](https://twitter.com/janzforcongress) \n\n"
                    "Janz supports universal health care, protecting Medicare, renewable energy, campaign finance reform, and college affordability. \n\n\n"

                    "Map of California District 22: https://www.govtrack.us/congress/members/CA/22 \n\n"

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
