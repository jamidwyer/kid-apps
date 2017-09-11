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

subs = ['jerseycity', 'frisson', 'blackladies', 'trumpeach', 'themajorityreport', 'redditforgrownups', 'nursing', 'enoughtrumpspam', 'badlawyer', 'newjersey', 'ecointernet', 'political_revolution', 'worldnews', 'bluemidterm2018', 'politicaltweets', 'technology', 'impeach_trump', 'autotldr', 'esist', 'indepthstories', 'keepournetfree', 'democrats', 'thehillauto', 'democracy', 'waexauto', 'unremovable', 'badgovnofreedom', 'thenewcoldwar', 'politicalvideo', 'autonewspaper', 'chapotraphouse', 'sandersforpresident', 'environment', 'keep_track', 'liberal', 'women', 'cornbreadliberals', 'greed', 'watchingcongress', 'restorethefourth', 'libs', 'indivisibleguide', 'goodlongposts', 'theconstitution', 'reddit.com', 'wayofthebern', 'climate', 'cnet_all_rss', 'pancakepalpatine', 'nottheonion', 'skydtech', 'PoliticalVideos', 'huffpoauto', 'geprnotes', 'UMukhasimAutoNews', 'trussiagate']

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['thomas macarthur', 'tom macarthur', 'rep. macarthur', 'rep macarthur', 'representative macarthur', 'congressman macarthur', 'half of Republicans have yet to hold a public town hall']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.state.nj.us/state/elections/voting-information.html) \n\n"
        "[**Andy Kim**](https://www.andykimforcongress.com/) is running against Tom Macarthur. \n\n"
        "[Donate](https://secure.actblue.com/donate/andykim) | "
        "[Reddit](https://www.reddit.com/r/AndyKim2018/) | "
        "[Facebook](https://www.facebook.com/AndyKimNJ) | "
        "[Twitter](https://twitter.com/AndyKimNJ) \n\n\n"

        "[Map of New Jersey District 3](https://www.govtrack.us/congress/members/NJ/3) \n\n"

        "^(I'm a bot and I'm learning. Let me know if I can do better. It's a lot of "
        "work to add all this info, but if you prefer a different candidate, let me know, and I'll add them.)")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
