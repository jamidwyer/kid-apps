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

local_subs = open("maine.dat", "r")
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
            terms = ['poliquin', 'me-2', 'ME-02']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.maine.gov/sos/cec/elec/voter-info/voterguide.html) \n\n"
            "[**Tim Rich**](http://richfortherestofus.com/) is running to represent Maine House District 2 in the United States Congress. \n\n"
            "[Donate](https://www.crowdpac.com/campaigns/304309/tim-rich-for-congress) | "
            "[Facebook](https://www.facebook.com/RichForTheRestOfUs/) | "
            "[Twitter](https://twitter.com/timothyarich) \n\n"
            "Rich supports universal health care, renewable energy, and raising the minimum wage. \n\n\n"

            "[**Jonathan Fulford**](http://fulfordforcongress.com/) is running to represent Maine House District 2 in the United States Congress. \n\n"
            "[Donate](https://act.myngp.com/Forms/578228833075727104) | "
            "[Facebook](https://www.facebook.com/FulfordForME/) | "
            "[Twitter](https://twitter.com/fulfordformaine) \n\n"
            "Fulford supports universal health care and renewable energy. \n\n\n"

            "[**Craig Olson**](http://craigforme2.com/) is running to represent Maine House District 2 in the United States Congress. \n\n"
            "[Donate](https://secure.actblue.com/donate/colson/) | "
            "[Facebook](https://www.facebook.com/CraigForME2/) | "
            "[Twitter](https://twitter.com/CraigForMe2) \n\n"
            "Olson supports universal health care and renewable energy. \n\n\n"

            "[Map of Maine District 2](https://www.govtrack.us/congress/members/ME/2) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

        submission.reply(text)
        print("Bot replying to : ", submission.title)

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