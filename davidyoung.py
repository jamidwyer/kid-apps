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
    for submission in subreddit.hot(limit=200):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['david young']
            for term in terms:
                 search(term, submission);

def search(term, submission):
            if re.search(term, submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://mymvd.iowadot.gov/Account/Login?ReturnUrl=%2fVoterRegistration) \n\n"
                    "[**Paul Knupp**](https://knuppforcongress.org/issues.html) is running against David Young. \n\n"
                    "[Donate](https://www.gofundme.com/knupp-for-congress) | "
                    "[Facebook](https://www.facebook.com/drpaulknupp) \n\n\n"

                    "Knupp supports universal health care, a living wage, affordable college, and funding the EPA and Planned Parenthood. \n\n\n"

                    "[**Cindy Axne**](https://cindyaxneforcongress.com/) is running against David Young. \n\n"
                    "[Donate](https://secure.actblue.com/donate/cindyaxneforcongress) | "
                    "[Facebook](https://www.facebook.com/CindyAxneForCongress/) | "
                    "[Twitter](https://twitter.com/Axne4Congress) \n\n\n"

                    "Map of Iowa District 3: https://www.govtrack.us/congress/members/IA/3 \n\n"

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
