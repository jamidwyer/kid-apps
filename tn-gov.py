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

local_subs = open("tennessee.dat", "r")
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
            terms = ['tennessee governor', 'tn gubernatorial', 'tennessee gubernatorial candidates', 'governor haslam', 'randy boyd', 'kay white', 'tn governor', 'Diane Black', 'bill lee', 'beth harwell', 'karl dean', 'mae beavers', 'Costs And Benefits Of Medical Marijuana Divide The Candidates']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://ovr.govote.tn.gov/Registration/#BM) by July 3, 2018 \n\n"
        "[**Karl Dean**](https://www.karldean.com/) is running to be Governor of Tennessee. \n\n "
        "[Facebook](https://www.facebook.com/electkarldean/) | "
        "[Twitter](https://twitter.com/karlfdean) | "
        "[Volunteer](https://www.karldean.com/volunteer-sign-up-form/) | "
        "[Donate](https://secure.actblue.com/contribute/page/karldean) \n\n"
        "Dean supports universal health care, public schools, and medical marijuana. \n\n\n"

        "Primary Election: August 2, 2018 | General Election: November 6, 2018 \n\n"
        "[Find your polling place](http://web.go-vote-tn.elections.tn.gov/) \n\n"

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