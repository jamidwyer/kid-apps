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
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['al-sen', 'roy moore', 'alabama senate race', ' al senate race', 'FAKE NEWS always fails to mention that the candidate I endorsed went up MANY points after endorsement', 'John Kasich Hints He May Leave the GOP', 'Democratic Party Roll Into Alabama', 'support the GOP if it doesn\'t reform', 'First Amendment only protects Christians', 'Breitbart is going to war against GOP incumbents', 'dumb it down, democrats', 'last 7 days are just mind-bogglingly bad', 'jones only 6 points behind', 'Strange Impotence of the Republican Party', 'likened the Koran to Mein Kampf and blamed 9', 'extremist candidate who thinks homosexuality should be a crime', 'Donald Trump humiliated as Senate candidate he backed loses', 'Alabama defeat leaves Trump weakened', 'Trump and his advisers are laughing in your faces', 'party of Lincoln in ruins', 'backing alabama loser', 'tweets supporting Luther Strange after he loses', 'loser, luther strange', 'backing Alabama primary loser', 'McConnell Wakes Up to His Political Nightmare', 'Trump deletes all tweets endorsing Luther Strange after he loses', 'Tweets That Show His Impotence', 'worst day of the worst week for the GOP', 'Implications of the Alabama Race for Republicans', 'eye shot at Alabama upset', 'erase all history of endorsing losing candidate', 'tweets backing Strange after primary loss', 'Alabama\'s GOP Primary', 'Trump publicly endorsed Luther Strange', 'erasing his support of Luther after his loss', 'deletes tweets backing Luther Strange', 'Trump deletes tweets backing Strange after primary loss', 'Trump deletes pro-Luther Strange tweets', 'Trump tweets backing the losing candidate in Alabama', 'Trump deleted his tweets that endorsed Luther Strange', 'Conservative firebrand defeats Trump pick', 'Republican Establishment And The Terrible', 'McConnell on Moore victory', 'Moore wins Alabama primary', 'Steve Bannon warns GOP establishment', 'Moore wins Republican Senate primary', 'Alabama may elect a senator who believes that Christian law supersedes American law', 'elections look worse for Republicans every single day', 'alabama senate election', 'Strange and Stranger', 'Republican party rages on in Alabama race', 'raucous rally in Alabama', 'Alabama may just hand them another one', 'Trump trashes McCain and McConnell on Alabama radio', 'Moore leading Strange', 'botches a Senate candidate', 'Scenarios That Could Change The 2018 Senate Map', 'This guy should not be the president', 'who he really is: A white supremacist', 'Strange in trouble in Alabama', 'The Racial Demagoguery of Trump', 'NFL Stars Erupt In Anger Over Donald Trump', 'Trump\'s Alabama speech', 'Kim Jong Un During Alabama Rally', 'NFL and NBA players are responding to Trump', '3 winners and 3 losers from Alabama', 'Alabama\'s GOP Senate Frontrunner', 'Pull Alabama Senator to Victory', 'Trump calls Colin Kaepernick a', 'false claims at Alabama rally', 'harder stance against kneeling for the national anthem than he took against Nazi', 'protecting players\' right to protest', 'Trump slams McCain', 'Trump was quicker and more vehement in his hatred of Colin Kaepernick', 's name at a political rally in Alabama', 'Alabama rally? He', 'To me, winning the popular vote is easier', 'Roy has a very good chance of not winning in the general election', 'Trump Says NFL Owners Should Fire Any', 'Trump Calls for NFL to Fire Protesting Players', 'NFL owners should fire players who kneel during anthem', 'NFL players who disrespect American flag should be fired.', 'Owners should get those SOBs off the field', 'chances against moore', 'alabama gop senate runoff', 'alabama\'s gop senate race', 'criticizes John McCain in Alabama rally', 'Behind New Obamacare Repeal Vote', 'This shit is going to pass isn', '9 to explain what it does', 'immorality, abortion, sodomy, sexual perversion sweep our land', '@lutherstrange', 'ray moore', 'Deep South Dems', 'As Bad as the GOP Is', 'GOP insurgency plans for a civil war in 2018 midterms', 'Steve Bannon is looking for retribution', 'Ala. Senate hopeful Moore', 'Trump candidate loses Alabama', 'moore didn\'t disclose at least', 'thoughts about alabama', 'reds and yellows', 'Alabama Senate frontrunner', 'alabama senate showdown', 'alabama senate primaries', 'alabama senate poll', 'sen. strange', 'senator strange', 'special election in alabama', 'alabama special election', 'Alabama Senate candidate', 'Senate Seat in Alabama', 'Alabama Senate: Special Election', 'trump voters in alabama', 'alabama sen. candidate']
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

            "Jones supports universal health care, public schools, living wages, protecting Medicare, equal pay for equal work, renewable energy, and LGBTQ equality.  \n\n "

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