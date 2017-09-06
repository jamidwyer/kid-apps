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
    for submission in subreddit.hot(limit=200):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['ted cruz', 'sen. cruz', 'senator cruz', 'dis cruz', 'Texas Congressmen voted against Sandy relief, now are begging for Harvey relief', 'hypocrisy on Harvey aid', 'Texas Lawmakers Who Voted Against Relief for Hurricane Sandy', 'Texas Republicans voted against aid', 'Socialist After a Natural Disaster', 'Cruz, Cornyn back Texas Gov\'s request for disaster declaration']
            for term in terms:
                search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://www.votetexas.gov/register-to-vote/) \n\n"
        "[**Beto O\'Rourke**](https://www.betofortexas.com/) is running against Ted Cruz. \n\n "
        "[Donate](https://secure.actblue.com/contribute/page/beto-homepage) | "
        "[Reddit](https://www.reddit.com/r/BetoORourke/) | "
        "[Facebook](https://www.facebook.com/betoorourke) | "
        "[Twitter](https://twitter.com/betoorourke) \n\n "
        "O\'Rourke supports universal health care, renewable energy, campaign finance reform, net neutrality, protecting Social Security, equal pay for equal work, LGBT equality, voting rights, and DACA.\n\n "

        "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
        print("Bot replying to : ", submission.id, submission.title)
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