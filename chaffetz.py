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

local_subs = open("utah.dat", "r")
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
            terms = ['chaffetz', 'john curtis', 'kathie allen', 'ut-3', 'ut-03', 'Republicans secretly yearn for a Hillary Clinton presidency', 'Issues Mark 2017 Campaign Season In Utah', '16 in generic Congressional vote', 'new Utah system allows moderates to win', 'The website of the Republican candidate for Utah', 'Seventh Republican retirement', 'Curtis overcome a flood of negative advertising', 'Utah judge rules that third party candidate be allowed on the 2017 special election ballot', 'chaffetz\'s open seat']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://secure.utah.gov/voterreg/index.html) by October 31, 2017 \n\n"
            "General Election: November 7, 2017 \n\n"
            "[Sign up to vote by mail](https://secure.utah.gov/voterreg/index.html) \n\n"

            "[**Kathie Allen**](https://www.drkathieforcongress.com/) is running to represent Utah District 3. \n\n"
            "[Donate](https://www.drkathieforcongress.com/donate-now/) | "
            "[Facebook](https://www.facebook.com/KathieAllenMDforCongress/) | "
            "[Twitter](https://twitter.com/kathieallenmd) \n\n"

            "Allen supports universal health care, public schools, living wages, campaign finance reform, LGBTQIA equality, and medical marijuana.  \n\n\n"

            "[Map of Utah District 3](https://www.govtrack.us/congress/members/UT/3) \n\n"

            "^(I'm a bot and I'm learning. Let me know how I can do better.)")
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