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

local_subs = open("florida.dat", "r")
text_file = open("standardsubs.dat", "r")
subs = local_subs.read().split('\n')
ssubs = text_file.read().split('\n')
subs.extend(ssubs)

# Get the top 500 values from our subreddit
def searchAndPost(sub):
    subreddit = reddit.subreddit(sub)
    for submission in subreddit.hot(limit=50):
        #print(submission.title)

        # If we haven't replied to this post before
        if submission.id not in posts_replied_to:

            # Do a case insensitive search
            terms = ['Fla. shooting survivor', 'third straight day of rage tweeting', 'students who survived the attack are calling on lawmakers to act', 'Florida students plead with Congress', 'Parkland shooting survivors rail against gun laws', '17 victims of the Parkland school shooting', 'turns out the kid did get trained by a white supremacist organisation', 'National School Walkout March 14', 'Parkland slain, president has forgone golf for extra TV', 'children who are the leading voices for action', 'teen shooting survivors announce march on Washington, demanding ', 'Students seize control of gun debate', 'Which is one more presidential', 'your team is proposing to dismantle the background check system?', 'NRA-sponsored massacre of our children', 'Mass shooting survivor to Donald Trump', 'supposed to bring this nation together, not divide us', 'Florida shooting survivors vow not to return to school', 'Rush Limbaugh defends NRA', 'march for our lives', 'Emma Gonzalez calls out the NRA ', 'Florida high school shooter to Russia', 'let American children get murdered in American schools on American soil', 'use the death of children, in an attempt to tarnish the FBI', 'NRA as nothing less than a terrorist organization', 'using the deaths of 17 people gunned down at a school to attack the FBI', 'Fort Lauderdale rally demands gun restrictions', 'a sweeping failure to enforce the law', 'Blaming Shooting On Russia Probe', 'orange shitgoblin was in Parkland', 'Parkland student on Trump', 'FBI consists of 6 guys named Moe', 'Florida teen shooting survivors', 'And yet you would use massacre victims', 'Mayors stand with residents demanding action on guns', 'Nikolas Cruz close shop indefinitely', 'Not Elected To Offer Thoughts and Prayers', 'skipping golf to honor the Florida shooting victims', 'Florida students want to be tipping point in gun debate', '10,000 to Train Nikolas Cruz in 2016', 'Disco Party After Meeting with Florida Shooting', 'Florida school massacre', 'Parkland shooting survivors rail against NRA', 'Dem criticizes Trump for ', 'FBI missed Florida shooter ', 'school shooting in Florida', 'Russian trolls flood Twitter after shooting', 'Bulletproof backpack sales rise in wake of mass school shooting', 'Sit-Ins Planned after Florida Shooting', 'Ignoring Parkland Shooting Victims', 'NRA, Russia and Trump', 'I will not write another check', 'Trump at Florida anti-gun rally', 'The new NRA logo. Designed for us to fight back.', 'Gun violence costs society at least ', 'message to politicians at anti-gun rally', 'Calls Out Trump and NRA at Gun Control Rally', 'Republican Donor Issues Ultimatum on Assault Weapons', 'Republicans are not going to do a single thing after this shooting we saw today', 'Russian effort to bamboozle Florida', 'sold AR-15 to school shooter Nikolas Cruz', 'Trump Ignores Shooting Victims', 's all political statements', 'Stupid Tammy', 'the power of Prayer is insufficient to stop bullets from killing school children', 'Florida Shooting Suspect Took Part in Training Program That Received NRA Grant', 'should not have to be worrying about light up shoes', 'Shake Us Out of Our Mass Shooting Stupor', 'Walkout To Protest Gun Violence', 'FL Shooter Had Record of Death Threats', 'Remember these feelings in November, and VOTE.', 'This is the third mass shooting she', 'Parkland survivor slams GOP', 'Republicans will never do anything', 'vote in Florida, but you can buy a gun', 'Florida Shooter\'s Instagram', 'You guys are the adults', 'stfu tomi', 'Instagram Profile Contains Trump MAGA Hat', 'Florida high school shooting', 'AR-15 assault rifle before they can legally buy a beer', 'hiding from gunman in Florida high school', 'open, violent clash involving guns', 'no evidence he even tried', 'Blames Mental Health Issues for Florida Shooting', 'time to talk about gun laws', 'Instagram profile picture of Nikolas Cruz', 'Only Nation Where This Regularly Happens', 'NRA money to help fight gun control', 'Democrat Upsets Republican Incumbant', 'New report gives Florida an', 'If guns were as dangerous as a woman', 'Thoughts and prayers right', 'Next week gun legislation will fail', 'florida school shooting', 'Big win in Sarasota, FL', 'Democrats Win Big Upset in Florida Special Election', 'Republican-held Florida state legislative', 'margaret good', 'Florida woman forced to marry her rapist at 11 years old', 'Miami congressional campaign', 'Desperate Republicans turn to Adelson', 'Democrats Are Targeting 12 States to Prevent Another Decade of GOP Gerrymandering', 'run for Jacksonville City Council', 'Restoration of Felon Voting Rights Federal Case', 'Posey for Congress', 'Judge strikes down Florida', 'lifetime ban on voting by felons is unconstitutional, federal judge rules', 'Florida system for restoring felons', 'Peters4Congress', 'Florida congressman', 'Republican congressman invited notorious Holocaust denier', 'alt-right activist to the State of the Union', 'philip levine', 'sean shaw', 's congressional delegation stands on Trump', 'Proposed Florida amendment', 'vote in Florida', 'victor torres', 'mayor gillum', 'Florida Congressional District 3', '10-year-old got flooded out of his school', 'Floridians will vote this fall', 'Florida voters', 'CustomsBorder got on a Greyhound bus yesterday in Ft Lauderdale', 'Vacation rentals become focal point of state', 'florida legislature', 'Floridians will elect a new governor', 'LGBT advocate for the pulse nightclub memorial', 'Anna Eskamani', 'Impeachment March to Mar-a-lago', 'FL House district 31', 'matt haggman', 'Marijuana legalisation causing violent crime to fall in US states, study finds', 'Kelly Smith for Pasco County Commissioner', 'Tampa progressives denounce GOP agenda', 'Orlando Lawmakers', 'Palm Beach County officials looking for small legislative wins in 2018', 'ron reid', '1.5 Million Missing Voters', 'bilirakis', 'Recreational marijuana in Florida', 'Florida is arguably one of if not the most important swing state', 'The Russians Meddled In The Election, We All Know That', 'Trump Donors Funding GOP Rep Who', 'Florida by Itself Can End the Electoral College', 'Congress Care When Israel Kills American Citizens', 'They\'re acting like dictators', 'Florida Cannabis Act', 'latvala', '^(?!.*gov. scott walker).*gov. scott.*$', 'Florida HD-58', 'gaetz', '2018 congressional races in Florida', 'rick scott', 'Florida Democratic governor', '^(?!.*governor scott).*governor scott.*$', 'florida governor', 'fla. governor', 'governor of florida', 'curbelo', 'brian mast', 'rep mast', 'rep. mast', 'representative mast', 'congressman mast', 'fl-18', 'lehtinen', 'fl-27', 'desantis', 'dennis ross', 'fl-15', 'andrew learned', 'balart', 'fl-25']
            for term in terms:
                 search(term, submission);

def search(term, submission):
    if re.search(term, submission.title, re.IGNORECASE):
        # Reply to the post
        text = ("Florida 2018 Election \n\n"
            "[Primary Election Voter Registration Deadline](https://registertovoteflorida.gov/en/Registration/Eligibility): July 30, 2018 \n\n"
            "[Primary Election](http://dos.myflorida.com/elections/for-voters/voting/absentee-voting/): August 28, 2018 \n\n"
            "[General Election Voter Registration Deadline](https://registertovoteflorida.gov/en/Registration/Eligibility): October 9, 2018 \n\n"
            "[General Election](http://dos.myflorida.com/elections/for-voters/voting/absentee-voting/): November 6, 2018 \n\n")
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