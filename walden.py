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

subs = ['cascadia', 'portland', 'oregon', 'bend', 'oregon2nd', 'indepthstories', 'democrats', 'chapotraphouse', 'bluemidterm2018', 'enoughtrumpspam', 'liberal', 'political_revolution', 'keepournetfree', 'thehillauto', 'cornbreadliberals', 'thenewcoldwar', 'esist', 'waexauto', 'unremovable', 'good_cake', 'technology', 'autonewspaper', 'wayofthebern', 'sandersforpresident', 'autotldr', 'marchagainsttrump', 'politicalvideo', 'goodlongposts', 'badgovnofreedom', 'libs', 'democracy', 'stupid_watergate', 'fcc', 'netneutrality', 'worldnews', 'nottheonion', 'newsbotbot', 'impeach_trump', 'fuckthealtright', 'collapse', 'environment', 'inthenews', 'hotandtrending', 'keep_track', 'thecolorisblue', 'PoliticalVideos', 'climate', 'cnet_all_rss', 'women', 'newsy', 'cnnauto', 'tytpolitics', 'huffpoauto', 'cbsauto', 'greed', 'watchingcongress', 'restorethefourth', 'trussiagate', '538auto', 'theconstitution', 'pancakepalpatine', 'geprnotes', 'progressive', 'datauncensored', 'skydtech', 'portland', 'oregon']

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['greg walden', '@repgregwalden', 'rep. walden', 'congressman walden', 'rep walden']
            for term in terms:
                 search(term, submission);

def search(term, submission):
            if re.search(term, submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://secure.sos.state.or.us/orestar/vr/register.do) \n\n"
                    "[**Ross Wordhouse**](http://rosswordhouse.com/washington-table-flipper/) is running against Greg Walden. \n\n"
                    "[Donate](https://secure.actblue.com/donate/wordhouse) | "
                    "[Facebook](https://www.facebook.com/wordhouseforcongress/) \n\n "
                    "Wordhouse supports universal health care, renewable energy, public schools, campaign finance reform, affordable college, and equal pay for equal work. \n\n\n"

                    "[**Jim Crary**](https://crary4congress.com/) is running against Greg Walden. \n\n"
                    "[Donate](https://secure.actblue.com/contribute/page/crary2018) | "
                    "[Facebook](https://www.facebook.com/crary4congress) | "
                    "[Twitter](https://twitter.com/crary4congress) \n\n"
                    "Crary supports universal health care, renewable energy, campaign finance reform, LGBTQ equality, and protecting Social Security. \n\n\n"

                    "[Map of Oregon District 2](https://www.govtrack.us/congress/members/OR/2) \n\n"

                    "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
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
