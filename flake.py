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

local_subs = open("arizona.dat", "r")
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
            if re.search('^(?!.*snowflake).*flake.*$', submission.title, re.IGNORECASE):
                # Reply to the post
                text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://www.azsos.gov/elections/voting-election/register-vote-or-update-your-current-voter-information) \n\n"
                    "[**Deedra Abboud**](http://deedra2018.com/) is running against Jeff Flake. \n\n"
                    "[Donate](https://secure.actblue.com/contribute/page/deedra-2018) | "
                    "[Facebook](https://www.facebook.com/Deedra2018/) | "
                    "[Twitter](https://twitter.com/deedra2018) \n\n"
                    "Abboud supports single-payer health care, public schools, and net neutrality. \n\n\n"

                    # "[**Kyrsten Sinema**](http://kyrstensinema.com/) is running against Jeff Flake. \n\n"
                    # "[Donate](https://secure.actblue.com/contribute/page/kyrstensinema) | "
                    # "[Facebook](https://www.facebook.com/ksinemaaz/) | "
                    # "[Twitter](https://twitter.com/kyrstensinema) \n\n"
                    # "Sinema supports renewable energy, increasing the minimum wage, protecting Social Security and Medicare, and equal pay for equal work. \n\n\n"

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