# coding: utf-8
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

local_subs = open("arizona.dat", "r")
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
            terms = [
                'az gov', \
                'mcsally', \
                '^(?!.*snowflake).*flake.*$', '@jeffflake', 'sinema', 'Kelli Ward'
                '@RepOHalleran', 'o\'halleran', 'kevin cavanaugh', 'steve smith', 'schweikert', \
                'democrat steve diamond', \
                'flip the senate', 'ice fails to properly redact', \
                'nothing less than a civil war', \
                'Simulations Of Homes In Chicago And Arizona', 'representing in az', \
                'nervous republicans', 'Trump backlash in suburbs', 'mark kelly', \
                'donations to senate republicans', 'justiceforelijah', 'meghan mccain', 'uss john mccain', \
                'arizona supreme court', \
                'arizona republican', 'jerry demings', 'elected in arizona', \
                'az vote', 'arizona congress', 'az-sen', 'Phoenix ICE facility', 'arizona bill', 'mesa police', \
                'rally in Mesa', 'arizona gop', 'az education', 'kelly townsend', 'HB2663', \
                'arizona teacher strike', 'arizona teachers rally', 'arizona state senat', 'arizona state capitol', 'AZ RedForEd', 'az08', 'education funding in arizona', 'rally in phoenix', 'azsen', 'az 06', 'rep. gallego', 'congressman gallego', 'scott menor', 'school vouchers in Arizona', 'grijalva', 'Arizona primary', 'Arizona Republican', 'candidates running in Arizona', 'Arizona Legislature', 'Scottsdale lawmaker', 'brailsford', 'Lea Marquez Peterson', 'daniel shaver', 'arpaio', 'gosar', 'Arizona Green Party', 'Oro Valley lawmaker', 'Arizona lawmaker', 'ducey', 'arizona governor', 'az. gubernatorial race', 'arizona\'s race for governor', 'arizona gubernatorial', 'arizona\'s republican governor', 'Congressman Biggs', 'andy biggs', 'az-5', 'az-05', 'rep biggs', 'rep. biggs', 'representative biggs', 'Congressman Tom O\´Halleran', \
            ]
            for term in terms:
                 search(term, submission)

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Arizona 2020 Election \n\n"
            "[Presidential Primary Voter Registration Deadline](https://servicearizona.com/webapp/evoter/register?execution=e1s2): February 18, 2020\n\n"
            "[Presidential Primary Election](https://azsos.gov/elections/voting-election/contact-information-county-election-officials): March 17, 2020\n\n"
            "[Primary Voter Registration Deadline](https://servicearizona.com/webapp/evoter/register?execution=e1s2): July 6, 2020\n\n"
            "[Primary Election](https://azsos.gov/elections/voting-election/contact-information-county-election-officials): August 4, 2020\n\n"
            "[General Voter Registration Deadline](https://servicearizona.com/webapp/evoter/register?execution=e1s2): October 5, 2020\n\n"
            "[General Election](https://azsos.gov/elections/voting-election/contact-information-county-election-officials): November 3, 2020 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write our post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub)

text_file.close()