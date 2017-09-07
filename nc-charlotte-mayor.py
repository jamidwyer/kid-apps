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

local_subs = open("northcarolina.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=200):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Kimberley Paige Barnette', 'Kimberley Barnette', 'Kim Barnette', 'charlotte mayor', 'Candidate uses white as a qualification', 'Charlotte, NC, Mayoral Candidate Reminds Voters That']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.ncsbe.gov/Voters/Registering-to-Vote) \n\n"
            "[**Jennifer Roberts**](https://www.jenniferrobertsformayor.com/) is running to be Mayor of Charlotte. \n\n"
            "[Donate](https://www.jenniferrobertsformayor.com) | "
            "[Facebook](https://www.facebook.com/JenRobertsNC/) | "
            "[Twitter](https://twitter.com/JenRobertsNC) \n\n"

            "Roberts supports living wages, paid family leave, affordable housing, equal pay for equal work, LGBTQ equality, police de-escalation training, and the Paris Climate Agreement.  \n\n\n"

            "[**Joel Ford**](https://joelfordformayor.com/) is running to be Mayor of Charlotte. \n\n"
            "[Donate](https://joelfordformayor.com/donate/) | "
            "[Facebook](https://www.facebook.com/joelfordformayor) | "
            "[Twitter](https://twitter.com/joeldford) \n\n"

            "Ford supports DACA, public transportation, police body cameras, community policing, and police de-escalation training.  \n\n\n"

            "[**Vi Lyles**](https://vilyles.com/) is running to be Mayor of Charlotte. \n\n"
            "[Donate](https://vilyles.com/contribute/) | "
            "[Facebook](https://www.facebook.com/ViLylesCLT) | "
            "[Twitter](https://twitter.com/ViLyles) \n\n"

            "Lyles supports affordable housing and public transportation.  \n\n\n"

            "[**Constance Partee-Johnson**](https://www.johnsonformayor.us/) is running to be Mayor of Charlotte. \n\n"
            "[Facebook](https://www.facebook.com/JOHNSONforCharlotteMayor/) \n\n\n"

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