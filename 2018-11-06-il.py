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

local_subs = open("illinois.dat", "r")
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
            terms = ['Illinois congresspeople   ', 'about new wave of female candidates', 'hultgren', 'il-14', 'shimkus', '\'chuy\' garcia', 'Rep. Gutierrez', 'anthony clark', 'legalizing marijuana in Illinois', 'open House seat in Illinois', '@cdrosa', 'Carlos Ramirez-Rosa', 'Rep. LaHood', 'solutions to fixing Illinois', '2018 DuPage, Kane County elections', 'Funding Illinois universities an imperative, not an option', 'mike bost', 'rep. bost', 'congressman bost', 'rep bost', 'representative bost', 'House Dem campaign arm highlights promising new candidates', 'House Dems highlight promising new candidates', 'rodney davis', 'davis\'s seat', 'Justice Dems Announces FOUR NEW Candidates', 'All 6 Missouri Republicans in House vote against Trump' ,'roskam', 'il-6', 'il-06', 'Republicans Ready to Move on a Tax Plan Few Have Seen', 'Suburban Chicago Republican congressmen back Trump', 'Tax Plan Cuts Rates for Individuals and Corporations and Eliminates Many Deductions', 'House GOP Worries About', 'GOP outraged after Trump refuses to consider Lois Lerner prosecution', 'GOP request to reopen case against former IRS official Lois Lerner', 'chris kennedy', 'rauner', 'IL gubernatorial', '@govrauner', '^(?!.*bissexual).*biss.*$', 'illinois governor', 'IL\'s next governor ', 'governor of illinois', 'il gov', 'jeanne ives', 'Illinois legalize recreational marijuana', 'contests between bajillionaires', 's all Speaker Madigan', 'Billions in Illinois bills not sent for payment', 'Welcome to the dysfunction of Illinois government', 'Gubernatorial Forum Sunday', 'High school students to host gubernatorial primary debate', 'rage at Rauner', 'Rauner Vetoes Geolocation Privacy Protection Act', 'unpaid bill backlog hits a record', 'pritzker', 'il governor\'s', 'Illinois democrats being primaried']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Illinois 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://ova.elections.il.gov/Step0.aspx): February 20, 2018 \n\n"
            "[Primary Election](https://www.elections.il.gov/VotingInformation/VotingByMail.aspx): March 20, 2018 \n\n"
            "[General Election](https://www.elections.il.gov/VotingInformation/VotingByMail.aspx): November 6, 2018 \n\n")
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