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
            terms = ['Handwritten Tax Cut Amendment Into The Record Because No One Can Read It', 'tax heist', 'the corporate tax break is permanent, but for regular people it', 'death to the phrase', 'Last-Minute Tax Bill With Handwritten Notes', 'Senate Passes Massive Tax Cuts For The Rich', 'evil turtle is happy', 'Entire Republican Party Is Rotten to the Core', 'The American people are catching on', 'One Of The Greatest Robberies In American History', 's richest in late-night vote', '1.5 trillion tax cut for the very wealthiest', 'republican senators, they sold out the lower class', 'gosar', 'GOP musters Senate votes to pass major tax reform bill', 'Flake to back tax bill', 'Arizona Green Party', '10 year old t1 diabetic, getting real tired of crap like this', 'Oro Valley lawmaker', 'Arizona Moms About School Vouchers', 'Advocating For The LGBTQ Community Can', 'Elitists, crybabies and junky degrees', 'ruining the economy to own the libs', 'Arizona lawmaker would outlaw masks', 'very Gets JDems Challenger', 'ducey', 'arizona governor', 'takes on McCain over health care vote', 'Trump attacks McCain and other Republicans over healthcare failure', 'permission to vote for Obamacare repeal', 'Murkowski is in the health-care spotlight. Again.', 'Obamacare Is Suddenly in Grave Danger', 'Momentum builds for Obamacare repeal', 'Revived Health Care Effort Is Just as Much of an Uphill Climb as the Last One', 'Scheme Fulfills an Old Conservative Dream', 'Arpaio Pardon Help Swing Arizona', 'az. gubernatorial race', 'arizona\'s race for governor', 'arizona gubernatorial', 'arizona\'s republican governor', 'Congressman Biggs', 'andy biggs', 'az-5', 'az-05', 'rep biggs', 'rep. biggs', 'representative biggs', 'House Republican introduces measure to defund key climate research', 'Congressman Tom O\´Halleran', '@RepOHalleran', 'o\'halleran', 'kevin cavanaugh', 'steve smith', 'trent franks', 'rep. franks', 'rep franks', 'congressman franks', 'representative franks', 'Time for an anti-abortion vote in the Republican House', 'http://thehill.com/homenews/administration/348061-trump-pardons-arpaio', 'The Republican Party is responsible for the pardon of the hate criminal Joe Arpaio', 'schweikert', 'mcsally', 'early money haul stuns GOP', '12 Districts as Democrats Gain Momentum', 'Cook Political Report shifts 11 House races towards Democrats', 'missteps are giving Democrats a better shot at winning back the House', 'House Ratings changes in 12 districts as Democrats gain candidates', '^(?!.*snowflake).*flake.*$', '@jeffflake', 'sinema', 'Kelli Ward', 'No Reason To Think Republicans Will Be In Better Shape', 'Most and Least Popular Senators', 'GOP senators dismiss calls for bill to protect Mueller from Trump', 'Congress can stop Trump from starting World War', 'Millennials will shape future of GOP', 'Conservatives to Trump critic McSally', 'Democrats are split on whether to support Trump', 'thank you for saying mean things to the bad man', 'fake things true and true things fake', 'The Happy Hooker Conservatives', 'Republicans won\'t quit Trump', 'GOP braces for what’s next amid Corker, Flake tumult', 'Republicans Need a Better Response Besides Quitting', 'Republican senators attacks on Donald Trump', 'Welcome to the Senate Mr. Arpaio', 'Female candidates are targeting 3 key Senate seats in 2018', 'As midterms approach, GOP', 'Dangerous Slopes Ahead for GOP in Arizona', 'Arizona is in violation of National Voter Registration Act']
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