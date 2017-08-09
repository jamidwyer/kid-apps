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

subs = ['iowa', 'indepthstories', 'democrats', 'chapotraphouse', 'bluemidterm2018', 'enoughtrumpspam', 'liberal', 'political_revolution', 'keepournetfree', 'thehillauto', 'cornbreadliberals', 'thenewcoldwar', 'esist', 'waexauto', 'unremovable', 'good_cake', 'technology', 'autonewspaper', 'wayofthebern', 'sandersforpresident', 'autotldr', 'marchagainsttrump', 'politicalvideo', 'goodlongposts', 'badgovnofreedom', 'libs', 'democracy', 'stupid_watergate', 'fcc', 'netneutrality', 'worldnews', 'nottheonion', 'newsbotbot', 'impeach_trump', 'fuckthealtright', 'collapse', 'environment', 'hotandtrending', 'keep_track', 'thecolorisblue', 'PoliticalVideos', 'climate', 'cnet_all_rss', 'women', 'newsy', 'cnnauto', 'tytpolitics', 'huffpoauto', 'cbsauto', 'greed', 'watchingcongress', 'restorethefourth', 'indivisibleguide', 'trussiagate', '538auto', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'progressive', 'datauncensored', 'skydtech']

# Get the top 200 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['travis harris', 'Iowa State House District 82', 'Iowa House special election', 'curt hanson']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.selftext, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; VOTE &#9733;&#9733;&#9733;](https://www.millerforiowahouse.com/vote) \n\n"
            "[**Phil Miller**](https://www.millerforiowahouse.com/) is running to represent Iowa State House District 82. \n\n"
            "[Phonebank](https://www.millerforiowahouse.com/call) | "
            "[Donate](https://secure.actblue.com/donate/phil-miller-for-iowa-house-1) | "
            "[Facebook](https://www.facebook.com/millerforiowahouse/) \n\n"

            "Miller supports public schools and a living wage. \n\n\n"

            "Map of [Iowa State House District 82](https://static.wixstatic.com/media/401cce_84d424e119b6487ea9c5d4b3db9e50c3~mv2_d_1650_1275_s_2.jpg/v1/fill/w_1098,h_848,al_c,q_85,usm_0.66_1.00_0.01/401cce_84d424e119b6487ea9c5d4b3db9e50c3~mv2_d_1650_1275_s_2.webp) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better.)")
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
