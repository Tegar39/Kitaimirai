label chapter_2_sastra:
    "{cps=35}I immediately hurried to [y]'s house.{/cps}"
    "{cps=35}Of course, to explain everything.{/cps}"
    "{cps=35}I hoped she hadn't left yet.{/cps}"
    "{cps=35}I'd arrived in front of her house.{/cps}"
    "{cps=35}Seemed like no one was home.{/cps}"
    "{cps=35}Should I just knock?{/cps}"
    menu:
        "Knock on the door":
            $ yuuka_rel += 3
            "{cps=35}I tried knocking on her door.{/cps}"
            mc "{cps=35}Excuse me.... [y]?{/cps}"
            mc "{cps=35}Are you home?{/cps}"
            y "{cps=35}Yeah, just a second....{/cps}"
            "{cps=35}Phew, good thing I knocked.{/cps}"
            "{cps=35}There was a lot of scrambling noise from inside the house.{/cps}"
            mc "{cps=35}Ummmm.... [y]?{/cps}"
            mc "{cps=35}Are you okay?{/cps}"
            y "{cps=35}Just a second!{/cps}"
            "{cps=35}No need to yell, either.{/cps}"
            "{cps=35}Eventually, [y] came out of the house.{/cps}"
            "{cps=35}Looking a little messy, with slightly red eyes.{/cps}"
            mc "{cps=35}What's wrong?{/cps}"
            if callyuukafirst:
                y "{cps=35}It's nothing.{/cps}"
                y "{cps=35}I just overslept earlier, hehe.{/cps}"
                mc "{cps=35}Really? Even your eyes are a bit red.{/cps}"
                y "{cps=35}Ah, this....{/cps}"
                y "{cps=35}I-it's from cutting onions.{/cps}"
                y "{cps=35}Y-yeah, cutting onions.{/cps}"
                mc "{cps=35}Suspicious...{/cps}"
                mc "{cps=35}Just be honest, [y].{/cps}"
                y "{cps=35}I am being honest.{/cps}"
                y "{cps=35}Come on, let's go to school.{/cps}"
                mc "{cps=35}Let's go.{/cps}"
                jump chapter_2_sastra_otw
            else:
                y "{cps=35}What do you think?{/cps}"
                mc "{cps=35}I'm guessing you were crying.{/cps}"
                y "{cps=35}Yeah.. I was crying.{/cps}"
                mc "{cps=35}Because of what?{/cps}"
                y "{cps=35}Just drop it.{/cps}"
                "{cps=35}[y] walked past me right away.{/cps}"
                mc "{cps=35}Hey, [y].{/cps}"
                mc "{cps=35}Wait for me.{/cps}"
                jump chapter_2_sastra_otw

        "Just leave":
            $ yuuka_rel -= 2
            "{cps=35}Looks like she already left.{/cps}"
            "{cps=35}Her shoes aren't here either.{/cps}"
            "{cps=35}Better head straight to school.{/cps}"
            mc "{cps=35}Sorry, [y], I'm going ahead.{/cps}"
            "{cps=35}Just as I was about to turn around—{/cps}"
            y "{cps=35}WAIT!{/cps}"
            "{cps=35}Huh?{/cps}"
            "{cps=35}[y] appeared from inside the house, out of breath.{/cps}"
            y "{cps=35}Hah.... hah....{/cps}"
            mc "{cps=35}What's wrong, [y]?{/cps}"
            y "{cps=35}Do you have a drink?{/cps}"
            mc "{cps=35}Ummm, do I?{/cps}"
            y "{cps=35}Here!{/cps}"
            "{cps=35}[y] immediately took my water bottle.{/cps}"
            "{cps=35}Then drank from it directly.{/cps}"
            y "{cps=35}Phew! Much better.{/cps}"
            mc "{cps=35}Ah...{/cps}"
            "{cps=35}An indirect kiss...{/cps}"
            "{cps=35}Wait, what am I thinking!?{/cps}"
            "{cps=35}She was probably just exhausted.{/cps}"
            y "{cps=35}Thanks, [mc].{/cps}"
            mc "{cps=35}You're welcome.{/cps}"
            y "{cps=35}Let's go.{/cps}"
            mc "{cps=35}Yeah.{/cps}"
            jump chapter_2_sastra_otw

label chapter_2_sastra_otw:
    "{cps=35}We walked to school together.{/cps}"
    "{cps=35}Each with our own destination, of course.{/cps}"
    "{cps=35}[y] with Student Council business, and me with Literature Club business.{/cps}"
    "{cps=35}But today...{/cps}"
    if callyuukafirst:
        "{cps=35}[y] looked different.{/cps}"
        "{cps=35}Her face still showed traces of crying.{/cps}"
        mc "{cps=35}Are you sure you're okay, [y]?{/cps}"
        mc "{cps=35}Is it because of me?{/cps}"
        "{cps=35}[y] stopped and faced me.{/cps}"
        y "{cps=35}You're not at fault, [mc].{/cps}"
        y "{cps=35}I'm just still a little shocked.{/cps}"
        mc "{cps=35}Shocked by what?{/cps}"
        y "{cps=35}You suddenly choosing Literature.{/cps}"
        y "{cps=35}Even though from the start I wanted us to be together.{/cps}"
        mc "{cps=35}Oh, that..{/cps}"
        mc "{cps=35}I'm sorry.{/cps}"
        mc "{cps=35}I also joined Literature for my own reasons, [y].{/cps}"
        y "{cps=35}Reasons? What reasons?{/cps}"
        y "{cps=35}Is it because of [sh]?{/cps}"
        mc "{cps=35}Yeah... something like that.{/cps}"
        y "{cps=35}Do you have feelings for her?{/cps}"
        mc "{cps=35}What do you mean?{/cps}"
        y "{cps=35}Romantic feelings.{/cps}"
        mc "{cps=35}It's not that. More like I'm curious about her.{/cps}"
        mc "{cps=35}Why she keeps appearing in my thoughts.{/cps}"
        mc "{cps=35}Even though I don't remember ever meeting her ten years ago.{/cps}"
        y "{cps=35}That means you still have unfinished business with her.{/cps}"
        mc "{cps=35}Maybe... but I don't know what that business is.{/cps}"
        mc "{cps=35}I've always stayed home, barely ever played outside.{/cps}"
        mc "{cps=35}You know how I am, [y].{/cps}"
        y "{cps=35}I've known you since five years ago, especially after you moved into this neighborhood.{/cps}"
        y "{cps=35}And while living here you barely ever went out to play.{/cps}"
        mc "{cps=35}Right?{/cps}"
        y "{cps=35}But something must have happened before you moved.{/cps}"
        mc "{cps=35}Maybe...{/cps}"
    else:
        mc "{cps=35}Um...{/cps}"
        y "{cps=35}Be quiet.{/cps}"
        mc "{cps=35}[y]?{/cps}"
        "{cps=35}She ignored me completely.{/cps}"
        mc "{cps=35}It's so cold today.{/cps}"
        y "{cps=35}You're the one who started it.{/cps}"
        mc "{cps=35}Why me?{/cps}"
        mc "{cps=35}What did I even do wrong?{/cps}"
        y "{cps=35}What do you think?{/cps}"
        mc "{cps=35}I don't know, that's why I'm asking.{/cps}"
        y "{cps=35}Figure it out yourself.{/cps}"
        mc "{cps=35}Any chance of that?{/cps}"
        y "{cps=35}No chance.{/cps}"
        mc "{cps=35}Straight to no chance?{/cps}"
        y "{cps=35}Figure out your own mistakes, idiot.{/cps}"
        mc "{cps=35}Fine, I was wrong. I'm sorry.{/cps}"
        y "{cps=35}That's it? Zero effort.{/cps}"
        y "{cps=35}And you're just like that.{/cps}"
        mc "{cps=35}What even...{/cps}"
        if jajan:
            mc "{cps=35}At least yesterday I treated you.{/cps}"
            y "{cps=35}Come on, that was nothing.{/cps}"
            y "{cps=35}I'll pay you back later.{/cps}"
            mc "{cps=35}I don't need the money. I just need your explanation.{/cps}"
            mc "{cps=35}Just explain already, [y].{/cps}"
        else:
            mc "{cps=35}Good thing I didn't go to the cafeteria.{/cps}"
            y "{cps=35}What's that got to do with anything?{/cps}"
            mc "{cps=35}If I'd gone, I'd have been forced to pay.{/cps}"
            y "{cps=35}Such a cheapskate.{/cps}"
            mc "{cps=35}Whatever.{/cps}"
            y "{cps=35}You're always like this.{/cps}"
            mc "{cps=35}Seriously, what's wrong with you, [y]?{/cps}"
            mc "{cps=35}Just explain!{/cps}"
        "{cps=35}[y] stopped walking.{/cps}"
        y "{cps=35}Do you really want to know?{/cps}"
        mc "{cps=35}Of course, so I know where I went wrong.{/cps}"
        y "{cps=35}Fine then.{/cps}"
        y "{cps=35}One!{/cps}"
        y "{cps=35}You never called me back.{/cps}"
        y "{cps=35}Even though I was waiting for you.{/cps}"
        mc "{cps=35}But at that time A—{/cps}"
        y "{cps=35}Two!{/cps}"
        y "{cps=35}You joined the Literature Club without my agreement.{/cps}"
        mc "{cps=35}But that—{/cps}"
        y "{cps=35}Three!{/cps}"
        mc "{cps=35}There's more!?{/cps}"
        y "{cps=35}You don't care about how I'm doing.{/cps}"
        y "{cps=35}Do you even know how mean you are!?{/cps}"
        "{cps=35}I went silent. The word 'mean' felt like a hard slap across my face.{/cps}"
        "{cps=35}Waiting for [y], whose breathing was getting heavier from emotion.{/cps}"
        mc "{cps=35}Done?{/cps}"
        y "{cps=35}That's enough.{/cps}"
        mc "{cps=35}Can I talk?{/cps}"
        y "{cps=35}Go ahead.{/cps}"
        "{cps=35}I took a long breath. The morning air felt very cold, but my chest felt far hotter.{/cps}"
        "{cps=35}I couldn't lie to her. Not after seeing her eyes this swollen.{/cps}"
        mc "{cps=35}First of all... I'm sorry. I know I've been selfish.{/cps}"
        y "{cps=35}That's all?{/cps}"
        mc "{cps=35}Hold on. Please just listen to me this once.{/cps}"
        mc "{cps=35}It's not that I don't care about you. I also remember your promise about the Student Council.{/cps}"
        y "{cps=35}And?{/cps}"
        mc "{cps=35}But this has to do with my past, [y].{/cps}"
        y "{cps=35}The past...?{/cps}"
        y "{cps=35}With who?{/cps}"
        mc "{cps=35}[sh].{/cps}"
        "{cps=35}That name made [y]'s shoulder tremble slightly.{/cps}"
        "{cps=35}She looked down, hiding her eyes behind her bangs.{/cps}"
        y "{cps=35}So... you're choosing to continue your relationship with her?{/cps}"
        y "{cps=35}And sacrificing your promise to me?{/cps}"
        mc "{cps=35}Not sacrificing, [y]. I just...{/cps}"
        y "{cps=35}Just what? Answer clearly so I understand, [mc].{/cps}"
        "{cps=35}Yuuka lifted her face. Tears started welling at the edges of her eyes, but she held them back hard.{/cps}"
        y "{cps=35}Was I... was I not important enough to you this whole time, [mc]?{/cps}"
        mc "{cps=35}Look, [y].{/cps}"
        "{cps=35}I gently touched [y]'s shoulder.{/cps}"
        y "{cps=35}Ha—{/cps}"
        mc "{cps=35}I chose the Literature Club because on the first day yesterday,{/cps}"
        mc "{cps=35}[sh] said she was someone I knew from ten years ago.{/cps}"
        mc "{cps=35}And I don't remember anything about that.{/cps}"
        mc "{cps=35}Then I felt like something was missing inside me.{/cps}"
        mc "{cps=35}So I thought I might be able to find out what all of this means.{/cps}"
        mc "{cps=35}And maybe it also has something to do with my late older sister.{/cps}"
        "{cps=35}[y] went silent.{/cps}"
        y "{cps=35}You... why didn't you say so from the start?{/cps}"
        y "{cps=35}If you'd told me from the beginning I could have helped you.{/cps}"
        mc "{cps=35}I wanted to, but you were the one who jumped to conclusions.{/cps}"
        y "{cps=35}But you don't have any other goal, right? Like getting closer to them?{/cps}"
        mc "{cps=35}None.{/cps}"
        y "{cps=35}Alright then..{/cps}"
        "{cps=35}For some reason I felt a little relieved after being honest with [y].{/cps}"
        "{cps=35}But...{/cps}"
        y "{cps=35}Hey, [mc].{/cps}"
        mc "{cps=35}What?{/cps}"
        y "{cps=35}How long are you going to keep holding my shoulder?{/cps}"
        mc "{cps=35}Ah right! Sorry.{/cps}"
        "{cps=35}Damn, I got too comfortable touching her shoulder.{/cps}"
        y "{cps=35}Oh right, look at the time.{/cps}"
        y "{cps=35}Let's hurry, [mc].{/cps}"
        mc "{cps=35}Yeah.{/cps}"
        "{cps=35}We immediately hurried toward school.{/cps}"
        

    scene bg_classroom_morning with fade
    play music "audio/bgm/schoolgate.mp3" fadein 2.0

    "{cps=35}I sat at my desk with mixed feelings. The usually noisy classroom atmosphere felt distant in my ears.{/cps}"
    "{cps=35}In front of me, Yuuka was already sitting in silence. She didn't greet me, didn't even look over. She was just flipping through her book pages with rough movements.{/cps}"

    # --- INTERACTION WITH YUUKA IN CLASS ---
    mc "{cps=40}[y]...{/cps}"
    
    y "{cps=40}...{/cps}"

    "{cps=35}Silence. She was really giving me the silent treatment because of my choice this morning.{/cps}"
    "{cps=35}Suddenly, a small shadow stood beside my desk.{/cps}"
    sh "{cps=35}Ikazaki...{/cps}"
    "{cps=35}[sh] looked at me with a slightly serious face.{/cps}"
    mc "{cps=35}Eh [sh], what's up?{/cps}"
    sh "{cps=35}N-nothing...{/cps}"
    "{cps=35}Weird...{/cps}"
    "{cps=35}She rarely ever approaches me like this.{/cps}"
    "{i}[sh] thinking: \"Damn little sister... why do I have to do this just to follow her orders...\"{/i}"
    sh "{cps=35}Are you free this afternoon?{/cps}"
    mc "{cps=35}Umm... yeah, why?{/cps}"
    sh "{cps=35}I want to talk with you later. Is that okay?{/cps}"
    "{cps=35}[y] looked at me with a cynical face.{/cps}"
    "{cps=35}Ugh...{/cps}"
    "{cps=35}Why did you come at the worst possible time, [sh]...{/cps}"
    "{cps=35}[y] immediately turned her face away from me.{/cps}"
    "{cps=35}As if saying 'Not my problem'.{/cps}"
    mc "{cps=35}Umn... sure, [sh].{/cps}"
    sh "{cps=35}Phew... thank goodness..{/cps}"
    sh "{cps=35}I'll wait for you later.{/cps}"
    "{cps=35}[sh] went straight back to her seat.{/cps}"
    v "{cps=35}Oho... adding another one, huh.{/cps}"
    mc "{cps=35}What are you on about, Vin.{/cps}"
    v "{cps=35}Ehehe...{/cps}"
    "{cps=35}The bell for class rang.{/cps}"
    sh "{cps=35}I wonder what we'll learn today...{/cps}"

    scene black with fade
    "{cps=35}Class started. But [sh]'s invitation kept ringing in my head. What was actually going to happen?{/cps}"

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
    
    # A more human math problem
    t "{cps=40}If 3x + 5 = 20, what is the value of x?{/cps}"

    "{cps=35}Ugh... my mind went blank. The numbers seemed to dance in front of my eyes.{/cps}"
    if jujur:
        "{cps=35}Yuuka looked panicked — she held up five fingers under the desk as a signal.{/cps}"
        "{cps=35}Then [sh]...{w=0.1} she also gave a signal for the number 5.{/cps}"
    else:
        "{cps=35}Yuuka looked completely normal, not giving any signal at all.{/cps}"
        "{cps=35}But [sh]...{w=0.1} she gave a signal for the number 5.{/cps}"
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
            if jujur:
                "{cps=35}Yuuka sighed in relief and gave me a small smile. Behind me, Vina looked slightly disappointed she couldn't laugh at me.{/cps}"
            else:
                "{cps=35}Yuuka stayed quiet, giving no reaction, but [sh] looked a little calmer.{/cps}"
            v "{cps=60}Tch... so the Rare Specimen can do math after all.{/cps}"

        "15":
            $ correct_answer = False
            $ yuuka_rel -= 2
            $ shoko_rel -= 2
            mc "{cps=40}The answer is... 15, Miss?{/cps}"
            
            "{cps=35}The whole class burst out laughing. Even Vina behind me had to cover her mouth so she wouldn't be too loud.{/cps}"
            t "{cps=40}Fifteen? Are you solving for x or calculating the price of fried snacks at the cafeteria? Wrong!{/cps}"
            t "{cps=40}Stand in front until my class is over!{/cps}"
            
            if jujur:
                "{cps=35}Yuuka slapped her forehead as if she couldn't believe I'd gotten it wrong. Behind me, Vina was laughing quietly at my answer.{/cps}"
            else:
                "{cps=35}Yuuka stayed quiet, giving no reaction, but [sh] looked a little disappointed.{/cps}"
        "3":
            $ correct_answer = False
            $ yuuka_rel -= 2
            $ shoko_rel -= 2
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
        v "{cps=35}But... why did you get it wrong?{/cps}"
        mc "{cps=35}I don't know.. I guess I had a lot on my mind.{/cps}"
        v "{cps=35}Felt like you weren't doing anything though...{/cps}"
        v "{cps=35}You think so too, right [y]?{/cps}"
        y "{cps=35}Ummm... yeah..{/cps}"
        if jujur:
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
            y "{cps=40}That's why you should pay attention in class. Don't just get lost in your own world.{/cps}"
            v "{cps=35}Hey... what's going on, Ka?{/cps}"
            y "{cps=40}I don't know. If you want to know, ask [mc] yourself.{/cps}"
            "{cps=40}[y] left us without another word.{/cps}"
            v "{cps=40}Looks like there's drama...{/cps}"
            v "{cps=40}What did you do to her?{/cps}"
            mc "{cps=40}Ah, it's not like that.{/cps}"
            v "{cps=40}Hah...{w=0.1} [y]!{/cps}"
            "{cps=40}[v] immediately ran after [y].{/cps}"
            "{cps=40}Leaving me alone.{/cps}"
    else:
        "{cps=40}[v] and [y] immediately came over to me.{/cps}"
        "{cps=40}Seemed like they wanted to give me some kind of 'lecture'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Smart one.{/cps}"
        mc "{cps=40}Hey!{/cps}"
        v "{cps=40}Come on, I was just kidding. But seriously, you did okay when you went up.{/cps}"
        mc "{cps=40}What even...{/cps}"
        v "{cps=35}Tell me how you managed to answer...{/cps}"
        "{cps=35}[y] stuck close beside me.{/cps}"
        mc "{cps=35}I don't know...{/cps}"
        "{cps=35}I looked around while turning my face away from [v]...{/cps}"
        
        "{cps=35}[y] looked a little annoyed.{/cps}"
        y "{cps=40}Hah... you two...{/cps}"
        y "{cps=35}[v], let's go to the cafeteria.{/cps}"
        v "{cps=40}Let's go! [mc], you coming?{/cps}"
        mc "{cps=40}Not this time, still full.{/cps}"
        v "{cps=40}Hmm... you sure?{/cps}"
        mc "{cps=40}Yap.{/cps}"
        v "{cps=40}Okay then, see you later.{/cps}"
        "{cps=40}[y] and [v] left me alone.{/cps}"
        
    # Can be improved here
    sh "{cps=35}As usual, always lively around you, [mc].{/cps}"
    "{cps=35}Shoko was suddenly already near me. Her calm voice contrasted with Yuuka and Vina's noise earlier.{/cps}"
    mc "{cps=35}Yeah, pretty much...{/cps}"
    sh "{cps=35}You're not going to the cafeteria with them?{/cps}"
    mc "{cps=35}Not right now.{/cps}"
    "{cps=35}Because I don't have any money on me.{/cps}"
    sh "{cps=35}Then the timing is perfect..{/cps}"
    mc "{cps=35}Timing? What do you—{/cps}"
    "{cps=35}Without warning, Shoko grabbed my hand. Her grip was small but very strong, forcing me to stand and follow her out of the classroom.{/cps}"
    mc "{cps=35}He-hey! Where are you taking me?{/cps}"
    sh "{cps=35}Just follow.{/cps}"
    "{cps=35}She led me away.{/cps}"

    # Changed because MC already joined Literature from the start
    sh "{cps=35}Come in, [mc].{/cps}"
    mc "{cps=35}*Gulp...* Alright.{/cps}"
    "{cps=35}And after I opened it—{/cps}"
    "{cps=35}I saw books neatly arranged on the shelves.{/cps}"
    "{cps=35}And a girl reading a book.{/cps}"
    "{cps=35}From her crimson hair... {w=0.1} she looked like [sh]'s twin who was late yesterday—only the hairstyle was different..{/cps}"
    yk "{cps=35}So, I want to ask you something, [mc]. Why did you choose Literature over the Student Council or any other organization?{/cps}"
    mc "{cps=35}Ummmnn....{/cps}"
    "{cps=35}How am I supposed to tell them{/cps}"
    "{cps=35}That my real goal is to recover the memories I've lost...{/cps}"
    "{cps=35}I'll just answer like this.{/cps}"
    mc "{cps=35}I'm just interested in Literature. Nothing else.{/cps}"
    yk "{cps=35}Hmm... suspicious...{/cps}"
    yk "{cps=35}You think the same, right, big sis?{/cps}"
    "{cps=35}Looks like [yk] can't be fooled.{/cps}"
    "{cps=35}What should I do...{/cps}"
    sh "{cps=35}I don't really care, [yk].{/cps}"
    yk "{cps=35}Haaah.... boring.{/cps}"
    sh "{cps=35}As long as you're here with me.. that's enough, [mc].{/cps}"
    yk "{cps=35}Yeah... after all, the goal was for us to be together again, right, big sis?{/cps}"

    # Shoko doesn't jump because MC already joined Literature from the start - different scene instead

    "{cps=35}I sat down and tried to focus, but I couldn't stop thinking about Shoko. Up ahead, she sat calmly as if nothing had happened, but I knew... starting today, everything would change.{/cps}"
    t "{cps=40}Now open your History books. We'll be discussing 'Tragedy and Betrayal' in the history of organizational movements.{/cps}"

    t "{cps=40}Throughout history, many great figures fell not because of enemies from outside, but because of broken 'Trust' from those closest to them.{/cps}"
    
    # Educational element
    t "{cps=40}There's a Latin phrase: {b}'Falsus in Uno, Falsus in Omnibus'{/b}. Anyone know what it means?{/cps}"

    "{cps=35}The class was silent. I glanced at [y] — she was taking notes very quickly, as if trying to ignore my existence.{/cps}"
    "{cps=40}As usual, she was completely focused.{/cps}"
    "{cps=40}Unlike me...{/cps}"
    "{cps=35}But [sh]... she'd been watching me ever since earlier.{/cps}"
    t "{cps=40}[mc], try answering. You've seemed to be daydreaming since the start of this lesson.{/cps}"
    mc "{cps=40}Why me, [t]?{/cps}"
    t "{cps=40}Who else has been daydreaming besides you?{/cps}"
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
            if jujur:
                $ yuuka_rel -= 5
                "{cps=35}Yuuka stopped writing for a moment. Her shoulder trembled slightly, but she still didn't look over.{/cps}"
                "{cps=35}She seemed to be processing those words, convincing herself that my decision to join Literature — sudden as it was — was a bitter honesty.{/cps}"
                unknown "{cps=35}Then why were you in the attic doing that...{/cps}"
                "{cps=35}A very soft murmur came from in front of me. So quiet, but full of suspicion.{/cps}"
            else:
                $ yuuka_rel -= 5
                unknown "{cps=35}Liar.{/cps}"
                "{cps=35}A very soft murmur came from in front of me. So quiet, but full of suspicion.{/cps}"
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
    
    "{cps=35}Yuuka stopped writing for a moment. Her shoulder trembled slightly; her hand gripped the pen so tightly her nails went white.{/cps}"
    "{cps=35}I knew she was listening to every word. And I knew Miss Nanami's words were landing right in the middle of the awkwardness between us.{/cps}"

    "{cps=35}Miss Nanami returned to the blackboard, the chalk screeching as she wrote a list of history's great traitors.{/cps}"
    "{cps=35}The classroom atmosphere grew heavy. There was only the sound of pens on paper and the wall clock ticking as if deliberately slowed down.{/cps}"

    "{cps=35}One hour passed...{/cps}"
    "{cps=35}The harsh midday sunlight slowly shifted, casting long shadows from the desk legs across the wooden classroom floor.{/cps}"
    "{cps=35}Some of my classmates started looking sleepy, their heads nodding along to Miss Nanami's monotone yet sharp voice.{/cps}"
    
    "{cps=35}[t]'s voice explaining the fall of great kingdoms from internal betrayal felt like a whisper judging every breath I took.{/cps}"

    "{cps=35}I glanced forward. [y] stayed in her position. She never once looked my way, even when she reached for a ruler or fixed her hair.{/cps}"
    "{cps=35}But [sh]... she was still watching me.{/cps}"
    "{cps=35}Two hours passed...{/cps}"
    "{cps=35}Time truly felt eternal. My legs felt stiff, and my thoughts drifted to Shoko, to the Literature Club, and to what happened during break..{/cps}"
    if correct_answer:
        "{cps=35}Every second we spent in this silence felt more painful than the punishment of standing in front of the class this morning.{/cps}"
    else:
        "{cps=35}Every second we spent in this silence felt more painful than a sharp object stabbing me.{/cps}"
    "{cps=35}The wall of ice [y] had built in front of me felt thicker and thicker. I wanted to speak, but my throat was locked by the weight of secrets and the choice I'd just made.{/cps}"
    "{cps=35}My presence here... in the back... felt completely erased from her little world.{/cps}"
    "{cps=35}But when I tried glancing slightly toward the very back row...{/cps}"
    "{cps=35}[sh] was still there. Behind Yukie, she watched me with a calm but intense gaze. As if she were watching over 'what was hers' so it wouldn't disappear again.{/cps}"


    scene black with fade
    stop music fadeout 3.0

    play sound "audio/sfx/school bell.mp3"
    "{cps=40}Ting... Tong...{/cps}"
    "{cps=40}The dismissal bell finally rang.{/cps}"
    
    # MC can go to Literature room or elsewhere with Shoko and Yukie
    
    # Improved: MC, Yukie, and Shoko are sent to the warehouse by the president (Fumi) to find documents, then meet Vina and Yuuka at the warehouse

    yk "{cps=35}Hmmm... I'm here to get a book with manuscripts in it.{/cps}"
    v "{cps=35}Manuscripts? What kind?{/cps}"
    yk "{cps=35}Some kind of book. Apparently it's really old.. from about twelve years ago.{/cps}"
    v "{cps=35}Hmm... need our help?{/cps}"
    yk "{cps=35}If it's not too much trouble.{/cps}"
    v "{cps=35}Okay then — in exchange, help us with the audit.{/cps}"
    yk "{cps=35}Deal!{/cps}"
    "{cps=35}So we worked together on the audit and searched for that book.{/cps}"
    "{cps=35}From what I'd heard, the book was quite old and worn.{/cps}"
    "{cps=35}But throughout the search and audit...{/cps}"
    "{cps=35}I didn't find the book at all.{/cps}"
    v "{cps=35}Hah... the audit's done. Thanks for helping us.{/cps}"
    yk "{cps=35}No problem.. but has the book been found?{/cps}"
    v "{cps=35}I didn't find it at all.{/cps}"
    v "{cps=35}Looking for a book in a place like this is like finding a needle in a haystack.{/cps}"
    yk "{cps=35}Ehehe, true..{/cps}"
    "{cps=35}Elsewhere..{/cps}"

    # Scene change is fine
    "{cps=35}[sh] and [y] were alone together, wanting to discuss everything that had happened.{/cps}"
    sh "{cps=35}Why did you call me so that it's just the two of us here?{/cps}"
    y "{cps=35}Look, [sh]...{/cps}"
    y "{cps=35}Why did you run up to the attic crying earlier?{/cps}"
    sh "{cps=35}Do you want to know the truth?{/cps}"
    y "{cps=35}Yes! Because I don't want anything weird happening to my childhood friend.{/cps}"
    sh "{cps=35}Alright then.{/cps}"
    "{cps=35}[sh] told her everything that had happened, from the reunion after ten years to the incident in the attic.{/cps}"
    y "{cps=35}So that's how it is...{/cps}"
    y "{cps=35}I didn't expect [mc] to be like that... it must be hard for you, [sh].{/cps}"
    sh "{cps=35}That's how it is. It hurts realizing I was the only one holding onto that promise alone.{/cps}"
    "{cps=35}Yuuka went silent. She looked at Shoko with a gaze that was no longer cynical. A sense of solidarity appeared between them as two people who'd both been 'given a headache' by [mc].{/cps}"
    y "{cps=35}Then why don't you just hate him?{/cps}"
    sh "{cps=35}Because... {w=0.5}he saved me earlier. Not just from falling, but from my own thoughts.{/cps}"
    y "{cps=35}I see...{/cps}"
    
    # MC doesn't have to get hit by them, the important part is getting the documents
    mc "{cps=35}Look at this... this book fell out of the box that almost hit [y] and [sh].{/cps}"
    "{cps=35}Seeing that book, Yukie and Shoko's expressions immediately turned serious. Their teasing stopped at once.{/cps}"
    yk "{cps=35}This book...{/cps}"
    yk "{cps=35}This is what Senior was looking for! Thank you, all three of you!{/cps}"
    "{cps=35}What kind of coincidence is this?{/cps}"
    "{cps=35}What even is this book?{/cps}"
    yk "{cps=35}If I'm not wrong...{w=0.1} this book is an old proposal from the Literature Club.{/cps}"
    "{cps=35}Wait, doesn't that have your name on it, [mc]?{/cps}"
    mc "{cps=35}Seems so. There's a faintly written name 'Ikazaki' on the cover.{/cps}"
    y "{cps=35}If I'm not wrong, the president once said your sister went to school here twelve years ago, right?{/cps}"
    mc "{cps=35}Yeah... from the name, no doubt, that's my sister.{/cps}"
    mc "{cps=35}Why would it be here?{/cps}"
    v "{cps=35}We should take this to the Student Council room.{/cps}"
    yk "{cps=35}But my senior asked for it...{/cps}"
    v "{cps=35}How about you contact your senior from Literature so they can gather in the Student Council room too?{/cps}"
    yk "{cps=35}Good idea!{/cps}"
    "{cps=35}[yk] immediately contacted the senior in the Literature room.{/cps}"
    yk "{cps=35}I've contacted them. She'll be in the Student Council room later.{/cps}"
    v "{cps=35}Alright, now let's move.{/cps}"
    "{cps=35}We moved to the Student Council room.{/cps}"

    # Improvement is fine, no need to be too romantic
    "{cps=35}One thing was certain: My life would never be the same again.{/cps}"
    scene black with fade
    stop music fadeout 2.0
    "{cps=35}Our footsteps echoed through the quiet corridor. The afternoon sun came through the windows, casting a sharp orange on the Student Council door.{/cps}"

    play sound "audio/sfx/knock door.mp3"
    "{b}*Tok! Tok! Tok!*{/b}"

    mc "{cps=35}Excuse me...{/cps}"

    play sound "audio/sfx/door.mp3"
    "{cps=35}As the door opened, the scent of jasmine tea and new paper greeted us. Behind the large desk, Senior Maya was already sitting perfectly upright.{/cps}"

    show maya_neutral at center with dissolve
    m "{cps=40}You're fifteen minutes late from the audit schedule. And I see... you've brought uninvited 'guests'.{/cps}"
    "{cps=35}Maya looked at Shoko and Yukie with a cold gaze I'd never seen before.{/cps}"

    y "{cps=35}Sorry, Senior. There was a small incident in the warehouse. And... we found this.{/cps}"

    "{cps=35}I stepped forward and placed the brown book on Maya's desk.{/cps}"

    "{cps=35}Instantly, I saw Maya's expression change. Just for a moment, but I could see her eyes widen. Her hand holding the pen tightened slightly.{/cps}"

    m "{cps=40}Where... where did you find this?{/cps}"
    sh "{cps=35}Under a shelf that almost hurt us, Senior.{/cps}"
    m "{cps=35}Almost hurt you? What were you even doing to end up like that?{/cps}"
    v "{cps=35}Yeah... hard to explain, Senior.{/cps}"
    "{cps=35}Shoko stepped forward, standing beside me. She no longer looked weak. She faced Senior [m] bravely.{/cps}"
    m "{cps=35}Shirohana Shoko... I already told you not to interfere in this matter.{/cps}"
    "{cps=35}Suddenly, footsteps could be heard from the still-open doorway.{/cps}"
    unknown "{cps=35}Sorry I'm late. Looks like the discussion has already started?{/cps}"
    m "{cps=35}Well well... so you finally show up too, after the opening yesterday.{/cps}"
    "{cps=35}Kisaragi [f].{/cps}"
    "{cps=35}Ah... right, I joined this organization because I was curious about [sh].{/cps}"
    "{cps=35}But I didn't even know who the members were, including the president.{/cps}"
    "{cps=35}How pathetic of me.{/cps}"
    f "{cps=35}Yeah... that's how it is.{/cps}"
    f "{cps=35}Lots of activities after new student orientation.{/cps}"
    f "{cps=35}Even though that should have been Student Council work.{/cps}"
    m "{cps=35}What can we do, [f]? Student Council members aren't enough to handle all of that.{/cps}"
    "{cps=35}[f] looked at [m] with a cynical face, as if unhappy with the current atmosphere.{/cps}"
    f "{cps=35}So? What's going on?{/cps}"
    m "{cps=35}You know this proposal, right?{/cps}"
    "{cps=35}[m] showed the proposal to [f].{/cps}"
    f "{cps=35}Ahh! After searching for a whole year... I finally found it.{/cps}"
    "{cps=35}[f] wanted to take the proposal.{/cps}"
    m "{cps=35}Hold it! Easy there — this is Student Council property, plus it's a rejected proposal.{/cps}"
    f "{cps=35}What!?{/cps}"
    sh "{cps=35}Rejected? Or hidden?{/cps}"
    "{cps=35}[m] was startled by [sh]'s answer.{/cps}"
    m "{cps=35}What do you mean?{/cps}"
    sh "{cps=35}If it wasn't hidden, why was the proposal in the warehouse?{/cps}"
    sh "{cps=35}And inside a box, no less.{/cps}"
    "{cps=35}[m] fell completely silent, as if she didn't know what answer to give.{/cps}"
    m "{cps=35}That... {w=0.5}that was the business of the board from twelve years ago! I only ordered you to do an audit, nothing more.{/cps}"
    f "{cps=35}Then why are you so afraid of that proposal, [m]?{/cps}"
    f "{cps=35}You're not hiding something, are you?{/cps}"
    m "{cps=35}Uhm....{/cps}"
    "{cps=35}The Student Council members stared at [m]'s face full of questions.{/cps}"
    m "{cps=35}Hah.... in the end I have to explain it again, huh?{/cps}"
    m "{cps=35}Alright. I'll explain about that proposal.{/cps}"
    "{cps=35}[m] stood up from her chair and began to tell the story.{/cps}"
    m "{cps=35}That proposal has existed since twelve years ago, made by Ikazaki [mi].{/cps}"
    m "{cps=35}But it was never realized by the school or the Student Council.{/cps}"
    m "{cps=35}Even though she was the Student Council President at the time.{/cps}"
    mc "{cps=35}How do you know it in such detail, Senior [m]?{/cps}"
    m "{cps=35}Because your sister gave me the mandate to realize the activities in that proposal.{/cps}"
    mc "{cps=35}Since when? As I recall, Senior [m] only said she knew my sister's name.{/cps}"
    "{cps=35}I looked at Senior [m] seriously and full of curiosity.{/cps}"
    "{cps=35}Why are you staring at me like that? Don't you trust me?{/cps}"
    "{cps=35}Even if [mi] gave you a mandate, try telling us about it.{/cps}"
    "{cps=35}[f] also joined in making [m] feel cornered.{/cps}"
    "{cps=35}It all happened about ten years ago... when the proposal was finished.{/cps}"
    
    # Flashback - leave as is, improve if wanted
    "[m]'s Older Sister" "{cps=35}Haaaaahhhhh... so sore.{/cps}"
    "[m]'s Older Sister" "{cps=35}Are you sure you want to run this project, [mi]? We're short on people.{/cps}"
    v "{cps=35}Who's asking?{/cps}"
    y "{cps=35}Hush! Senior [m] is still telling the story. Just listen.{/cps}"
    v "{cps=35}Ehehe, sorry.{/cps}"
    m "{cps=35}The one asking was my older sister. Her name is Kirishima [sz].{/cps}"
    v "{cps=35}Hmm...{/cps}"
    m "{cps=35}Can I continue?{/cps}"
    y "{cps=35}Please continue, Senior.{/cps}"
    "{cps=35}Alright.{/cps}"
    mi "{cps=35}Hmmm, how about this...{/cps}"
    mi "{cps=35}Let's postpone this project for now.{/cps}"
    sz "{cps=35}Are you sure?{/cps}"
    mi "{cps=35}Yeah... I haven't submitted it to the teachers yet, plus we don't know if the Literature kids want to collaborate.{/cps}"
    sz "{cps=35}True enough.{/cps}"
    sz "{cps=35}But postpone until when?{/cps}"
    mi "{cps=35}Well... what about your little sister?{/cps}"
    sz "{cps=35}Hue— she's still a kid! Are we supposed to wait ten years?{/cps}"
    "{cps=35}Well.. better than the project never happening, right? I'll have my little sister enroll at our school later.{/cps}"
    sz "{cps=35}She's a boy, you know.{/cps}"
    mi "{cps=35}Yeah... who knows, maybe the rules will change to allow boys in.{/cps}"
    sz "{cps=35}You... dreaming in broad daylight.{/cps}"
    mi "{cps=35}I'm not dreaming. It'll happen for sure.{/cps}"
    mi "{cps=35}You'll be the one handling our school's administration later anyway.{/cps}"
    sz "{cps=35}Hah? Since when did I want to be school admin?{/cps}"
    sz "{cps=35}I want to be a doctor.{/cps}"
    mi "{cps=35}Who knows.{/cps}"
    mi "{cps=35}Ah! [sz]'s little sister!{/cps}"
    m "{cps=35}Hm? What is it, sis?{/cps}"
    mi "{cps=35}You'll enroll at the same school as your sister, okay!{/cps}"
    m "{cps=35}Why?{/cps}"
    mi "{cps=35}You'll be the one to continue your sister's work.{/cps}"
    sz "{cps=35}Hey! What if she doesn't want to?{/cps}"
    mi "{cps=35}Relax... you'll be helped by my little brother.{/cps}"
    m "{cps=35}Your little brother? What's his name?{/cps}"
    mi "{cps=35}Ikazaki [mc]. Remember that name, because you'll definitely meet him.{/cps}"
    mi "{cps=35}Plus he'll definitely help you.{/cps}"
    sz "{cps=35}Hey [mi]... don't indoctrinate my little sister with weird stuff!{/cps}"
    mi "{cps=35}I'm not. I'm just giving input, and he might not even want to.{/cps}"
    m "{cps=35}Ummm... I'll try.{/cps}"
    "Maya (thinking)" "{cps=35}I won't let my sisters' struggles be in vain.{/cps}"
    "Maya (thinking)" "{cps=35}I can definitely make this happen!{/cps}"
    m "{cps=35}Back then I was full of burning enthusiasm.{/cps}"
    m "{cps=35}But in the final moments... before they sent that proposal to the teachers...{/cps}"
    m "{cps=35}A disaster happened that postponed the event and made the proposal 'disappear'.{/cps}"
    m "{cps=35}I can't tell you the details because I don't know what happened at that time.{/cps}"
    v "{cps=35}Damn.. why leave it hanging like this.{/cps}"
    "{cps=35}If you're curious, you can ask my older sister.{/cps}"
    "{cps=35}Senior [m]'s older sister is named [sz], right?{/cps}"
    "{cps=35}Sounds like the teacher in the health and administration office..{/cps}"
    "{cps=35}Yes, that's her.{/cps}"
    "Everyone" "{cps=35}WHAT!?{/cps}"
    mc "{cps=35}Wait... which Doctor Kirishima is that?{/cps}"
    m "{cps=35}The one you met in the administrative office on the first day.{/cps}"
    mc "{cps=35}Hmmmm....{/cps}"
    "{cps=35}So different!{/cps}"
    f "{cps=35}Why does she look so different from you?{/cps}"
    m "{cps=35}Well... I don't want to look too similar, plus we're from different eras.{/cps}"
    m "{cps=35}Any other questions?{/cps}"
    v "{cps=35}Maybe this... what should we do with the proposal?{/cps}"
    "{cps=35}[f] stepped forward, her hand touching the worn cover of the book. Her gaze was no longer cynical, but full of determination.{/cps}"
    f "{cps=35}Maybe let the Literature Club revise it, and you all receive it — how about that?{/cps}"
    f "{cps=35}Plus from the story earlier, the Literature Club was the intended target.{/cps}"
    f "{cps=35}You don't mind, right?{/cps}"
    "{cps=35}[f] looked at us with a hopeful face.{/cps}"
    mc "{cps=35}I don't mind... how about you all?{/cps}"
    yk "{cps=35}As long as big sis agrees, I don't mind.{/cps}"
    mc "{cps=35}What about you, [sh]?{/cps}"
    sh "{cps=35}It's fine, [mc]. Besides, you want to make new memories, right?{/cps}"
    v "{cps=35}Hmm, what memories?{/cps}"
    y "{cps=35}You... always like this, [v].{/cps}"
    v "{cps=35}Hmm, what?{/cps}"
    sh "{cps=35}You don't mind, right [y]?{/cps}"
    y "{cps=35}Hmm! No problem.{/cps}"
    if jujur:
        "Yuuka (thinking)" "{cps=35}(As long as this can help [mc] find himself and fulfill his sister's promise... I'll support him. Even if it means working with Literature.){/cps}"
    else:
        y "{cps=35}But make sure [mc] isn't lying.{/cps}"
        mc "{cps=35}Hey!{/cps}"
        sh "{cps=35}Relax, I can definitely make [mc] into an honest person.{/cps}"
    m "{cps=35}Alright, I'll hand this proposal over to you all. Make sure the event from this proposal can actually happen!{/cps}"
    "{cps=35}Maya handed the brown book to Fumi. The red light of the afternoon sun entered through the window, illuminating the book as if giving its blessing.{/cps}"
    "Literature Members" "{cps=35}Understood!{/cps}"
    "{cps=35}That afternoon, in the sacred Student Council room, a promise buried for twelve years finally began to pulse again.{/cps}"
    f "{cps=35}Alright, we'll head back to our room, [m]. See you!{/cps}"
    m "{cps=35}See you.{/cps}"
    "{cps=35}*click*{/cps}"
    "{cps=35}We walked toward our room.{/cps}"
    "{cps=35}Along the way, [sh] and [yk] were ahead of me as usual.{/cps}"
    "{cps=35}And Senior [f] stood beside me and started a conversation.{/cps}"
    f "{cps=35}Hunnngggh so sore...{/cps}"
    f "{cps=35}Sorry, [mc]. Your first day in the Literature Club ended up like this...{/cps}"
    mc "{cps=35}It's fine, Senior. Besides, it was my fault for joining late.{/cps}"
    f "{cps=35}But I'm curious — at registration only [sh] and [yk] actually signed up.{/cps}"
    f "{cps=35}So why did you suddenly want to join our club?{/cps}"
    f "{cps=35}As president I need to know each of my members' goals.{/cps}"
    mc "{cps=35}Ummnnn... how do I put this, Senior..{/cps}"
    mc "{cps=35}I'm pretty interested in this club's activities — writing stories, making poems and so on.{/cps}"
    mc "{cps=35}Plus the proposal we discussed earlier...{/cps}"
    "{cps=35}Senior [f] patted my shoulder.{/cps}"
    f "{cps=35}Don't worry! We can definitely run this project!{/cps}"
    f "{cps=35}For your sister's sake.{/cps}"
    mc "{cps=35}Yes, Senior. I'll do my best.{/cps}"

    f "{cps=35}That's the spirit! Oh right, since it's already afternoon, you three should just head home.{/cps}"
    f "{cps=35}I'll try reading this proposal at home first. So tomorrow we can start dissecting the contents together.{/cps}"
    sh "{cps=35}Understood, Senior [f]. See you tomorrow.{/cps}"
    yk "{cps=35}Daa-daa Senior [f]! Come on [mc], [sh]-nee, let's go to the gate together!{/cps}"
    "{cps=35}The three of us parted with Senior [f] in front of the club room. She hugged the brown book tightly, as if holding the key to all our futures.{/cps}"

    "{cps=35}Our footsteps echoed through the corridor that was growing quieter. The red light of the dying sun behind the school building left long shadows that seemed to dance on the wooden walls.{/cps}"

    "{cps=35}Today began with confusion, was colored by the warehouse incident, and ended with the weight of a twelve-year-old promise.{/cps}"

    "{cps=35}I touched my shoulder, where the blue Student Council armband had briefly been attached. I could still feel the lingering cold of that fabric there.{/cps}"

    yk "{cps=35}Hey, [mc]!{/cps}"

    mc "{cps=35}Hm?{/cps}"

    yk "{cps=35}Stop zoning out! If you get possessed by the old library spirit, I'm not taking responsibility!{/cps}"

    mc "{cps=35}I'm not zoning out. I'm just... thinking about a lot of things.{/cps}"

    yk "{cps=35}Hah... typical.{/cps}"

    "{cps=35}[yk] ran ahead of me. She spun around nimbly, then pulled [sh]'s hand — who'd been walking slowly beside me the whole time.{/cps}"

    yk "{cps=35}Big sis, don't just stay quiet either! Come on, say something to him!{/cps}"

    sh "{cps=35}Ah! What are you— {w=0.3} Yukie, let go!{/cps}"

    "{cps=35}Yukie gave Shoko a very clear wink signal. Shoko paused for a moment, her pale face flushing slightly under the evening light.{/cps}"

    sh "{cps=35}Ah... {w=0.5}true enough.{/cps}"

    "{cps=35}The two of them stopped right in front of the large school gate. The evening wind blew through their crimson hair, creating a scene that somehow felt so familiar... as if I'd seen it ten years ago.{/cps}"

    show shoko_smile at left
    show yukie_smile at right
    with dissolve

    "[sh] & [yk]" "{cps=35}Starting today, we look forward to working with you, [mc]!{/cps}"

    "{cps=35}Their voices united, clear, breaking the evening silence. I was stunned for a moment before finally nodding lightly.{/cps}"

    mc "{cps=35}Yeah. Looking forward to working with you too.{/cps}"

    scene black with fade
    stop music fadeout 3.0

    # THE ENDING IS DEFINITELY LIKE THIS
    "{cps=35}One thing was certain: Starting tomorrow, that missing melody would begin to be heard again.{/cps}"

    "{cps=35}And starting today... I swore I wouldn't let anyone 'disappear' again.{/cps}"

    jump chapter_2_end
