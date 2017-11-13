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
            terms = ['rohrabacher', 'michael kotick', '@danarohrabacher', 'rohrabracher', 'what is the plan to exploit it for midterms', 'Rep. Hill received memo', 'The Republican civil war, and why Trump is winning it', 'Brought Holocaust Denier To Capitol Meeting', 'Transcript of McCarthy', 'transcript of the conversation among GOP leaders obtained by The Post', 'congressman openly loyal to Russia', 'broken clock and all.', 'GOP Congressman Met in Moscow With Kremlin', 'pro-Russia congressman', 'lackey in Congress met with Veselnitskaya', 'This M.F. Has To Go!', 'Congressman calls Charlottesville protest', 'GOP Congressman Sought Trump Deal on WikiLeaks, Russia', 'GOP Rep Goes Full Crazy And Claims Charlottesville Nazis', 'White Nationalist Rally Was a Left-Wing Set-Up', 'left-wingers manipulating Civil War reenactors', 'pro-assange gop congressman', 'Republican congressman praises ISIS attack in Iran', 'Republican Congressman Meets With WikiLeaks Founder Julian Assange', 'Paid by Putin Meets With WikiLeaks Founder Julian Assange', 'pro-putin california congressman', 'Pro-Russia GOP Rep.', 'Putin\'s congressman', 'Assange meets U.S. congressman', 'one of our local Members of Congress...', 'rhorabacher']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("California 2018 Election \n\n"
            "[Voter Registration Deadline](http://registertovote.ca.gov/): May 16, 2018 \n\n"
            "[Primary Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): June 5, 2018 \n\n"
            "[General Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): November 6, 2018 \n\n")
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