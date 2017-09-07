# coding: utf-8
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

local_subs = open("wisconsin.dat", "r")
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
            terms = ['paul ryan', 'rep. ryan', 'congressman ryan', 'rep ryan', 'speaker ryan', '@speakerryan', 'Trump sides with Democrats over length of debt limit hike', 'Trump welcome to the resistance', 'Republican plans into chaos', 'GOP Will Settle For The Usual Litany Of Tax Cuts', 'Republicans Could Protect Dreamers', 'Republicans Will Let America Burn', 'Took Millions From Russian Oligarch Tied To Putin', 'Time for the GOP to abandon ship', 'Wisconsin\'s First Congressional District', 'WI: 34%']
            for term in terms:
                 search(term, submission);

def search(term, submission):
            if re.search(term, submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://myvote.wi.gov/en-us/registertovote) \n\n"
                    "[**Randy Bryce**](https://randybryceforcongress.com/) is running against Paul Ryan. \n\n"
                    "[Donate](https://secure.actblue.com/donate/randy-bryce-for-congress-1) | "
                    "[Reddit](https://www.reddit.com/r/RandyBryce) | "
                    "[Facebook](https://www.facebook.com/RandyBryce2018) | "
                    "[Twitter](https://twitter.com/IronStache) \n\n"
                    "Bryce supports universal health care, living wages, protecting Social Security and Medicare, affordable college, renewable energy, campaign finance reform, and DACA. \n\n\n"

                    "[**Cathy Myers**](https://cathymyersforcongress.com/) is running against Paul Ryan. \n\n"
                    "[Donate](https://secure.actblue.com/donate/cathy-for-congress-1?refcode=website) | "
                    "[Facebook](https://www.facebook.com/cathymyersforcongress/) \n\n"

                    "[Map of Wisconsin District 1](https://www.govtrack.us/congress/members/WI/1) \n\n"

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