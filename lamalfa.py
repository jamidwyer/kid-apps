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

local_subs = open("california.dat", "r")
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
            terms = ['lamalfa', 'ca-01', 'cease-and-desist letter from his congressman', 'California GOP congressman gets an earful at town hall', '@replamalfa', 'OFF STAGE during OROVILLE Town Hall']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://registertovote.ca.gov/) by May 16, 2018 \n\n"
            "[Sign up to vote by mail](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply) \n\n\n"

            "[**Dennis Duncan**](https://www.dennis2018.com/) is running against Doug LaMalfa. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/dennis2018) | "
            "[Facebook](https://www.facebook.com/Dennis4district1/) | "
            "[Twitter](https://twitter.com/DennisCD01) \n\n"
            "Duncan supports Medicare for all, living wages, college affordability, renewable energy, and campaign finance reform.\n\n\n"

            "[**Jessica Holcombe**](https://jessicaforcongress.org/) is running against Doug LaMalfa. \n\n"
            "[Donate](https://www.crowdpac.com/campaigns/245830/progress-for-californias-1st-congressional-district) | "
            "[Facebook](https://www.facebook.com/Jessica-Holcombe-for-Congress-1775710765779809/) \n\n "
            "Holcombe supports universal health care, living wages, public schools, college affordability, and renewable energy.\n\n\n"

            "Primary Election: June 5, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of California District 1](https://www.govtrack.us/congress/members/CA/1) \n\n"

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