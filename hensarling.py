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

local_subs = open("texas.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['hensarling', 'Naming and Shaming', 'Four Texas House Members Voted Against Harvey Relief', 'Texas Republican vows to fight for flood insurance overhaul', 'The House just passed the massive Trump-Pelosi-Schumer deal', 'Harvey aid package to Trump despite objections from conservatives', 'Texas Republicans voted against Harvey relief']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.votetexas.gov/register-to-vote/) by October 5, 2018 \n\n"

        "[**Dan Wood**](https://www.votedanwood.com/) is running against Jeb Hensarling. \n\n"
        "[Facebook](https://www.facebook.com/votedanwood/) | "
        "[Twitter](https://twitter.com/danwood2018) | "
        "[Volunteer](https://www.votedanwood.com/volunteer) | "
        "[Donate](https://www.crowdpac.com/campaigns/192921/dan-wood-for-congress-tx-5th-district) \n\n"

        "Wood supports universal health care, living wages, protecting Medicare, equal pay for equal work, and campaign finance reform.  \n\n"

        "[Map of Texas District 5](https://www.govtrack.us/congress/members/TX/5) \n\n"

        "General Election: November 6, 2018 \n\n"
        "[Find your polling place](https://www.rockthevote.com/get-informed/elections/find-your-polling-place/) \n\n"

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