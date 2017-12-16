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
            terms = ['Lea Marquez Peterson', 'states could be the next Alabama', 'States Angling to Vote on Recreational Cannabis', 'retaking the Senate in 2018', 'If police can execute an innocent man on video, none of us are safe', 'daniel shaver', 'Senate Republicans are divided over whether to pursue Medicare cuts in 2018', 'ALS confronts Senator', 'man begs for life, shot by officer', 'Brutally Killing An Unarmed Man', 'Man begs for life, shot by officer', 'Sociopathic Police Problem', 'arpaio', '6,000 lobbyists worked on the Republican tax bill', 'Seizes Assets of Anyone Who Plans or Participates in Protests', 'approve GOP Tax Plan', 'call your Senators RIGHT NOW and ask them to kill the Trump Tax Scam', 'When White People Riot', 'Why We Got Arrested in DC', 'FCC Wants to Kill Net Neutrality. Congress Will Pay the Price', 'this is class warfare', '6 GOP Senators that have to run on it', 'republicans are looting the treasury', 'Handwritten Tax Cut Amendment Into The Record Because No One Can Read It', 'tax heist', 'the corporate tax break is permanent, but for regular people it', 'death to the phrase', 'Last-Minute Tax Bill With Handwritten Notes', 'Senate Passes Massive Tax Cuts For The Rich', 'evil turtle is happy', 'Entire Republican Party Is Rotten to the Core', 'The American people are catching on', 'One Of The Greatest Robberies In American History', 's richest in late-night vote', '1.5 trillion tax cut for the very wealthiest', 'republican senators, they sold out the lower class', 'gosar', 'GOP musters Senate votes to pass major tax reform bill', 'Flake to back tax bill', 'Arizona Green Party', '10 year old t1 diabetic, getting real tired of crap like this', 'Oro Valley lawmaker', 'Arizona Moms About School Vouchers', 'Advocating For The LGBTQ Community Can', 'Elitists, crybabies and junky degrees', 'ruining the economy to own the libs', 'Arizona lawmaker would outlaw masks', 'very Gets JDems Challenger', 'ducey', 'arizona governor', 'takes on McCain over health care vote', 'Trump attacks McCain and other Republicans over healthcare failure', 'permission to vote for Obamacare repeal', 'Murkowski is in the health-care spotlight. Again.', 'Obamacare Is Suddenly in Grave Danger', 'Momentum builds for Obamacare repeal', 'Revived Health Care Effort Is Just as Much of an Uphill Climb as the Last One', 'Scheme Fulfills an Old Conservative Dream', 'Arpaio Pardon Help Swing Arizona', 'az. gubernatorial race', 'arizona\'s race for governor', 'arizona gubernatorial', 'arizona\'s republican governor', 'Congressman Biggs', 'andy biggs', 'az-5', 'az-05', 'rep biggs', 'rep. biggs', 'representative biggs', 'House Republican introduces measure to defund key climate research', 'Congressman Tom O\´Halleran', '@RepOHalleran', 'o\'halleran', 'kevin cavanaugh', 'steve smith', 'Time for an anti-abortion vote in the Republican House', 'http://thehill.com/homenews/administration/348061-trump-pardons-arpaio', 'The Republican Party is responsible for the pardon of the hate criminal Joe Arpaio', 'schweikert', 'mcsally', 'early money haul stuns GOP', '12 Districts as Democrats Gain Momentum', 'Cook Political Report shifts 11 House races towards Democrats', 'missteps are giving Democrats a better shot at winning back the House', 'House Ratings changes in 12 districts as Democrats gain candidates', '^(?!.*snowflake).*flake.*$', '@jeffflake', 'sinema', 'Kelli Ward']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Arizona 2018 Election \n\n"
            "[Primary Voter Registration Deadline](https://servicearizona.com/webapp/evoter/register?execution=e1s2): July 30, 2018 \n\n"
            "[Primary Election](https://www.vote.org/absentee-ballot/): August 28, 2018 \n\n"
            "[General Election](https://www.vote.org/absentee-ballot/): November 6, 2018 \n\n")
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
     searchAndPost(sub);

text_file.close()