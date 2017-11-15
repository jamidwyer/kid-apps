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

local_subs = open("utah.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top 5 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['orrin hatch', 'sen. hatch', 'senator hatch', 'Democrats furious over new GOP attempt to gut Obamacare', 'Mitt Romney May Be Headed to the Senate', 'Trump headed to Utah in December with plans to shrink Bears Ears', 'tax bill shrouded in secrecy', 'open marine sanctuaries to oil drilling', 'attack on Bears Ears National Monument', 'Trump plans to shrink two national monuments in Utah', 'secret oatmeal cookie president', 'Trump plans to shrink size of Utah national monuments', 'Trump shrinks national monument sacred to local tribe', 'President Donald Trump is shrinking two national monuments in Utah', 'Trump to shrink Utah national monument', 'Trump to Shrink Two Utah National Monuments', 'Trump says he will shrink Bears Ears National Monument', 'Hatch-authored drug law that may hurt DEA enforcement', 'Corporations to keep tax break lost by millions of Americans', 'sponsored by Hatch', 'Bannon putting Senate majority at risk in 2018', 'no significant benefit for poorest families', 'Congress to hold off on gun silencer legislation', 'jokes that Republican tax-reform plan is', 'Will Hatch run again or retire', 'governor and senator for two different states', 'Wilson would beat Hatch', 'Mitt Romney has politicos asking', 'Bipartisan Push Shakes Up Capitol Hill', 'Hatch has some daunting numbers to overcome', 'hatch: calling trump racist', 'racist bone in his body ', 'shot their wad', 'Meant It the Civil War Way', 'definitively say whether he is breaking promise, running again', 'announcement on his political future has been pushed back']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://secure.utah.gov/voterreg/index.html) \n\n"
        "[**Jenny Wilson**](http://wilsonforsenate.com/) is running to represent Utah in the United States Senate. \n\n "
        "[Donate](https://www.crowdpac.com/candidates/58d92c47d9e704560d2afff1/jenny-wilson) | "
        "[Facebook](https://www.facebook.com/WilsonForSenate/) | "
        "[Twitter](https://twitter.com/jennywilsonut) \n\n "

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