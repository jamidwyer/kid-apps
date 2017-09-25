#!/usr/bin/python
# coding: utf-8

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

local_subs = open("alabama.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=100):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['luther strange', 'al-sen', 'doug jones', 'Trump trashes McCain and McConnell on Alabama radio', 'Moore leading Strange', 'botches a Senate candidate', 'Scenarios That Could Change The 2018 Senate Map', 'This guy should not be the president', 'who he really is: A white supremacist', 'Strange in trouble in Alabama', 'The Racial Demagoguery of Trump', 'NFL Stars Erupt In Anger Over Donald Trump', 'Trump\'s Alabama speech', 'Kim Jong Un During Alabama Rally', 'NFL and NBA players are responding to Trumpd', 'Alabama\'s GOP Senate Frontrunner', 'strange in alabama', 'Pull Alabama Senator to Victory', 'Trump calls Colin Kaepernick a', 'false claims at Alabama rally', 'harder stance against kneeling for the national anthem than he took against Nazi', 'protecting players\' right to protest', 'Trump slams McCain', 'Trump was quicker and more vehement in his hatred of Colin Kaepernick', 's name at a political rally in Alabama', 'Alabama rally? He', 'To me, winning the popular vote is easier', 'Roy has a very good chance of not winning in the general election', 'Trump Says NFL Owners Should Fire Any', 'Trump Calls for NFL to Fire Protesting Players', 'NFL owners should fire players who kneel during anthem', 'NFL players who disrespect American flag should be fired.', 'Owners should get those SOBs off the field', 'chances against moore', 'alabama gop senate runoff', 'alabama\'s gop senate race', 'criticizes John McCain in Alabama rally', 'Behind New Obamacare Repeal Vote', 'This shit is going to pass isn', '9 to explain what it does', 'immorality, abortion, sodomy, sexual perversion sweep our land', '@lutherstrange', 'high-stakes health-care gamble', 'Ala. Senate hopeful Moore', 'Moore stands behind use of terms widely seen as racially charged', 'US Says No Money for Social Programs', 'reds and yellows', 'Moore laments racial division between', 'Alabama Senate frontrunner', 'Messy Republican Runoff That Threatens to Divide GOP', 'Alabama GOP primary', 'alabama senate showdown', 'alabama senate primaries', 'Can the GOP survive Trump', 'interviews for Senate seat were a sham', 'Strange Has Alabama Conservatives Reeling', 'alabama senate poll', 'sen. strange', 'senator strange', 'the perfect alabama candidate', 'special election in alabama', 'alabama special election', 'Alabama Senate candidate', 'alabama senate race', 'Senate Seat in Alabama', 'How Roy Moore Won Alabama', 'Alabama Senate: Special Election', 'trump voters in alabama', 'alabama gop senate race', 'Trump-Backed Candidate in Alabama', 'alabama sen. candidate']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("[&#9733;&#9733;&#9733; Register to Vote &#9733;&#9733;&#9733;](https://www.alabamainteractive.org/sos/voter_registration/voterRegistrationWelcome.action) by Monday, November 27, 2017 \n\n"
            "General Election: December 12, 2017 \n\n"
            "[Find your polling place](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do) \n\n"

            "[**Doug Jones**](http://dougjonesforsenate.com/) is running to represent Alabama in the U.S. Senate. \n\n "
            "[Facebook](https://www.facebook.com/dougjonessenate) | "
            "[Twitter](https://twitter.com/gdouglasjones) | "
            "[Donate](https://secure.actblue.com/donate/homepage-donate) \n\n "

            "Jones supports universal health care, public schools, living wages, protecting Medicare, equal pay for equal work, and renewable energy.  \n\n "

            "^(I'm a bot and I'm learning. Let me know how I can do better. I'll add candidates who will represent working-class people instead of billionaire political donors.)")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Store the current id into our list
        posts_replied_to.append(submission.id)

for sub in subs:
     print(sub)
     searchAndPost(sub);

# Write our updated list back to the file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")

text_file.close()
local_subs.close()