label chapter_2_sastra_kesempatan:
    scene bg_classroom_morning with fade
    play music "audio/bgm/schoolgate.mp3" fadein 2.0

    "{cps=35}I sat at my desk with mixed feelings. The usually noisy classroom felt far away in my ears.{/cps}"
    "{cps=35}In front of me, Yuuka was already sitting quietly. She didn't greet me, didn't even turn. She was only flipping through the pages of her book with rough movements.{/cps}"

    mc "{cps=40}[y]...{/cps}"
    
    y "{cps=40}...{/cps}"

    "{cps=35}Silence. She was really giving me the silent treatment because of my choice this morning.{/cps}"

    if jujur:
        "{cps=35}Even though I had already been honest about my older sister, she still seemed unable to accept why I chose Literature over the Student Council with her.{/cps}"
    else:
        "{cps=35}Especially since I hadn't told her the real reason. The one-meter distance between our desks felt like a kilometer.{/cps}"

    "{cps=35}Suddenly, a small shadow stood beside my desk.{/cps}"
    sh "{cps=35}Ikazaki...{/cps}"
    "{cps=35}[sh] looked at me with a slightly serious face.{/cps}"
    mc "{cps=35}Eh [sh], what's up?{/cps}"
    sh "{cps=35}N-nothing...{/cps}"
    "{cps=35}Strange...{/cps}"
    "{cps=35}It's unusual for her to approach me.{/cps}"
    "{i}In [sh]'s heart: \"Damn little sister... why do I have to do this just to follow her orders...\"{/i}"
    sh "{cps=35}Are you free this afternoon?{/cps}"
    mc "{cps=35}Umm... yeah, why?{/cps}"
    sh "{cps=35}I want to talk with you later. Is that okay?{/cps}"
    "{cps=35}[y] looked at me with a cynical expression.{/cps}"
    "{cps=35}Ugh...{/cps}"
    "{cps=35}Why did you have to come at such a bad time, [sh]...{/cps}"
    "{cps=35}[y] immediately turned her face away from me.{/cps}"
    "{cps=35}As if saying 'Not my business'.{/cps}"
    mc "{cps=35}Um... sure, [sh].{/cps}"
    sh "{cps=35}Phew... thank goodness..{/cps}"
    sh "{cps=35}I'll wait for you later.{/cps}"
    "{cps=35}[sh] went straight back to her seat.{/cps}"
    v "{cps=35}Oho... another one, huh.{/cps}"
    mc "{cps=35}What are you talking about, Vin.{/cps}"
    v "{cps=35}Ehehe...{/cps}"
    "{cps=35}The bell for class to start rang.{/cps}"
    sh "{cps=35}I wonder what we'll learn today...{/cps}"

    scene black with fade
    "{cps=35}Class began. But [sh]'s invitation kept echoing in my head. What exactly was going to happen?{/cps}"

    "{cps=40}While I was spacing out....{/cps}"
    "{cps=40}SLAM!{/cps}"
    mc"{cps=40}Wah! What the—{/cps}"
    "{cps=40}[t] threw a book onto my desk quite hard.{/cps}"
    t "{cps=40}Hah.... so this is how it is, [mc].{/cps}"
    t "{cps=40}Even if you're sleepy...{/cps}"
    t "{cps=40}{b}AT LEAST PAY ATTENTION!{/b}{/cps}"
    mc "{cps=50}Yes, Ma'am...{/cps}"
    "{cps=50}Damn... {w=0.1}why does this always happen...{/cps}"
    "{cps=50}I could hear [v] chuckling quietly behind me. She was definitely enjoying the show.{/cps}"

    t "{cps=40}Since you seem to have a world of your own inside that head, try solving the problem on the board.{/cps}"
    
    t "{cps=40}If 3x + 5 = 20, what is the value of x?{/cps}"

    "{cps=35}Ugh... my mind went completely blank. The numbers seemed to dance in front of my eyes.{/cps}"
    if jujur:
        "{cps=35}Yuuka looked panicked; she held up five fingers under the desk as a signal.{/cps}"
        "{cps=35}Then [sh]...{w=0.1} she also gave a signal with the number 5.{/cps}"
    else:
        "{cps=35}Yuuka looked completely normal and didn't give any signal at all.{/cps}"
        "{cps=35}But [sh]...{w=0.1} she gave a signal with the number 5.{/cps}"
    "{cps=40}What should I answer...{/cps}"
    menu:
        "5":
            $ correct_answer = True
            $ yuuka_rel += 5
            $ vina_rel += 5
            mc "{cps=40}The answer is... 5, Ma'am.{/cps}"
            
            "{cps=35}Miss Nanami paused for a moment, then lowered her glasses.{/cps}"
            
            t "{cps=40}Correct. Simple, isn't it?{/cps}"
            t "{cps=40}Remember, in Algebra, our goal is to find the 'Missing Value' (x) by balancing both sides.{/cps}"
            
            "{cps=35}Miss Nanami quickly wrote on the board.{/cps}"
            t "{cps=40}If you have a big problem (20) and a small disturbance (+5), remove the disturbance first (20-5). Then divide the remaining load (15) by your capacity (3).{/cps}"
            
            "{cps=35}For some reason, Miss Nanami's explanation just now didn't only sound like math—it sounded like a way of facing this messy life of mine.{/cps}"
            t "{cps=35}Understood?{/cps}"
            mc "{cps=35}Yes, Ma'am.{/cps}"
            t "{cps=40}Next time, pay attention to my explanations. Sit down and focus!{/cps}"
            t "{cps=35}Now return to your seat.{/cps}"
            mc "{cps=35}Y-yes, Ma'am.{/cps}"
            
            show yuuka_smile with dissolve
            if jujur:
                "{cps=35}Yuuka let out a sigh of relief and gave me a small smile. Behind me, Vina looked a little disappointed that she couldn't laugh at me.{/cps}"
            else:
                "{cps=35}Yuuka stayed quiet and gave no reaction, but [sh] looked a little calmer.{/cps}"
            v "{cps=60}Tsk... so the Rare Specimen can do math after all.{/cps}"

        "15":
            $ correct_answer = False
            $ yuuka_rel -= 2
            $ shoko_rel -= 2
            mc "{cps=40}The answer is... 15, Miss?{/cps}"
            
            "{cps=35}The entire class burst out laughing. Even Vina behind me had to cover her mouth so she wouldn't be too loud.{/cps}"
            t "{cps=40}Fifteen? Are you solving for x or calculating the price of fried snacks at the cafeteria? Wrong!{/cps}"
            t "{cps=40}Stand at the front until my class is over!{/cps}"
            
            if jujur:
                "{cps=35}Yuuka facepalmed as if she couldn't believe I still got it wrong. Behind me, Vina chuckled at my answer.{/cps}"
            else:
                "{cps=35}Yuuka stayed quiet and gave no reaction, but [sh] looked a little disappointed.{/cps}"
        "3":
            $ correct_answer = False
            $ yuuka_rel -= 2
            $ shoko_rel -= 2
            mc "{cps=40}The answer is... 3?{/cps}"
            
            t "{cps=40}Wrong! Apparently your daydreaming really did destroy your logical ability.{/cps}"
            t "{cps=40}Please stand beside the blackboard until I finish explaining.{/cps}"
            
            "{cps=35}I could only hang my head while several other girls whispered and laughed at me.{/cps}"

    "{cps=50}Class continued as usual.{/cps}"
    if correct_answer:
        "{cps=35}Thank goodness my answer was correct earlier...{/cps}"
    else:
        "{cps=35}If only my answer had been correct... maybe my legs wouldn't be this sore from standing in front of the class.{/cps}"
    
    "{cps=40}And before I knew it, it was already break time.{/cps}"
    
    play sound "audio/sfx/school bell.mp3"
    t "{cps=40}Alright, since it's this time already, you may take a break.{/cps}"
    t "{cps=40}We'll meet again in the afternoon session.{/cps}"
    
    "The Class" "{cps=40}Yes, Ma'am!{/cps}"
    "{cps=40}[t] left the classroom right away.{/cps}"

    mc "{cps=40}Hah.... finally.{/cps}"
    
    if correct_answer == False:
        "{cps=40}[v] and [y] came straight over to me.{/cps}"
        "{cps=40}It seemed they wanted to give me some kind of 'lecture'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Dummy.{/cps}"
        mc "{cps=40}Hey!{/cps}"
        v "{cps=40}Come on, I'm just kidding. But seriously, your face earlier was hilarious.{/cps}"
        mc "{cps=40}What the...{/cps}"
        v "{cps=40}But how are your legs? {w=0.1} Still okay?{/cps}"
        mc "{cps=40}They're so fine I don't even feel like walking.{/cps}"
        v "{cps=40}Ahaha, just as I thought.{/cps}"
        v "{cps=35}But... how did you get it wrong?{/cps}"
        mc "{cps=35}I don't know... I have a lot on my mind.{/cps}"
        v "{cps=35}I feel like you weren't doing anything special...{/cps}"
        v "{cps=35}You think so too, right [y]?{/cps}"
        y "{cps=35}Ummm... yeah...{/cps}"
        if jujur:
            y "{cps=40}I already gave you the signal, [mc]. Why were you spacing out?{/cps}"
            mc "{cps=40}Sorry... my head went blank when I saw those numbers.{/cps}"
            y "{cps=40}That's just like you.{/cps}"
            v "{cps=40}Huh, what signal?{/cps}"
            y "{cps=40}It's nothing.{/cps}"
            "{cps=40}[y] walked away from me right away.{/cps}"
            v "{cps=40}Huh? Why'd she leave?{/cps}"
            v "{cps=40}[y].....{/cps}"
            "{cps=40}[v] immediately chased after [y].{/cps}"
            "{cps=40}Leaving me alone.{/cps}"
        else:
            y "{cps=40}That's why you should pay attention in class. Don't just space out on your own.{/cps}"
            v "{cps=35}Hey... what's wrong with her?{/cps}"
            y "{cps=40}I don't know. If you want to know, ask [mc] yourself.{/cps}"
            "{cps=40}[y] left us without another word.{/cps}"
            v "{cps=40}Looks like there's some drama going on...{/cps}"
            v "{cps=40}What did you do to her?{/cps}"
            mc "{cps=40}It's not like that.{/cps}"
            v "{cps=40}Hah...{w=0.1} [y]!{/cps}"
            "{cps=40}[v] immediately chased after [y].{/cps}"
            "{cps=40}Leaving me alone.{/cps}"
    else:
        "{cps=40}[v] and [y] came straight over to me.{/cps}"
        "{cps=40}It seemed they wanted to give me some kind of 'lecture'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Smart one.{/cps}"
        mc "{cps=40}Hey!{/cps}"
        v "{cps=40}Come on, I'm just kidding. But seriously, you did okay when you went up front.{/cps}"
        mc "{cps=40}What the...{/cps}"
        v "{cps=35}Tell me how you managed to answer...{/cps}"
        "{cps=35}[y] stuck close beside me.{/cps}"
        mc "{cps=35}I don't know...{/cps}"
        "{cps=35}I looked around while turning my face away from [v]...{/cps}"
        if jujur:
            "{cps=35}[y] looked a little annoyed.{/cps}"
            y "{cps=40}Hah... you two...{/cps}"
            y "{cps=35}[v], let's go to the cafeteria.{/cps}"
            v "{cps=40}Let's go! [mc], you coming?{/cps}"
            mc "{cps=40}Not this time, still full.{/cps}"
            v "{cps=40}Hmm... you sure?{/cps}"
            v "{cps=40}Alright then, see you later.{/cps}"
            "{cps=40}[y] and [v] left, leaving me alone.{/cps}"
        else:
            "{cps=35}[y] looked like she wanted to avoid me. I didn't know what was going on with her.{/cps}"
            v "{cps=35}Hey... what's wrong with her?{/cps}"
            y "{cps=40}I don't know. If you want to know, ask [mc] yourself.{/cps}"
            "{cps=40}[y] left us without another word.{/cps}"
            v "{cps=40}Looks like there's some drama going on...{/cps}"
            v "{cps=40}What did you do to her?{/cps}"
            mc "{cps=40}It's not like that.{/cps}"
            v "{cps=40}Hah...{w=0.1} [y]!{/cps}"
            "{cps=40}[v] immediately chased after [y].{/cps}"
            "{cps=40}Leaving me alone.{/cps}"


    sh "{cps=35}As usual, always noisy around you, [mc].{/cps}"
    "{cps=35}Shoko was suddenly already near me. Her calm voice contrasted with Yuuka and Vina's earlier chaos.{/cps}"
    mc "{cps=35}Yeah, that's how it is...{/cps}"
    sh "{cps=35}You're not going to the cafeteria with them?{/cps}"
    mc "{cps=35}Not for now.{/cps}"
    "{cps=35}(Because I don't have money on me.){/cps}"
    sh "{cps=35}Then the timing is perfect...{/cps}"
    mc "{cps=35}Timing? What do you mea—{/cps}"
    "{cps=35}Without warning, Shoko grabbed my hand. Her grip was small but very strong, forcing me to stand and follow her out of the classroom.{/cps}"
    mc "{cps=35}H-hey! Where are you taking me?{/cps}"
    sh "{cps=35}Just follow me.{/cps}"
    "{cps=35}She pulled me along.{/cps}"
    "{cps=35}I didn't know where we were going.{/cps}"
    "{cps=35}I could only resign myself to being pulled down the corridor. Shoko's back looked very straight, as if she had planned this from earlier.{/cps}"
    "{cps=35}Hopefully not somewhere strange...{/cps}"
    "{cps=35}And we stopped in front of a familiar room.{/cps}"
    "{cps=35}The smell from the room... and the surroundings...{/cps}"
    "{cps=35}It felt as if I had been here before...{/cps}"
    sh "{cps=35}Go in, [mc].{/cps}"
    mc "{cps=35}*Gulp...* Alright.{/cps}"
    "{cps=35}I gathered the courage to open the door of this room.{/cps}"
    "{cps=35}And after I opened it...{/cps}"
    "{cps=35}I saw books neatly arranged on the shelves.{/cps}"
    "{cps=35}And a girl reading a book.{/cps}"
    "{cps=35}From her crimson hair... {w=0.1} she looked like [sh]'s twin who was late yesterday—only the hairstyle was different...{/cps}"
    yk "{cps=35}Hmn?{/cps}"
    yk "{cps=35}Big sis... Why did it take you so long to bring him here?{/cps}"
    sh "{cps=35}It's not my habit, [yk].{/cps}"
    sh "{cps=35}You could have brought him here yourself.{/cps}"
    yk "{cps=35}Hmm, but it suits big sis better to bring him.{/cps}"
    sh "{cps=35}Hah...{/cps}"
    "{cps=35}[sh] immediately took a book from the shelf and started reading.{/cps}"
    "{cps=35}Without explaining why I was here.{/cps}"
    mc "{cps=35}Um...{/cps}"
    yk "{cps=35}Ah right! Welcome to the Literature Club, [mc].{/cps}"
    yk "{cps=35}I don't think we need introductions since the three of us are in the same class.{/cps}"
    yk "{cps=35}So.... well, I hope you'll be comfortable here.{/cps}"
    "{cps=35}Yukie's warm smile made my nervousness ease a little. She felt much friendlier than her sister.{/cps}"
    mc "{cps=35}Thank you, Yukie. But... how did you know I would join here?{/cps}"
    yk "{cps=35}Ummm... why indeed...{/cps}"
    yk "{cps=35}Big sis knows, right?{/cps}"
    sh "{cps=35}I heard it from Senior Maya.{/cps}"
    "{cps=35}Her again...{/cps}"
    mc "{cps=35}So... what am I supposed to do now?{/cps}"
    sh "{cps=35}For now, just treat this room as your home.{/cps}"
    "{cps=35}[sh] answered while continuing to read.{/cps}"
    yk "{cps=35}Good grief... Big sis, you should tone down that cold attitude of yours.{/cps}"
    sh "{cps=35}What?{/cps}"
    "{cps=35}Shoko closed her book slowly, then looked at me with an expression that was hard to read.{/cps}"
    yk "{cps=40}Hey [mc], do you know why Maya was so insistent that you join an organization?{/cps}"
    mc "{cps=40}She said it was for 'contribution'. But I feel like there's another reason.{/cps}"
    yk "{cps=35}True. Because by joining an organization...{/cps}"
    yk "{cps=35}You can improve a lot of {i}soft skills{/i}.{/cps}"
    yk "{cps=35}Like public speaking, networking, and so on.{/cps}"
    mc "{cps=35}Yeah... something like that.{/cps}"
    yk "{cps=35}So, I want to ask you, [mc]. Why did you choose Literature over the Student Council or another organization?{/cps}"
    mc "{cps=35}Ummmnn....{/cps}"
    "{cps=35}How do I tell them...{/cps}"
    "{cps=35}That my real goal is to recover the memories I've lost...{/cps}"
    "{cps=35}I'll just answer like this.{/cps}"
    mc "{cps=35}I was just interested in Literature. Nothing else.{/cps}"
    yk "{cps=35}Hmm... suspicious...{/cps}"
    yk "{cps=35}You think the same, right, big sis?{/cps}"
    "{cps=35}Looks like [yk] can't be fooled.{/cps}"
    "{cps=35}What should I do...{/cps}"
    sh "{cps=35}I don't really care, [yk].{/cps}"
    yk "{cps=35}Haaah.... boring.{/cps}"
    sh "{cps=35}As long as you're by my side... that's enough, [mc].{/cps}"
    yk "{cps=35}Yeah... after all, the goal was for us to be together again, right, big sis?{/cps}"
    yk "{cps=35}Like ten years ago.{/cps}"
    sh "{cps=35}Hmm!{/cps}"
    "{cps=35}What exactly happened ten years ago?{/cps}"
    mc "{cps=35}Wait... I still can't process everything that's happening so fast...{/cps}"
    mc "{cps=35}Did the three of us used to play together ten years ago?{/cps}"
    "{cps=35}The atmosphere suddenly became very heavy. Yukie's smile disappeared, replaced by a deep sad look.{/cps}"
    "{cps=35}In the corner of the room, Shoko froze. Her hands trembled hard as she held her chest, as if there was an unbearable tightness there.{/cps}"
    sh "{cps=35}You... {w=0.5}really forgot?{/cps}"
    mc "{cps=35}I'm sorry, Shoko... I really—{/cps}"
    sh "{cps=35}[yk]... I'm going outside for a bit.{/cps}"
    yk "{cps=35}Eh? Nee-sa—{/cps}"
    "{cps=35}*SLAM*{/cps}"
    "{cps=35}Shoko ran out of the room as fast as lightning. The door slammed hard, leaving a stifling silence between me and Yukie.{/cps}"
    "{cps=35}From the corridor, a faint small sob could be heard...{/cps}"
    "{cps=35}For some reason I felt so guilty...{/cps}"
    yk "{cps=35}Hah... I already expected it would be like this.{/cps}"
    yk "{cps=35}She's always like this.{/cps}"
    yk "{cps=35}Even the last time before we were separated...{/cps}"
    mc "{cps=35}What happened, Yukie? Why is she like this? What happened ten years ago?{/cps}"
    yk "{cps=35}I can't explain it to you now, [mc]. That is a wound only Shoko can tell.{/cps}"
    yk "{cps=35}Hurry and go after her! She hasn't gone far. Don't leave her alone in that condition.{/cps}"
    menu:
        "Go after Shoko now":
            $ shoko_rel += 10
            "{cps=35}I had no other choice. I had to take responsibility for the pain I had accidentally caused.{/cps}"

        "Ask Yukie more first":
            $ shoko_rel -= 5
            mc "{cps=35}But I need answers, Yukie!{/cps}"
            yk "{cps=35}Are you a man or not!?{/cps}"
            yk "{cps=35}Answers are useless if the person is already broken! Go after her, [mc]!{/cps}"

    "{cps=35}I immediately tried to find [sh]...{w=0.1} but...{w=0.1} where was she?{/cps}"
    "{cps=35}I didn't know the exact location...{/cps}"
    mc "{cps=35}Where are you... [sh]{/cps}"
    "{cps=35}Time kept moving closer to the bell.{/cps}"
    "{cps=35}I kept searching for [sh].{/cps}"
    "{cps=35}Until I was in front of the classroom.{/cps}"
    "{cps=35}And came face to face with [y] and [v].{/cps}"
    v "{cps=35}Huh, [mc]? Why are you panicking like that? Like you just got chased by a ghost.{/cps}"
    mc "{cps=35}You two... did you see [sh] pass by here?{/cps}"
    v "{cps=35}[sh]? You mean the red-haired girl?{/cps}"
    v "{cps=35}I didn't see her... what about you, [y]?{/cps}"
    if jujur:
        "{cps=35}Yuuka looked at me for a moment. Even though there was a slight spark of jealousy, her worry was much greater.{/cps}"
        y "{cps=35}If I'm not wrong, I saw a red-haired girl running toward the attic. Her face was covered by her hands; it looked like she was crying...{/cps}"
        mc "{cps=35}The attic? What would she do there?{/cps}"
        y "{cps=35}Why are you asking me?{/cps}"
        mc "{cps=35}You're a Student Council member.{/cps}"
        y "{cps=35}Not every Student Council member knows everything!{/cps}"
        v "{cps=35}Alright, alright, you should just go to the attic, [mc]. I'm worried something bad might happen...{/cps}"
        mc "{cps=35}Alright then... thank you [y], [v]!{/cps}"
        y "{cps=35}Be careful, [mc]...{/cps}"
    else:
        "{cps=35}Yuuka crossed her arms, looking at me with a very cold expression.{/cps}"
        y "{cps=35}I don't know. And even if I did, why should I tell you?{/cps}"
        v "{cps=35}Yuuka...{/cps}"
        y "{cps=35}You chose Literature. Go deal with your Literature Club problems yourself.{/cps}"
        "{cps=35}Her words hurt, but I had no time to argue.{/cps}"
        v "{cps=35}I think I saw someone run toward the stairs to the attic earlier...{/cps}"
        mc "{cps=35}Thanks, Vin.{/cps}"

    scene black with fade
    "{cps=35}I ran up the stairs to the attic. My breathing grew heavy, and my heart pounded hard—not only from running, but from guilt.{/cps}"
    "{cps=35}There, under the dim light from a cracked window, Shoko was sitting hugging her knees. The small gold bell on her red choker trembled with her soft sobs.{/cps}"

    mc "{cps=35}[sh]...{/cps}"
    sh "{cps=35}...Don't look at me.{/cps}"
    mc "{cps=35}I'm sorry. I didn't mean to hurt you.{/cps}"
    sh "{cps=35}Ten years... and you really forgot everything...{/cps}"
    "{cps=35}I sat down a short distance from her. I didn't force her to talk. I just stayed there until her breathing gradually calmed down.{/cps}"
    sh "{cps=35}...Thank you for coming after me.{/cps}"
    mc "{cps=35}Anytime.{/cps}"
    "{cps=35}For the first time that day, Shoko gave me a very thin smile—fragile, but real.{/cps}"

    scene black with fade
    stop music fadeout 3.0

    "{cps=35}Among the embarrassment in the classroom, the secret of the Kirishima family, and the heavy dream of [mi]-nee...{/cps}"
    "{cps=35}One thing was certain: Starting tomorrow, that lost melody would begin to be heard again.{/cps}"
    "{cps=35}And starting today... I swore I would not let anyone 'disappear' again.{/cps}"

    # === SHARED FLAGS FOR CHAPTER 3 (aligned with main sastra route) ===
    $ masuk_club = True
    $ club_choice = "sastra"
    $ kitaimirai_known = True
    $ chapter2_route = "sastra"
    $ sayoko_known = True
    $ megumi_archive_found = True

    jump chapter_2_end
