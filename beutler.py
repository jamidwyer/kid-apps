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

local_subs = open("washington.dat", "r")
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
            terms = ['herrera beutler', '@herrerabeutler', 'wa-3', 'wa-03', 'wa\'s 3rd district']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://weiapplets.sos.wa.gov/MyVoteOLVR/MyVoteOLVR) by July 30, 2018 \n\n"

            "[**Dorothy Gasque**](http://dorothyforcongress.com/) is running to represent Washington's 3rd Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/Dorothy4Congress) | "
            "[Twitter](https://twitter.com/dorothy4house) | "
            "[Volunteer](http://dorothyforcongress.com/volunteer/) | "
            "[Donate](https://secure.actblue.com/contribute/page/dorothy4congress) \n\n"
            "Gasque supports single-payer health care, a living wage, renewable energy, and campaign finance reform. \n\n"

            "[**David McDevitt**](http://mcdevittforcongress.com/home/issues/) is running to represent Washington's 3rd Congressional District. \n\n"
            "[Facebook](https://www.facebook.com/McDevittMBAJD/) | "
            "[Twitter](https://twitter.com/@McDevittMBAJD/) | "
            "[Volunteer](http://mcdevittforcongress.com/get-involved/volunteer/) | "
            "[Donate](http://mcdevittforcongress.com/get-involved/donate/) \n\n"
            "McDevitt supports single-payer health care, public schools, affordable college, a living wage, protecting Social Security, equal pay for equal work, campaign finance reform, LGBTQ equality, net neutrality, and decriminalizing marijuana. \n\n"

            "Primary Election: August 7, 2018 | General Election: November 6, 2018"
            "[Map of Washington District 3](https://www.govtrack.us/congress/members/WA/3) \n\n"

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