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
            terms = ['Hearing To Discuss Ending Marijuana Prohibition', 'andy ngo', 'killed a bill by running away', 'what the hell just happened in oregon', 'stimson lumber', 'Marijuana Imports And Exports', 'terrorists in oregon', 'the insanity in oregon', 'boquist', 'oregon militia', 'oregon capitol', 'Banning Books That Teach Prisoners How to Code', 'skipped town to avoid a climate change', 'Enforcing Marijuana Laws In Legal States', 'peter defazio', 'firefighting jobs with largest federal', 'Trump falls short on infrastructure', 'blumenauer', 'oregon vot', 'bend city council', 'mcleod-skinner', 'buehler', 'oregon legislat', 'portland dsa', 'kate brown', 'campaigning in Oregon', 'alex diblasi', 'oregon primaries', 'National Popular Vote Interstate Compact', 'Oregon passes net neutrality law', 'oregon governor', 'march today in eugene, oregon', 'val hoyle', 'oregon gop', 'oregon republican', 'oregon state senat', 'multnomah county gop', 'oregon senate', 'dallas heard', 'Oregon House passes', 'Oregon constitutional amendment', 'sen. kruse', 'senator kruse', 'sen kruse', 'Oregon\'s Senate Rules Committee', 'greg walden', '@repgregwalden', 'rep. walden', 'congressman walden', 'rep walden']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Oregon 2020 Election \n\n"
            "[Register to Vote](https://secure.sos.state.or.us/orestar/vr/register.do?lang=eng&source=SOS) \n\n"
            "[Primary Election](http://sos.oregon.gov/voting/Pages/drop-box-locator.aspx): May 19, 2020 \n\n"
            "[General Election](http://sos.oregon.gov/voting/Pages/drop-box-locator.aspx): November 3, 2020 \n\n")
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