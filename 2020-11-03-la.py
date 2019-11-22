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

local_subs = open("louisiana.dat", "r")
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
            terms = ['Gun deaths from homicide vs. suicide in US states', 'jbe win', 'redistricting table in Louisiana', 'louisiana gov', 'louisiana is a republican', 'john bel edwards', 'I lost my job for refusing to hide climate crisis facts', 'with a straight face, gop leader', 'Gulf Coast beaches closed due to algae bloom', 'planned ice raids', 'ICE shows up at your door', 'thc overdose', 'louisiana sports betting', 'LaPlace woman overdose on marijuana', 'rep. ralph abraham', 'the current state of American liberalism', 'nungesser', 'us children are living below the poverty line', 'louisiana decided to curb mass incarceration', 'Louisiana Anti-Protest Law', 'renee fontenot', 'jeff landry', 'district in louisiana', 'david vitter', 'louisiana fall elections', 'twitter troll from baton rouge', 'Higgins campaign', 'louisiana congress', 'deepwater horizon', 'House of Representatives in Louisiana', 'Shreveport mayor', 'louisiana secession', 'la district 3', 'louisiana state lawmaker', 'louisiana lawmaker', 'louisiana elect', 'louisiana budget cuts', 'bayou bridge pipeline', 'tom schedler', 'la. house republican', 'louisiana legislat', 'wendy vitter', 'louisiana senators', 'louisiana law', 'louisiana senate', 'la. state senator', 'Dave Langlinais', 'la 3rd', 'LouisianaPolitics', 'Protest in Abbeville', 'deyshia hargrave', 'Vermilion school board', 'Vermillion school board', 'Louisiana district', 'Louisiana School District', 'Louisiana superintendent', 'most incarcerated state', 'scalise', 'clay higgins', 'Louisiana Prison ']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Louisiana 2020 Election \n\n"
            "[Primary Registration Deadline](https://voterportal.sos.la.gov/VoterRegistration): February 15, 2020 \n\n"
            "[Primary Election](https://voterportal.sos.la.gov/Home/VoterLogin): March 7, 2020 \n\n"
            "[General Election Registration Deadline](https://voterportal.sos.la.gov/VoterRegistration): October 13, 2020 \n\n"
            "[General Election](https://voterportal.sos.la.gov/Home/VoterLogin): November 3, 2020 \n\n")
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