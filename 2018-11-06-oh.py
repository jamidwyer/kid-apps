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
            terms = ['Cincinnati\'s mini-Trump', 'Amazon Employees In Ohio', 'ohio senate frontrunner', 'ohio senate candidate', 'jay goyal', 'Ohio congressional candidates', 'rick neal', 'deported to Jordan after living in Ohio for 40 years', 'move to toss inactive voters from rolls goes to Supreme Court', 'Supreme Court to take up Ohio', 'moving to Ohio in 2018', 'Ohio House and Senate', 'Summit County Has Four Congressional Districts', 'I wish I had faked this. Wow.', 'redistricting reform really happen in Ohio', 'stivers latest', 'No Ohio suit over net neutrality', 'Republicans step up attacks on Mueller', 'city run internet service in Columbus', 'Ohio passes law barring abortion', 'Ohio\'s 16th District', 'proposed Ohio ballot initiative', 'Marijuana in Ohio', 'jimmy gould', 'recreational marijuana soon be legal in Ohio', 'Scared To Death Of Robert Mueller', 'Taser Use in US Jails Reveals Torture', 'Recreational marijuana ballot measure planned for Ohio in 2018', '3 protest locations in Columbus', 'denied worker comp benefits in Ohio', 'cordray', 'help Protect Net Neutrality', 'Tour On the Road', 'stivers', 'Bernie in Akron, Ohio', 'Sander in Dayton Today Motivating The Crowd', 'mike turner', 'bob gibbs', 'jim jordan', 'I heard him call his constituents idiots and he hung up on me', 'jim renacci', 'dave joyce', 'This is your Rep from the 2nd Congressional District', 'discuss Ohio politics and candidates', '2018 elections in Ohio', 'representative latta', 'Ohio members of Congress', 'Ohio court justice deletes Facebook post', 'Representative Bill Johnson', 'bill o\'neill', '50 very attractive females', 'steve chabot', 'rep. chabot', 'rep chabot', 'representative chabot', 'congressman chabot', 'oh-1', 'oh-01', 'Republican county in Ohio just flipped nine seats blue', '136 Democrats support Medicare-For-All', 'ken harbaugh', 'josh mandel', 'kasich', 'ohio governor', 'oh gov', 'oh governor\'s', 'jerry springer', 'Mary Taylor']
            for term in terms:
                search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Ohio Special Election \n\n"
            "[Primary Election Registration Deadline](https://olvr.sos.state.oh.us/): April 9, 2018 \n\n"
            "[Primary Election](https://www.sos.state.oh.us/globalassets/elections/forms/11-a_english.pdf): May 8, 2018 \n\n"
            "[General Election Registration Deadline](https://olvr.sos.state.oh.us/): July 8, 2018 \n\n"
            "[General Election](https://www.sos.state.oh.us/globalassets/elections/forms/11-a_english.pdf): August 7, 2018 \n\n")
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
