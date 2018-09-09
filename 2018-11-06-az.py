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
            terms = ['Played Golf During John McCain', 'invest in ed initiative', 'jerry demings', 'flag after mccain death', 'mccain gets the last word', 'white house flag back to full staff', 'elected in arizona', 'az voter guide', 'arizona congress', 'voted for Neil Gorsuch', 'Baby Appears In Immigration Court', '1-Year-Old Boy Faces Immigration Judge', 'Law, Order, and Justice', 'deadweight donald', 'az-sen', 'Kids detained in shelters by Trump', 'Phoenix ICE facility', 'arizona bill', 'mesa police', 'People rally in Mesa', 'haspel', 'arizona gop lawmaker', 'az education bill', 'kelly townsend', 'HB2663', 'arizona teacher strike', 'arizona teachers rally', 'arizona state capitol', 'AZ RedForEd', 'az08', 'education funding in arizona', 'Man Protests on Street Corner of Red State Arizona', 'All Governor Races in 2018, rated. Update', 'arizona teachers demand', 'DeWit to resign', 'Bill to undermine possible renewable energy', 'zinke blames free visits' '16 laggards', 'dismantle dodd-frank', 'Republican Congress deregulate the banks', 'bank deregulation bill', 'because that makes sense.', 'sanders speaks at a rally in phoenix', 'arizona teacher here', 'azsen', 'selling out on bank regulation', 'dismantle Dodd-Frank', 'roll back parts of the Dodd-Frank', 'az 06', 'congressman gallego', 'Senate Republicans vote to expand gun access for mentally impaired', 'Help Get One More Vote in the Senate To Protect Net Neutrality', 'scott menor', 'school vouchers in Arizona', 'grijalva', 'GOPers Dismissed Bills To Protect Mueller', 'Democrats Need a Sweep to Take Senate', 'Democrats to Take the Senate', 'Arizona primary', 'Arizona Republican', 'candidates running in Arizona', 'Democrats Win the Senate', 'Arizona Legislature', 'Meals on Wheels slowly wither and die', 'Scottsdale lawmaker', 'For Profit Prison Gave Him Tylenol After Burning Open The Top Of His Head', 'Cop Murder Innocent Unarmed Dad Begging For His Life', 't justify every shooting', 'brailsford', 'ady barkan', 'Lea Marquez Peterson', 'states could be the next Alabama', 'States Angling to Vote on Recreational Cannabis', 'retaking the Senate in 2018', 'daniel shaver', 'arpaio', 'tax heist', 'gosar', 'Arizona Green Party', '10 year old t1 diabetic, getting real tired of crap like this', 'Oro Valley lawmaker', 'Arizona lawmaker',  'ducey', 'arizona governor', 'az. gubernatorial race', 'arizona\'s race for governor', 'arizona gubernatorial', 'arizona\'s republican governor', 'Congressman Biggs', 'andy biggs', 'az-5', 'az-05', 'rep biggs', 'rep. biggs', 'representative biggs', 'House Republican introduces measure to defund key climate research', 'Congressman Tom O\´Halleran', '@RepOHalleran', 'o\'halleran', 'kevin cavanaugh', 'steve smith', 'Time for an anti-abortion vote in the Republican House', 'http://thehill.com/homenews/administration/348061-trump-pardons-arpaio', 'The Republican Party is responsible for the pardon of the hate criminal Joe Arpaio', 'schweikert', 'mcsally', 'early money haul stuns GOP', '12 Districts as Democrats Gain Momentum', 'Cook Political Report shifts 11 House races towards Democrats', 'missteps are giving Democrats a better shot at winning back the House', 'House Ratings changes in 12 districts as Democrats gain candidates', '^(?!.*snowflake).*flake.*$', '@jeffflake', 'sinema', 'Kelli Ward']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Arizona 2018 Election \n\n"
            "[General Election Registration Deadline](https://servicearizona.com/webapp/evoter/register?execution=e1s2): October 9, 2018 \n\n"
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