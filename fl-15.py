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

local_subs = open("florida.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['dennis ross', 'fl-15', 'andrew learned']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register To Vote &#9733;&#9733;&#9733;](https://registertovoteflorida.gov/en/Registration/Eligibility) by July 30, 2018 \n\n"
        "[Sign up to vote by mail](http://dos.myflorida.com/elections/for-voters/voting/absentee-voting/) \n\n\n"

        "[**Andrew Learned**](http://andrewlearned.com/) is running to represent Florida House District 15 in the United States Congress. \n\n"
        "[Facebook](https://www.facebook.com/AndrewLearned) | "
        "[Twitter](https://twitter.com/AndrewLearned) | "
        "[Volunteer](http://andrewlearned.com/Get_Involved/) | "
        "[Donate](https://secure.actblue.com/donate/leadership1) \n\n "
        "Learned supports renewable energy. \n\n\n "

        "Primary Election: August 28, 2018 | General Election: November 6, 2018 \n\n"
        "[Map of Florida District 15](https://www.govtrack.us/congress/members/FL/15) \n\n"

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