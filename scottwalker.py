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

local_subs = open("wisconsin.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['scott walker', 'governor walker', 'wisconsin governor', 'wi gov', 'wi governor\'s', 'Gerrymandering Is Still About Race', 'How Much Gerrymandering Is Too Much', 'Gorsuch was a pompous bore', 'Ginsburg Slaps Gorsuch in Gerrymandering Case', 'Return Control of Our Elections to the People', 'Did district lines rig Wisconsin elections', 'Redistricting Case That Could Remake American Politics', 'skeptical of partisan gerrymandering', 'Wisconsin\'s partisan gerrymander', 'Wisconsin Case Before Justices Could Reshape Redistricting', 'people prevented from voting in key swing state won by Trump', 'Cusp of Failing Before Our Eyes', 'state voter ID law confusion', 'Deterred Voters in Wisconsin', 'ID law kept up to 23,000 from voting', 'Wisconsin Strict ID Law', 'and Protection From Its Court System', 'under GOP health bill', 'site that critics call propaganda', 'Republican Governors Association', 'Republican Gov Association', 'lawmakers vote to pay Foxconn']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://myvote.wi.gov/en-us/registertovote) \n\n"
            "[**Andy Gronik**](https://www.andygronik.com) is running to be Governor of Wisconsin. \n\n"
            "[Donate](https://secure.actblue.com/donate/gronik-for-wisconsin) | "
            "[Facebook](https://www.facebook.com/AndyGronik) | "
            "[Twitter](https://twitter.com/AndyGronik) \n\n"
            "Gronik supports universal health care, public schools, affordable college, equal pay for equal work, and voting rights. \n\n\n"

            "[**Bob Harlow**](https://bobharlow.net/) is running to be Governor of Wisconsin. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/harlow-for-wisconsin) | "
            "[Facebook](https://www.facebook.com/HarlowForWisconsin/) | "
            "[Twitter](https://twitter.com/bobharlow_) \n\n"
            "Harlow supports universal health care and public schools. \n\n\n"

        "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

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

text_file.close()
local_subs.close()