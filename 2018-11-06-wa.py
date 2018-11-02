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

local_subs = open("washington.dat", "r")
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
            terms = ['state rep defends christian ', 'Yakama Nation chairman denied access', 'Spokane may halt police sales of forfeited guns', 'wa-05', 'First U.S. Carbon Fee', 'seattle minimum wage', 'initiative 1639', 'spokane increased registered vot', 'i1639', 'a race in the 5th', 'wa state primary', 'washington state republican', 'Patriot Prayer', 'mcmorris rogers', 'goodspaceguy', 'thurston county vote', 'lisa brown', 'Dan Satterberg', 'the head tax', 's up bootlickers', 'a father, a veteran, and an anarchist', 'Seattle-area prosecutor', 'initiative 1600', 'Seattle Democratic Socialists of America', 'washington state\'s net Neutrality law', 'washington lawmakers', 'washington Legislature', 'Washington State Legislature', 'McMorris Rodgers', 'joey gibson', 'cathymcmorris', 'Washington\'s 3rd Congressional Dist', 'Washington Bill', 'gasque', 'wa-8', 'ed orcutt', 'Governor of Washington State', 'matt manweller', 'sarah smith', 'herrera beutler', '@herrerabeutler', 'wa-3', 'wa-03', 'wa\'s 3rd district']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Washington 2018 Election \n\n"
            "[Ballots Due](https://weiapplets.sos.wa.gov/MyVote/#/login): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our updated list back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()