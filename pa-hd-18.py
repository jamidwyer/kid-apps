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

local_subs = open("pennsylvania.dat", "r")
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
            terms = ['tim murphy', 'pa-18', 'bob solomon', 'congressman to resign after report alleged he asked woman to have an abortion', 'Congressman Resigns After Allegedly Urging Mistress to Get an Abortion', 'Republican congressman who urged mistress to get an abortion refuses to quit']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        vote_link = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.pavoterservices.pa.gov/Pages/VoterRegistrationApplication.aspx) \n\n"
        "[Find your polling place](https://www.pavoterservices.pa.gov/Pages/PollingPlaceInfo.aspx) \n\n")

        dems = ("[**Bob Solomon**](https://www.solomon4pa18.com/) is running to represent Pennsylvania District 18 in the United States Congress. \n\n"
        "[Facebook](https://www.facebook.com/SolomonforCongress) | "
        "[Donate](https://secure.actblue.com/donate/solomon4pa18) \n\n"
        "Solomon supports single-payer health care, net neutrality, redistricting reform, and medical marijuana. \n\n\n"

        "[**Pam Iovino**](https://pamforpa.com/) is running to represent Pennsylvania District 18 in the United States Congress. \n\n"
        "[Facebook](https://www.facebook.com/pamforpa/) | "
        "[Twitter](https://twitter.com/pamforpa) | "
        "[Volunteer](https://pamforpa.com/take-action/serve-with-pam/) | "
        "[Donate](https://secure.actblue.com/donate/pam-iovino-for-congress-1) \n\n"
        "Iovino supports health care that is affordable and accessible for every American and a living wage. \n\n\n"

        "[**Mike Crossey**](http://crossey4congress.com/) is running to represent Pennsylvania District 18 in the United States Congress. \n\n"
        "[Facebook](https://www.facebook.com/crossey4congress/) | "
        "[Twitter](https://twitter.com/MC4Congress18) | "
        "[Donate](https://secure.actblue.com/donate/crossey4congress) \n\n"
        "Crossey supports public schools, renewable energy, affordable college, and background checks on every gun sale. \n\n\n")

        map = ("[Map of Pennsylvania House District 18](https://www.govtrack.us/congress/members/PA/18) \n\n")

        with open('disclaimer.txt', 'r') as myfile:
            disclaimer=myfile.read().replace('\n', '')

        text = '\n'.join([vote_link, dems, map, disclaimer])
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