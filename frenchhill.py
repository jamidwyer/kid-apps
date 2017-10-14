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

local_subs = open("arkansas.dat", "r")
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
            terms = ['french hill', 'ar-02', 'ar-2', 'rep. hill', 'rep hill', 'representative hill', 'congressman hill']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.kdor.ks.gov/apps/voterreg/default.aspx) by July 17, 2018 \n\n"
            "[Sign up to vote by mail](http://www.kssos.org/forms/elections/AV1.pdf) \n\n\n"

            "[**Robb Ryerse**](http://robb2018.com) is running against Steve Womack. \n\n"

            "[Donate](https://www.crowdpac.com/campaigns/244359/robb-ryerse-for-congress) | "
            "[Facebook](https://www.facebook.com/robb2018/) | "
            "[Twitter](https://twitter.com/robb2018) \n\n"

            "Ryerse supports universal health care, renewable energy, LGBTQ equality, and affordable college. \n\n\n"

            "[**Josh Mahony**](https://joshuamahony.com/) is running against Steve Womack. \n\n"
            "[Donate](https://secure.actblue.com/donate/mahony) | "
            "[Facebook](https://www.facebook.com/mahonyarkansas/) | "
            "[Twitter](https://twitter.com/joshuamahony?lang=en) \n\n\n"

            "Primary Election: August 7, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of Arkansas District 3](https://www.govtrack.us/congress/members/AR/3) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better.)")

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

text_file.close()
local_subs.close()