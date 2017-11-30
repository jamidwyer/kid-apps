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

local_subs = open("nevada.dat", "r")
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
            terms = ['sisolak', 'Tax reform will harm Nevada', 'programs providing pro bono legal assistance to veterans', 'Democrats have had success promoting Universal Basic Income', '^(?!.*hellerweather).*heller.*$', 'sbaih', 'Nevada GOP candidate criticizes', 'Anyone Who Supports Donald Trump Jeopardizes Their Own', 'jared fisher', 'governor sandoval', 'nevada governor', 'NV\'s next governor ', 'governor of nevada', 'nv gov', 'nv governor\'s', 'Marijuana clubs are a bad idea']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Nevada 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://nvsos.gov/sosvoterservices/Registration/step1.aspx): May 15, 2018 \n\n"
            "[Primary Election](https://nvsos.gov/votersearch/index.aspx): June 12, 2018 \n\n"
            "[General Election Registration Deadline](https://nvsos.gov/sosvoterservices/Registration/step1.aspx): October 7, 2018 \n\n"
            "[General Election](https://nvsos.gov/votersearch/index.aspx): November 6, 2018 \n\n")
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