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
            terms = ['2 percent ron', 'flip florida', 'shalala', 'george zimmerman', 'Palm Beach County Chapter of the Democratic Socialists of America', 'Florida GOP gubernatorial', 'andrewgillum', 'pam bondi', 'ballots in florida', 'andrew gillum', 'parkland teens', 'florida state house', 'melissa howard', 'Guns From Dozens of Dangerous People', 'campus ban on early voting', 'miami-dade teachers', 'cameron_kasky', 'lee mangold', 'florida republican', 'commissioner of agriculture of florida', 'vern buchanan', 'fl-16', 'jeremy ring', 'mar-a-lago', 'algae bloom threatens Florida', 'fladems', 'Lake Okeechobee Algae Bloom', 'FL-21', 'fl governor', 'aron davis', 'parkland survivor', 'fl-gov', 'nelson campaign', 'scottforflorida', 'orlando mass shooting', 'pulse shooting', 'senator nelson', 'Gary Wayne Lindsey', 'gerrymandering in florida', 'save rural florida', 'school safety commission', 'adam putnam', 'parkland kid', 'bill nelson', 'parkland parents', 'early voting ban on college campuses', 'joe negron', 'lauren baer', 'mayor of tallahassee', 'hogg wild', 'scott-nelson', 'fl-6', 'parkland student activist', 'david hogg', 'Emma Gonzales', 'parkland shoot', 'wildlife conservation council', 'florida legislators', 'stoneman douglas students', 'flgov', 'florida state senator', 'fla. senate', 'kelli stargel', 'florida senate', 'florida poll', 'gwen graham', 'fl lawmaker', 'Tampa Bay lawmaker', 'Florida GOP Votes', 'florida lawmaker', 'Florida House', 'debra kaplan', 'Tom Rooney', 'march for our lives', 'Florida high school shooting', 'florida school shooting', 'margaret good', 'Miami congressional campaign', 'Posey for Congress', 'Peters4Congress', 'Florida congressman', 'philip levine', 'sean shaw', 'Proposed Florida amendment', 'vote in Florida', 'victor torres', 'mayor gillum', 'Florida Congressional District 3', 'Florida voters', 'florida legislature', 'Anna Eskamani', 'FL House district 31', 'matt haggman', 'Kelly Smith for Pasco County Commissioner', 'Orlando Lawmakers', 'ron reid', 'bilirakis', 'Recreational marijuana in Florida', 'Florida Cannabis Act',  '^(?!.*klatvala).*latvala.*$' '^(?!.*gov. scott walker).*gov. scott.*$', 'Florida HD-58', 'gaetz', '2018 congressional races in Florida', 'rick scott', 'Florida Democratic governor', '^(?!.*governor scott).*governor scott.*$', 'florida governor', 'fla. governor', 'governor of florida', 'curbelo', 'brian mast', 'rep mast', 'rep. mast', 'representative mast', 'congressman mast', 'fl-18', 'lehtinen', 'fl-27', 'desantis', 'dennis ross', 'fl-15', 'andrew learned', 'balart', 'fl-25']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Florida 2018 Election \n\n"
            "[Early Voting](https://dos.myflorida.com/elections/for-voters/voting/early-voting/): October 22-November 4, 2018 \n\n"
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