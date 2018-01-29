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
            terms = ['Koch Network Plans to Spend ', 'Arizona, Trump Supporters Call Navajo Lawmaker', 'grijalva', 'GOPers Dismissed Bills To Protect Mueller', 'Democrats Need a Sweep to Take Senate', 'Easy for the Democrats to Take the Senate in 2018', 'Senate Dems drop Dreamer demand', '30 senators join push for immigration deal', 'is it just me or are ice agents evil people', 'facing federal charges for leaving water in the desert', 'democrats voted to confirm Azar', 'filmed dumping water left for migrants', 'Blue House Wave, but Not Yet a Senate One', 'I emailed my representative back in October, got a response today', 'Criminalize Poverty For Dreamers', 'GOP Contenders Defend President, Criticize Flake', 'Medicaid Work Requirements Could Make it Impossible to Qualify for Medicaid', 'Democrats Also Voted to Shut Down Debate on Trump Administration', 'Blue House Wave, but Not Yet a Senate One', 's. 139', 'Marijuana legalisation causing violent crime to fall', 'GOP faces brutal Arizona primary fight', 'Arizona Republican embraces Trump', 'Republicans Have 4 Convicted Criminals Running For Congress In 2018', 'Senator says she will vote to restore net neutrality', 'Senate Chances In 2018 Overrated', 'Arizona can destroy trump', 'We just need one more Republican to win in the Senate and take the fight to the House', 'everyone in Washington has known its key themes, and refused to act', 'Old racist man tries one last time to prove he is relevant', 'the best GOP have to offer', 'vote to restore net neutrality rules', 'progressive candidates running in Arizona', 'Democrats Win the Senate', '2017 the hottest year on record in the US', 'Arizona Legislature', 'Endorsement Was A Cherished Prize', 'Senate Dems united as election year begins', '14,099 Dreamers have lost their DACA status', 'Meals on Wheels slowly wither and die', 'Scottsdale lawmaker', 'For Profit Prison Gave Him Tylenol After Burning Open The Top Of His Head', 'Cop Murder Innocent Unarmed Dad Begging For His Life', 't justify every shooting', 'brailsford', 'ady barkan', 'Lea Marquez Peterson', 'states could be the next Alabama', 'States Angling to Vote on Recreational Cannabis', 'retaking the Senate in 2018', 'daniel shaver', 'arpaio', 'Handwritten Tax Cut Amendment Into The Record Because No One Can Read It', 'tax heist', 'the corporate tax break is permanent, but for regular people it', 'death to the phrase', 'Last-Minute Tax Bill With Handwritten Notes', 'Senate Passes Massive Tax Cuts For The Rich', 'evil turtle is happy', 'Entire Republican Party Is Rotten to the Core', 'The American people are catching on', 'One Of The Greatest Robberies In American History', 's richest in late-night vote', '1.5 trillion tax cut for the very wealthiest', 'republican senators, they sold out the lower class', 'gosar', 'GOP musters Senate votes to pass major tax reform bill', 'Flake to back tax bill', 'Arizona Green Party', '10 year old t1 diabetic, getting real tired of crap like this', 'Oro Valley lawmaker', 'Arizona Moms About School Vouchers', 'Advocating For The LGBTQ Community Can', 'Elitists, crybabies and junky degrees', 'ruining the economy to own the libs', 'Arizona lawmaker would outlaw masks', 'very Gets JDems Challenger', 'ducey', 'arizona governor', 'takes on McCain over health care vote', 'Trump attacks McCain and other Republicans over healthcare failure', 'permission to vote for Obamacare repeal', 'Murkowski is in the health-care spotlight. Again.', 'Obamacare Is Suddenly in Grave Danger', 'Momentum builds for Obamacare repeal', 'Revived Health Care Effort Is Just as Much of an Uphill Climb as the Last One', 'Scheme Fulfills an Old Conservative Dream', 'Arpaio Pardon Help Swing Arizona', 'az. gubernatorial race', 'arizona\'s race for governor', 'arizona gubernatorial', 'arizona\'s republican governor', 'Congressman Biggs', 'andy biggs', 'az-5', 'az-05', 'rep biggs', 'rep. biggs', 'representative biggs', 'House Republican introduces measure to defund key climate research', 'Congressman Tom O\´Halleran', '@RepOHalleran', 'o\'halleran', 'kevin cavanaugh', 'steve smith', 'Time for an anti-abortion vote in the Republican House', 'http://thehill.com/homenews/administration/348061-trump-pardons-arpaio', 'The Republican Party is responsible for the pardon of the hate criminal Joe Arpaio', 'schweikert', 'mcsally', 'early money haul stuns GOP', '12 Districts as Democrats Gain Momentum', 'Cook Political Report shifts 11 House races towards Democrats', 'missteps are giving Democrats a better shot at winning back the House', 'House Ratings changes in 12 districts as Democrats gain candidates', '^(?!.*snowflake).*flake.*$', '@jeffflake', 'sinema', 'Kelli Ward']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Arizona 2018 Election \n\n"
            "[Primary Election Registration Deadline](https://servicearizona.com/webapp/evoter/register?execution=e1s2): July 30, 2018 \n\n"
            "[Primary Election](https://www.vote.org/absentee-ballot/): August 28, 2018 \n\n"
            "[General Election Registration Deadline](https://servicearizona.com/webapp/evoter/register?execution=e1s2): October 09, 2018 \n\n"
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