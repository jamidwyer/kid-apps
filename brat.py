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

subs = ['atheism', 'virginiapolitics', 'virginia', 'uspolitics', 'lgbtnews', 'atheismrebooted', 'enoughlibertarianspam', 'conspiratard', 'rva', 'indepthstories', 'democrats', 'chapotraphouse', 'bluemidterm2018', 'enoughtrumpspam', 'liberal', 'political_revolution', 'keepournetfree', 'thehillauto', 'cornbreadliberals', 'thenewcoldwar', 'esist', 'waexauto', 'unremovable', 'good_cake', 'technology', 'autonewspaper', 'wayofthebern', 'sandersforpresident', 'autotldr', 'marchagainsttrump', 'politicalvideo', 'goodlongposts', 'badgovnofreedom', 'libs', 'democracy', 'stupid_watergate', 'fcc', 'netneutrality', 'worldnews', 'nottheonion', 'newsbotbot', 'impeach_trump', 'fuckthealtright', 'collapse', 'environment', 'hotandtrending', 'keep_track', 'thecolorisblue', 'PoliticalVideos', 'climate', 'cnet_all_rss', 'women', 'newsy', 'cnnauto', 'tytpolitics', 'huffpoauto', 'cbsauto', 'greed', 'watchingcongress', 'restorethefourth', 'indivisibleguide', 'trussiagate', '538auto', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'progressive', 'datauncensored', 'skydtech', 'gogopgo']

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=500):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['dave brat', 'rep. brat', 'congressman brat', 'rep brat']
            for term in terms:
                 search(term, submission);

def search(term, submission):
            if re.search(term, submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.elections.virginia.gov/citizen-portal/index.html) \n\n"
                    "[**Eileen Bedell**](https://www.bedellforvirginia.com/issues) is running against Dave Brat. \n\n"
                    "[Donate](https://secure.actblue.com/contribute/page/bedell-for-virginia--inc-1) | "
                    "[Facebook](https://www.facebook.com/EileenBedellforVirginia/) | "
                    "[Twitter](https://twitter.com/BedellforVA) \n\n"

                    "Bedell supports universal health care, renewable energy, living wages, and LGBTQ equality.  \n\n"

                    "Map of Virginia District 7: https://www.govtrack.us/congress/members/VA/7 \n\n"

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
