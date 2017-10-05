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

local_subs = open("minnesota.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://mnvotes.sos.state.mn.us/VoterRegistration/VoterRegistrationMain.aspx) \n\n"
            "[**Brian Santa Maria**](https://www.briansantamariaforcongress.com/) is running against Erik Paulsen. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/bsm) | "
            "[Facebook](https://www.facebook.com/BrianSantaMariaforCongress/) | "
            "[Twitter](https://twitter.com/briansantamaria) \n\n"
            "Santa Maria supports universal health care, paid maternity leave, and renewable energy. \n\n\n"

            "[**Dean Phillips**](https://www.phillipsforcongress.org/) is running against Erik Paulsen. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/deanforcongress) | "
            "[Facebook](https://www.facebook.com/deanphillipsforcongress) | "
            "[Twitter](https://twitter.com/deanbphillips) \n\n"
            "Phillips supports net neutrality. \n\n\n"

            "Map of Minnesota District 3: https://www.govtrack.us/congress/members/MN/3 \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people.)")

        print("Bot replying to : ", submission.title)
        submission.reply(text)

        # Store the current id into our list
        posts_replied_to.append(submission.id)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['erik paulsen', 'rep. paulsen', 'rep paulsen']
            for term in terms:
                 search(term, submission);

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
