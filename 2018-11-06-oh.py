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

local_subs = open("ohio.dat", "r")
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
            terms = ['Cleveland March For Our Lives', 'Ismail Mohamed', 'Chabot thanks Ohio GOP', 'blueohio2018', 'erin neace', 'Ohio House district 65', 'ohio lawmakers', 'ohio gubernatorial', 'aftab pureval', 'ohio senate passes bill', 'ivote', 'sherrod brown', 'Women\'s march Cincinnati', 'Women\'s March in Columbus', 'pillich', 'husted v.', 'jon husted', 'robert barr', 'kucinich', 'Ohio Attorney General', 'Ohio purge of voter rolls', 'ohio senate frontrunner', 'ohio senate candidate', 'jay goyal', 'Ohio congressional candidates', 'rick neal', 'Supreme Court to take up Ohio', 'Ohio House and Senate', 'stivers latest', 'Ohio\'s 16th District', 'proposed Ohio ballot initiative', 'Marijuana in Ohio', 'jimmy gould', 'cordray', 'stivers', 'mike turner', 'bob gibbs', 'jim jordan', 'renacci', 'dave joyce', 'Ohio politics and candidates', '2018 elections in Ohio', 'representative latta', 'Ohio members of Congress', 'Representative Bill Johnson', 'bill o\'neill', 'steve chabot', 'rep. chabot', 'rep chabot', 'representative chabot', 'congressman chabot', 'oh-1', 'oh-01', 'ken harbaugh', 'josh mandel', 'kasich', 'ohio governor', 'oh gov', 'oh governor\'s', 'jerry springer', 'Mary Taylor']
            for term in terms:
                search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Ohio 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://olvr.sos.state.oh.us/): April 9, 2018 \n\n"
            "[Primary Election](https://www.sos.state.oh.us/globalassets/elections/forms/11-a_english.pdf): May 8, 2018 \n\n"
            "[General Election Registration Deadline](https://olvr.sos.state.oh.us/): October 9, 2018 \n\n"
            "[General Election](https://www.sos.state.oh.us/globalassets/elections/forms/11-a_english.pdf): November 6, 2018 \n\n")
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
