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
            terms = ['poll on alabama senate', 'Republicans in Congress refuse to do anything about it', 'The Onion nails it again', 'donate what you can to help Doug', 'condemn moore', 'Democrats Need to Hold Hearings on Trump', 'calls for a woman to replace him', 'real accountability for both parties', 'Al Franken resigns from Senate', 'touch the poop', 'touch poop', 'Moores allegations', 'the Democratic Party and The Black Vote', 'only one of our two great parties has any integrity', 'franken and moore', 'refund of donation to Moore campaign', 'A plea to Alabama voters', 'elect a child molester', 'When someone says that both parties are the same...', 'elect another accused sexual predator', 'Moore will face ethics complaint if elected', 'Organization Helps Disgraced Pedophiles Rebuild Their Lives By Getting Them Elected To Political Office', 'gravis poll in alabama', 'support for moore', 's called the Senate GOP Conference', 'The GOP Has Become A Dangerous Cult', 'trashing the FBI to endorse a child molester', 'people of Alabama decide', 'Jones rallies black voters', 'oppose Moore', 'Democrat Wins Alabama', 'Moore up 1 in Alabama', 'to raise a large family', 'alabama senate result', 'Hijacked the Alabama Election', 'moore campaign', 'alabamians will get it', 'democrat in alabama', 'Allegations Against Moore', 'lee busby', 'Question about write in candidates', 'Republican candidate accused of child sex abuse', 'Republican congressmen, and others who don’t want to acknowledge Moore', 'Republican accused of child sexual abuse', 'Senate Candidate Accused of Sexual Misconduct by 9', 'If Democrats Take Back the Senate', 'al-sen', '@mooresenate', 'doug jones', 'roy moore', 'moore in alabama', 'democrat jones', 'jones leads moore', 'Moore trails Jones', 'Jones beating Moore', 'moore scandal', 'moore accuser', 'moore lawyer', 'NEW ALABAMA POLL', 'stupid face of a soulless, intellectually corrupt party', 'the guy who lost Alabama', 'the party of trump and moore', 'on GOP establishment may backfire with first battle', 'Moore stands with homophobic supporters', 'Democrats Will Win the House and Senate', 'I have no reason to disbelieve', 'asking Strange to resign', 'rising Dem odds in Alabama', 'moore mud', 'Bannon to stick with Moore', 'If The Democrat Won In Alabama', 'Black Voters Could Help Democrats Replicate Virginia', 'Disloyalty to Moore', 'explain allegations or else he must exit race', 'Hannity breaks with Moore', 'RNC cuts off Moore', 'Democrats Need To Win In Alabama To Take The Senate', 'days as majority leader', 'no reason to doubt these young women', 'Mo Brooks sticking by Moore', 'unfit for office', 'opportunity in the South after Virginia rout', 'Bold Predictions for Democrats in 2018', 'predatory behavior at mall', 'write-in campaign against Moore', 'i believe the women', 'Moore accusations', 'Moore at 55%, Jones at 45%', 'evangelicals more likely to vote for Moore after allegations', 'Jones takes lead against Moore', 'jones takes the lead', 'Jones Down 48-46', 'The Swine of Conservatism', 'Hannity after Moore coverage', 'dangerous to have as a senator a man who places God', 'Roy dated high school girls', 'Former Moore colleague', 'Fox News And Steve Bannon Invited To Go Fuck Themselves', 'Key Takeaways From Steve Bannon', 'moore is unfit for office', 'judge moore', 'senate race in alabama', 'Moore Fundraising Appeals', 'moore to drop out', 'Moore to step down', 'moore/jones', 'Moore for Senate', 'MOORE And jones', 'Conservatives appeasing right-wing crackpots rather than deflating them', 'The end of the conservative Republican', 'The Republican purge has only just begun', 'love to be able to look my grandkids in the eye, but if I do', 'What the Trump Abyss Looks Like', 'How Trump Has Reshaped the GOP', 'The fate of America is at stake', 'Has Strange or Shelby actually bothered to excuse why they', 'Steve Bannon Is Kicking Our Ass', 'Bends Toward Trump, Critics Either Give In or Give Up', 'Dems lead 50-35 on generic ballot', 'Conservatives are appeasing right-wing crackpots', 'As GOP Senators Bail, Republicans Are Learning What A Trump Party Looks Like', 'one of these put up alongside 565', 'what steve Bannon told the California Republican Party', 'Moore as income to IRS', 'Injuring The Gop In Alabama', 'Koch donors and Bannon take aim', 'as Republican feud rages', 'I can\'t support the GOP if it doesn', 'Kasich Hints That He May Need To Leave The GOP', 'Steve Bannon renews call for war', 'Chill in the air as McConnell', 'Bannon after interview declaring war on GOP', 'GOP Landslide 2018', 'Nobody can run and hide', 'Steve Bannon\'s Republican insurgency', 'conservative donors may still punish Republicans in 2018', 'Unraveling Could Lead to a Major Democratic Wave', 'The unraveling of Donald J. Trump', 'Corker Is Just the Beginning of Trump', 'Steve Bannon thinks DJT has a 30', 'I Hate Everyone in the White House!', 'some of the stuff in here is pretty horrifying', 'Why Republicans Are Starting to Worry About the Trump Presidency', 'could cost them the Senate', 'Bob Corker and the Disgrace of Republican Silence', 'war against Mitch McConnell', 'path to Senate majority in 2018', 'alabama senate race', ' al senate race', 'alabama senate election', 'Alabama\'s GOP Senate Frontrunner', 'alabama\'s gop senate race', '@lutherstrange', 'ray moore', 'Deep South Dems', 'Ala. Senate hopeful Moore', 'reds and yellows', 'alabama senate poll', 'sen. strange', 'senator strange', 'special election in alabama', 'alabama special election', 'Alabama Senate candidate', 'Senate Seat in Alabama', 'Alabama Senate: Special Election', 'trump voters in alabama', 'alabama sen. candidate']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Alabama Senate Special Election 2017 \n\n"
            "[Non-Military Absentee Postmark Date](http://sos.alabama.gov/alabama-votes/voter/absentee-voting): December 11, 2017 \n\n"
            "[General Election](https://myinfo.alabamavotes.gov/VoterView/PollingPlaceSearch.do): December 12, 2017 \n\n")
        print("Bot replying to : ", submission.title)
        try:
            submission.reply(text)
        except Exception:
            print("Error : ", submission.title)
            pass

        # Write the post id to the tracking file
        with open("posts_replied_to.txt", "a") as f:
            f.write(submission.id + "\n")

for sub in subs:
     print(sub)
     searchAndPost(sub);

text_file.close()
local_subs.close()