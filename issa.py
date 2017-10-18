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
        #print(submission.selftext)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['darrell issa', 'rep. issa', 'rep issa', 'Thirteen New Candidates', 'Justice Democrats launched 13 new candidates', 'Mike Pence pitches tax reform in Rancho Cordova', 'single-payer healthcare becomes a pivotal issue', 'Last California Republicans', 'states that will lose under Cassidy-Graham', 'Issa told to pay challenger for legal expenses in lawsuit', 's hottest congressional races, ranked', 'the california gop\'s last gasp', 'Republicans booed top White House officials']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://registertovote.ca.gov/) by May 16, 2018 \n\n"
            "[Sign up to vote by mail](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply) \n\n\n"

            "[**Mike Levin**](https://mikelevin.org/priorities/) is running against Darrell Issa. \n\n "
            "[Facebook](https://www.facebook.com/LevinforCongress) | "
            "[Twitter](https://twitter.com/MikeLevinCA) | "
            "[Volunteer](https://mikelevin.org/volunteer/) | "
            "[Donate](https://secure.actblue.com/contribute/page/mikelevin) \n\n"
            "Levin supports Medicare for All, renewable energy, public schools, affordable college, living wages, equal pay for equal work, protecting Social Security and Medicare, campaign finance reform, LGBTQ equality, and DACA.\n\n "

            "[**Doug Applegate**](http://www.applegateforcongress.com/issues/) is running against Darrell Issa. \n\n "
            "[Facebook](https://www.facebook.com/ApplegateForCongress/) | "
            "[Twitter](https://twitter.com/APPLEGATECA49) | "
            "[Volunteer](http://www.applegateforcongress.com/volunteer) | "
            "[Donate](https://secure.actblue.com/donate/voteda49) \n\n"
            "Applegate supports single-payer health care, renewable energy, living wages, campaign finance reform, LGBTQ equality, and protecting Social Security and Medicare.\n\n "

            "Primary Election: June 5, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of California District 49](https://www.govtrack.us/congress/members/CA/49) \n\n "

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