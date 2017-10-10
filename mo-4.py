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

local_subs = open("missouri.dat", "r")
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
            terms = ['jenna marie bourgeois', 'hartzler', 'mo-4', 'How Missouri previewed Democrats']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register to Vote &#9733;&#9733;&#9733;](https://www.sos.mo.gov/elections/goVoteMissouri/register) by July 11, 2018 \n\n"
            "[**Jenna Marie Bourgeois**](http://www.jennamarieformissouri.com/) is running to represent Missouri's 4th Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/JennaMarieMO4/) | "
            "[Twitter](https://twitter.com/JennaMarieMO4) | "
            "[Volunteer](http://www.jennamarieformissouri.com/volunteer) | "
            "[Donate](https://secure.campaigncontributions.net/58390/Contribute-to-Jenna-Bourgeois) \n\n "

            "Bourgeois supports single-payer health care, public schools, a living wage, protecting Social Security, renewable energy, and LGBTQ equality. \n\n\n"

            "Primary Election: August 7, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of Missouri District 4](https://www.govtrack.us/congress/members/MO/4) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better.)")
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