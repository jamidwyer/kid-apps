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

local_subs = open("tennessee.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Greenville local races', 'Bill seeks to place monument to ', 'House Bill 2381', 's Poor Campaign will come together across the South', 'Tennessee bill', 'dum a\*\* women', 'Tennessee to legalize medical marijuana', 'easier for trans people to update birth certificates in Russia', 'TN Representative Candidate', 'tennessee lawmakers', 'WAY TO GO KNOXVILLE', 'Women\'s March in Chattanooga', 'Spread the word, young lady', 'Tennessee Republican files bill aimed at ending private prison usage', 'RAM holding 5-day free medical', 'running for the House seat for Anderson County', 'Rental costs rising beyond reach in Nashville', 'john duncan', 'Failure Of Insure Tennessee', 'Comcast finalize court victory over Nashville and Google Fiber', 'Group seeks 7-day alcohol sales in Tennessee', 'How liberal or not is Chatanooga', 'congressman slept with patients and paid for their abortions', 'Dolly Parton ever running for an office', 'Could Knoxville implement broadband like Chattanooga did', 'biggest election years Tennessee', 'members-only unionism trap', 'pay to browse fast in the post-net neutrality age', 'Republican net neutrality bill', 'Tennessee House Republicans', 'police officers using a taser to commit torture', 'Net Neutrality Bill Has Glaring Loopholes', 'Democrats just shifted a deep red district in Tennessee by 46', 's a New Day for Democrats', 'gay rights activists predict consequences for GOP', 'corker kick back', 'Democrats are fired up heading into 2018', 'Corker asks', 'corker kickback', 'corkerkickback', 'corker demands', 'TV telling me that GOP Has The Votes', 'Buried in 503-page tax bill', 'GOP tax bill adds last minute 20', 'reports mean GOP must halt the tax bill', 'CORker says', 'Deficit Hawk Myth Dead', 'Tennessee Chooses, 2018', 'Democrats see new prospects in U.S. South', 'elected to Congress despite their scandals', 'In Ohio they are about to vote', 'Retaking the Senate in Tennessee', 'fighting for Net Neutrality in Knoxville', 'protest tonight at the Verizon on Gunbarrel', 'TN Democrats Vote To Support Medical Marijuana', 'Knoxville demolishes the mental health ward', 'last Democrat to win a statewide race in Tennessee', 'bredesen', 'Net Neutrality protections in North Knoxville', 'where you stand, Marsha', 'kustoff', 'tennessee governor', 'tn gubernatorial', 'gov. of tn', 'tennessee gubernatorial candidates', 'governor haslam', 'randy boyd', 'kay white', 'tn governor', 'House Budget chair', 'Diane Black', 'bill lee', 'beth harwell', 'karl dean', 'mae beavers', 'tennessee senate race', 'bob corker', 'sen. corker', 'mackler', 'blackburn', 'corker\'s u.s. senate seat', 'replace corker', 'disgusting lies about Planned Parenthood', 'Corker fight', 'baby body parts', 'Berke considering run', 'andy ogles', 'senator corker', 'Corkers seat', 'marsha blackburn', 'tn-7', 'tn-07']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Tennessee 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://ovr.govote.tn.gov/Registration/#BM): July 3, 2018 \n\n"
            "[Primary Election](http://web.go-vote-tn.elections.tn.gov/): August 2, 2018 \n\n"
            "[General Election Registration Deadline](https://ovr.govote.tn.gov/Registration/#BM): October 9, 2018 \n\n"
            "[General Election](http://web.go-vote-tn.elections.tn.gov/): November 6, 2018 \n\n")
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