print("""
DEV MENU

1. Start Game
2. Test Assembly
3. Test Cricket
""")
dev_choice = input("Choose: ")
if dev_choice == "3":
    # give test stats
    teacher = 50
    student = 50
    goat_popularity = 35
    friend_popularity = 20
    stability = 55
    goat_relationship = 50

    # jump straight to Cricket

teacher = 50
student = 50
goat_popularity = 35
friend_popularity = 20
stability = 55
goat_relationship = 50

print("""
SUPREME STUDENT ADMINISTRATOR

DATE: Monday, 7:42 AM

You arrive at school.

A notice is hanging outside the office.

IMPORTANT ADMINISTRATIVE ANNOUNCEMENT

Due to an unfortunate clerical misunderstanding,
the following positions have been merged:

• Head Boy
• Chess Captain
• Cricket Representative
• Corridor Discipline Monitor
• Lunch Queue Supervisor
• Assistant IT Technician

The resulting office shall be known as:

SUPREME STUDENT ADMINISTRATOR

Congratulations.

You have been appointed.
""")
input("\nPress Enter to continue...")
print("""
CURRENT SITUATION REPORT

Issue #1: Assembly Crisis

The scheduled speaker has not arrived.

Assembly begins in 20 minutes.

Issue #2: Cricket Crisis

The cricket team is playing football.

The football team is playing cricket.

Issue #3: Projector Crisis

The projector is displaying a potato.

Additional Observation:

A goat has entered school grounds.

Support for the goat appears unusually high.

Several students have begun referring to it as:

"The People's Candidate."

The principal closes the folder.

"Handle it."
""")
input("\nPress Enter to continue...")

print("""
ASSEMBLY CRISIS

The scheduled speaker has not arrived.

Assembly begins in 20 minutes.

The principal turns to you.

"Administrator. We need a speech."

Choose your response:

A. Fiery Speech

B. Neutral Speech

C. Anti-Goat Speech

D. Pro-Goat Speech
""")

while True:
    choice = input("Choose A, B, C or D: ").upper()

    if choice in ["A", "B", "C", "D"]:
        break

    print("Invalid choice. Please choose A, B, C, or D.")
if choice == "A":
    student += 10
    teacher += 5
    stability += 5

    print("""
The students seem impressed by your confidence.

Several begin discussing your promises before assembly has even ended.

Teachers appreciate the initiative, although a few privately question whether the situation truly required such dramatic language.

For the first time that morning, the school feels slightly less chaotic.""")

if choice == "B":
    teacher += 10
    stability += 5
    print("""
The speech proceeds without incident.

Teachers approve of the professional tone and measured response.

Most students listen politely before immediately returning to more important matters, such as lunch and the goat.

The assembly concludes peacefully.""")

if choice == "C":
    teacher += 15
    student -= 10
    goat_popularity += 5
    goat_relationship -= 15
    print("""Teachers strongly approve of your commitment to maintaining order.

Unfortunately, many students had not been thinking about the goat until you mentioned it repeatedly.

By lunchtime, several new goat-related posters have appeared around the school.

The goat remains silent on the matter.""")

if choice == "D":
    teacher -= 20
    student += 15
    goat_popularity += 15
    goat_relationship += 15 
    print("""The students respond enthusiastically.

Several applaud.

One student begins taking notes on the goat's leadership philosophy.

Teachers exchange concerned looks.

The principal briefly closes their eyes and reconsiders several recent administrative decisions.

The goat appears pleased.""")

print("\n--- DEBUG STATS ---")
print("Teacher Approval:", teacher)
print("Student Approval:", student)
print("Goat Popularity:", goat_popularity)
print("Friend Popularity:", friend_popularity)
print("Stability:", stability)
print("Goat Relationship:", goat_relationship)

input("\nPress Enter to continue...")
print ("""
 CRICKET CRISIS

You arrive at the sports ground.

The cricket team is playing football.

The football team is playing cricket.

Both teams insist this is intentional.

The PE teacher is having a minor existential crisis.
Choose your response: 
Option A: Restore order
Option B: Let them continue
Option C: Create hybrid Sports
Option D: Recruit the Goat as Coach
""")
while True:
    choice = input("Choose A, B, C or D: ").upper()

    if choice in ["A", "B", "C", "D"]:
        break

    print("Invalid choice. Please choose A, B, C, or D.")
if choice == "A":
    student -= 5
    teacher += 10
    stability += 10

    print("""
"Cricket plays cricket.
Football plays football."

The teams are reluctantly returned to their assigned sports.

The PE teacher appears relieved.

Several students complain that the administration
has "no vision."

Order is restored.""")

if choice == "B":
    teacher -= 10
    stability -= 5
    student += 10
    print("""
"If they're happy, they're happy."

The students enthusiastically continue
their sporting experiment.

The PE teacher spends several minutes
staring into the distance.

The students declare this
the best sports period in months.""")

if choice == "C":
    teacher -= 5
    student += 10
    stability += 5
    print("""
After careful consideration,
you merge both sports.

The new sport shall be known as:

CRICKETBALL

Nobody fully understands the rules.

This does not stop anyone from playing.

A heated debate begins over whether
a wicket counts as a goal.

The PE teacher develops a second
existential crisis.""")

if choice == "D":
    teacher -= 15
    student += 5
    goat_popularity += 10
    goat_relationship += 10
    print("""You decide that conventional leadership
has failed.

The goat is appointed temporary coach.

The goat enters the field.

Both teams immediately stop arguing.

Nobody knows why.

The PE teacher files several complaints.

The goat's popularity continues to grow.

""")

print("\n--- DEBUG STATS ---")
print("Teacher Approval:", teacher)
print("Student Approval:", student)
print("Goat Popularity:", goat_popularity)
print("Friend Popularity:", friend_popularity)
print("Stability:", stability)
print("Goat Relationship:", goat_relationship)

input("\nPress Enter to continue...")

print ("""
POTATO PROJECTOR CRISIS
You arrive in the IT room.

The projector is displaying a potato.

Nothing else.

Slides? Potato.

Desktop? Potato.

School logo? Potato.

The IT teacher has spent 45 minutes attempting repairs.

The potato remains.
Choose your response: 
Option A: Student Solution.
Option B: Proper Repairs
Option C: Embrace Potato
Option D: Replace Potato with Goat
""")


while True:
    choice = input("Choose A, B, C or D: ").upper()

    if choice in ["A", "B", "C", "D"]:
        break

    print("Invalid choice. Please choose A, B, C, or D.")
if choice == "A":
    student += 10
    teacher -= 5
    stability += 10
    print("""
"Have you tried turning it off and on again?"

A student suggests restarting the projector.

You reluctantly try it.

The projector immediately returns to normal.

The students celebrate.

The IT teacher stares silently at the floor.""")

if choice == "B":
    teacher += 10
    student -= 5
    stability += 5
    print("""
Send the projector for professional repairs.

The projector is removed and sent to a service center.

Teachers approve of the responsible approach.

Students are disappointed because there is now no projector at all.""")

if choice == "C":
    teacher -= 5
    student += 5
    stability -= 10
    print("""
Declare the potato an educational resource.

You announce:

"The potato will remain until further notice."

The administration introduces:

ADVANCED POTATO STUDIES

as a temporary enrichment program.

Teachers are extremely confused.""")

if choice == "D":
    teacher -= 10
    student += 5
    goat_popularity += 15
    goat_relationship += 10
    stability -= 5
    print("""If a potato can be displayed,

so can a goat.

The IT department is ordered to replace the potato image with a live image of the goat.

Several students applaud.

The goat appears pleased.

The IT teacher requests a transfer.""")

print("\n--- DEBUG STATS ---")
print("Teacher Approval:", teacher)
print("Student Approval:", student)
print("Goat Popularity:", goat_popularity)
print("Friend Popularity:", friend_popularity)
print("Stability:", stability)
print("Goat Relationship:", goat_relationship)

input("\nPress Enter to continue...")

print("""
========================
DAY 1 COMPLETE
========================

The principal closes the office door.

A folder is placed on the desk.

"Administrator."

"We have reviewed today's performance."

The principal adjusts their glasses.

"Here are our findings."
""")

# STUDENT APPROVAL

if student <= 20:
    print("""
STUDENT APPROVAL: REVOLT RISK

The student body appears to actively dislike you.

Several petitions have been submitted.

Most contain spelling mistakes.

This does not make them less concerning.
""")

elif student <= 40:
    print("""
STUDENT APPROVAL: UNPOPULAR

Students generally avoid supporting you.

Your approval ratings remain low.

The goat is currently polling higher.
""")

elif student <= 60:
    print("""
STUDENT APPROVAL: TOLERATED

Students do not strongly support you.

However, they also do not strongly oppose you.

This is considered progress.
""")

elif student <= 80:
    print("""
STUDENT APPROVAL: POPULAR

Students appear satisfied with your leadership.

Several have begun defending your decisions.

This is unusual.
""")

else:
    print("""
STUDENT APPROVAL: STUDENT LEGEND

Your popularity has reached remarkable levels.

Several students have requested autographs.

One student has started a fan club.

The administration is monitoring the situation.
""")

# TEACHER APPROVAL

if teacher <= 20:
    print("""
TEACHER APPROVAL: FIRED

"We do not like you."

The principal pauses.

"We REALLY do not like you."

Termination paperwork is being prepared.
""")

elif teacher <= 40:
    print("""
TEACHER APPROVAL: UNDER INVESTIGATION

Teachers have expressed concerns.

Several meetings have been scheduled.

None of them sound encouraging.
""")

elif teacher <= 60:
    print("""
TEACHER APPROVAL: ACCEPTED

Teachers remain willing to work with you.

This is considered acceptable.
""")

elif teacher <= 80:
    print("""
TEACHER APPROVAL: TRUSTED

Staff confidence remains high.

Your decisions are generally respected.

The complaints box has become quieter.
""")

else:
    print("""
TEACHER APPROVAL: PRINCIPAL'S FAVORITE

The principal appears extremely satisfied.

This is beginning to concern other teachers.
""")
if teacher <= 20:
    print("""
=================================
GAME OVER
=================================

The principal closes the folder.

"We appreciate your efforts."

The principal pauses.

"Actually, no we don't."

Your administrative appointment has been terminated.

The office keys are confiscated.

The goat watches silently.

DAY 1 FAILED
""")

    input("\nPress Enter to exit...")
    quit()
# STABILITY

if stability <= 20:
    print("""
STABILITY: COLLAPSE

The school appears to be disintegrating.

Nobody knows who is responsible anymore.

There are rumors the goat has taken over three committees.
""")

elif stability <= 40:
    print("""
STABILITY: CRISIS

The situation remains unstable.

New problems continue to emerge faster than old ones disappear.
""")

elif stability <= 60:
    print("""
STABILITY: FUNCTIONAL

The school continues to operate.

This is considered a success.
""")

elif stability <= 80:
    print("""
STABILITY: STABLE

Order has largely been restored.

The administration appears competent.

For now.
""")

else:
    print("""
STABILITY: MODEL SCHOOL

The school has become surprisingly efficient.

Nobody understands how this happened.
""")

# GOAT POPULARITY

if goat_popularity <= 20:
    print("""
GOAT POPULARITY: JOKE CANDIDATE

The goat is not considered a serious contender.

Most students are laughing.

The goat remains confident.
""")

elif goat_popularity <= 40:
    print("""
GOAT POPULARITY: LOCAL MEME

Support remains limited.

However, the movement continues to grow.
""")

elif goat_popularity <= 60:
    print("""
GOAT POPULARITY: SERIOUS CAMPAIGN

The goat is now being discussed as a legitimate candidate.

The principal is uncomfortable with this development.
""")

elif goat_popularity <= 80:
    print("""
GOAT POPULARITY: MAJOR THREAT

The goat is polling surprisingly well.

Several teachers have requested explanations.

None have been provided.
""")

else:
    print("""
GOAT POPULARITY: GOAT MANIA

The movement has exceeded expectations.

The goat arrives to applause.

This is not normal.
""")

# FRIEND POPULARITY

if friend_popularity <= 20:
    print("""
FRIEND POPULARITY: UNKNOWN

Most students are unsure who your friend is.

This may become a problem during elections.
""")

elif friend_popularity <= 40:
    print("""
FRIEND POPULARITY: RECOGNIZED

Students know your friend exists.

This is a promising start.
""")

elif friend_popularity <= 60:
    print("""
FRIEND POPULARITY: COMPETITIVE

Your friend is now considered a legitimate candidate.

Campaign staff are optimistic.
""")

elif friend_popularity <= 80:
    print("""
FRIEND POPULARITY: POPULAR CANDIDATE

Support continues to grow.

The election is becoming competitive.
""")

else:
    print("""
FRIEND POPULARITY: ELECTION FAVORITE

Your friend has emerged as the clear frontrunner.

Other candidates are becoming nervous.
""")

# GOAT RELATIONSHIP

if goat_relationship <= 20:
    print("""
GOAT RELATIONSHIP: HATRED

The goat strongly dislikes you.

This is unlikely to end well.
""")

elif goat_relationship <= 40:
    print("""
GOAT RELATIONSHIP: UNFRIENDLY

Relations remain poor.

The goat avoids eye contact.
""")

elif goat_relationship <= 60:
    print("""
GOAT RELATIONSHIP: INDIFFERENT

The goat acknowledges your existence.

No further comment has been provided.
""")

elif goat_relationship <= 80:
    print("""
GOAT RELATIONSHIP: FRIENDLY

The goat appears willing to cooperate.

This is probably useful.
""")

else:
    print("""
GOAT RELATIONSHIP: BUDDIES

The goat appears to consider you a trusted ally.

Several members of the Goat Movement approve.
""")

input("\nPress Enter to continue...")

print("""
=================================
SPECIAL ANNOUNCEMENT
=================================

The principal closes the folder.

"There is one final matter."

The office door suddenly opens.

A group of students enters carrying campaign posters.

At the front stands the goat.

The posters read:

GOAT FOR ADMINISTRATOR

The principal stares silently.

The goat stares back.

Neither side blinks.

After several uncomfortable seconds, the principal sighs.

"Student elections will begin tomorrow."

Official Candidates:

• Your Friend
• The Goat
• Candidate #3
• Candidate #4

DAY 1 COMPLETE

ACT 2: ELECTION SEASON""")

input("\nPress Enter to continue...")

print("""
 ELECTION CAMPAIGN.

The corridors are covered in posters.

Most support your friend.

A surprising number support the goat.

One poster simply reads:

"HE HAS NEVER FAILED A TEST."

Nobody knows who created it.

Choose your response:
Option-A Support Friend
Option-B Remain Neutral.
Option-C Remove Posters.
Option-D Allow Goat Posters.""")

while True:
    choice = input("Choose A, B, C or D: ").upper()

    if choice in ["A", "B", "C", "D"]:
        break

    print("Invalid choice. Please choose A, B, C, or D.")
if choice == "A":
    friend_popularity += 10
    goat_popularity -= 5
    print("""
You quietly authorize additional poster space
for your friend's campaign.

Within hours, new posters appear across the school.

"EXPERIENCE. LEADERSHIP. HUMAN."

Supporters begin distributing campaign leaflets.

The goat movement responds by placing a goat poster
directly beside every new poster.

The poster war has begun.""")

if choice == "B":
    teacher += 5
    stability += 5
    print("""
You announce that the administration
will not interfere in the election.

Campaign teams are permitted to operate freely.

Teachers approve of your professionalism.

Students immediately accuse you
of secretly supporting somebody anyway.

Nobody is satisfied.

The election continues.""")

if choice == "C":
    teacher += 10
    student -= 10
    
    print("""
You order all unauthorized posters removed.

By lunchtime, every campaign poster has disappeared.

Teachers praise the decision.

Students begin drawing replacement posters
directly onto notebooks, whiteboards,
and occasionally each other.

The goat movement releases a statement
condemning administrative censorship.""")

if choice == "D":
    student += 5
    goat_popularity += 15
    goat_relationship += 10
    print("""You approve the goat campaign's request
for additional poster space.

New posters appear across the school.

"HE HAS NEVER BEEN LATE."

"HE HAS NEVER FAILED AN EXAM."

"HE HAS NEVER CREATED HOMEWORK."

The campaign gains momentum.

Several students begin wearing
hand-drawn goat badges.

The principal develops a headache.""")

print("\n--- DEBUG STATS ---")
print("Teacher Approval:", teacher)
print("Student Approval:", student)
print("Goat Popularity:", goat_popularity)
print("Friend Popularity:", friend_popularity)
print("Stability:", stability)
print("Goat Relationship:", goat_relationship)


input("\nPress Enter to continue...")

print("""
ELECTION DEBATE

The school has organized an official candidate debate.

Attendance is unusually high.

The goat has somehow qualified.

Nobody is willing to explain how.

Four chairs have been prepared.

Three are occupied by candidates.

The goat is standing on the fourth.

The principal looks tired.

Choose your response:

Option A: Help Your Friend Prepare
Option B: Expose The Goat
Option C: Ensure A Fair Debate
Option D: Allow The Goat To Speak
""")

while True:
    choice = input("Choose A, B, C or D: ").upper()

    if choice in ["A", "B", "C", "D"]:
        break

    print("Invalid choice. Please choose A, B, C, or D.")

if choice == "A":
    friend_popularity += 15
    teacher += 5

    print("""
You spend the afternoon helping your friend prepare.

Possible questions are reviewed.

Potential mistakes are discussed.

The debate begins.

Your friend performs confidently.

Several students appear impressed.

The goat continues chewing campaign material.
""")

if choice == "B":
    goat_popularity -= 10
    teacher -= 5
    student -= 5

    print("""
You prepare a detailed presentation
regarding the goat's qualifications.

The presentation contains one major point:

"The goat is a goat."

The argument is technically correct.

Unfortunately, several students interpret
the criticism as an attack on the movement.

The debate becomes increasingly chaotic.

The goat remains calm.
""")

if choice == "C":
    teacher += 10
    stability += 10

    print("""
You focus entirely on maintaining fairness.

Each candidate receives equal speaking time.

Rules are enforced consistently.

Teachers praise the professional organization.

Students describe the debate as
"surprisingly normal."

This is considered a success.
""")

if choice == "D":
    goat_popularity += 15
    goat_relationship += 10

    print("""
The goat is invited to address the audience.

The hall falls silent.

The goat steps forward.

The goat says:

""

Nothing.

Absolutely nothing.

The silence lasts several seconds.

Students immediately begin discussing
the deeper meaning of the statement.

Support for the goat increases dramatically.

The principal develops another headache.
""")

print("\n--- DEBUG STATS ---")
print("Teacher Approval:", teacher)
print("Student Approval:", student)
print("Goat Popularity:", goat_popularity)
print("Friend Popularity:", friend_popularity)
print("Stability:", stability)
print("Goat Relationship:", goat_relationship)

input("\nPress Enter to continue...")

print("""
CAMPAIGN ENDORSEMENT CRISIS

The election is approaching.

Campaign teams have become increasingly aggressive.

Your friend requests an official endorsement.

Ten minutes later, the Goat Movement arrives.

They also request an official endorsement.

Candidate #3 submits a 17-page proposal.

Nobody reads it.

Candidate #4 forgot to attend.

Choose your response:

Option A: Endorse Friend
Option B: Endorse Goat
Option C: Refuse Endorsement
Option D: Sell Endorsements To Highest Bidder
""")

while True:
    choice = input("Choose A, B, C or D: ").upper()

    if choice in ["A", "B", "C", "D"]:
        break

    print("Invalid choice. Please choose A, B, C, or D.")

if choice == "A":
    friend_popularity += 15
    goat_popularity -= 5
    teacher += 5

    print("""
You officially endorse your friend.

The announcement spreads quickly.

Supporters celebrate.

Campaign volunteers immediately begin printing posters.

The Goat Movement describes the decision as:

"Disappointing, but predictable."

Your friend appears grateful.

The election becomes noticeably more competitive.
""")

if choice == "B":
    goat_popularity += 20
    goat_relationship += 15
    teacher -= 10

    print("""
You officially endorse the goat.

The room falls silent.

Several teachers assume this is a joke.

It is not.

The Goat Movement celebrates throughout the corridors.

New posters appear within minutes.

The principal requests an explanation.

You do not have one.
""")

if choice == "C":
    teacher += 10
    stability += 10

    print("""
You refuse to endorse any candidate.

The administration will remain neutral.

Teachers strongly approve.

Supporters of every candidate accuse you
of secretly supporting somebody else.

Nobody is happy.

This is interpreted as proof
that the process is fair.
""")

if choice == "D":
    student -= 10
    teacher -= 15
    stability -= 10
    friend_popularity += 5
    goat_popularity += 5

    print("""
You announce that endorsements
will be awarded to the highest bidder.

The resulting auction lasts 23 minutes.

Campaign teams begin negotiating.

Several students attempt to bribe you
with snacks.

The principal discovers the scheme.

An emergency meeting is scheduled.

Nobody involved appears regretful.
""")

print("\n--- DEBUG STATS ---")
print("Teacher Approval:", teacher)
print("Student Approval:", student)
print("Goat Popularity:", goat_popularity)
print("Friend Popularity:", friend_popularity)
print("Stability:", stability)
print("Goat Relationship:", goat_relationship)

input("\nPress Enter to continue...")

print("""
CAMPAIGN SCANDAL

The election campaign has encountered a problem.

A rumor begins spreading throughout the school.

Nobody knows where it started.

Nobody knows whether it is true.

Unfortunately, this has not stopped anyone from discussing it.

The rumor claims that one of the candidates
has been receiving unfair assistance.

Nobody can agree which candidate.

By lunch, every candidate has been accused.

Including the goat.

Especially the goat.

The principal places a folder on your desk.

"We need this situation handled."

Choose your response:

Option A: Launch Investigation
Option B: Ignore The Rumor
Option C: Ban Discussion
Option D: Blame Candidate #3
""")

while True:
    choice = input("Choose A, B, C or D: ").upper()

    if choice in ["A", "B", "C", "D"]:
        break

    print("Invalid choice. Please choose A, B, C, or D.")

if choice == "A":
    teacher += 10
    stability += 10
    student -= 5

    print("""
You announce an official investigation.

Teachers approve.

Students immediately begin creating new theories.

The investigation ultimately discovers nothing.

This somehow creates even more rumors.

The principal describes the outcome as:

"Unhelpful."
""")

if choice == "B":
    student += 5
    teacher -= 5
    stability -= 10

    print("""
You refuse to comment.

The administration will not respond to rumors.

For several hours the situation appears calm.

Then three new rumors emerge.

The original rumor is now considered outdated.

Nobody remembers what it was about.
""")

if choice == "C":
    teacher += 5
    student -= 15
    stability -= 5

    print("""
You prohibit discussion of election rumors.

Students immediately begin discussing them more.

Secret campaign meetings appear throughout the school.

Several handwritten newsletters are discovered.

The ban is considered ineffective.
""")

if choice == "D":
    student += 10
    stability -= 15

    print("""
Without evidence, you publicly blame Candidate #3.

Candidate #3 is shocked.

Most students find this extremely funny.

Candidate #3 demands an apology.

The scandal shifts entirely toward why you blamed Candidate #3.

The original rumor is forgotten.
""")

print("\n--- DEBUG STATS ---")
print("Teacher Approval:", teacher)
print("Student Approval:", student)
print("Goat Popularity:", goat_popularity)
print("Friend Popularity:", friend_popularity)
print("Stability:", stability)
print("Goat Relationship:", goat_relationship)

input("\nPress Enter to continue...")

print("""
FINAL CAMPAIGN RALLY

The election begins tomorrow.

Campaigning officially ends tonight.

Each candidate has organized a final rally.

Your friend's rally is taking place in the courtyard.

The goat's rally is taking place on the sports field.

Nobody remembers approving either event.

Candidate #3 has prepared a PowerPoint presentation.

Nobody attends.

Candidate #4 remains technically in the election.

The principal approaches.

"Administrator."

"This is the final campaign event."

"Try not to make it worse."

Choose your response:

Option A: Support Your Friend's Rally
Option B: Attend The Goat Rally
Option C: Remain Neutral
Option D: Organize An Official School Rally
""")

while True:
    choice = input("Choose A, B, C or D: ").upper()

    if choice in ["A", "B", "C", "D"]:
        break

    print("Invalid choice. Please choose A, B, C, or D.")

if choice == "A":
    friend_popularity += 15
    student += 5

    print("""
You appear alongside your friend.

A large crowd gathers.

Your friend delivers a confident speech.

Supporters cheer.

Several undecided students appear impressed.

The goat campaign describes the rally as:

"Politically motivated."

Nobody is surprised.
""")

if choice == "B":
    goat_popularity += 20
    goat_relationship += 10
    student += 5

    print("""
You attend the goat rally.

Attendance exceeds expectations.

The goat walks onto the field.

The crowd erupts into applause.

The goat says absolutely nothing.

The applause somehow increases.

Several students describe the event
as inspirational.

The principal leaves early.
""")

if choice == "C":
    teacher += 10
    stability += 10

    print("""
You refuse to endorse any candidate.

Instead, you supervise the rallies.

Rules are enforced.

No major incidents occur.

Teachers praise your professionalism.

Students describe the evening as
surprisingly peaceful.

This is considered unusual.
""")

if choice == "D":
    teacher += 5
    student += 10
    stability -= 5

    print("""
You organize an official school rally.

All candidates are invited.

The event begins normally.

It does not remain normal.

The friend campaign begins chanting.

The goat campaign begins chanting louder.

Candidate #3 attempts to present statistics.

Nobody listens.

The rally becomes complete chaos.

Students describe it as
the greatest campaign event of the year.
""")

print("\n--- DEBUG STATS ---")
print("Teacher Approval:", teacher)
print("Student Approval:", student)
print("Goat Popularity:", goat_popularity)
print("Friend Popularity:", friend_popularity)
print("Stability:", stability)
print("Goat Relationship:", goat_relationship)

input("\nPress Enter to continue...")
print("""
=================================
END OF ACT 2
=================================

The campaign has ended.

The candidates prepare for Election Day.

The school waits.

The principal waits.

The students wait.

The goat waits.

Tomorrow, the future of the school
will be decided.

ACT 3:
ELECTION DAY
""")

input("\nPress Enter to continue...")

friend_votes = friend_popularity
goat_votes = goat_popularity

if goat_votes > friend_votes:
    winner = "GOAT"

elif friend_votes > goat_votes:
    winner = "FRIEND"

else:
    winner = "TIE"
if winner == "GOAT":

    print("""
CERTIFICATION CRISIS

The Goat has won the election.

The principal turns toward you.

"Administrator."

"The results require certification."

Option A: Certify Results
Option B: Refuse Certification
""")

    while True:
        choice = input("Choose A or B: ").upper()

        if choice in ["A", "B"]:
            break

    if choice == "A":
        certified = True

    else:
        certified = False 

# ENDING CHECKER

if winner == "GOAT":

    if certified:

        if goat_relationship >= 80:
            print("""
=================================
ENDING: DEPUTY GOAT ADVISOR
=================================

The Goat wins the election.

You certify the results and remain loyal.

Soon you become the administration's
most trusted adviser.

Many decisions pass through your office.

The Goat may be the leader.

But everyone knows who actually writes
the paperwork.
""")

        elif goat_popularity >= 90:
            print("""
=================================
ENDING: GOAT MANIA
=================================

The Goat wins by a landslide.

Support reaches unprecedented levels.

Students wear Goat badges.

Goat posters cover every corridor.

The movement becomes larger than the election itself.

The Goat is no longer merely a candidate.

The Goat is a phenomenon.
""")

        else:
            print("""
=================================
ENDING: GOAT ADMINISTRATION
=================================

The Goat wins the election.

The results are certified.

Power transfers peacefully.

The Goat becomes Student Leader.

Nobody knows exactly what policies
the Goat supports.

The school enters a strange but
surprisingly stable era.
""")

    else:

        if stability <= 20:
            print("""
=================================
ENDING: SCHOOL COLLAPSE
=================================

The election crisis pushes the school
past its limit.

Rules stop being enforced.

Committees stop functioning.

Nobody knows who is in charge.

The administration collapses completely.

The school enters a state of
permanent chaos.
""")

        elif goat_popularity >= 80 and teacher >= 70:
            print("""
=================================
ENDING: CIVIL WAR
=================================

The election results are rejected.

Both sides claim legitimacy.

Teachers back the administration.

Students back the Goat.

The school divides into rival factions.

The conflict becomes known as:

THE GREAT SCHOOL CIVIL WAR.
""")

        elif goat_popularity >= 80:
            print("""
=================================
ENDING: GOAT COUP
=================================

You refuse to certify the election.

The Goat Movement refuses to accept defeat.

Students occupy classrooms.

Teachers lose control of the situation.

Within days, the Goat seizes power anyway.

The election is over.

The coup has succeeded.
""")

        else:
            print("""
=================================
ENDING: STUDENT PROTEST
=================================

The election results are rejected.

Large demonstrations begin.

Students organize rallies.

Petitions circulate.

The administration faces constant pressure.

The future of the school remains uncertain.
""")
elif winner == "TIE":
    print("""
=================================
ENDING: DEADLOCK
=================================

The election ends in a perfect tie.

Nobody can agree on what happens next.

Recounts produce the same result.

Arguments continue for weeks.

The principal eventually announces:

"We are doing this entire election again."

Nobody is happy.
""")

elif winner == "FRIEND":

    if goat_popularity >= 60:
        print("""
=================================
ENDING: THE REAL CANDIDATE
=================================

Your friend wins the election.

But everyone knows who dominated the campaign.

The Goat never won.

Yet somehow the Goat became the story.

Years later, students remember the Goat.

Few remember the election itself.s
""")

    else:
        print("""
=================================
ENDING: FRIEND VICTORY
=================================

Your friend wins the election.

The transition is peaceful.

The campaign comes to an end.

For the first time in weeks,

the school feels normal again.

Mostly.
""")
input("\nPress Enter to Exit...")