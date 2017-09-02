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

local_subs = open("iowa.dat", "r")
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
            terms = ['david young', 'Democratic Party Fundraiser Leaders Snub Iowa Candidate']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://mymvd.iowadot.gov/Account/Login?ReturnUrl=%2fVoterRegistration) \n\n"
            "[**Heather Ryan**](https://www.ryanforiowa.com/) is running against David Young. \n\n"
            "[Donate](https://secure.actblue.com/donate/heatherryan) | "
            "[Facebook](https://www.facebook.com/HeatherRyanForIowa/) | "
            "[Twitter](https://twitter.com/LoudAndLiberal) \n\n\n"

            "Ryan supports universal health care, public schools, affordable college, a living wage, subsidized child care, equal pay for equal work, renewable energy, and campaign finance reform. \n\n\n"

            "[**Pete D'Alessandro**](http://peteforiowa.com/) is running against David Young. \n\n"
            "[Donate](https://secure.actblue.com/donate/pete-for-iowa) | "
            "[Facebook](https://www.facebook.com/peteforiowa/) | "
            "[Twitter](https://twitter.com/peteforiowa) \n\n\n"

            "D'Alessandro supports universal health care, renewable energy, a living wage, and affordable college. \n\n\n"

            "[**Austin Frerick**](http://www.austinfrerick.com/) is running against David Young. \n\n"
            "[Donate](https://secure.actblue.com/donate/austin-frerick) | "
            "[Facebook](https://www.facebook.com/AustinFrerick) | "
            "[Twitter](https://twitter.com/AustinFrerick) \n\n\n"

            "Frerick supports universal health care, a living wage, paid family leave, affordable college, campaign finance reform, and LGBTQ equality. \n\n\n"

            "[**Paul Knupp**](https://knuppforcongress.org/issues.html) is running against David Young. \n\n"
            "[Donate](https://www.gofundme.com/knupp-for-congress) | "
            "[Facebook](https://www.facebook.com/drpaulknupp) \n\n\n"

            "Knupp supports universal health care, a living wage, affordable college, and funding the EPA and Planned Parenthood. \n\n\n"

            "[**Cindy Axne**](https://cindyaxneforcongress.com/) is running against David Young. \n\n"
            "[Donate](https://secure.actblue.com/donate/cindyaxneforcongress) | "
            "[Facebook](https://www.facebook.com/CindyAxneForCongress/) | "
            "[Twitter](https://twitter.com/Axne4Congress) \n\n\n"

            "[Map of Iowa District 3](https://www.govtrack.us/congress/members/IA/3) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")

        print("Bot replying to : ", submission.title)
        submission.reply(text)

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