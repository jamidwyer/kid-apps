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

local_subs = open("utah.dat", "r")
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
            terms = ['mia love', 'mia b. love', 'rep love', 'rep. love', 'representative love', 'congressman love', 'ut-04', 'ut-4', 'love\'s constituent meeting format', 'constituents say they were left off her invite list', 'Love has a new chief of staff', 'Love\'s not on board.', 'better way to talk with constituents']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://secure.utah.gov/voterreg/index.html) \n\n"
            "[**Tom Taylor**](https://www.tomforutah.com/issues.php) is running against Mia Love. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/thomastaylor) | "
            "[Facebook](https://www.facebook.com/TomForUtah/) | "
            "[Twitter](https://twitter.com/tomforutah) \n\n"

            "Taylor supports Medicare for all, public schools, renewable energy, and campaign finance reform.  \n\n\n"

            "[**Darlene McDonald**](https://darlenemcdonald.com/) is running against Mia Love. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/votedarlene) | "
            "[Facebook](https://www.facebook.com/Darlene4Congress/) | "
            "[Twitter](https://twitter.com/VoteDarlene) \n\n"

            "McDonald supports universal health care.  \n\n\n"

            "[**Marla Mott-Smith**](http://marla4congress.com/) is running against Mia Love. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/marla4congress) | "
            "[Facebook](https://www.facebook.com/mlmsb/) | "
            "[Twitter](https://twitter.com/marlamottsmith) \n\n"

            "Mott-Smith supports campaign finance reform and LGBT equality. \n\n\n"

            "[Map of Utah District 4](https://www.govtrack.us/congress/members/UT/4) \n\n"

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