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

local_subs = open("washington.dat", "r")
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
            terms = ['reichert', 'dave reichert', 'rep. reichert', 'rep reichert', 'representative reichert', 'congressmen reichert', 'congressman reichert', 'wa-8', 'wa-08', '@davereichert', 'wa\'s 8th district' ]
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://weiapplets.sos.wa.gov/MyVoteOLVR/MyVoteOLVR) \n\n"
        "[**Tola Marts**](https://tola.nationbuilder.com/) is running against Dave Reichert. \n\n"
        "[Donate](https://secure.anedot.com/marts/donate) | "
        "[Facebook](https://www.facebook.com/electtolamarts/) | "
        "[Twitter](https://twitter.com/electtolamarts) \n\n"

        "Marts supports universal health care and affordable college.  \n\n"

        "[**Mona Das**](https://www.electmona.com/more-about-mona) is running against Dave Reichert. \n\n"
        "[Donate](https://secure.squarespace.com/commerce/donate?donatePageId=595b20538419c2e81ee2f471) | "
        "[Facebook](https://www.facebook.com/electmona/) | "
        "[Twitter](https://twitter.com/elect_mona) \n\n"

        "Das supports universal health care.  \n\n"

        "[Map of Washington District 8](https://www.google.com/maps/d/u/0/viewer?ll=47.59875500000003%2C-121.21215799999999&spn=2.222513%2C2.883911&hl=en&t=m&msa=0&z=8&source=embed&ie=UTF8&mid=1qzIBZU5QZgKWh_woys_JM2h5HqY) \n\n"

        "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)")
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