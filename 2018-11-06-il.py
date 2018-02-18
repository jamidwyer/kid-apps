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
            terms = ['Ives is trying hard to weasel her way in', 'illinoispolitics', 'Illinois Primaries', 'encouraging letter from my future Representative', 'flip illinois', 'marie newman', 'Biss Lands Major Progressive Group', 'Governor denies clemency to Army veteran', 'chuy garcia', '#ilgov', 'Holocaust denier likely to be GOP nominee for Congress', 'Nazi running for congress', 'Nazi running unopposed for a Republican congressional seat', 'Holocaust denier running unopposed in GOP', 'If You Live in Illinois\'s 3rd Congressional District', 'Nazi Party Member Is About To Get The Republican Nomination', 'Republican congressional primary in Illinois', 'Nazi Is About To Get The Republican Nomination', 'danielbiss', 'arthur jones', 'Illinois Congressional race', 'Illinois GOP Rep', 'Skokie, is picked up by ICE', 'police reform in question amid attorney general race', 'Democratic Governor Debate last night at SIU', 'An Illinois college kid learned that his State Senator', 'illinois green Party', 'Illinois Greens Fundraising', 'online video of recent gubernatorial debate', 'Illinois Democratic Gubernatorial', 'Illinois 13th\'s Congressman', 'Chicago for Womens March', '2018 illinois election', 'Illinois Dem gubernatorial candidates', 'rotering', 'Northbrook-area state lawmakers', 'Thousands of black students leave Chicago for other segregated districts', 'Queen of Illinois with absolute authority', 'Illinois attorney general', 'New Illinois Senate Bill', 'Chicago Congressional Primary', '10 Democratic Primaries To Watch In 2018', 'Green Party Continues to Grow in Jackson County, IL', 'Illinois Farm Bureau Plans Another Push to Legalize Hemp', 'Katie Harper-Wright Elementary', 'Legionnaires\' outbreaks at Illinois Veterans Home', 'Women\'s March Chicago', 'rep lahood', 'Illinois congresspeople', 'hultgren', 'il-14', 'shimkus', '\'chuy\' garcia', 'Rep. Gutierrez', 'anthony clark', '@cdrosa', 'Carlos Ramirez-Rosa', 'Rep. LaHood', 'mike bost', 'rep. bost', 'congressman bost', 'rep bost', 'representative bost', 'rodney davis', 'davis\'s seat', 'roskam', 'il-6', 'il-06', 'chris kennedy', '^(?!.*trauner).*rauner.*$', 'IL gubernatorial', '@govrauner', '^(?!.*bissexual).*biss.*$', 'illinois governor', 'IL\'s next governor ', 'governor of illinois', 'il gov', 'jeanne ives', 'pritzker', 'il governor\'s']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Illinois 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://ova.elections.il.gov/Step0.aspx): February 20, 2018 \n\n"
            "[Primary Election](https://www.elections.il.gov/VotingInformation/VotingByMail.aspx): March 20, 2018 \n\n"
            "[General Election Registration Deadline](https://ova.elections.il.gov/Step0.aspx): October 21, 2018 \n\n"
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