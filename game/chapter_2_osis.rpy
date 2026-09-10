label chapter_2_osis:
    "{cps=35}As usual, [y] was already waiting in front of the house.{/cps}"
    y "{cps=35}Good morning, [mc].{/cps}"
    mc "{cps=35}Good morning...{/cps}"
    "{cps=35}[y] scrutinized me carefully.{/cps}"
    y "{cps=35}Hah... look at you, [mc]...{/cps}"
    y "{cps=35}Already this worn out first thing in the morning?{/cps}"
    y "{cps=35}And your tie is a mess again!{/cps}"
    "{cps=35}[y] immediately pulled at my tie.{/cps}"
    mc "{cps=35}UWA!? What are you—{/cps}"
    y "{cps=35}Do I really have to fix this for you every day?{/cps}"
    y "{cps=35}Sure, we're neighbors, but this is a bit much.{/cps}"
    mc "{cps=35}Just be quiet.{/cps}"
    y "{cps=35}See? I tell you and this is how you act.{/cps}"
    mc "{cps=35}If you don't want to fix it, then stop complaining.{/cps}"
    "{cps=35}I immediately stepped away from [y].{/cps}"
    y "{cps=35}Hey! I'm not done yet!{/cps}"
    mc "{cps=35}Weren't you the one who wanted us to hurry?{/cps}"
    y "{cps=35}Well, yeah... but—{/cps}"
    mc "{cps=35}Enough. Let's go already.{/cps}"
    y "{cps=35}Tch! You jerk...{/cps}"
    y "{cps=35}Wait for me!{/cps}"
    "{cps=35}We walked toward school together.{/cps}"
    "{cps=35}The whole way, [y] wouldn't stop chattering about the Student Council schedule she'd gotten from the group chat last night. Her energy truly had no limits.{/cps}"
    if jajan:
        y "{cps=60}Oh right, [mc]! Yesterday you treated me and Vina. Today at the cafeteria, it's my turn to treat you!{/cps}"
        mc "{cps=40}Ah, no need.{/cps}"
        y "{cps=60}I insist! I'm not staying in debt forever. Besides, we're in the same organization now — supporting each other is only natural.{/cps}"
        mc "{cps=35}I'm not so sure about that...{/cps}"
        y "{cps=35}Are you insulting me?{/cps}"
        mc "{cps=35}No, of course not...{/cps}"
        
    else:
        y "{cps=60}By the way... you don't regret choosing the Student Council, right? Yesterday you looked a bit... hesitant?{/cps}"
        mc "{cps=40}No. This was my own choice.{/cps}"
        y "{cps=60}Thank goodness. Let's do this together!{/cps}"
        mc "{cps=35}Yeah, [y]..{/cps}"
    
    y "{cps=35}Oh right!{/cps}"
    y "{cps=35}Apparently today we're getting split into divisions. I hope we end up in the same one — it'd be more fun!{/cps}"
    mc "{cps=35}Divisions? When there are only eight members total?{/cps}"
    mc "{cps=35}And that already includes our year.{/cps}"
    y "{cps=35}Well... maybe there'll be extra members.{/cps}"
    mc "{cps=35}Whatever you say, [y].{/cps}"
    mc "{cps=35}In the end the president decides anyway.{/cps}"
    y "{cps=35}True, but it'd still be fun if we were together.{/cps}"
    "{cps=35}Thinking about it, [y] and I already have a connection.{/cps}"
    mc "{cps=35}Though I'll probably just end up causing her trouble.{/cps}"
    mc "{cps=35}You'll just make things harder for me again.{/cps}"
    y "{cps=35}Isn't it the other way around?{/cps}"
    mc "{cps=35}Adududu... what even...{/cps}"
    "{cps=35}[y] pinched my cheek.{/cps}"

    "???" "{cps=35}Ouch... already being all lovey-dovey this early, [mc]?{/cps}"
    y "{cps=35}Ah, [yk]! Good morning!{/cps}"
    yk "{cps=35}Otsu!{/cps}"
    "{cps=35}Behind [yk], [sh] was just watching us with a blank expression.{/cps}"
    y "{cps=35}Big sis, say good morning too.{/cps}"
    sh "{cps=35}Morning.{/cps}"
    mc "{cps=35}Morning...{/cps}"
    "{cps=35}[sh] immediately left her little sister talking with us.{/cps}"
    yk "{cps=35}Ah! Wait....{/cps}"
    yk "{cps=35}Sorry, big sis is in a bad mood today.{/cps}"
    y "{cps=35}You should just go after her.{/cps}"
    yk "{cps=35}Obviously. See you in class, [mc], [y]!{/cps}"
    "{cps=35}[yk] immediately ran after [sh].{/cps}"
    "{cps=35}And they started talking up ahead of us.{/cps}"
    y "{cps=35}[sh] seems off...{/cps}"
    y "{cps=35}Do you know something, [mc]?{/cps}"
    mc "{cps=35}No idea...{/cps}"
    "{cps=35}Even though I knew perfectly well... it was my fault.{/cps}"
    "{cps=35}I should talk to her.{/cps}"
    y "{cps=35}Hey... [y] to [mc]...{/cps}"
    mc "{cps=35}Ah!{/cps}"
    y "{cps=35}You're not thinking anything weird, right?{/cps}"
    mc "{cps=35}Ummn.... no.{/cps}"
    y "{cps=35}Suspicious... I'll talk to [v] about this later.{/cps}"
    mc "{cps=35}Do whatever you want, [y].{/cps}"

    scene bg_classroom_morning with fade
    "{cps=35}We arrived at class right as the bell rang. Luckily, [t] wasn't there yet.{/cps}"

    if jajan:
        "{cps=35}I sat at my desk, still thinking about Yuuka's promise to treat me. Maybe my wallet would survive today.{/cps}"
    elif ciduk:
        "{cps=35}I sat at my desk, trying to forget yesterday when I almost got caught by Senior Maya. At least now I was officially in the Student Council.{/cps}"
    else:
        "{cps=35}I sat at my desk, feeling a little guilty for not going to the cafeteria yesterday. At least Yuuka wasn't mad.{/cps}"

    "{cps=35}Vina, sitting behind me, immediately nudged my chair.{/cps}"

    show vina_smile with dissolve
    v "{cps=60}Hey, Specimen! I heard you ran into the Shirohana family at the gate earlier?{/cps}"
    mc "{cps=40}How do you know that?{/cps}"
    v "{cps=60}Fufufu, nothing stays hidden from Vina at this school~{/cps}"
    
    if guess_correct:
        v "{cps=60}They say you can tell Shoko and Yukie apart from behind? Not bad.{/cps}"
    else:
        v "{cps=60}They say you mixed up their names? Embarrassing.{/cps}"

    mc "{cps=35}Hold on...{/cps}"
    mc "{cps=35}I feel like you've known everything I've done since yesterday.{/cps}"
    mc "{cps=35}Are you stalking me?{/cps}"
    v "{cps=35}Hah? Of course not.{/cps}"
    mc "{cps=35}Your face isn't very convincing, [v].{/cps}"
    v "{cps=35}That's just your imagination, [mc].{/cps}"
    v "{cps=35}I just have a lot of connections.{/cps}"
    v "{cps=35}Plus you're the only guy here.{/cps}"
    v "{cps=35}So of course plenty of people are watching you.{/cps}"
    mc "{cps=35}Ah! No way.{/cps}"
    mc "{cps=35}As if a guy like me would have that many stalkers.{/cps}"
    v "{cps=35}You just haven't noticed yet, [mc].{/cps}"
    v "{cps=35}But someone really is doing it.{/cps}"
    v "{cps=35}It's such a big secret I won't tell you, though.{/cps}"
    v "{cps=35}Besides, you don't even care.{/cps}"
    mc "{cps=35}Explain it at break.{/cps}"
    v "{cps=35}If I remember...{/cps}"
    "{cps=35}The bell for first period rang.{/cps}"

    "{cps=40}While I was zoning out....{/cps}"
    "{cps=40}SLAM!{/cps}"
    mc"{cps=40}Hue! What the—{/cps}"
    "{cps=40}[t] threw a book onto my desk fairly hard.{/cps}"
    t "{cps=40}Hah.... look at you, [mc].{/cps}"
    t "{cps=40}Even if you're sleepy...{/cps}"
    t "{cps=40}{b}AT LEAST PAY ATTENTION!{/b}{/cps}"
    mc "{cps=50}Yes, Miss...{/cps}"
    "{cps=50}Damn... {w=0.1}why is it always like this...{/cps}"
    "{cps=50}I could hear [v] laughing quietly behind me. She was definitely enjoying the show.{/cps}"

    t "{cps=40}Since you seem to have a whole world inside that head of yours, try solving the problem on the board.{/cps}"
    
    t "{cps=40}If 3x + 5 = 20, what is the value of x?{/cps}"

    "{cps=35}Ugh... my mind went blank. The numbers seemed to dance in front of my eyes.{/cps}"
    "{cps=35}Yuuka in front of me looked panicked — she held up five fingers under the desk as a signal.{/cps}"
    "{cps=40}What should I answer...{/cps}"
    menu:
        "5":
            $ correct_answer = True
            $ yuuka_rel += 5
            $ vina_rel += 5
            mc "{cps=40}The answer is... 5, Miss.{/cps}"
            
            "{cps=35}Miss [t] paused for a moment, then lowered her glasses.{/cps}"
            
            t "{cps=40}Correct. Simple, isn't it?{/cps}"
            t "{cps=40}Remember, in Algebra, our goal is to find the 'Missing Value' (x) by balancing both sides.{/cps}"
            
            "{cps=35}Miss [t] quickly wrote on the board.{/cps}"
            t "{cps=40}If you have a big problem (20) and a small distraction (+5), remove the distraction first (20-5). Then divide the remaining burden (15) by your capacity (3).{/cps}"
            
            "{cps=35}Somehow, Miss [t]'s explanation just now didn't only sound like math — it sounded like a way to face this messy life.{/cps}"
            t "{cps=35}Understood?{/cps}"
            mc "{cps=35}Yes, Miss?{/cps}"
            t "{cps=40}Next time, pay attention to my explanation. Sit down and focus!{/cps}"
            t "{cps=35}Now go back to your seat.{/cps}"
            mc "{cps=35}Y-yes, Miss.{/cps}"
            
            show yuuka_smile with dissolve
            "{cps=35}Yuuka sighed in relief and gave me a small smile. Behind me, Vina looked slightly disappointed she couldn't laugh at me.{/cps}"
            v "{cps=60}Tch... so the Rare Specimen can do math after all.{/cps}"

        "15":
            $ correct_answer = False
            $ yuuka_rel -= 2
            mc "{cps=40}The answer is... 15, Miss?{/cps}"
            
            "{cps=35}The whole class burst out laughing. Even Vina behind me had to cover her mouth so she wouldn't be too loud.{/cps}"
            t "{cps=40}Fifteen? Are you solving for x or calculating the price of fried snacks at the cafeteria? Wrong!{/cps}"
            t "{cps=40}Stand in front until my class is over!{/cps}"
            
            show yuuka_sad with dissolve
            "{cps=35}Yuuka facepalmed. She'd given me the signal, and I'd still gotten it wrong.{/cps}"

        "3":
            $ correct_answer = False
            $ yuuka_rel -= 2
            mc "{cps=40}The answer is... 3?{/cps}"
            
            t "{cps=40}Wrong! Apparently daydreaming really has ruined your logic.{/cps}"
            t "{cps=40}Please stand beside the blackboard until I finish explaining.{/cps}"
            
            "{cps=35}I could only hang my head while a few other girls whispered and laughed at me.{/cps}"

    "{cps=50}Class continued as usual.{/cps}"
    if correct_answer:
        "{cps=35}Good thing I got it right...{/cps}"
    else:
        "{cps=35}If only I'd gotten it right... maybe my legs wouldn't be this sore from standing in front.{/cps}"
    
    "{cps=40}And before I knew it, it was already break time.{/cps}"
    
    play sound "audio/sfx/school bell.mp3"
    t "{cps=40}Alright, since it's this late, you're free to take a break.{/cps}"
    t "{cps=40}We'll meet again in the afternoon period.{/cps}"
    
    "The Class" "{cps=40}Yes, Miss!{/cps}"
    "{cps=40}[t] left the classroom right away.{/cps}"

    mc "{cps=40}Hah.... finally.{/cps}"
    
    if correct_answer == False:
        "{cps=40}[v] and [y] immediately came over to me.{/cps}"
        "{cps=40}Seemed like they wanted to give me some kind of 'lecture'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Dumb kid.{/cps}"
        mc "{cps=40}Hey!{/cps}"
        v "{cps=40}Come on, I was just kidding. But seriously, your face earlier was hilarious.{/cps}"
        mc "{cps=40}What even...{/cps}"
        v "{cps=40}But how's your leg? {w=0.1} Still okay?{/cps}"
        mc "{cps=40}So okay I don't even feel like walking.{/cps}"
        v "{cps=40}Ahaha, figured as much.{/cps}"
        y "{cps=40}I already gave you the signal, [mc]. Why were you still zoning out?{/cps}"
        mc "{cps=40}Sorry... my head went blank looking at those numbers.{/cps}"
        y "{cps=40}That's just like you.{/cps}"
        v "{cps=40}Hmm, what signal?{/cps}"
        y "{cps=40}Nothing.{/cps}"
        "{cps=40}[y] immediately left me behind.{/cps}"
        v "{cps=40}Huh? Why'd she just leave?{/cps}"
        v "{cps=40}[y].....{/cps}"
        "{cps=40}[v] immediately ran after [y].{/cps}"
        "{cps=40}Leaving me alone.{/cps}"
            
    else:
        "{cps=40}[v] and [y] immediately came over to me.{/cps}"
        "{cps=40}Seemed like they wanted to give me some kind of 'lecture'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Smart kid.{/cps}"
        mc "{cps=40}I just got lucky earlier.{/cps}"
        v "{cps=40}Too bad there was no drama...{/cps}"
        v "{cps=40}I was really hoping to see you get punished.{/cps}"
        mc "{cps=40}Hey! That's a terrible intention.{/cps}"
        y "{cps=40}Thank goodness you could answer it, [mc]. I almost panicked earlier.{/cps}"
        y "{cps=40}Next time don't zone out again, okay?{/cps}"
        mc "{cps=40}Yeah, sorry...{/cps}"
        v "{cps=40}Anyway. At least today was safe, right?{/cps}"
        mc "{cps=40}Safe enough...{/cps}"
        v "{cps=40}Want to go to the cafeteria?{/cps}"
        if jajan == True:
            mc "{cps=40}No thanks, I'm still full.{/cps}"
            "{cps=40}(Mostly because I don't want to spend money...){/cps}"
        else:
            mc "{cps=40}Maybe not this time, Vin. I'm still full.{/cps}"
        
        v "{cps=40}Hah... alright then.{/cps}"
        v "{cps=40}Come on Ka, let's go to the cafeteria!{/cps}"
        y "{cps=40}Let's go.{/cps}"

        "{cps=40}They left me alone.{/cps}"
        "{cps=40}...{/cps}"

    "{cps=40}This quiet atmosphere...{/cps}"
    "{cps=40}When was the last time I felt this...{/cps}"
    "{cps=35}In the middle of this silence,{/cps}"
    "{cps=35}someone suddenly called me.{/cps}"
    yk "{cps=35}Yo, [mc].{/cps}"
    mc "{cps=35}Ah! [yk], what's up?{/cps}"
    yk "{cps=35}You've been zoning out this whole time. What are you thinking about?{/cps}"
    mc "{cps=35}Nothing weird.{/cps}"
    yk "{cps=35}Then why didn't you go to the cafeteria with them?{/cps}"
    if correct_answer == False:
        mc "{cps=35}They left me behind.{/cps}"
        yk "{cps=35}Hah? Someone left [mc] behind?{/cps}"
        mc "{cps=35}Why are you so surprised?{/cps}"
        yk "{cps=35}Well... you three are usually together.{/cps}"
        mc "{cps=35}You saw it yourself yesterday.{/cps}"
        yk "{cps=35}True enough.{/cps}"
    else:
        mc "{cps=35}I just don't feel like going with them right now.{/cps}"
        yk "{cps=35}Really? You looked pretty close with them.{/cps}"
        mc "{cps=35}That's just how it looks to you.{/cps}"
    
    mc "{cps=35}Plus I don't have much money on me.{/cps}"
    yk "{cps=35}How much did you bring?{/cps}"
    mc "{cps=35}200 yen.{/cps}"
    yk "{cps=35}That's nothing!{/cps}"
    mc "{cps=35}Don't insult me!{/cps}"
    yk "{cps=35}I'm not insulting you... more like pitying you.{/cps}"
    mc "{cps=35}I don't need pity.{/cps}"
    yk "{cps=35}I'm not pitying you — I'm pitying your stomach...{/cps}"
    "{cps=35}*grumble....*{/cps}"
    mc "{cps=35}Ah... caught, huh?{/cps}"
    yk "{cps=35}Come with me.{/cps}"
    mc "{cps=35}To do what?{/cps}"
    yk "{cps=35}You should ask someone who actually knows the answer.{/cps}"
    mc "{cps=35}And who would that be?{/cps}"
    yk "{cps=35}Just look around this class.{/cps}"
    "{cps=35}I looked around the classroom, searching for whoever might know.{/cps}"
    mc "{cps=35}Hmmm...{/cps}"
    "{cps=35}I felt two people looking at me.{/cps}"
    "{cps=35}One of them I knew.{/cps}"
    "{cps=35}The other, I didn't recognize.{/cps}"
    "{cps=35}She was watching me from the doorway.{/cps}"
    "{cps=35}Until our eyes met by accident.{/cps}"
    mc "{cps=35}Ah!{/cps}"
    "???" "{cps=35}Hue—{/cps}"
    "{cps=35}She left immediately.{/cps}"
    "{cps=35}Who was that girl...{/cps}"
    yk "{cps=35}Hey... your answer?{/cps}"
    mc "{cps=35}Oh right! Almost forgot.{/cps}"
    mc "{cps=35}I'm coming.{/cps}"
    yk "{cps=35}Okay then... [sh]-nee.{/cps}"
    "{cps=35}What's going on?{/cps}"
    yk "{cps=35}Let's eat together!{/cps}"
    "{cps=35}Is there even enough food for three?{/cps}"
    yk "{cps=35}Didn't big sis cook extra this morning?{/cps}"
    "{cps=35}Huh?{/cps}"
    yk "{cps=35}Anyway, let's just eat.{/cps}"
    mc "{cps=35}Where, though? The classroom is too crowded.{/cps}"
    yk "{cps=35}We're good on that.{/cps}"
    yk "{cps=35}Follow me.{/cps}"
    mc "{cps=35}U-uh..{/cps}"
    "{cps=35}[sh] and I followed [yk]. Unlike [y], whose steps were always rushed,{/cps}"
    "{cps=35}[yk] walked lightly, as if she were dancing across the corridor floor.{/cps}"
    "{cps=35}Of course, [sh] was right beside her.{/cps}"
    yk "{cps=35}Alright, this is the place.{/cps}"
    "{cps=35}We arrived at a door at the quiet end of the corridor. The nameplate read 'Literature Club'.{/cps}"
    mc "{cps=35}Hey... this is your club room.{/cps}"
    yk "{cps=35}So?{/cps}"
    mc "{cps=35}Well... I'm not a member.{/cps}"
    yk "{cps=35}But you're starving.{/cps}"
    yk "{cps=35}We can't just leave someone hungry.{/cps}"
    yk "{cps=35}You think so too, right, [sh]-nee?{/cps}"
    sh "{cps=35}That's right, [yk].{/cps}"
    if correct_answer == False:
        yk "{cps=35}You even got the question wrong earlier — must be because you haven't eaten, right?{/cps}"
    else:
        yk "{cps=35}Your stomach was already growling earlier.{/cps}"
    mc "{cps=35}Ugh... fair enough.{/cps}"
    yk "{cps=35}It's fine, [mc].{/cps}"
    yk "{cps=35}We're the ones who invited you.{/cps}"
    mc "{cps=35}Umm... wasn't it just you who invited me?{/cps}"
    "{cps=35}[yk] only grinned mischievously, then looked toward her sister who was holding the door handle.{/cps}"
    yk "{cps=35}What do you say, [sh]-nee?{/cps}"
    sh "{cps=35}No problem.{/cps}"
    "{cps=35}[sh]'s answer was short, but enough to get me inside.{/cps}"

    play sound "audio/sfx/sliding door.mp3"
    scene bg_lit_club_room with dissolve

    yk "{cps=35}Okay... what's on the menu today, sis?{/cps}"
    sh "{cps=35}The usual — sandwiches.{/cps}"
    yk "{cps=35}Woah... looks really good.{/cps}"
    yk "{cps=35}Let's eat!{/cps}"
    "{cps=35}The lunch was ordinary enough.{/cps}"
    "{cps=35}But the warmth in this room... made me feel comfortable.{/cps}"
    yk "{cps=35}[mc], why aren't you eating?{/cps}"
    mc "{cps=35}Ah.... it's nothing.{/cps}"
    mc "{cps=35}I just remembered something from the past.{/cps}"
    "{cps=35}[sh], hearing that, immediately went still.{/cps}"
    sh "{cps=35}Memories...{/cps}"
    mc "{cps=35}Hm?{/cps}"
    sh "{cps=35}Have you remembered?{/cps}"
    mc "{cps=35}Different thing. Not about you.{/cps}"
    sh "{cps=35}Oh..{/cps}"
    "{cps=35}[sh] immediately looked down, as if I'd said something deeply upsetting.{/cps}"
    sh "{cps=35}So still not yet...{/cps}"
    yk "{cps=35}It's okay, big sis.{/cps}"
    sh "{cps=35}Little by little.{/cps}"
    sh "{cps=35}You'll remember all our memories eventually, [mc].{/cps}"
    mc "{cps=35}Hopefully...{/cps}"
    "{cps=35}We ate in a comfortable silence.{/cps}"
    "{cps=35}But the moment the first bite touched my tongue...{/cps}"
    "{cps=35}A faint flash of memory appeared in my head.{/cps}"
    scene bg_event_flashback with vpunch
    stop music fadeout 1.0

    "{cps=35}A little girl with crimson hair sat beside me...{/cps}"
    "{cps=35}She held out a sandwich with the edges neatly trimmed.{/cps}"
    
    "Little Girl" "{cps=30}[mc], come on, eat... or your mom will get mad.{/cps}"
    
    "{cps=35}I couldn't see her face, but her voice... sounded so sincere.{/cps}"
    yk "{cps=35}Heeey... [mc].{/cps}"
    scene bg_lit_club_room with flash
    mc "{cps=35}Hah!?{/cps}"
    yk "{cps=35}Are you okay?{/cps}"
    yk "{cps=35}You've looked weird ever since I invited you...{/cps}"
    mc "{cps=35}Umn..{/cps}"
    "{cps=35}[sh] suddenly stood up from her chair.{/cps}"
    "{cps=35}And immediately touched my forehead.{/cps}"
    sh "{cps=35}From the temperature... you're fine.{/cps}"
    sh "{cps=35}But you look like you have a lot on your mind.{/cps}"
    mc "{cps=35}Seems that way...{/cps}"
    sh "{cps=35}If something's bothering you, just talk about it.{/cps}"
    sh "{cps=35}Don't hold it in.{/cps}"
    mc "{cps=35}Maybe... but it's not the time yet.{/cps}"
    sh "{cps=35}You shouldn't force yourself.{/cps}"
    mc "{cps=35}Yeah...{/cps}"
    "{cps=35}Lunch ended in an awkward silence.{/cps}"
    mc "{cps=35}I'm heading back to class first!{/cps}"
    yk "{cps=35}Okay, see you later!{/cps}"
    "{cps=35}[sh] only nodded at my words.{/cps}"
    "{cps=35}I left the club room and walked back toward class.{/cps}"
    "{cps=35}And when I reached the corridor junction—{/cps}"
    v "{cps=35}Well well well...{/cps}"
    if correct_answer == True:
        v "{cps=35}You said you were full.{/cps}"
        v "{cps=35}So why are you wandering around?{/cps}"
    else:
        "{cps=35}What are you doing in the hallway at this hour?{/cps}"
        "{cps=35}Class is about to start, isn't it?{/cps}"

    mc "{cps=35}None of your business, [v].{/cps}"
    v "{cps=35}Wow, cold.{/cps}"
    v "{cps=35}You did something, didn't you?{/cps}"
    mc "{cps=35}I just came from the bathroom. Nothing more.{/cps}"
    v "{cps=35}But your stomach looks fuller?{/cps}"
    v "{cps=35}You can't hide it from me, no matter how hard you try to lie.{/cps}"
    "{cps=35}[v] suddenly got closer.{/cps}"
    v "{cps=35}Plus, from your breath — there's a sweet taste I can't quite place.{/cps}"
    "{cps=35}Ugh... I really can't lie to her.{/cps}"
    mc "{cps=35}Fine. I just ate.{/cps}"
    v "{cps=35}There we go. Honesty.{/cps}"
    v "{cps=35}Where?{/cps}"
    mc "{cps=35}At the Literature Club.{/cps}"
    v "{cps=35}Huh?{/cps}"
    v "{cps=35}What were you doing at the Literature Club?{/cps}"
    mc "{cps=35}[yk] invited me.{/cps}"
    v "{cps=35}Hmm.... and you just went along with it?{/cps}"
    mc "{cps=35}I was hungry, and I didn't have any money either.{/cps}"
    mc "{cps=35}That's partly because of you two — I treated you yesterday.{/cps}"
    v "{cps=35}Ah! Still a little salty about that?{/cps}"
    "{cps=35}Not really.{/cps}"
    v "{cps=35}Be honest...{/cps}"
    "{cps=35}I said no.{/cps}"
    v "{cps=35}See, you are salty.{/cps}"
    "{cps=35}I should just leave [v] already.{/cps}"
    "{cps=35}Before I get interrogated again.{/cps}"
    mc "{cps=35}Sorry Vin, I've got something else to do.{/cps}"
    v "{cps=35}Eh!? Wai—{/cps}"
    "{cps=35}I immediately ran away from her.{/cps}"
    v "{cps=35}Hah... maybe I teased him too much.{/cps}"
    v "{cps=35}But I should probably tell [y].{/cps}"
    "{cps=35}Meanwhile...{/cps}"
    mc "{cps=35}Phew... looks like [v] isn't chasing me.{/cps}"
    mc "{cps=35}I hope she doesn't tell [y] all of that.{/cps}"
    y "{cps=35}Tell me about what, [mc]?{/cps}"
    mc "{cps=35}Huh? How long have you been there!?{/cps}"
    y "{cps=35}Ummnn.... {w=0.1} since you ran into that corner.{/cps}"
    y "{cps=35}Come on, tell me, [mc]. I'm curious.{/cps}"
    mc "{cps=35}Even if I told you, you wouldn't get it.{/cps}"
    y "{cps=35}Come on, why are you avoiding this?{/cps}"
    y "{cps=35}We're in the same organization, you know.{/cps}"
    mc "{cps=35}It's not that, [y], it's just...{/cps}"
    y "{cps=35}Just?{/cps}"
    y "{cps=35}Just tell me already so everything's clear.{/cps}"
    y "{cps=35}If you keep this up I won't know what's going on.{/cps}"
    mc "{cps=35}You won't get mad, right?{/cps}"
    y "{cps=35}As long as you're honest, no.{/cps}"
    "{cps=35}Yeah right.{/cps}"
    "{cps=35}I've known [y] for more than just one or two years.{/cps}"
    mc "{cps=35}umn....{/cps}"
    menu:
        "Tell her":
            $ tell_yuuka = True
            $ yuuka_rel += 3
            mc "{cps=60}Fine, if that's what you want.{/cps}"
            mc "{cps=35}I just ate at the Literature Club.{/cps}"
            y "{cps=35}Hmm... who invited you?{/cps}"
            mc "{cps=35}[yk].{/cps}"
            y "{cps=35}How come I wasn't invited?{/cps}"
            mc "{cps=35}You weren't even with me earlier.{/cps}"
            mc "{cps=35}If you had been, you'd have gotten a sandwich too.{/cps}"
            y "{cps=35}Tch.{/cps}"
            y "{cps=35}Lucky you...{/cps}"
            mc "{cps=35}Anything else?{/cps}"
            y "{cps=35}Ummmmm.....{/cps}"

        "No need":
            $ tell_yuuka = False
            $ yuuka_rel -= 3
            mc "{cps=35}You probably shouldn't ask, [y].{/cps}"
            y "{cps=35}Why are you always like this lately?{/cps}"
            y "{cps=35}You weren't like this before we started school here.{/cps}"
            y "{cps=35}And now we're in the same organization.{/cps}"
            mc "{cps=35}Even if I told you, what would you do about it?{/cps}"
            y "{cps=35}What's wrong with me knowing?{/cps}"
            mc "{cps=35}It's not even interesting.{/cps}"
            y "{cps=35}No way it's not interesting.{/cps}"
            y "{cps=35}I'm always waiting for your stories.{/cps}"
            mc "{cps=35}Hah... I'll tell you later.{/cps}"
            y "{cps=35}Remember — you have to tell me on the way home!{/cps}"
            mc "{cps=35}Yeah. Anything else?{/cps}"
            y "{cps=35}Ummm....{/cps}"


    y "{cps=35}Why aren't you going to class?{/cps}"
    mc "{cps=35}Well... I was heading there and got blocked by [v].{/cps}"
    y "{cps=35}Hah.. typical.{/cps}"
    y "{cps=35}I'll talk to her later.{/cps}"
    y "{cps=35}Come on, let's get to class, [mc].{/cps}"
    mc "{cps=35}Hm!{/cps}"
    "{cps=35}We headed straight to our classroom.{/cps}"
    "{cps=35}Of course, the whole way [y] kept talking about everything under the sun.{/cps}"
    v "{cps=35}Yo, [mc]!{/cps}"
    "{cps=35}What?{/cps}"
    "{cps=35}Come on, no need to be that stiff.{/cps}"
    "{cps=35}What do you want?{/cps}"
    "{cps=35}Are you asking because [y] already warned you?{/cps}"
    "{cps=35}Ah! So you noticed?{/cps}"
    "{cps=35}Obviously.{/cps}"
    "{cps=35}Yeah, basically.{/cps}"
    "{cps=35}Such a tattletale.{/cps}"
    "{cps=35}You're one to talk, stirrer.{/cps}"
    "{cps=35}I don't remember bringing a stove to school.{/cps}"
    "{cps=35}Enough, Vin. I'm tired of talking to you.{/cps}"
    "{cps=35}Yee...{/cps}"
    "{cps=35}Ah damn, the bell already rang.{/cps}"
    "{cps=35}[v] went straight back to her seat.{/cps}"
    
    "{cps=35}The figure who'd punished me in front of the class this morning appeared again. At this school, [t] was known as the 'all-rounder' teacher with a packed schedule.{/cps}"

    t "{cps=40}Put your gadgets away. Even though this is the afternoon period when everyone's sleepy, our material now is far heavier than this morning's math.{/cps}"

    t "{cps=40}Open your History books. We'll be discussing 'Tragedy and Betrayal' in the history of organizational movements.{/cps}"

    "{cps=35}I flinched. Why did this afternoon's material feel like it was calling out my current situation?{/cps}"

    t "{cps=40}Throughout history, many great figures fell not because of enemies from outside, but because of broken 'Trust' from those closest to them.{/cps}"
    
    # Educational element
    t "{cps=40}There's a Latin phrase: {b}'Falsus in Uno, Falsus in Omnibus'{/b}. Anyone know what it means?{/cps}"

    "{cps=35}The class was silent. I glanced at [y] — she was taking notes very quickly, as if trying to ignore my existence behind her.{/cps}"
    "{cps=40}As usual, she was completely focused.{/cps}"
    "{cps=40}Unlike me...{/cps}"

    t "{cps=40}[mc], try answering. You seem to have a lot on your mind this afternoon.{/cps}"
    mc "{cps=40}Why me, [t]?{/cps}"
    t "{cps=40}Who else fits better than you?{/cps}"
    mc "{cps=40}There are others...{/cps}"
    "{cps=40}I looked around the class.{/cps}"
    "{cps=40}But none of them showed any sign of wanting to answer.{/cps}"
    t "{cps=40}Well?{/cps}"
    mc "{cps=40}Nothing, Miss...{/cps}"
    t "{cps=40}If there's nothing, answer quickly.{/cps}"
    mc"{cps=40}Ummm...{/cps}"

    menu:
        "One lie ruins everything":
            $ correct_answer_2 = True
            mc "{cps=40}It means... once you lie about one thing, everything you say will be considered a lie, Miss.{/cps}"
            t "{cps=40}Correct. That is a moral law often far harsher than written law.{/cps}"
            t "{cps=40}Once you break trust, it takes a lifetime to rebuild it.{/cps}"

        "One person's mistake is shared by all":
            $ correct_answer_2 = False
            mc "{cps=40}It means one person's mistake is the mistake of the whole group?{/cps}"
            
            t "{cps=40}Wrong. That's collective responsibility. Our focus is individual integrity.{/cps}"
            t "{cps=40}Seems you need to read more instead of just daydreaming, [mc].{/cps}"
            
            v "{cps=40}Fufufu... Looks like [mc]'s brain is already smoking from this morning's lesson.{/cps}"
            v "{cps=40}Careful, [mc]. If you zone out too often, someone else might 'pick' your integrity right out of you.{/cps}"
            
            mc "{cps=40}(Damn... Vina always finds a gap to jab at me. Is there anything at this school she doesn't know?){/cps}"

    t "{cps=40}Once you break trust, it takes a lifetime to rebuild it.{/cps}"
    
    "{cps=35}Yuuka stopped writing for a moment. Her shoulder trembled slightly; her hand gripped the pen so tightly her knuckles went white.{/cps}"
    "{cps=35}I knew she was listening to every word. And I knew Miss Nanami's words were landing right in the middle of the awkwardness between us.{/cps}"

    "{cps=35}Miss Nanami returned to the blackboard, the chalk screeching as she wrote a list of history's great traitors.{/cps}"
    "{cps=35}The classroom atmosphere grew heavy. There was only the sound of pens on paper and the wall clock ticking as if deliberately slowed down.{/cps}"

    "{cps=35}One hour passed...{/cps}"
    "{cps=35}The harsh midday sunlight slowly shifted, casting long shadows from the desk legs across the wooden classroom floor.{/cps}"
    "{cps=35}Some of my classmates started looking sleepy, their heads nodding along to Miss Nanami's monotone yet sharp voice.{/cps}"
    
    "{cps=35}[t]'s voice explaining the fall of great kingdoms from internal betrayal felt like a whisper judging every breath I took.{/cps}"

    "{cps=35}I glanced forward. [y] stayed in her position. She never once looked my way, even when she reached for a ruler or fixed her hair.{/cps}"

    "{cps=35}Two hours passed...{/cps}"
    "{cps=35}Time truly felt eternal. My legs felt stiff, and my thoughts drifted to Shoko, to Maya, and to the silver armband now attached to my shoulder.{/cps}"
    "{cps=35}Every second we spent in this silence felt more painful than the punishment of standing in front of the class this morning.{/cps}"
    
    "{cps=35}The wall of ice [y] had built beside me felt thicker and thicker. I wanted to speak, but my throat was locked by the weight of secrets and the choice I'd just made.{/cps}"
    "{cps=35}My presence here... behind her... felt completely erased from her little world.{/cps}"

    scene black with fade
    # Placeholder for optional encounter scene
    "{cps=35}{/cps}"
    "{cps=35}{/cps}"
    "{cps=35}{/cps}"
    "{cps=35}{/cps}"
    "{cps=35}{/cps}"

    # MC goes to the Student Council room
    "{cps=35}I stood in front of the Student Council door. The orange light of the afternoon sun slipped through the corridor window, casting a long shadow that seemed to pull me into a new spiral of trouble.{/cps}"
    "{cps=35}I took a deep breath, straightened my uniform collar, and slowly pushed the door open.{/cps}"
    show maya_stern at center
    show vina_smile at right
    show yuuka_determined at left
    with dissolve

    m "{cps=40}So you finally made it here.{/cps}"
    
    "{cps=35}{/cps}"
    "{cps=35}{/cps}"
    "{cps=35}{/cps}"
    
    # CHAPTER 2 OSIS ENDING
    "{cps=35}We left the Student Council room as the corridor lights began turning on one by one. The blue folder was still in my hand — feeling far warmer... and far heavier.{/cps}"

    "{cps=35}The school's secrets, my sister's death, and Senior Maya's promise. Everything had now shifted onto my shoulders.{/cps}"

    scene black with fade
    stop music fadeout 2.0
    jump chapter_2_end
