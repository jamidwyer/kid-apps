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
            terms = ['regret jocking Kanye', 'Disney Wages Affect all of Central Florida', 'Lol, Kanye done it again.', 'I get why there is so many homeless.', 'mayor of tallahassee', 'hogg wild', ' trying to take our beaches.', 'scott-nelson', 'ICE Stop Abusing Somali Detainees in Florida', 'scott is running for senate', 'no good reason to stop felons from voting', 'climate change affect miami, florida', 'attacking the parkland kids', 's Jim Crow governor', 's Public beach to be Private', 'Republicans are running against Hillary Clinton', 'be so public anymore under new law', 'fl-6', 'miami streets could flood every single day', 'parkland student activist', 'david hogg', 'Emma Gonzales', 'parkland shooting', 'wildlife conservation council', 'florida legislators', 'stoneman douglas students', 'flgovernment', 'florida state senator', 'fla. senate', 'kelli stargel', 'florida senate', 'florida poll', 'gwen graham', 'fl lawmaker', 'Tampa Bay lawmaker', 'Florida GOP Votes', 'Florida House members', 'florida lawmaker', 'Florida House votes', 'debra kaplan', 'Tom Rooney', 'National School Walkout March 14', 'march for our lives', 'Florida high school shooting', 'florida school shooting', 'margaret good', 'Miami congressional campaign', 'Posey for Congress', 'Peters4Congress', 'Florida congressman', 'philip levine', 'sean shaw', 'Proposed Florida amendment', 'vote in Florida', 'victor torres', 'mayor gillum', 'Florida Congressional District 3', 'Florida voters', 'florida legislature', 'Anna Eskamani', 'FL House district 31', 'matt haggman', 'Kelly Smith for Pasco County Commissioner', 'Orlando Lawmakers', 'ron reid', 'bilirakis', 'Recreational marijuana in Florida', 'Florida Cannabis Act',  '^(?!.*klatvala).*latvala.*$' '^(?!.*gov. scott walker).*gov. scott.*$', 'Florida HD-58', 'gaetz', '2018 congressional races in Florida', 'rick scott', 'Florida Democratic governor', '^(?!.*governor scott).*governor scott.*$', 'florida governor', 'fla. governor', 'governor of florida', 'curbelo', 'brian mast', 'rep mast', 'rep. mast', 'representative mast', 'congressman mast', 'fl-18', 'lehtinen', 'fl-27', 'desantis', 'dennis ross', 'fl-15', 'andrew learned', 'balart', 'fl-25']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Florida 2018 Election \n\n"
            "[Primary Election Voter Registration Deadline](https://registertovoteflorida.gov/en/Registration/Eligibility): July 30, 2018 \n\n"
            "[Primary Election](http://dos.myflorida.com/elections/for-voters/voting/absentee-voting/): August 28, 2018 \n\n"
            "[General Election Voter Registration Deadline](https://registertovoteflorida.gov/en/Registration/Eligibility): October 9, 2018 \n\n"
            "[General Election](http://dos.myflorida.com/elections/for-voters/voting/absentee-voting/): November 6, 2018 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write the post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()