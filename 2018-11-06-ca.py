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

local_subs = open("california.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.selftext)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Received this gem in my emails today', 'California Democrats fear that a proposed Census question', 'Californians know that legalizing marijuana means safer', 'Dem Midterm Wave', 'Dems retake the House', 'House Gives Trump Administration Broad Latitude to Spy on Americans', '2 Vacant Investor-Owned Homes for Every Homeless Person in America', 'New Bill in Congress Would Ban Federal Cannabis Enforcement in Legal States', 'Water-saving measures in California', 'New bill proposed to stop Sessions\' agenda', 'Republicans will keep control of Congress this year', 'jess phoenix', '1969 Santa Barbara Oil Spill', 'GOP blocking key Russia witnesses', 'Republican efforts to block access in Russia probe', 'Opposing His Own Surveillance Bill', 'ca-49', 'These House lawmakers voted to extend NSA spying and reject privacy reforms', 'not reauthorizing FISA before remembering he supports it', 'Governors want to know why Florida got out of the massive new offshore drilling plan', 'Trump Super PAC Took Illegal Donation From Private Prison Company', 'dim GOP hopes of keeping the House', '31 House Republicans won\'t seek re-election in 2018', 'Royce\'s and Issa\'s', 'Section 702 of the Foreign Intelligence Surveillance Act', 'NSA Surveillance Bill', 'We Need to Elect More Scientists to Congress.', '39th District Race to Toss-Up', 'ACLU Opposes New Surveillance Bill', 'ed royce', 'rep. royce', 'congressman royce', 'rep royce', 'ca-39', 'Car Drives Through California Protest', 'california Will be Vital for Democrats', 'Daniel Wenzek', '2016 Election Map where each 250,000 votes are represented by a figure, distributed by state', 'NextGen America launches 2018 registration', 'California Introduces Its Own Bill to Protect Net Neutrality', 'war on marijuana may become a war on small business', 'California Puts Freeze on New Uses of Bee-killing Pesticides', 'Increase the Odds Congress Will Make Marijuana Legal', 'List of Scientists Running for Congress', 'Dems Have a Very Obvious, Very Fixable Recruiting Hole', 'justify giving control of the internet to a few large corporations', 'My congressman, everyone. Sellout', 'california governor', 'oil drilling proposed off California coast', 'marijuana businesses in California', 'And if you are really rich, you don', 'andrew janz', 'Energized Battle Ahead in California', 'Republicans are selling out everything to protect their Dear Leader', 'Republican coverup on Trump and Russia', 'In states where marijuana is legal, entrepreneurs should be able to access the same banking services', 'polling looks extremely good for Democrats ', 'All California Republicans Are At Risk', 'Proposition 13 and what to do about it', 'The GOP Are Aiding and Abetting', 'Democrats need only one thing to win', 'Activist Who Confronted Caitlyn Jenner', 'Californians will vote by mail', 'vicious attack in Congress by anti-conservation zealots', 'ca-45', 'duncan hunter', 'rep. hunter', 'congressman hunter', 'rep hunter', 'ca-50', 'Can The Dems Take The House in 2018', 'We have to end the use of private prisons in the United States', 'Rackauckas', 'todd spitzer', 'orange county da ', 'orange county d.a.', 'orange county district attorney', 'gerrymandering, political reform, and saving democracy', 'A Serial Killer In Orange County', 'restorative justice for all those who had their lives destroyed', 'Southern California wildfire now largest in state history', 'with a Pen, 5 Seconds After Exiting His Patrol Car', 'progressive renaissance of 2018', 'CASEN 2018', 'expansion of mass surveillance', 'mimi walters', 'Kia Hamadanchy', 'congressional districts to target for 2018', 'devin nunez', 'Orange County Alt-Right', 'devin nunes', 'rep. nunes', 'congressman nunes', 'House Intel chief', 'Nunes Subpoenaed', 'rep nunes', 'darrell issa', 'rep. issa', 'rep issa', 'the california gop\'s last gasp', 'rohrabacher', 'michael kotick', '@danarohrabacher', 'rohrabracher', 'Transcript of McCarthy', 'pro-assange gop congressman', 'pro-putin california congressman', 'Pro-Russia GOP Rep.', 'Putin\'s congressman', 'rhorabacher', 'steve knight', 'rep. knight', 'congressman knight', 'rep knight', 'representative knight', 'ca-25', 'valadao']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("California 2018 Election \n\n"
            "[Primary Election Registration Deadline](http://registertovote.ca.gov/): May 16, 2018 \n\n"
            "[Primary Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): June 5, 2018 \n\n"
            "[General Election Registration Deadline](http://registertovote.ca.gov/): October 22, 2018 \n\n"
            "[General Election](http://www.sos.ca.gov/elections/voter-registration/vote-mail/#apply): November 6, 2018 \n\n")
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