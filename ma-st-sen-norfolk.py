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

local_subs = open("massachusetts.dat", "r")
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
            terms = ['paul feeney', '@PaulieFeeney', 'james timilty', 'Michael Berry', 'Jacob Ventura', 'Harry Brousaides', 'Tim Hempton', 'Joe Shortsleeve', 'Election Night September 19th']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register to Vote &#9733;&#9733;&#9733;](https://www.sec.state.ma.us/OVR/) by September 27, 2017 \n\n"
            "General Election: October 17, 2017 \n\n"
            "[Find your polling place](http://www.sec.state.ma.us/WhereDoIVoteMA/bal/MyElectionInfo.aspx)\n\n"

            "[**Paul Feeney**](http://www.votefeeney.com/) is running to represent the Bristol & Norfolk District. \n\n"
            "[Facebook](https://www.facebook.com/PaulFeeneyforStateSenate/) | "
            "[Twitter](https://twitter.com/PaulieFeeney) | "
            "[Volunteer](http://www.votefeeney.com/join) | "
            "[Donate](https://secure.actblue.com/contribute/page/votefeeney) \n\n"

            "Feeney supports renewable energy, public schools, affordable college, universal pre-K, a living wage, and equal pay for equal work. \n\n\n"

            "[Map of Bristol & Norfolk District](https://statisticalatlas.com/state-upper-legislative-district/Massachusetts/Bristol-and-Norfolk-District/Overview) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better.)")
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