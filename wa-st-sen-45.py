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
            terms = ['manka dhingra', 'anonymously to derail politics in Washington state', 'state Senate candidate Englund is hot', 'Eastside Democrat into high-stakes Senate race', 'help get Democrats elected November 7th', 'next national special election clash', 'jinyoung', 'Trump fired up female candidacies', 'Race to decide if West Coast keeps its only GOP']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://weiapplets.sos.wa.gov/MyVoteOLVR/MyVoteOLVR) by October 30, 2017 \n\n"
        "Election Date: November 7, 2017 \n\n"

        "[**Manka Dhingra**](http://www.electmanka.com/) is running to represent Washington's 45th Senate District. \n\n"
        "[Donate](https://act.myngp.com/Forms/1478398861426297344) | "
        "[Reddit](https://www.reddit.com/r/MankaDhingra/) | "
        "[Facebook](https://www.facebook.com/electmanka/) | "
        "[Twitter](https://twitter.com/ElectManka) \n\n"
        "Dhingra supports public schools. \n\n\n"

        "[Map of Washington State Senate District 45](https://upload.wikimedia.org/wikipedia/commons/4/45/LD_45.pdf) \n\n"

        "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)")
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