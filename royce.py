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

local_subs = open("california.dat", "r")
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
            terms = ['ed royce', 'rep. royce', 'congressman royce', 'rep royce', 'ca-39', 'In a swing district, a Democrat runs on']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://registertovote.ca.gov/) by May 16, 2018 \n\n"
            "[Sign up to vote by mail](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply) \n\n\n"

            "[**Mai Khanh Tran**](https://doctran2018.com/) is running against Ed Royce. \n\n"
            "[Donate](https://secure.actblue.com/donate/drtranforcongress) | "
            "[Facebook](https://www.facebook.com/DocTran2018/) | "
            "[Twitter](https://twitter.com/DocTran2018) \n\n"
            "Tran supports universal health care coverage and Planned Parenthood. \n\n\n"

            "[**Andy Thorburn**](https://www.thorburnforcongress.com/) is running against Ed Royce. \n\n"
            "[Donate](https://secure.actblue.com/donate/andythorburnca?refcode=website) | "
            "[Facebook](https://www.facebook.com/AndyThorburnCA) | "
            "[Twitter](https://twitter.com/AndyThorburnCA) \n\n"
            "Thorburn supports universal health care coverage. \n\n\n"

            "[**Phil Janowicz**](http://philforhouse.com/#issues) is running against Ed Royce. \n\n"
            "[Donate](https://secure.actblue.com/contribute/page/phil) | "
            "[Facebook](https://www.facebook.com/philforhouse) | "
            "[Twitter](https://twitter.com/PhilforHouse) \n\n"
            "Janowicz supports renewable energy, living wages, LGBTQ equality, equal pay for equal work, and increasing funding for science.\n\n"

            "Primary Election: June 5, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of California District 39](https://www.govtrack.us/congress/members/CA/39) \n\n"

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