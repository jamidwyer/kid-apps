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

local_subs = open("colorado.dat", "r")
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
            terms = ['Chicken President Visits Denver', 't would like to remind you to update your voter info', 'Students, Teachers Call for Nationwide School Walkouts', 'Thoughts and Prayers and N.R.A. Funding', 'funding at the Office of Energy Efficiency and Renewable Energy', 'co ag candidate', 'colorado governor', 'colorado poll', 'Colorado GOP chairman convicted of voter fraud', 'colorado voters', 'emily sirota', 'Colorado Trump campaign supporters', '2018 Women\'s March in Denver', 'jared polis', 'days of CHIP funding left', 'Coloradans marched through the cold weather on Colfax', 'National Park Service advisory panel resign in frustration', 'Women\'s March Denver 2018', 'Colorado Cities Keep Voting To Build Their Own Broadband Networks', 'Colorado Just Had Its 3rd Warmest Year Ever', 'Colorado Might Gain a Congressional Seat', 'unkept promises on Dreamers, CHIP', 'State Where Everyone Wants to Be Governor', 'Colorado city moves ahead with muni broadband', 'CO is spending it\'s MJ tax revenue', 'Time to Nationalize the Internet', 'Doug Lamborn', 'ken buck', 'Voters can preserve net neutrality for their communities by authorizing municipal broadband', 'fight against Fort Collins municipal broadband', 'Colorado\'s investment in IUDs', 'former GOP party chairman in Colorado', 'steve curtis', 's Republican Party found guilty of voter fraud', 'Colorado becomes first in the nation to secure election system', 'Colorado CHIP notice letters sent out', 'mike coffman', 'co-06', 'co-6', 'rep. coffman', 'rep coffman', 'representative coffman', 'congressman coffman']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Colorado 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://www.sos.state.co.us/voter/pages/pub/olvr/verifyNewVoter.xhtml): June 26, 2018 \n\n"
            "[Primary Election Date](https://www.sos.state.co.us/pubs/elections/vote/VoterHome.html): June 26, 2018 \n\n"
            "[General Election Registration Deadline](https://www.sos.state.co.us/voter/pages/pub/olvr/verifyNewVoter.xhtml): November 6, 2018 \n\n"
            "[General Election](https://www.sos.state.co.us/pubs/elections/vote/VoterHome.html): November 6, 2018 \n\n")
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