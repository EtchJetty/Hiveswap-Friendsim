

label epilogue_fix:
    $ renpy.block_rollback()

    $ main_menu = False

    show expression "gui/game_menu.png"

    scene bg black

    $ quick_menu = True









    $ checkallends()

    menu:
        "Do you want to understand?"
        "[pick] NO" if True:

            call ending ("scratch end", False, True) from _call_ending_108_fix
            return

        "[pick] YES" if persistent.understand:

            o "Of course you do. Your sort of creature always does."

            show bg alternia with fade


            "You’re worn out. Last night was...well, it sure was something. You lived (probably), you learned (definitely), you made choices (you had to)."

            "And after all this time, here you still are!"

            "{size=21}So after a day of recuperation from ragers and houses of horror, you’re out walking the streets of the place you may as well start calling home. You’ve changed out of your party gear, opting for your old hoodie standby. It fits the mood you’re in.{/size}"

            "You’re not really looking to meet anyone new tonight. Well, like. You wouldn’t say no, probably. But you’re not jonesin’ for it. Only a little. It’s complicated."

            show field2 with fade


            "After an indeterminable amount of minutes of aimless walking, you look around at where you’ve ended up. You seem to have wandered into a dirt pile."

            "Oh, you know this dirt pile! It’s Fozzer’s corpsefield. Hmm. How did you get here, you wonder? You’re pretty sure you were just on the other side of the city, with no particular desire to come anywhere near here."

            "It’s probably fine. Just your deep, innate bro-honing skills taking over your goddamn body. Just Little Friendship Things."

            "You look around for your pal Fozzer, peeking down into a few of the deeper holes. You might as well say hello, since you’re here and all."

            if persistent.flash:
                show field2column behind fozzer
                show field2flash
            elif True:
                show field2column_slow behind fozzer




            "Holy shit, that...again?"

            "Curiosity killed the cat, but you’ve definitely got more than nine lives, so you shrug and slide (not gracefully) down into the shiny hole."

            show hole with wipeup



            "Fozzer is nowhere to be found, but there is a window down here. It’s almost completely unearthed, and doesn’t take much effort to free it the rest of the way."

            "At first you think it might be some cool new trash you could make art with, but when you look closer, you reconsider. There’s a whole-ass room you can see through the pane of glass laying at your feet."

            "That’s...weird. Weirdness isn’t typically a deterrent for you you, but usually there’s at least some causational coherence. Doors are in walls, walls surround rooms. You aren’t used to finding parlors in ditches."

            "Is there a latch or something? Should you do a polite little knock? There might be friends in there! Damn, you could really go for some friends right now. Is there protocol for approaching ditch windo--"
            show holelight

            o "Allow me to stop you there. I am a timeless being of the void, but even my patience has its limits."
            o "Fun is fun, but this frivolous navelgazing is no longer necessary."
            o "Come in from behind the shadow of that narrative text. It’s so very hard to see your face."

            show blackcover with dissolve
            show depixelate behind blackcover at flippeddefault
            show reader nervous behind depixelate at flippeddefault
            show room behind reader
            play music "volumes/volume18/music/FS_SCRATCH.wav" loop
            hide blackcover with dissolve





            hide depixelate with dissolve
            reader "You aren’t sure where you are, and it’s unsurprisingly a little nerve-wracking! You look over your shoulder at the window you guess you just fuckin' came on through."

            show scratch neutral at offscreenflippedright
            reader "The Alternian sky is framed by the edge of your dirt hole, and the knot in your stomach loosens a bit. Hopefully that means this is a two-way portal."

            show scratch at right1280
            show reader at left1280
            with ease
            reader oh "You turn to look at your surroundings, and oh! There’s someone here! The guy you just heard, you assume. He doesn’t look like any of the other aliens you’ve met."

            s toself "Oh. I’m not an alien. Or, no more than any of us are alien to each other. In fact, nothing is alien to me. The root concept behind that term is alienation, being forced from that which is natural."
            s "Nothing is unnatural to me. I look upon all realities as equally inviting and approachable. It’s you, my dear, who are out of place."
            s "I could see that even if I was not omniscient. Which I am."

            reader oh "Okay, so, not an alien. With no horns or a caste sign, though, he’s definitely not a troll. Whoever he is, he seems to be...white. Just, really white. And round, and his outfit is...admittedly, kind of dope."

            show reader at halfleft1280 with ease
            reader "Looking at him really ramps up your friendthirst. He’s just got this quality about him that you’ve got to get with. You take a step toward him, almost without thinking about it."

            s neutral "Oh, my apologies."
            s "That compulsion has become extraneous. Let me take care of it for you."

            show scratch behind reader at nod
            show reader faint at loweredpos
            reader "He snaps his fingers and your knees buckle. The force of the universe presses down on you like g-force."

            show scratch gesturing at loweredmid with move
            reader "You blink, and somehow he’s there immediately, arms outstretched to catch you as you fall. He steers you to a chaise lounge and you drape yourself weakly onto it."


            show scratch gesturing at middle
            show reader at left1280
            with ease
            show reader at smalllower
            s "Please, have a seat. The emotional transition might be a tad uncomfortable, but I know you’ve handled worse."
            show scratch neutral at right1280 with ease
            s neutral "You’re quite the soldier. Allow me be the first to say that I am very pleased with your work."
            s toself "I knew exactly what you were going to do, of course."
            s "And most of your work was, in fact, my work. Regardless, congratulations are in order."
            show scratch neutral

            reader getittogether "{size=25}What is this guy talking about? Your work? You try to parse what he’s saying, but your body is still shaking from whatever he just did to you, and it’s hard to think in here. You suddenly, sharply don’t feel friendly toward him at all anymore, or toward anyone.{/size}"

            reader "The void left by that feeling is a freshly gaping horror. It’s like who you thought you were caved in itself, a black hole of personality eating your body up from the inside."

            show reader at smalllowertodefault
            reader "You try to pull your shit together. He seems like he means business. This is no time to lose it, no matter if your sense of self is shattering."

            s toself "{size=20}When you truly reflect on yourself, you surely can’t with any honesty claim to believe any of this was by your own making? Crash landing on a hostile alien world? Surviving the impact? Dragging around a half-broken body and somehow not immediately being eaten by local fauna?{/size}"

            s neutral "Did you learn an alien language just by thinking about it very, very hard?"

            reader confused "{size=25}Right...Mallek said something about that. That you were speaking perfect Alternian. And it was kind of weird but you kind of just...accepted it. For no good reason. That’s your whole deal. Your friends all accepted your quirks. That’s what friends do!{/size}"

            reader "You say it to convince yourself as much as to prove it to him."

            s "So many trolls, so many {i}fascinating{/i} aliens, and all of them wanted to know you. Did you really think you managed that on your own laurels?"
            s sarcastic "Were they all drawn to an indefinable something, a...je n'ais se quoi?"

            reader "Well...yeah? You had this whole emotional arc. You got self-confidence! You grew as a person and helped others to grow!"

            show scratch sigh at smalllower
            reader "The white text guy doesn’t make expressions, but you get the feeling he’s looking at you pityingly."

            s "I find you sweet. Honestly, I do."
            show scratch sarcastic at smalllowertodefault
            s sarcastic "I don’t intend to cause emotional injury; I’m just telling you the truth."
            s "I never lie, you’ll find."
            s "It isn’t like you don’t have admirable qualities of your own, of course."
            s "You have made quite the valuable vessel for me, and I appreciate that very much."
            s "I could not have done it without you."
            s toself "I am only joking; I absolutely could have done it without you. It is just infinitely more fun to do these things together, is it not?"

            reader falter "What things? What did he do? What did {i}you{/i} do? You hope you didn’t do something that would fuck over all your friends."

            reader "{size=25}Though when you try to think about them now, the bonds you felt before come up all twisted. Without the artificial friendship drive he’d given you pushing you forward, you’re not even sure what those memories are supposed to feel like.{/size}"

            show reader at breathe
            reader "You close your eyes and breathe. You try to remember the way Polypa touched your face after you’d touched hers, her claws trailing down your cheek. How Tyzias slept, trusting, as you kept watch."

            reader "How Tagora gave you a chance when he saw something in you you didn’t even see in yourself. How, not that long ago, you got the chittr handle of an extremely friendly jadeblood boy."

            reader "Those moments are like the memory of warmth to you now. Blurry, cold, and out of reach. Was all of that nothing? Your heart is a chasm."

            show reader falter
            s "Don’t worry so much about it. I simply needed some dots connected, some pieces in place for my next move."
            s "Choose whichever metaphor suits you."
            s "Whichever way you frame it, because of you, everyone will soon be in their right place."

            show reader hoodie at nod
            reader "Shit, what have you done? Your head starts to spin and you think you might cry, so you pull your hood up over your head to block out the harsh green of the room."

            reader "You try to imagine it still smells a little like Mallek. It doesn’t. It doesn’t smell like anything, really, but you remember what it smelled like at first, and you hold on to that."

            reader "It was real, you tell yourself. Your friends were real, and what you felt for them, and with them, was real too."

            reader "You’re so afraid for them, and as guilty as you feel for craving it, the fear just makes you need those feelings you felt before even more. You’re clawing desperately for the euphoria of caring, of being cared for."

            reader "Who cares if your hand was forced? You felt it, and it still mattered. Matters."

            reader "{size=25}You remember how you felt watching Chixie perform, bathed in light and righteous anger, and also how you drunkenly commiserated with her later, when--no. That’s not right. That didn’t happen. Except...you still remember how hungover you were the next day.{/size}"

            show scratch neutral behind room at default
            show reader hoodie behind room at default
            show reader behind room at right1280
            show scratch behind room at left1280
            show roomflip behind scratch
            hide room
            with pop
            reader "Just when you started making sense of things, the whole fucking world shifts under your feet again. You just can’t keep up with all this moving real estate in your brain!"

            s "Ah, yes. All of the resets. Annoying, but necessary."
            s "You are just indescribably bad at keeping yourself alive and in one piece. And you weren’t quite as adept at befriending aliens to start out with."
            s toself "My intervention was necessary to keep you on the right path. Time and space mean very little to me, but I had to move quickly and, again, repeatedly."
            s "Swipe some incriminating notetaking here, befriend an impressionable young upstart there. Anger a Cholerbear, inspire some bandits, you know how it is. You have to throw the temporal spaghetti at the wall to see what sticks."
            show reader determined
            s "I’m sure if you look back, you will be able to see traces of my deft touch."
            s "So a few memories may have slipped through the cracks here and there. Timelines tend to collapse in on each other if you aren’t careful."
            s "Your ability to mentally withstand such an event, and so often, is a testament to my acumen in choosing you for the task."
            s "You even almost caught on a few times, which I must say I was not expecting."
            s neutral "You almost listened to the silly little girl who likes to dress up in big coats and cause me trouble."
            s "And, as always, some bystanders end up caught in the crossfire."
            s "The one with the shovel, for instance. I doubt his mind will ever be the same. A pity."

            show reader angry at nod
            reader "You sit up straighter and clench your hands into fists. Over the course of his pompous monologuing, you’ve moved past fear and grief and onto deep, globechafing rage."

            reader "How dare he do this to your mind? To your friends’ lives? What was so important that one white orb asshole had to fuck with the destinies of everyone you’ve grown to care about?"

            reader "There are answers out there, and you deserve them. And so, you demand them."

            s "Adorable."

            show reader gross at nod
            reader "Yikes. You shift on the chaise lounge so as to better hide your famous legs from this creepy round fucker."

            s annoyed "Oh, calm down."
            s "All of you and your adherence to societal expectations and archetypes."
            s "Perhaps one day you could just learn to take a compliment. Besides, I was being condescending."
            s "So you demand answers."

            show scratch sigh at sigh
            reader "He sighs theatrically. You aren’t sure where the noise is coming from. He doesn’t have a mouth. How is he even talking? How the fuck does anything work at all?"

            show reader determined
            s "I knew you would, but I find explaining myself incredibly tedious."
            s sarcastic "Suffice it to say, I am a man with many boards and fields of play, and although there are countless ways to move the players around those boards, some are doubtlessly more entertaining than others."
            show reader angry
            s "You were simply one pawn among many."
            s "I won’t bore you with the details. Doubtless you are aware of the greater contextual framework of this story."

            show reader at bounce
            reader "The hell you are! You aren’t aware of jack shit. Your head is full of question marks!"

            s toself "Oh, of course. How thoughtless of me. See, yet another unfortunate side effect of the limitless conversing with the narratively limited."

            show scratch annoyed at nod
            reader "He taps a thumb and forefinger to his orb."

            s neutral "Perhaps it would suit you better to understand gradually."
            s "And when I say gradually, please understand that I mean it. You won’t be leaving."
            s "But, yes, I do believe this will clarify some things for you."
            show scratch at offscreenleft with ease
            show scratch gesturing at offscreenflipped
            show scratch at left1280 with ease
            s "This way, please."

            reader "He opens a door and gestures inside. There’s light coming from in there, but it still gives off the vibe of a dark closet door in an unfamiliar bedroom at 3 am. You’re afraid, yeah, but you want to understand even more."

            reader "{size=25}You stand up and take a step, conscious of the movement of the muscles in your legs. With the rosy sheen of your friendship hypnosis or whatever the fuck he did to you gone, the sensation of moving your own body feels heightened. Important. Yours.{/size}"

            reader "There’s probably a version of you that would try to turn him down, or that would fight or run or take a nap on this surprisingly comfortable piece of antique furniture."

            reader "You even consider rushing back to say goodbye to somebody, anybody, at least, but you know there isn’t time to click through all that bullshit."

            reader "Those tributaries flicker in your mental periphery, so tangible you can almost see yourself choosing one, but you pull your focus back to your present and look him right in the orb."

            reader "{size=25}You just have to trust they’ll remember you, because the you you’ve become after this journey, after all this friendship and growth and death and time-- that you needs to understand. You owe it to your friends, but even more, you owe it to yourself.{/size}"

            reader "You’ve found your river, and you’re going to see where it leads."

            hide scratch with moveoutleft
            hide reader with moveoutleft
            reader "So you follow him."

            show blackcover with dissolve
            show scratch gesturing behind blackcover at flipped
            show scratch at right1280
            show computer behind scratch
            hide blackcover with dissolve


            s "Sit here, please."
            s "In the interest of expediency, I will leave you to your own devices while I go deal with an expected but entirely unwanted guest."
            s "It shouldn’t be too hard to parse out the truth on your own."
            s "All you need to do is read a brief webcomic."


            play music "music/victory_jingle.mp3" fadeout 1.0 noloop
            scene bg black with fade
            $ achievement.grant("ACH_FINALE")
            $ achievement.sync()
            $ webbrowser.open("http://www.homestuck.com/001901")

            return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
