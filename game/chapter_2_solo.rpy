label chapter_2_solo:
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
    v "{cps=60}Yo! [mc]. Your face looks like someone who just escaped the final judgment. What happened?{/cps}"

    mc "{cps=40}You always show up out of nowhere, [v].{/cps}"

    v "{cps=60}Fufufu, not really. Oh right, where did Senior [m] take you yesterday?{/cps}"
    v "{cps=60}Did she throw you into the back warehouse, or did you manage to 'negotiate' with her?{/cps}"
    
    "{cps=35}Vina rested her chin on her folded hands on the back of my chair. Her sharp eyes seemed to be scanning every inch of my reaction.{/cps}"
    
    mc "{cps=40}Negotiate? What do you mean?{/cps}"
    
    v "{cps=60}Come on [mc], just tell me. She definitely mentioned the name 'Ikazaki [mi]', right?{/cps}"
    "{cps=35}Huh? How does she know about my sister?{/cps}"
    v "{cps=35}Hm? Why did your face turn as pale as paper?{/cps}"
    
    mc "{cps=40}Were you... eavesdropping?{/cps}"
    
    v "{cps=60}Well... let's just say I have 'ears' everywhere... besides, this school has walls thin enough for trained ears.{/cps}"
    "{cps=35}So, what's your choice?{/cps}"
    mc "{cps=40}I... {w=0.1}didn't join any organization.{/cps}"
    mc "{cps=40}I just handed the form to Senior [m] at the gate earlier.{/cps}"
    if jujur == False:
        "[y] and [v]" "{cps=35}HAH!?{/cps}"
        "{cps=35}I heard the sound of a chair falling in front of me.{/cps}"
        "{cps=35}Then [y] came over to me.{/cps}"
    else:
        "{cps=35}I heard the sound of a chair in front of me.{/cps}"
        "{cps=35}Then [y] came over to me.{/cps}"
        "{cps=35}Looks like an intense conversation is about to start...{/cps}"
    y "{cps=35}You're serious about not joining any organization?{/cps}"
    mc "{cps=35}Yep, I've made my decision.{/cps}"
    "{cps=35}Really?{/cps}"
    mc "{cps=35}Would I lie about that?{/cps}"
    if jujur == False:
        mc "{cps=35}Sorry I told you late, [y]...{/cps}"
        "{cps=35}Because I knew if I told you from the start, you wouldn't accept it.{/cps}"
    else:
        mc "{cps=35}You don't mind, right?{/cps}"
    v "{cps=35}Well... I wouldn't say I mind exactly.{/cps}"
    v "{cps=35}But... if you joined the Student Council the atmosphere would be more fun!{/cps}"
    v "{cps=35}You agree, right [y]?{/cps}"
    y "{cps=35}That's right! Why don't you just join the Student Council, [mc]?{/cps}"
    v "{cps=35}Your sister was in the Student Council too, wasn't she?{/cps}"
    "{cps=35}*SLAM*{/cps}"
    mc "{cps=35}Don't ever bring my sister into this conversation.{/cps}"
    v "{cps=35}Hue— what?{/cps}"
    "{cps=35}I... need to go to the bathroom first.{/cps}"
    "{cps=35}I stood up, leaving the two of them in the classroom.{/cps}"
    v "{cps=35}What's with him?{/cps}"
    v "{cps=35}I only wanted to invite him to join.{/cps}"
    y "{cps=35}That's not the way to do it, [v]!{/cps}"
    v "{cps=35}Then how?{/cps}"
    y "{cps=35}If we bring up his sister, of course he'll react like that.{/cps}"
    y "{cps=35}He's been like that since middle school...{/cps}"
    "{cps=35}The cold corridor air cooled my head a little. I leaned against the wall, staring at the tip of my shoes that were starting to look dull.{/cps}"
    "{cps=40}Damn... Why did I get so angry? Vina only... she just didn't know anything.{/cps}"
    "{cps=35}I stopped in front of a large window overlooking the front courtyard. I clenched my fists, trying to hold back the overflowing emotions.{/cps}"
    "???" "{cps=35}What are you doing standing there?{/cps}"
    mc "{cps=35}Huh?{/cps}"
    "{cps=35}I jumped. At the end of the corridor, leaning against the wall, was a very familiar girl...{/cps}"
    mc "{cps=40}You... who are you?{/cps}"
    "???" "{cps=35}HAH? You're serious you don't know me?{/cps}"
    mc "{cps=35}Wait... let me try to remember...{/cps}"
    "{cps=35}What was her name again?{/cps}"
    menu:
        "Kisaragi [f]":
            $ tebak = True
            $ fumi_rel += 5
            mc "{cps=40}Senior [f]?{/cps}"
            f "{cps=35}That's right!{/cps}"
            f "{cps=35}So you have a good memory after all?{/cps}"
            mc "{cps=35}Not really..{/cps}"
            f "{cps=35}Ah! How about this.{/cps}"
            f "{cps=35}I'll introduce myself again.{/cps}"

        "The host from the welcome ceremony?":
            $ tebak = False
            mc "{cps=40}The host from the entrance ceremony?{/cps}"
            "???" "{cps=40}Well... that's not wrong...{/cps}"
            "???" "{cps=40}But how can you not know my name?{/cps}"
            "???" "{cps=40}I introduced myself back then, you know.{/cps}"
            mc "{cps=40}Sorry, Senior, I don't remember that well...{/cps}"
            "???" "{cps=40}Tsk! Fine, I'll say it again.{/cps}"

    "{cps=35}She had short mauve-brown hair and calm red eyes—the friendly smile of someone used to standing on stage.{/cps}"
    f "{cps=35}My name is Kisaragi [f], host of the welcome ceremony yesterday and also the president of the Literature Club.{/cps}"
    f "{cps=35}Your name is Ikazaki [mc], right?{/cps}"
    "{cps=35}How does she know my name?{/cps}"
    mc "{cps=35}Y-yes, Senior, why?{/cps}"
    f "{cps=35}Why are you wandering the corridor? First period is about to start...{/cps}"
    mc "{cps=35}I don't know, Senior.. I feel like I've done a lot of bad things...{/cps}"
    f "{cps=35}Hmm... like what?{/cps}"
    mc "{cps=35}Do I really need to tell you everything?{/cps}"
    f "{cps=35}Just the outline is fine. Besides, it looks like you need someone to talk to.{/cps}"
    mc "{cps=40}Hah... I'm tired, Senior. Everyone looks at me as if I'm a replica of my late older sister.{/cps}"

    mc "{cps=40}They want me to join the Student Council, they want me to become 'great' like him. But when I refuse, I'm treated like a coward running away.{/cps}"

    f "{cps=35}Standing under the shadow of a big tree is cool, but you'll never get sunlight for yourself, right?{/cps}"

    "{cps=35}I fell silent. That sentence... felt far too accurate.{/cps}"

    "{cps=35}Fumi looked at me with a very calm gaze. There was no pity in her eyes, only a deep understanding.{/cps}"
    f "{cps=35}I understand how you feel, [mc]...{/cps}"
    "{cps=35}What does Senior even know?{/cps}"
    "{cps=35}My family name is Kisaragi too, right? And in this school, that name carries its own 'burden' because of my older sibling.{/cps}"
    mc "{cps=40}Yes, Senior, so what?{/cps}"
    f "{cps=40}Do you know the famous idol, Kisaragi [sa]?{/cps}"

    mc "{cps=40}I know her, Senior. If I'm not wrong she was in the same era as Ogata [ri] and Morikawa [yu], right?{/cps}"
    f "{cps=35}Exactly.{/cps}"
    mc "{cps=35}And?{/cps}"
    f "{cps=35}I'm her younger sister.{/cps}"
    mc "{cps=35}Huh? {w=0.1} Are you serious, Senior?{/cps}"
    f "{cps=35}If you think I'm just bragging that's fine. Later during break, try coming to the Literature Club room.{/cps}"
    f "{cps=35}I'll tell you everything.{/cps}"
    mc "{cps=35}Ummm....{/cps}"
    f "{cps=35}See you later.{/cps}"
    mc "{cps=35}Wait, Sen—{/cps}"
    "{cps=35}[f] left without a trace.{/cps}"
    mc "{cps=35}Senior...{/cps}"

    "{cps=35}*DING DING DING*{/cps}"
    "{cps=35}The first period bell had already rung.{/cps}"
    mc "{cps=35}Damn.. why does it have to end on a cliffhanger like this...{/cps}"
    "{cps=35}I have to meet her later.{/cps}"

    scene bg_classroom with fade
    "{cps=35}I returned to class just as the teacher was about to start.{/cps}"
    "{cps=35}The rest of the morning passed in a blur of lectures and the same math problem as the other routes...{/cps}"

    t "{cps=40}If 3x + 5 = 20, what is the value of x?{/cps}"
    if jujur:
        "{cps=35}Yuuka in front of me looked panicked; she held up five fingers under the desk as a signal.{/cps}"
    else:
        "{cps=35}Yuuka in front of me looked completely normal and didn't give any signal at all.{/cps}"
    menu:
        "5":
            $ correct_answer = True
            $ yuuka_rel += 5
            $ vina_rel += 5
            mc "{cps=40}The answer is... 5, Ma'am.{/cps}"
            t "{cps=40}Correct. Simple, isn't it?{/cps}"
            t "{cps=40}Remember, in Algebra, our goal is to find the 'Missing Value' (x) by balancing both sides.{/cps}"
            "{cps=35}For some reason, the explanation didn't only sound like math—it sounded like a way of facing this messy life of mine.{/cps}"
        "15":
            $ correct_answer = False
            $ yuuka_rel -= 2
            mc "{cps=40}The answer is... 15, Miss?{/cps}"
            t "{cps=40}Fifteen? Wrong! Stand at the front until my class is over!{/cps}"
        "3":
            $ correct_answer = False
            $ yuuka_rel -= 2
            mc "{cps=40}The answer is... 3?{/cps}"
            t "{cps=40}Wrong! Please stand beside the blackboard until I finish explaining.{/cps}"

    if correct_answer:
        "{cps=35}Thank goodness my answer was correct earlier...{/cps}"
    else:
        "{cps=35}If only my answer had been correct... maybe my legs wouldn't be this sore from standing in front of the class.{/cps}"

    play sound "audio/sfx/school bell.mp3"
    "{cps=40}Break time arrived.{/cps}"

    "{cps=35}I decided to go to the Literature Club room as Senior Fumi had suggested.{/cps}"
    scene bg_literature_club with fade
    play music "audio/bgm/literatur2.mp3" fadein 2.0

    "{cps=35}The room smelled of old paper and jasmine. Fumi was already there, flipping through a thick notebook.{/cps}"
    f "{cps=35}You came. Good.{/cps}"
    f "{cps=35}Sit down. I'll tell you about my sister—and about why the name 'Kisaragi' is both a blessing and a curse in this school.{/cps}"

    "{cps=35}Fumi spoke about Sayoko: a legendary singer who never released an official song, who dropped out right before graduation, and whose name was almost erased from school records.{/cps}"
    f "{cps=35}Standing in someone's shadow is easy. Breaking free from it is the real work.{/cps}"
    f "{cps=35}You chose not to join any club. That choice is yours. But don't use it as an excuse to stop moving forward.{/cps}"
    mc "{cps=35}...Thank you, Senior.{/cps}"

    "{cps=35}Before I left, Fumi handed me a thin booklet—notes about old school festivals and a project once called 'Kitaimirai'.{/cps}"
    f "{cps=35}Read it when you're ready. Your sister left traces here too.{/cps}"

    scene black with fade
    stop music fadeout 3.0

    "{cps=35}That night, in my quiet room, I opened the booklet under the dim desk lamp.{/cps}"
    "{cps=35}The name Ikazaki [mi] appeared again and again—alongside plans for a concert that was never fully realized.{/cps}"
    "{cps=35}'Kitaimirai'... Hope for the Future.{/cps}"
    "{cps=35}I still stood at a crossroads. But at least now I knew I wasn't the only one who had walked this path before.{/cps}"

    # Shared flags for Chapter 3
    $ masuk_club = False
    $ club_choice = None
    $ kitaimirai_known = True
    $ chapter2_route = "solo"
    $ sayoko_known = True
    $ megumi_archive_found = True

    jump chapter_2_end
