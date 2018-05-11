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

local_subs = open("oklahoma.dat", "r")
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
            terms = ['Billboards encourage Oklahoma teachers to move to Texas', 'high court upholds voter ID law', 'governor of oklahoma', 'Oklahoma group cleared to collect signatures to put recreational marijuana on the ballot', 'oklahoma legislative', 'senate seat in oklahoma', 'Michael Brooks-Jimenez', 'oklahoma strike', 'Oklahoma teacher walkout', 'mary memed', 'striking okalhoma educators', 'tyson meade', 'Oklahoma Education Budget Crisis', 'Oklahoma State Capitol', 'kevin mcdugle', 'rep scott inman', 'Governor told Oklahoma Teachers to Step Up', 'ballot in oklahoma', 'oklahoma city district', 'Republicans consider the ultimate heresy', 'drew edmondson', 'oklahoma teachers free meals', 'trip to oklahoma capitol' 'more money working at a gas station than as a teacher', 'tulsa public schools to join', 'tulsa public schools teachers begin', 'State teachers union lays out demands to prevent strike', 'ranks of oklahoma teachers', 'oklahoma teachers are now striking', 'group of high schoolers in Tulsa ', 'proud of you tusla', 'oklahoma teachers planning a statewide strike', 'oklahoma prepare for statewide school walkout', 'tulsa students plan march for our lives', 'teachers talking about walkout', 'governor fallin', 'I will never truly understand Oklahoma', 'Oklahoma Senate committee', 'Senator Daniels backpedals', 'Chuck Strohm', 'jenks lawmaker', 'Oklahoma senators', 'sb1016', 'voting in Oklahoma', 'Oklahoma, if you are caught growing or selling over 25 pounds of marijuana', 'Oklahoma Lawmaker', 'State road projects on hold because of Congress budget battle', 'Oklahoma among nation', 'You\'re awesome, Tulsa', 'march in OKC today', 'Drew Edmondson', '72yo Grandma Shot Dead as SWAT Raided Her Home To Arrest Her Son For Marijuana', 'cash seized, forfeited by Oklahoma law enforcement', 'Ballot Effort to Remove Legislature from Redistricting Process', 'medical cannabis look like in Oklahoma', 'A preview of the US without pensions', 'Oklahoma Poised To Cut Off 20,000 Disabled and Elderly People', 'Oklahoma City mayor', 'GOP rep from Oklahoma', 'rep. tom cole', 'NativeVote18', 'Tax Bill Blowback Rally today', 'Oklahoma opponents of federal income tax bills', 'Tulsa forum to focus on medical marijuana', 'Gov Fallin', 'This is my governor. She', 'markwayne', 'ok-02', 'ok-2', 'oklahoma\'s 2nd District', 'Native American Candidates for Congress', 'bridenstine', 'ok-01', 'ok-1', 'oklahoma\'s 1st District', 'My Congressman Directly Opposes Net Neutrality', 'Budget Crisis in Oklahoma', 'steve russell', 'Oklahoma Democrats open door', 'mary fallin', 'Oklahoma House of Representatives and State Senate', 'any opinions on our 2018 gubernatorial election', 'Oklahoma Tried the GOP', 'Voter Registration by County', 'says ou wants students to have abortions']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Oklahoma 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://www.ok.gov/elections/Voter_Info/Register_to_Vote/): June 2, 2018 \n\n"
            "[Primary Election Date](https://services.okelections.us/AbsenteeApplication/): June 26, 2018 \n\n"
            "[General Election Date](https://services.okelections.us/AbsenteeApplication/): November 6, 2018")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write the post id back to the file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()