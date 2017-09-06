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

subs = ['SouthCarolinaPolitics', 'russialago', 'worldpolitics', 'southcarolina', 'anythinggoesnews', 'greenville', 'thenewsrightnow', 'occupy', 'newsofthestupid', 'democrats', 'chapotraphouse', 'bluemidterm2018', 'enoughtrumpspam', 'liberal', 'political_revolution', 'keepournetfree', 'thehillauto', 'cornbreadliberals', 'thenewcoldwar', 'esist', 'waexauto', 'unremovable', 'good_cake', 'technology', 'autonewspaper', 'wayofthebern', 'sandersforpresident', 'autotldr', 'marchagainsttrump', 'politicalvideo', 'goodlongposts', 'badgovnofreedom', 'libs', 'democracy', 'stupid_watergate', 'fcc', 'netneutrality', 'worldnews', 'nottheonion', 'BreakingNews24hr', 'newsbotbot', 'impeach_trump', 'fuckthealtright', 'collapse', 'environment', 'inthenews', 'hotandtrending', 'keep_track', 'thecolorisblue', 'PoliticalVideos', 'climate', 'cnet_all_rss', 'women', 'newsy', 'cnnauto', 'tytpolitics', 'huffpoauto', 'cbsauto', 'greed', 'watchingcongress', 'trussiagate', '538auto', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'progressive', 'datauncensored', 'skydtech']

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['gowdy']
            for term in terms:
                 search(term, submission);

def search(term, submission):
            if re.search(term, submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://info.scvotes.sc.gov/eng/ovr/start.aspx) \n\n"
                    "[**Chris Fedalei**](http://www.votefedalei.com/) is running against Trey Gowdy. \n\n"
                    "[Donate](https://scdp.ngpvanhost.com/form/3838457334105966592) | "
                    "[Facebook](https://www.facebook.com/votefedalei) | "
                    "[Twitter](https://twitter.com/VoteFedalei) \n\n"
                    "Fedalei supports protecting Social Security. \n\n\n"

                    "Map of South Carolina District 4: https://www.govtrack.us/congress/members/SC/4 \n\n"

                    "^(I'm a bot and I'm learning. Let me know if I can do better. It's a lot of "
                    "work to add all this info, but if you prefer a different candidate, let me know, and I'll add them.)")
                print("Bot replying to : ", submission.title)
                submission.reply(text)

                # Store the current id into our list
                posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
