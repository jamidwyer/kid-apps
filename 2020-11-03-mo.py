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

local_subs = open("missouri.dat", "r")
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
            terms = ['panic at missouri walmart', 'missouri medicaid', 'mo auditor', 'missouri abortion', 'cancer is killing our firefighters', 'Judge orders DHSS to release full list of marijuana applicants', 'lucile bluford', 'Washington University will raise its minimum wage', 'cori bush', 'black missouri drivers', 'Right Gets Tired of Democracy', 'equal rights amendment', 'forced by the state of missouri', 'hope Clinic for Women', 'Missouri is \'leaking\' sales tax revenue', 'rally in missouri', 'rally in Cape Girardeau', 'missouri senat', 'st. louis abortion', 'billy long', 'missouri house', 'st. louis prosecutor', 'ferguson reformer', 'missouri election', 'ferguson prosecutor', 'missouri gop', 'wesley bell', 'bob mcculloch', 'right to work in missouri', 'missouri prison', 'missouri state primary', 'missouri vote', 'missouri 2020 primary', 'j.p johnson', 'mo-7', 'st. louis minimum wage', 'missouri congress', 'michael brown was shot', 'curtiswylde', 'greitens', 'lauren arthur', 'missouripolitics', 'ferguson city council', 'missouri house moves', 'kc voters', 'osmack', 'missouri bill', 'new approach missouri', 'Missouri lawmaker', 'austin petersen', 'Missouri Medical Marijuana Campaign', 'josh hawley', 'courtland sykes', 'US Senate in Missouri', 'MO GOP Senate Nomination', 'snake-filled heads', 'career obsessed banshees', 'Missouri pregnancy mortality', 'sam graves', 'Blaine Luetkemeyer', 'kathy ellis', 'mccaskill', 'ann wagner', 'mo-2', 'jenna marie bourgeois', 'hartzler', 'mo-4']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Missouri 2020 Election \n\n"
            "[Presidential Preference Primary Registration Deadline](https://s1.sos.mo.gov/votemissouri/request): February 12, 2020 \n\n"
            "[Presidential Preference Primary](https://voteroutreach.sos.mo.gov/PRD/VoterOutreach/VOSearch.aspx): March 10, 2020 \n\n"
            "[Primary Registration Deadline](https://s1.sos.mo.gov/votemissouri/request): July 8, 2020 \n\n"
            "[Primary Election](https://voteroutreach.sos.mo.gov/PRD/VoterOutreach/VOSearch.aspx): August 4, 2020 \n\n"
            "[General Election Registration Deadline](https://s1.sos.mo.gov/votemissouri/request): October 7, 2020 \n\n"
            "[General Election](https://voteroutreach.sos.mo.gov/PRD/VoterOutreach/VOSearch.aspx): November 3, 2020 \n\n")
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