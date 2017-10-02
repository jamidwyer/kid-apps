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
            terms = ['letitia plummer', 'pete olson', 'rep. olson', 'rep olson', 'representative olson', 'congressman olson', 'tx-22', 'tx22', 'A black, female politician\'s AMA was overrun with terrible comments', 'shitty dude really triggered all the Diggler boys out there', 'A TOTALLY NOT SEXIST sub, a woman running for office, a custody nightmare. AMA! This should go great!', 'Woman running for Congress holds AMA, comments make clear that this world can only be cleansed with fire']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.votetexas.gov/register-to-vote/) by October 5, 2018 \n\n"

        "[**Letitia Plummer**](https://letitiaplummer2018.com) is running to represent Texas District 22 in the United States Congress. \n\n"
        "[Facebook](https://www.facebook.com/plummerTX22) | "
        "[Twitter](https://twitter.com/plummerTX22) | "
        "[Donate](https://secure.actblue.com/donate/letitiaplummer2018) \n\n"

        "Plummer supports Medicare for all.  \n\n"

        "[Map of Texas District 26](https://www.govtrack.us/congress/members/TX/26) \n\n"

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