label chapter_2_osis_kesempatan:
    scene bg_classroom with fade
    play music "audio/bgm/schoolgate.mp3" fadein 2.0

    "{cps=35}I stepped into the classroom still slightly out of breath. The morning classroom was noisy as usual—typical of a class left unsupervised by a teacher.{/cps}"

    "{cps=35}I saw Yuuka already at her desk. She was surrounded by a few other girls, but her eyes occasionally glanced toward the door.{/cps}"

    if jujur == False:
        "{cps=35}When our eyes met, Yuuka immediately looked away and pretended to laugh at whatever her neighbor was saying.{/cps}"
        "{cps=35}My heart sank. Today was going to be a very long day.{/cps}"
    else:
        "{cps=35}Yuuka gave me a small wave, though her smile wasn't as wide as usual. At least she was still willing to look at me.{/cps}"

    "{cps=35}I walked toward my desk. But before I could sit down, someone tapped my shoulder from behind.{/cps}"

    "{cps=50}And just as I expected...{/cps}"

    "{cps=40}[v] appeared behind me with a slightly suspicious look on her face.{/cps}"

    show vina_smile with dissolve
    v "{cps=60}Ara, ara... [mc]. Your face looks like someone who just barely escaped a death sentence.{/cps}"

    mc "{cps=40}[v], you always show up out of nowhere...{/cps}"

    v "{cps=60}Fufufu. I'm just curious. Yesterday Senior [m] took you away with that terrifying aura of hers.{/cps}"
    v "{cps=60}So... {w=0.1}how did it go?{/cps}"
    v "{cps=60}Did she throw you into the back warehouse, or did you manage to 'negotiate' with her?{/cps}"
    
    "{cps=35}Vina rested her chin on her folded hands on the back of my chair. Her sharp eyes seemed to be scanning every inch of my reaction.{/cps}"
    
    mc "{cps=40}Negotiate? What do you mean? She's the President, not a market vendor.{/cps}"
    
    v "{cps=60}Fufufu. In this school, Senior Maya IS the law. And the law always has a price.{/cps}"
    
    v "{cps=60}Come on, be honest, Specimen. She definitely mentioned the name 'Ikazaki [mi]', right? Your face goes pale every time that name comes up.{/cps}"
    
    "{cps=35}I was startled. How did Vina know? Yesterday's conversation was supposed to be completely private.{/cps}"
    
    mc "{cps=40}Were you... eavesdropping?{/cps}"
    
    v "{cps=60}Well... let's just say I have 'ears' everywhere. So, what's your choice?{/cps}"
    mc "{cps=40}I... {w=0.1}chose the Student Council.{/cps}"
    mc "{cps=40}I just handed the form to Senior [m] at the gate earlier.{/cps}"

    v "{cps=60}Ehh?! You're serious?{/cps}"
    if jujur == False:
        "{cps=35}Yuuka, who overheard this conversation, looked shocked—as if she couldn't believe I had actually chosen the Student Council.{/cps}"
    
    "{cps=35}Vina's eyes widened slightly, then her laughter burst out.{/cps}"
    
    v "{cps=60}Hahaha! I didn't expect you to give in that quickly.{/cps}"
    v "{cps=60}But... {w=0.1}a smart choice for a guy who wants to 'survive' in this school.{/cps}"
    mc "{cps=40}Hey! I didn't gi—{/cps}"
    y "{cps=60}He didn't give in, [v].{/cps}"
    y "{cps=60}[mc] just... realized he has potential.{/cps}"

    v "{cps=60}Oh? Is that so, [y]-san?{/cps}"
    v "{cps=60}Or maybe he just couldn't stand watching you keep frowning all the time?{/cps}"

    y "{cps=60}W-what?! That's not it!{/cps}"

    "{cps=35}Yuuka turned away with a flushed face, while Vina looked back at me with a more serious smile.{/cps}"

    v "{cps=60}Well, whatever the reason, welcome aboard this stormy ship, [mc].{/cps}"
    v "{cps=60}As a Student Council member, I have only one piece of advice.{/cps}"
    v "{cps=60}Prepare yourself for this afternoon. Senior Maya never gives a sweet 'welcome'.{/cps}"

    mc "{cps=40}I already felt it earlier...{w=0.1} She even ordered me to come to her office right after the final bell.{/cps}"

    v "{cps=60}Fufufu. That's only the beginning. Come on, sit down. The teacher will be here soon.{/cps}"

    scene black with fade
    "{cps=35}Class began. But Vina's warning kept echoing in my head. What exactly had Senior Maya prepared for me in the Student Council room later?{/cps}"

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
        "{cps=35}Yuuka in front of me looked panicked. She held up five fingers under the desk as a signal.{/cps}"
    else:
        "{cps=35}Yuuka in front of me looked completely normal. She didn't give me any signal at all.{/cps}"
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
            v "{cps=60}Tsk... so the Rare Specimen can do math after all.{/cps}"

        "15":
            $ correct_answer = False
            $ yuuka_rel -= 2
            mc "{cps=40}The answer is... 15, Miss?{/cps}"
            
            "{cps=35}The entire class burst out laughing. Even Vina behind me had to cover her mouth so she wouldn't be too loud.{/cps}"
            t "{cps=40}Fifteen? Are you solving for x or calculating the price of fried snacks at the cafeteria? Wrong!{/cps}"
            t "{cps=40}Stand at the front until my class is over!{/cps}"
            
            show yuuka_sad with dissolve
            "{cps=35}Yuuka facepalmed. She had given me the signal, but I completely misread it.{/cps}"

        "3":
            $ correct_answer = False
            $ yuuka_rel -= 2
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
        "{cps=40}.....{/cps}"
            
    else:
        "{cps=40}[v] and [y] came straight over to me.{/cps}"
        "{cps=40}It seemed they wanted to give me some kind of 'lecture'.{/cps}"
        
        show yuuka_determined at left
        show vina_smile at right
        with dissolve

        v "{cps=40}Yo! {w=0.1}Smart kid.{/cps}"
        mc "{cps=40}I just got lucky earlier.{/cps}"
        v "{cps=40}Too bad there was no drama...{/cps}"
        v "{cps=40}I really wanted to see you get punished.{/cps}"
        mc "{cps=40}Hey! Your intentions are terrible.{/cps}"
        if jujur:
            y "{cps=40}Thank goodness you could answer it, [mc]. I was panicking earlier.{/cps}"
            y "{cps=40}Next time don't space out again, okay?{/cps}"
            mc "{cps=40}Yeah, sorry...{/cps}"
        else:
            y "{cps=40}So you can solve it on your own after all. Good.{/cps}"
        v "{cps=40}Well, whatever. At least today is safe, right?{/cps}"
        mc "{cps=40}Safe, I guess...{/cps}"
        v "{cps=40}Want to go to the cafeteria?{/cps}"
        if jajan == True:
            mc "{cps=40}No thanks, I'm still full.{/cps}"
            "{cps=40}(Mostly because I don't want to spend money...){/cps}"
        else:
            mc "{cps=40}I don't think so, Vin. I'm still full.{/cps}"
        
        v "{cps=40}Hah... fine then.{/cps}"

        if jujur:
            v "{cps=40}Come on Ka, let's go to the cafeteria!{/cps}"
            y "{cps=40}Alright.{/cps}"
        else:
            v "{cps=40}Come on Yu— Huh? Where'd that girl go?{/cps}"
            v "{cps=40}[mc], you saw her, right?{/cps}"
            mc "{cps=40}Didn't she already leave ahead?{/cps}"
            v "{cps=40}Eh!? [y], wait a second...{/cps}"

        "{cps=40}They left, leaving me alone.{/cps}"
        "{cps=40}...{/cps}"
    "{cps=40}This quiet atmosphere...{/cps}"
    "{cps=40}When was the last time I felt something like this...{/cps}"

    
    play sound "audio/sfx/walk.mp3"
    yk "{cps=60}He-ey! [mc]! Why does your face look like you're thinking about the end of the world?{/cps}"

    show yukie_smile with dissolve
    "{cps=35}Yukie stood in front of me. Unlike the serious [y] or the mischievous [v], [yk] always carried a... light aura.{/cps}"

    mc "{cps=40}Oh, [yk]. You're not going to the cafeteria with the others?{/cps}"

    yk "{cps=60}I already ate the lunch I brought. Besides, I couldn't bear to leave that 'Beautiful Statue' alone in the corner.{/cps}"

    "{cps=35}Yukie glanced toward Shoko, who was still sitting quietly staring out the window.{/cps}"

    yk "{cps=60}Oh right, [mc]. Since you're now a 'dutiful' Student Council member, can I ask a favor?{/cps}"
    yk "{cps=60}I have to go to the teachers' room for a bit. Could you give this boxed milk to big sis? She hasn't had a drink since this morning.{/cps}"

    mc "{cps=40}Why not just leave it on her desk?{/cps}"

    yk "{cps=60}Fufufu. When [sh] spaces out, she won't notice the world around her unless someone talks to her.{/cps}"
    yk "{cps=60}Please, 'Rare Specimen'!{/cps}"

    hide yukie with dissolve
    "{cps=35}Yukie ran out of the classroom before I could refuse. Now, in this nearly empty classroom, it was just me and her.{/cps}"

    "{cps=35}I stood beside Shoko's desk. She truly wasn't moving. Only her eyes seemed to follow the dust particles floating in the sunlight.{/cps}"

    mc "{cps=40}Shirohana-san...{/cps}"

    "{cps=35}The gold bell on her red choker chimed softly as she tilted her head slightly. She didn't fully turn; she only glanced at me from the corner of her clear eyes.{/cps}"

    sh "{cps=50}...Hesitant footsteps. Did you bring something for me, Ikazaki?{/cps}"

    mc "{cps=40}Yukie asked me to give you this. She said you haven't had a drink since morning.{/cps}"

    "{cps=35}I placed the boxed milk on her desk. Shoko was quiet for a moment, then her pale fingers touched the cold box.{/cps}"
    if correct_answer == True:
        sh "{cps=50}Thank you. And... congratulations on your success earlier.{/cps}"

        mc "{cps=40}You mean the math problem? Ah, that was just luck.{/cps}"

        sh "{cps=50}Not the numbers... but your courage in searching for 'balance' in front of the class earlier.{/cps}"
        sh "{cps=50}Most people only see the variable 'x' as a burden. But you... you looked at it as if you were searching for something missing from yourself.{/cps}"

    else:
        sh "{cps=50}Thank you. And... congratulations on your failure earlier.{/cps}"

        mc "{cps=40}So you were watching?{/cps}"

        sh "{cps=50}Not about right or wrong... but your courage in searching for an 'answer' in front of the class earlier.{/cps}"
        sh "{cps=50}Most people only see your mistakes. But you... you responded as if you were searching for something missing from yourself.{/cps}"

    "{cps=35}Her words left me stunned. It felt like she had just read my mind.{/cps}"

    mc "{cps=40}Maybe you're right...{/cps}"
    "{cps=40}I think I should tell her.{/cps}"
    mc "{cps=40}Oh right, [sh], I chose the Student Council.{/cps}"
    "{cps=40}[sh] went quiet, and her reaction made it seem like something important was starting to slip away.{/cps}"
    sh "{cps=40}Oh....{/cps}"
    sh "{cps=40}Congratulations.{/cps}"
    mc "{cps=40}It looks like you feel like something is missing. What is it?{/cps}"
    sh "{cps=40}Nothing...{/cps}"
    "{cps=40}It seemed [sh] was starting to pull away from me a little...{/cps}"
    mc "{cps=40}What do you think of the Student Council?{/cps}"

    sh "{cps=50}The Student Council... a very noisy place. Lots of voices, but few that actually speak.{/cps}"
    sh "{cps=50}But I understand. For someone who carries the name 'Ikazaki', maybe noise is a way to forget the past, isn't it?{/cps}"

    mc "{cps=40}What do you mean? Do you... know something about my family?{/cps}"

    "{cps=35}Shoko finally turned fully. Her gaze was deep, as if she were looking beyond time.{/cps}"

    sh "{cps=50}Ten years is a long time for a memory, but too short for a promise that hasn't been fulfilled...{/cps}"

    "{cps=35}The air around us suddenly felt cold. My heart pounded hard.{/cps}"
    mc "{cps=40}What do you mean by te—{/cps}"

    play sound "audio/sfx/door.mp3"
    g1 "{cps=40}[mc]! {w=0.1} Is [mc] here?!{/cps}"

    "{cps=35}The sound of the door being slid open roughly shattered the silence between us.{/cps}"

    mc "{cps=40}W-what's wrong?{/cps}"

    g1 "{cps=40}Phew, glad I found you! Get to the corridor in front of the Student Council room right now! Senior Maya is looking for you. She looks... very impatient.{/cps}"

    mc "{cps=40}Now? But it's still break time?{/cps}"

    g1 "{cps=40}As if I'd dare ask her why! Just hurry before she gets even angrier!{/cps}"

    "{cps=35}I let out a long sigh. I turned back toward Shoko, but she was already staring out the window again, as if our conversation had never happened.{/cps}"

    sh "{cps=50}Go... the 'President' doesn't like waiting for uncertain variables.{/cps}"

    mc "{cps=40}I... I'll go first, Shirohana-san.{/cps}"

    scene black with fade
    stop music fadeout 1.5

    "{cps=35}I stepped out of the classroom with a heavy feeling. The secret about the ten-year promise was once again covered by the shadow of [m]'s orders.{/cps}"

    scene bg_school_corridor with fade
    play music "audio/bgm/emptyroom.mp3" fadein 2.0

    "{cps=35}I walked down the main building corridor. The noise from the cafeteria was faint in the distance, but the corridor in front of the Student Council room felt so quiet and cold.{/cps}"

    "{cps=35}Maya stood there, leaning her back against the large window. She was looking at her watch with a flat expression that was hard to read.{/cps}"

    show maya_stern with dissolve
    m "{cps=40}Three minutes and twenty seconds. You're slower than I expected, Ikazaki [mc].{/cps}"

    mc "{cps=40}Sorry, Senior. There was a little... matter in class earlier.{/cps}"

    m "{cps=40}A matter with the Shirohana sisters?{/cps}"

    "{cps=35}Thump. How did she know? Does the Student Council really have 'eyes' in every corner of this school?{/cps}"

    m "{cps=40}Don't make that surprised face. As President, I need to know where every one of my 'assets' is.{/cps}"

    mc "{cps=40}Asset? So I'm just an asset to you now?{/cps}"

    m "{cps=40}That depends on how you prove yourself this afternoon. But for now...{/cps}"

    "{cps=35}Maya reached into her blazer pocket and pulled out a blue armband. The official Student Council armband of this school.{/cps}"

    m "{cps=40}Put this on. I don't want any 'illegal' members wandering around my office this afternoon.{/cps}"

    if correct_answer == True:
        "{cps=40}Ugh! My arms are still a bit sore...{/cps}"
    else:
        "{cps=40}Should I mess with Senior Maya a little...{/cps}"
    
    "{cps=40}What should I do?{/cps}"
    
    menu:
        "Put it on myself":
            $ pasang = False
            $ maya_rel += 2
            "{cps=35}I took the armband from her hand. It felt cold and heavy.{/cps}"
            mc "{cps=40}Thank you. I'll come this afternoon.{/cps}"
            m "{cps=40}Good. Don't make that armband look embarrassing on your uniform.{/cps}"

        "Ask her to put it on":
            $ maya_rel += 5
            $ yuuka_rel -= 3
            $ pasang = True
            mc "{cps=40}My hands are still shaking from standing as punishment earlier. Could you put it on for me, Senior?{/cps}"
            m "{cps=40}Hah?{/cps}"
            "{cps=35}Maya raised an eyebrow slightly. For a moment, her flat mask cracked with surprise.{/cps}"
            m "{cps=40}You... really do have interesting guts.{/cps}"
            "{cps=35}She stepped closer. The cold atmosphere shifted to a sharp yet calming perfume. Her skillful fingers fastened the armband onto my uniform shoulder.{/cps}"
            m "{cps=40}Done. Now go eat. I don't need members who faint during coordination meetings.{/cps}"
            mc "{cps=35}Yes, Senior.{/cps}"
            

    hide maya with dissolve
    "{cps=35}Maya turned and entered her office without waiting for my reply.{/cps}"

    "{cps=35}I touched the armband on my shoulder. It felt like a shackle, yet at the same time a strange sense of pride began to rise.{/cps}"
    
    stop music fadeout 3.0
    pause 1.0

    "{cps=35}As I was about to turn back toward the classroom, I caught a silhouette at the end of the corridor bend.{/cps}"
    
    "{cps=35}Just a flash. The shadow disappeared before I could confirm who it was.{/cps}"
    if pasang:
        if jujur:
            unknown "{cps=40}...Why... does it have to be that uniform?{/cps}"
            "{cps=35}The voice was almost like a whisper of wind. So soft, yet full of disbelief.{/cps}"
            "{cps=35}There were hurried footsteps moving away. Like someone trying to hold their breath so they wouldn't cry.{/cps}"
            
            $ yuuka_rel -= 1
        else:
            unknown "{cps=40}Liar...{/cps}"
            "{cps=35}A single short word that cut through the cold air of the corridor.{/cps}"
            "{cps=35}I heard something fall—maybe a keychain or some other small object—before the footsteps ran away heavily.{/cps}"
            "{cps=35}A vibration of sadness was left behind, as if a trust that had been built for so long had just cracked.{/cps}"
            
            $ yuuka_rel -= 5

    else:
        if jujur:
            unknown "{cps=40}Congratulations...{/cps}"
            "{cps=40}The voice was almost like a whisper of wind. So soft, yet full of a happy tone.{/cps}"
            "{cps=40}There were hurried footsteps moving away.{/cps}"
            "{cps=40}But with a feeling of joy.{/cps}"
            $ yuuka_rel += 2
        else:
            unknown "{cps=40}I didn't think this was real...{/cps}"
            unknown "{cps=40}But why didn't you tell me from the start...{/cps}"
            unknown "{cps=40}Liar.{/cps}"
            "{cps=40}The voice was almost like a whisper of wind. So soft, yet with a tone that seemed to be losing trust.{/cps}"
            $ yuuka_rel -= 2

    mc "{cps=40}Who's there?{/cps}"

    "{cps=35}No answer. Only the echo of my own footsteps bouncing off the walls of the main building.{/cps}"
    "{cps=35}Suddenly, the pride of wearing this armband evaporated, replaced by a tightness I couldn't explain.{/cps}"

    "{cps=40}And while I was thinking...{/cps}"
    "{cps=40}*Ding dong ding dong~*{/cps}"
    "{cps=40}Break time was over.{/cps}"
    "{cps=40}As if time had moved too fast.{/cps}"
    mc "{cps=40}Damn, it's already time.{/cps}"

    scene bg_classroom with fade
    play music "audio/bgm/evewalk.mp3" fadein 2.0

    "{cps=35}I stepped into the classroom. The afternoon air felt very stuffy, made worse by the awkward atmosphere surrounding my desk and [y]'s desk.{/cps}"

    "{cps=35}I had just sat down when the classroom door opened again. And sure enough...{/cps}"

    show teacher_t_serious with dissolve
    
    "{cps=35}The same figure who had punished me in front of the class this morning appeared again. In this school, [t] was known as an all-rounder teacher with a packed schedule.{/cps}"

    t "{cps=40}Put your gadgets away. Even though this is the afternoon slot when people tend to get sleepy, today's material is much heavier than this morning's math.{/cps}"

    t "{cps=40}Open your History books. We will be discussing 'Tragedy and Betrayal' in the history of organizational movements.{/cps}"

    "{cps=35}I flinched. Why did this afternoon's material feel like it was mocking my current situation?{/cps}"

    t "{cps=40}In history, many great figures fell not because of enemies from outside, but because of broken 'Trust' from those closest to them.{/cps}"
    
    t "{cps=40}There is a Latin term: {b}'Falsus in Uno, Falsus in Omnibus'{/b}. Does anyone know what it means?{/cps}"

    "{cps=35}The class was silent. I glanced at [y]; she was writing notes very quickly, as if trying to ignore my presence behind her.{/cps}"
    "{cps=40}As usual, she was always focused.{/cps}"
    "{cps=40}Unlike me...{/cps}"

    t "{cps=40}[mc], try answering. You seem to have a lot on your mind this afternoon.{/cps}"
    mc "{cps=40}Why me, Miss Nanami?{/cps}"
    t "{cps=40}Who else is more suitable than you?{/cps}"
    mc "{cps=40}Well there are...{/cps}"
    "{cps=40}I looked around the class.{/cps}"
    "{cps=40}But no one showed any sign of wanting to answer.{/cps}"
    t "{cps=40}Well?{/cps}"
    mc "{cps=40}Nothing, Ma'am...{/cps}"
    t "{cps=40}If there's nothing, answer quickly.{/cps}"
    mc"{cps=40}Ummm...{/cps}"

    menu:
        "One lie ruins everything":
            $ correct_answer_2 = True
            mc "{cps=40}It means... once you lie about one thing, everything you say will be considered a lie, Ma'am.{/cps}"
            
            if jujur and pasang == False:
                $ yuuka_rel += 5
                "{cps=35}Yuuka stopped writing for a moment. Her shoulders trembled slightly, but she still didn't turn around.{/cps}"
                "{cps=35}She seemed to be digesting those words, convincing herself that my sudden decision to join the Student Council—though bitter—was honest.{/cps}"

            elif jujur and pasang == True:
                $ yuuka_rel -= 2
                unknown "{cps=35}Then why did you let her do that...{/cps}"
                unknown "{cps=35}You said you joined the Student Council for us, but why were you playing around with the President behind my back...{/cps}"
                "{cps=35}A very soft murmur came from in front of me. So quiet, yet full of suspicion.{/cps}"

            elif jujur == False and pasang == False:
                $ yuuka_rel -= 3
                unknown "{cps=35}What a hypocrite...{/cps}"
                "{cps=35}The voice was almost inaudible, but the word 'hypocrite' echoed in my ears louder than Miss Nanami's voice.{/cps}"
                "{cps=35}Yuuka gripped her pen tightly. She knew I had lied to her this morning.{/cps}"

            elif jujur == False and pasang == True:
                $ yuuka_rel -= 5
                unknown "{cps=35}Liar...{/cps}"
                unknown "{cps=35}After lying to me, you went and had fun with her in the corridor...{/cps}"
                "{cps=35}A sharp whisper that made my hair stand on end. Yuuka wasn't even writing anymore; she just stared blankly at her book with glassy eyes.{/cps}"

            t "{cps=40}Correct. That is a moral law that is often harsher than written law.{/cps}"
            t "{cps=40}Once you destroy trust, it takes a lifetime to build it back.{/cps}"

        "One person's mistake is everyone's burden":
            $ correct_answer_2 = False
            mc "{cps=40}It means one person's mistake is the mistake of the entire group?{/cps}"
            
            t "{cps=40}Wrong. That is collective responsibility. Our focus is individual integrity.{/cps}"
            t "{cps=40}It seems you need to read more instead of just spacing out, [mc].{/cps}"
            
            v "{cps=40}Fufufu... Looks like [mc]'s brain is already smoking from this morning's class.{/cps}"
            v "{cps=40}Be careful, [mc]. If you space out too often, someone else might 'pluck' your integrity, you know.{/cps}"
            
            mc "{cps=40}(Damn... Vina always finds a way to jab at me. Is there anything in this school she doesn't know?){/cps}"

    t "{cps=40}Once you destroy trust, it takes a lifetime to build it back.{/cps}"
    
    "{cps=35}Yuuka stopped writing for a moment. Her shoulders trembled slightly; her hand gripped the pen so tightly her knuckles turned white.{/cps}"
    "{cps=35}I knew she was listening to every word. And I knew Miss Nanami's words were striking right at the center of the awkwardness between us.{/cps}"

    "{cps=35}Miss Nanami returned to the blackboard, the chalk in her hand screeching as she wrote a list of great traitors in history.{/cps}"
    "{cps=35}The classroom atmosphere grew very heavy. There was only the sound of pens on paper and the wall clock that seemed to slow down on purpose.{/cps}"

    "{cps=35}One hour passed...{/cps}"
    "{cps=35}The harsh afternoon sunlight slowly shifted, casting long shadows from the table legs across the wooden classroom floor.{/cps}"
    "{cps=35}Some of my classmates started looking sleepy, their heads nodding along to Miss Nanami's monotone yet sharp voice.{/cps}"
    
    "{cps=35}[t]'s voice explaining the collapse of great kingdoms due to internal betrayal felt like a whisper judging every breath I took.{/cps}"

    "{cps=35}I glanced forward. [y] remained in her position. She never once looked my way, even when she picked up a ruler or fixed her hair.{/cps}"

    "{cps=35}Two hours passed...{/cps}"
    "{cps=35}Time truly felt eternal. My legs felt stiff, and my mind drifted to Shoko, to Maya, and to the silver armband now attached to my shoulder.{/cps}"
    "{cps=35}Every second we spent in this silence felt more painful than the standing punishment in front of the class this morning.{/cps}"
    
    "{cps=35}The wall of ice [y] had built beside me felt thicker and thicker. I wanted to speak, but my throat felt locked by the weight of secrets and the choice I had just made.{/cps}"
    "{cps=35}My presence here... behind her... felt as if it had been completely erased from her little world.{/cps}"

    scene black with fade
    stop music fadeout 3.0

    play sound "audio/sfx/school bell.mp3"
    "{cps=40}Ding... Dong...{/cps}"
    "{cps=40}The dismissal bell finally rang. Other students began pouring out cheerfully, but I...{/cps}"

    "{cps=35}I touched the blue Student Council armband on my shoulder. The armband seemed to remind me that my 'playtime' was over.{/cps}"
    "{cps=35}I had to head to the meeting room, leaving this classroom silence for the real 'battlefield'.{/cps}"

    jump chapter_2_osis_kfm

label chapter_2_osis_kfm:
    scene bg_council_room_sunset with fade
    play music "audio/bgm/emptyroom.mp3" fadein 2.0

    "{cps=35}I stood in front of the Student Council room door. Orange evening sunlight came through the corridor window gaps, casting long shadows that seemed to pull me into a new swirl of problems.{/cps}"
    "{cps=35}I took a deep breath, straightened my uniform collar, then slowly pushed the door open.{/cps}"

    show maya_stern at center
    show vina_smile at right
    show yuuka_determined at left
    with dissolve

    m "{cps=40}Finally, our 'transfer' member arrives on time.{/cps}"
    
    if jujur and pasang == False:
        $ yuuka_rel += 3
        y "{cps=40}You're on time, [mc]. I've prepared the files you need to study as a new member.{/cps}"
        "{cps=35}Yuuka looked at me calmly. Although her face looked tired after Miss Nanami's class, there was a glint of support in her eyes.{/cps}"
        v "{cps=40}Hmm... you two are quite in sync. Even though this morning in class it looked like an ice wall separated you. Fufufu...{/cps}"
        y "{cps=40}W-what?{/cps}"
        "{cps=40}[y] blushed at [v]'s remark.{/cps}"

    elif jujur and pasang == True:
        $ yuuka_rel -= 1
        "{cps=35}Yuuka immediately stared sharply at the shoulder of my uniform. Her eyes narrowed when she saw the perfectly fastened blue armband.{/cps}"
        y "{cps=40}That armband... is very neat, [mc]. Looks like it was put on by someone 'very skilled'.{/cps}"
        v "{cps=40}Fufufu, of course it's neat. I happened to see Senior Maya giving 'special service' in the corridor earlier. Right, President?{/cps}"
        "{cps=35}Yuuka clenched the hem of her skirt. She looked away, trying hard to focus again on the pile of papers in front of her.{/cps}"
        m "{cps=40}That's enough. No need to discuss it.{/cps}"
        m "{cps=40}Besides, [mc]'s arms were sore earlier.{/cps}"
        y "{cps=40}But still, he couldn't put it on himself?{/cps}"
        v "{cps=40}Oh? Did you want to put it on for him?{/cps}"
        y "{cps=40}That's not what I meant...{/cps}"
        "{cps=40}[y]'s face looked a little embarrassed.{/cps}"

    elif jujur == False and pasang == False:
        $ yuuka_rel -= 1
        "{cps=35}The atmosphere instantly became very cold when I entered. Yuuka didn't even lift her head to look at me.{/cps}"
        y "{cps=40}President, all documents are ready. We don't need to wait for explanations from an 'outsider' who can't respect time, right?{/cps}"
        v "{cps=40}Oof, what's with this atmosphere? Feels like I'm inside a fridge. So cold~{/cps}"
        "{cps=35}Yuuka treated me like an inanimate object. My lie this morning had truly built a steel wall between us.{/cps}"
        m "{cps=40}No need to go that far, [y].{/cps}"
        m "{cps=40}Besides, we still need him.{/cps}"
        y "{cps=40}Need him? For what, Senior Maya?{/cps}"
        m "{cps=40}Because he's the only boy here.{/cps}"
        m "{cps=40}His strength can be put to good use.{/cps}"
        y "{cps=40}Well... true.{/cps}"

    elif jujur == False and pasang == True:
        $ yuuka_rel -= 2
        "{cps=35}The moment I entered, Yuuka stood up suddenly from her chair. The screech of the chair was very harsh in the quiet room.{/cps}"
        y "{cps=40}So this is why you weren't honest with me earlier?{/cps}"
        y "{cps=40}Not only joining the Student Council in secret, but also immediately becoming the President's favorite 'pet'?{/cps}"
        v "{cps=40}Whoa... whoa... the atmosphere is hotter than I imagined. [mc], it seems you really committed a major sin today.{/cps}"
        "{cps=35}Yuuka looked at me with empty eyes. Not explosive anger, but a very deep disappointment.{/cps}"
        m "{cps=40}That's enough, [y]. [mc]'s arms were sore earlier, and besides he wanted to surprise you.{/cps}"
        y "{cps=40}Yeah... I already got a surprise.{/cps}"
        y "{cps=40}I was so shocked my chest feels tight.{/cps}"
        y "{cps=40}Senior Maya, may I step out for a moment? I need some fresh air.{/cps}"
        m "{cps=40}Hah....{/cps}"

    m "{cps=40}Enough drama. We're here to work, not to put on a cheap afternoon soap opera.{/cps}"
    "{cps=35}Maya tapped her pen hard on the table. Her authoritative voice instantly silenced everyone.{/cps}"
    if jujur == False and pasang == True:
        m "{cps=30}[y], watch your attitude! Stay here because I'm about to start the meeting.{/cps}"
        y "{cps=30}Hah... fine, Senior.{/cps}"
        "{cps=30}[y] sat down in a seat farther than usual.{/cps}"
    

    m "{cps=40}So... since you are new members, I have a first assignment.{/cps}"
    m "{cps=40}Your first task is to audit the inventory of the auditorium warehouse.{/cps}"
    m "{cps=40}[mc], since you joined late, you need to learn the field as quickly as possible. You will go to the warehouse with Yuuka.{/cps}"
    v "{cps=40}Then what about me, Senior?{/cps}"
    m "{cps=40}You help me here with the paperwork.{/cps}"
    v "{cps=40}Haaah....{/cps}"
    m "{cps=40}You don't mind, do you [y]?{/cps}"

    if yuuka_rel < 0:
        y "{cps=40}...Understood, President. I will guide him... as best I can.{/cps}"
        "{cps=35}Yuuka answered without looking at me at all. She walked straight toward the door with quick, heavy steps.{/cps}"
    else:
        y "{cps=40}Understood.{/cps}"

    scene black with fade
    stop music fadeout 3.0
    
    m "{cps=40}After you finish at the warehouse, I will wait for the report in this room. Understood?{/cps}"
    y "{cps=40}Understood, Senior.{/cps}"
    m "{cps=40}Any questions?{/cps}"
    y "{cps=40}None for now.{/cps}"
    m "{cps=40}Alright. Since the job division is done, get to work.{/cps}"
    v "{cps=40}Have fun in that dusty warehouse, [mc].{/cps}"
    mc "{cps=40}Hey!{/cps}"
    "{cps=40}I returned to my desk, preparing everything needed for the audit.{/cps}"
    v "{cps=60}Pssst... Specimen! Come here a sec.{/cps}"
    "{cps=35}Vina tugged the edge of my uniform until I almost tripped. She pulled me in front of her desk.{/cps}"

    mc "{cps=40}What now, Vin? I have to get to the warehouse with Yuuka.{/cps}"

    v "{cps=60}That's exactly it! Do you know why Senior Maya gave that task to the two of you?{/cps}"

    mc "{cps=40}Because I'm a new member and Yuuka knows the audit procedure best?{/cps}"

    v "{cps=60}Tsk! So naive.{/cps}"

    "{cps=35}Vina facepalmed. Then she crossed her arms, looking at me with a fake 'love expert' stare.{/cps}"

    v "{cps=60}Senior Maya never assigns a two-person task without a reason. She's the efficient type. If it was just an audit, one person would be enough.{/cps}"

    v "{cps=60}She's giving you two 'space'. She knows this morning's class atmosphere was a mess because your relationship with [y] went south, right?{/cps}"

    mc "{cps=40}You mean... Senior Maya deliberately wants me and Yuuka to make up?{/cps}"

    v "{cps=60}Maybe. But don't celebrate yet. Senior Maya never gives a 'gift' without a price.{/cps}"

    v "{cps=60}Remember, Specimen. Senior Maya isn't as robotic as you think. She's watching you... for some reason, the way she looks at you is different from how she looks at the rest of us.{/cps}"

    mc "{cps=40}Different how?{/cps}"

    v "{cps=60}You'll find out yourself later. Now go! Before your handler gets mad again.{/cps}"

    if jujur and pasang == True:
        y "{cps=40}[mc]! What are you doing taking so long? Let's go!{/cps}"
    else:
        "{cps=40}[y] was visible at the door of the room with a very annoyed face.{/cps}"

    v "{cps=60}See, her horns are already out. Good luck, Specimen!{/cps}"

    if yuuka_rel < 0:
        "{cps=35}While I was still talking with [v]...{/cps}"
        v "{cps=35}Looks like you need to hurry, [mc]...{/cps}"
        mc "{cps=35}What do you mean?{/cps}"
        v "{cps=35}Look at the door.{/cps}"
        "{cps=40}[y] left without me.{/cps}"
        mc "{cps=35}Huh!? [y], wait for me!{/cps}"
    else:
        y "{cps=40}W-what are you saying, Vin? It's not like I'll be there until night.{/cps}"
        v "{cps=40}Ehehe, who knows...{/cps}"
        y "{cps=40}Come on [mc], we have to finish this before night.{/cps}"
        mc "{cps=40}Alright. Let's go, [y].{/cps}"


    "{cps=35}The meeting ended with mixed feelings. Yuuka and I now walked toward the auditorium building at the back of the school.{/cps}"
    "{cps=35}The silence along this corridor felt far more torturous than [t]'s History class earlier.{/cps}"
    mc "{cps=40}Um... [y]...{/cps}"

    if jujur and pasang == False:
        y "{cps=40}Hm? What is it?{/cps}"
        mc "{cps=40}About earlier... thank you for defending me in front of Vina.{/cps}"
        y "{cps=40}W-what, that's just a fellow member's duty. Besides, I'm glad you didn't do anything weird earlier.{/cps}"
        "{cps=35}Yuuka slowed her pace a little so she was walking beside me. The atmosphere felt much lighter.{/cps}"

    elif jujur and pasang == True:
        y "{cps=40}Can you still smell it?{/cps}"
        mc "{cps=40}Huh? Smell what?{/cps}"
        y "{cps=40}Senior Maya's perfume. You two were standing very close earlier, right?{/cps}"
        mc "{cps=40}That... she was the one who suddenly put it on for me.{/cps}"
        y "{cps=40}Hmph. Next time if you need help, just tell me. No need to bother the President.{/cps}"
        "{cps=35}Yuuka walked a bit faster, as if trying to throw her irritation into the air.{/cps}"

    elif jujur == False and pasang == False:
        y "{cps=40}Save your voice for counting items later, [mc].{/cps}"
        mc "{cps=40}Yuuka, about me not telling you from the start...{/cps}"
        y "{cps=40}I don't need an explanation right now. I just want this task finished quickly.{/cps}"
        "{cps=35}Yuuka didn't look at me at all. The distance between us felt very far even though we walked side by side.{/cps}"

    elif jujur == False and pasang == True:
        y "{cps=40}...{/cps}"
        mc "{cps=40}Yuuka, wait a second. Listen to me first...{/cps}"
        y "{cps=40}Don't come closer.{/cps}"
        mc "{cps=40}What did I even do wrong? Why are you this cold?{/cps}"
        y "{cps=40}Ask yourself.{/cps}"
        y "{cps=40}Just focus on your task. I'm only here following the President's orders, not as your friend.{/cps}"
        "{cps=35}Her words were so sharp, colder than the AC in the Student Council room earlier. I could only hang my head behind her.{/cps}"

    "{cps=35}Before long, we arrived in front of a large iron door that was already slightly rusted.{/cps}"
    
    play sound "audio/sfx/door.mp3"
    "{cps=35}The screech of the iron door being forced open broke the silence of the back area of the school.{/cps}"
    
    scene bg_warehouse_dark with dissolve
    "{cps=35}The smell of dust and old wood hit our noses the moment we stepped into the dim auditorium warehouse.{/cps}"

    
    y "{cps=40}Ugh, so dirty... Senior Maya really gave us a troublesome 'treasure'.{/cps}"
    "{cps=35}Without preamble, [y] immediately tried to shift a pile of rusty folding chairs. The sound of metal scraping the concrete floor rang out in the quiet room.{/cps}"
    
    mc "{cps=40}Here, [y], let me help. These things are too heavy for you to lift alone.{/cps}"

    if jujur and pasang == False:
        y "{cps=40}Thank you, [mc].{/cps}"
        y "{cps=40}Sorry your first Student Council task is physical work like this. But... at least we can finish it together.{/cps}"
        "{cps=35}Yuuka gave me a thin smile. Even though her face was a little dirty from the dust, the atmosphere between us felt very warm.{/cps}"

    elif jujur and pasang == True:
        y "{cps=40}No need. Better save your strength to serve your beloved 'President'.{/cps}"
        mc "{cps=40}Come on [y], don't start again. I'm here with you now.{/cps}"
        y "{cps=40}Who knows, maybe she'll suddenly call you again because your 'arms are sore'?{/cps}"
        "{cps=35}Yuuka slammed the chair roughly. She was really showing her fangs because of the corridor incident earlier.{/cps}"

    elif jujur == False and pasang == False:
        y "{cps=40}Just do what the President ordered. No need to feel sorry for me.{/cps}"
        mc "{cps=40}I'm not feeling sorry. I just want to help my childhood friend.{/cps}"
        y "{cps=40}Childhood friend?{/cps}"
        y "{cps=40}I wonder... what kind of childhood friend keeps a secret this big, [mc]?{/cps}"
        "{cps=35}Yuuka stopped moving. She stared at the pile of dust in front of her with an empty, wounded look.{/cps}"

    elif jujur == False and pasang == True:
        y "{cps=40}Don't touch me.{/cps}"
        "{cps=35}Yuuka roughly brushed my hand away when I tried to take over the box she was carrying.{/cps}"
        mc "{cps=40}Yuuka, this is dangerous if you force it alone!{/cps}"
        y "{cps=40}What's more dangerous than someone who pretends to be kind to me but laughs behind my back with another woman?{/cps}"
        y "{cps=40}If you really don't see me as important, at least don't give me false hope by pretending to help me now.{/cps}"
        "{cps=35}Her voice trembled. She was truly at the edge of her patience.{/cps}"

    "{cps=35}Silence covered the warehouse again. Evening light coming through the roof gaps stretched out, creating giant shadows among the piles of discarded items.{/cps}"

    y "{cps=40}Alright, open the report book quickly. We'll start from the east rack.{/cps}"
    "{cps=35}We started working in silence. One by one we recorded the items. Chairs, stage tables, even last year's worn festival equipment.{/cps}"
    
    mc "{cps=40}Yuuka, look at this...{/cps}"
    
    "{cps=35}I pulled a silver trophy from under a pile of dusty black cloth. The trophy felt very heavy and cold in my hands.{/cps}"
    
    mc "{cps=40}'Best Vocal'. The name is... Kisaragi Sayoko.{/cps}"
    
    "{cps=35}Yuuka stopped writing. She stared at the trophy for a long time, as if looking at a monument of failure.{/cps}"
    
    y "{cps=40}Kisaragi Sayoko... {w=0.5} The legendary diva who left behind not a single official recording.{/cps}"
    
    mc "{cps=40}What do you mean? She won this trophy, right?{/cps}"
    
    y "{cps=40}She did win it. But Sayoko-senior is the only winner who never graduated from this school. She chose to drop out right before graduation day.{/cps}"
    
    mc "{cps=40}She left? Why?{/cps}"

    "{cps=35}Yuuka didn't answer right away. She carefully put the trophy back into its dusty box.{/cps}"
    y "{cps=40}No one knows for sure. There are only rumors... about a failed concert, and a name that was erased from the school records.{/cps}"
    y "{cps=40}Anyway, record it. 'One Best Vocal trophy, condition: slightly tarnished'.{/cps}"

    "{cps=35}We continued the audit until the evening light grew thinner. Among the junk, I also found an old folder with the name 'Ikazaki [mi]' written on it—my older sister's name.{/cps}"
    "{cps=35}My hands trembled slightly as I held it. But before I could open it, Yuuka's voice cut in.{/cps}"
    y "{cps=40}[mc], the report is almost done. Let's go back before Senior Maya gets impatient again.{/cps}"
    mc "{cps=40}...Alright.{/cps}"

    "{cps=35}I slipped the old folder into my bag. A piece of the past that now became my responsibility to carry.{/cps}"

    scene black with fade
    stop music fadeout 2.0

    # Shared flags for Chapter 3 (aligned with main sastra / osis routes)
    $ masuk_club = True
    $ club_choice = "osis"
    $ kitaimirai_known = True
    $ chapter2_route = "osis"
    $ sayoko_known = True
    $ megumi_archive_found = True

    jump chapter_2_end
