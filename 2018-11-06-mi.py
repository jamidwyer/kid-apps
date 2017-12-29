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

local_subs = open("michigan.dat", "r")
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
            terms = ['Nothing in Moderation', 'HENRY YANEZ', 'Michigan State Police officer who killed teen', 'The people of Michigan have come together', 'fight against gerrymandering faces its next obstacle', 'petition signatures sent to state', 'gretchen whitmer', 'Michigan, these are your Members of Congress', 'Tim Kelly', 'progressives from 24 local groups are gathered here in', 'Michigan still a blue state', 'Michigan Senator Responds to Net Neutrality Email', 'Joe Schwarz', 'Gerrymandering Will End Up at the State Supreme Court', 'Political Issues in Michigan', 'sandy levin', 'jack bergman', 'Only a third of Republican voters blame humans as main cause of climate change', 'Flint, whose water is still not fixed', 'Marijuana legalization one step closer to getting on the ballot in Michigan', 'marijuana legalization in Michigan', 'fred upton', 'mi-06', 'mi-6', 'michigan\'s 6th District', 'rep. upton', 'rep upton', 'representative upton', 'congressman upton', 'benac', '^(?!.*trotte).*trott.*$', 'Gerrymandering complaints lead to ballot campaign', 'frustrations may doom their majority', 'GOP worries as state Dems outperform in special elections', 'Mercurial Trump Rattles Republican Party Ahead of Midterms', '2018 as 3rd House Republican Says He', 'Michigan Republican congressman won\'t seek re-election', 'Congressional GOP Retirement Surge', 'mike bishop', 'rep. bishop', 'rep bishop', 'representative bishop', 'congressman bishop', 'mi-08', 'mi-8', 'Michigan\'s 8th District', 'prohibit protecting the ocean as national park, place extreme restrictions on national parks', 'rick snyder', 'governor snyder', 'gov snyder', 'gov. snyder', 'michigan governor', 'governor of michigan', 'michigan\'s governor', 'stabenow', 'kid rock', 'john james', 'Robert Ritchie', '^(?!.*yamashiro).*amash.*$', 'mi-03', 'mi-3', 'michigan\'s 3rd District']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Michigan 2018 Election \n\n"
            "[Primary Voter Registration Deadline](http://www.dmv.org/mi-michigan/voter-registration.php): July 8, 2018 \n\n"
            "[Primary Election](https://webapps.sos.state.mi.us/MVIC/votersearch.aspx): August 7, 2018 \n\n"
            "[General Election](https://webapps.sos.state.mi.us/MVIC/votersearch.aspx): November 6, 2018 \n\n")
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