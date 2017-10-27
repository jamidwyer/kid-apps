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
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['duncan hunter', 'rep. hunter', 'congressman hunter', 'rep hunter', 'ca-50', 'Republicans by 15 points in Fox News poll', 'Dems lead by 15 points on generic ballot', 'GOP lawmaker calls for preemptive strike on North Korea', 'medical marijuana. Will Congress listen?', 'GOP lawmaker gives profane tribute to Trump', 'House GOP blocks vote protecting medical', 'House to vote on an amendment that would bar the Justice Department from pursuing states that have legalized medical marijuana', 'House GOP Blocks Vote For Protecting Medical Cannabis', 'our a--hole', 'our asshole', 'California congressman lauds Trump with profane comment']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://registertovote.ca.gov/) by May 16, 2018 \n\n"
            "[Sign up to vote by mail](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply) \n\n\n"

            "[**Pierre (Pete) Beauregard**](http://beauregard4congress.com/) is running against Duncan Hunter. \n\n"
            "[Facebook](https://www.facebook.com/Beauregard4Congress/) | "
            "[Twitter](https://twitter.com/BeauregardCA50) | "
            "[Volunteer](http://beauregard4congress.com/mainpage.beauregard4congress.com/) | "
            "[Donate](https://secure.actblue.com/contribute/page/pete-beauregard-1) \n\n"
            "Beauregard supports universal health care, living wages, renewable energy, campaign finance reform, and net neutrality. \n\n\n"

            "[**Josh Butner**](https://joshbutnerforcongress.com/) is running against Duncan Hunter. \n\n"
            "[Facebook](https://www.facebook.com/JoshButnerCA50/) | "
            "[Twitter](https://twitter.com/JoshButnerCA50) | "
            "[Volunteer](https://joshbutnerforcongress.com/) | "
            "[Donate](https://secure.actblue.com/contribute/page/butner-homepage) \n\n"
            "Butner supports DACA. \n\n\n"

            "Primary Election: June 5, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of California District 50](https://www.govtrack.us/congress/members/CA/50) \n\n"

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