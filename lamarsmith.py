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
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['^(?!.*anthony lamar smith).*lamar smith.*$', 'house science committee chair', 'rapidly shifting politics make it a bellwether of the country', 'tx-21', 'tx21']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.votetexas.gov/register-to-vote/) \n\n"
            "[**Chris Perri**](https://www.chrisperrifortexas.com/) is running against Lamar Smith. \n\n"
            "[Facebook](https://www.facebook.com/ChrisPerriforTexas/) | "
            "[Twitter](https://twitter.com/ChrisPerriTX) | "
            "[Volunteer](https://www.chrisperrifortexas.com/volunteer/) | "
            "[Donate](https://secure.actblue.com/donate/chris-perri-for-texas) \n\n"
            "Perri supports universal health care, public schools, affordable college, living wages, protecting Social Security, renewable energy, campaign finance reform, and DACA. \n\n\n"

            "[**Derrick Crowe**](https://www.electcrowe.com/#issues-home-section) is running against Lamar Smith. \n\n"
            "[Facebook](https://www.facebook.com/electcrowe) | "
            "[Twitter](https://twitter.com/electcrowe) | "
            "[Volunteer](https://www.electcrowe.com/join/) | "
            "[Donate](https://secure.actblue.com/contribute/page/electcrowe) \n\n"
            "Crowe supports universal health care, living wages, paid family leave, affordable college, renewable energy, campaign finance reform, LGBTQ equality, and DACA. \n\n\n"

            "[Map of Texas District 21](https://www.govtrack.us/congress/members/TX/21) \n\n"

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