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

subs = ['losangeles', 'enoughtrumpspam', 'orangecounty', 'political_revolution', 'worldnews', 'bluemidterm2018', 'california_politics', 'politicaltweets', 'technology', 'impeach_trump', 'autotldr', 'esist', 'indepthstories', 'keepournetfree', 'democrats', 'thehillauto', 'democracy', 'waexauto', 'unremovable', 'badgovnofreedom', 'thenewcoldwar', 'politicalvideo', 'autonewspaper', 'chapotraphouse', 'sandersforpresident', 'environment', 'keep_track', 'liberal', 'women', 'cornbreadliberals', 'greed', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'politicalrevolutionca', 'goodlongposts', 'theconstitution', 'reddit.com', 'wayofthebern', 'climate', 'cnet_all_rss', 'pancakepalpatine', 'nottheonion', 'skydtech', 'PoliticalVideos', 'huffpoauto', 'geprnotes']

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['ed royce', 'rep. royce', 'congressman royce', 'rep royce']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://registertovote.ca.gov/) \n\n"
            "[**Mai Khanh Tran**](https://doctran2018.com/) is running against Ed Royce. \n\n"
            "[Donate](https://secure.actblue.com/donate/drtranforcongress) | "
            "[Facebook](https://www.facebook.com/DocTran2018/) | "
            "[Twitter](https://twitter.com/DocTran2018) \n\n"
            "Tran supports universal health care coverage and Planned Parenthood. \n\n\n"

            "[**Phil Janowicz**](http://philforhouse.com/#issues) is running against Ed Royce. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/phil) | "
            "[Facebook](https://www.facebook.com/philforhouse) | "
            "[Twitter](https://twitter.com/PhilforHouse) \n\n"
            "Janowicz supports renewable energy, living wages, LGBTQ equality, equal pay for equal work, and increasing funding for science.\n\n"

            "Map of California District 39: https://www.govtrack.us/congress/members/CA/39 \n\n"

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
