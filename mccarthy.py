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
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['kevin mccarthy', 'rep. mccarthy', 'congressman mccarthy', 'rep mccarthy', 'As Russia case unfolds, Trump and Republicans', 'speech to the California GOP tonight has some Republicans nervous', 'Just After Las Vegas, Republicans Are Voting to Restrict', 'Trump administration backpedals on citizenship', 'Trump Administration supports DACA recipients path to Citizenship', 'McCarthy backs Trump', 'A Senate Republcan leader backs Trump', 'help take down a well-known GOP member of the House']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](http://registertovote.ca.gov/) by May 16, 2018 \n\n"
            "[Sign up to vote by mail](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply) \n\n\n"

            "[**Wendy Reed**](http://wendyreedforcongress.com/issues/) is running against Kevin McCarthy. \n\n"
            "[Facebook](https://www.facebook.com/wendyreedforcongress/) | "
            "[Twitter](https://twitter.com/wendyreedtweet) | "
            "[Donate](https://secure.actblue.com/contribute/page/reed2018) \n\n"
            "Reed supports universal health care. \n\n\n"

            "[**Tatiana Matta**](http://tatianamatta.com/) is running against Kevin McCarthy. \n\n"
            "[Facebook](https://www.facebook.com/TatianaMattaForCongress/) | "
            "[Twitter](https://twitter.com/TatianaMatta_) | "
            "[Donate](https://secure.actblue.com/donate/tatianamattaforcongress) \n\n"

            "Primary Election: June 5, 2018 | General Election: November 6, 2018 \n\n"
            "[Map of California District 23](https://www.govtrack.us/congress/members/CA/23) \n\n"

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