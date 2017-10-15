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
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['mark walker', 'rep. walker', 'Huge, Exploding Deficits', 'Representative walker', 'congressman walker', 'rep walker', 'repealing the Johnson Amendment isn', 'Ignore The Deficit']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.ncsbe.gov/Voters/Registering-to-Vote) by October 12, 2018 \n\n"
            "[Sign up to vote by mail](https://www.ncsbe.gov/Portals/0/Forms/NCAbsenteeBallotRequestForm.pdf) \n\n\n"

            "[**Ryan Watts**](http://wattsforcongress.com/) is running to represent North Carolina District 6. \n\n"
            "[Facebook](https://www.facebook.com/WattsforCongress/) | "
            "[Twitter](https://twitter.com/watts4congress) | "
            "[Volunteer](https://act.myngp.com/Forms/-860671247869146368) | "
            "[Donate](https://act.myngp.com/Forms/-4754596075684361472) \n\n"
            "Watts supports Medicare as a public option for health insurance, equal pay for equal work, and renewable energy. \n\n\n"

            "General Election: November 6, 2018 \n\n"
            "[Map of North Carolina District 6](https://www.govtrack.us/congress/members/NC/6) \n\n "

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