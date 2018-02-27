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

local_subs = open("oregon.dat", "r")
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
            terms = ['Oregon House passes net neutrality bill', 'Oregon moves toward state net-neutrality law', 'Oregon constitutional amendment on universal care', 'sen. kruse', 'senator kruse', 'sen kruse', 'A few pictures from the Indigenous Women', 'Portland Women\'s March', 'National March for Impeachment in Downtown Portland', 'Oregon\'s Senate Rules Committee', 'Portland Women\'s March', 'youth detention conditions in The Dalles', 'how much money they got from ISPs', 'greg walden', '@repgregwalden', 'rep. walden', 'congressman walden', 'rep walden', 'but a bill to log 10,000 acres of the land is', 'Fund CHIP With Cuts To Medicare And Public Health', 'Net neutrality billboard targets Walden']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Oregon 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://secure.sos.state.or.us/orestar/vr/register.do): April 24, 2018 \n\n"
            "[Primary Election](http://sos.oregon.gov/voting/Pages/drop-box-locator.aspx): May 15, 2018 \n\n"
            "[General Election Registration Deadline](https://secure.sos.state.or.us/orestar/vr/register.do): October 16, 2018 \n\n"
            "[General Election](http://sos.oregon.gov/voting/Pages/drop-box-locator.aspx): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")


for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()