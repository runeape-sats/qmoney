# Transcript: Artur Ekert — Bell Inequalities: From Curiosity to Security

Source video: https://www.youtube.com/watch?v=Fbcfx_vZyG0  
Title: OSP2025 | Artur Ekert | Bell Inequalities: From Curiosity to Security | Okinawa School in Physics  
Channel: Okinawa Institute of Science and Technology (OIST)  
Duration: 1:42:28  
Transcript source: YouTube transcript fetched locally with `youtube-transcript-api` on 2026-05-04.  
Video ID: Fbcfx_vZyG0

> Note: This is an automatically generated transcript. It preserves timestamps and wording closely enough for research triage, but it has not been fully human-corrected.

## Timestamped transcript

```text
0:10 So yesterday my it was a sort of like a
0:13 a random walk through um the um
0:19 well just a little bit of everything,
0:20 right? A little bit of a history of
0:22 randomness. My sort of like a narrative
0:24 line was uh to take you from randomness
0:27 to quantum and give some kind of a broad
0:31 landscape of uh quantum information
0:34 science, quantum computing mostly how we
0:38 go from
0:39 um describing randomness in terms of
0:42 probability theory colog approach and
0:45 how uh quantum enters this and how we
0:48 use complex numbers and you know I'm
0:51 managed to throw in some interesting
0:54 characters like Girro Lammo, Cardano and
0:56 others. Right. So the today I'm I'm
1:00 going to still use slides and um and
1:04 it's still going to be kind of a fun
1:06 lecture rather than anything uh where we
1:10 just go into the equation subscript and
1:13 superscript level. Um so it's it's going
1:17 to be a story about
1:20 today I'm going to stress more
1:21 communication aspect. So yesterday was
1:23 mostly about computation. How should we
1:26 sort of have a broad view of of quantum
1:29 computing and today is is sort of going
1:31 in the direction of crypto. So I would
1:34 like to tell you a story how
1:37 investigations of um
1:41 foundations of quantum physics sort of
1:43 nicely merged with the with people
1:46 interested in security. So it'll be a
1:48 little bit of a history and uh I hope
1:52 you know I hope it's going to be again
1:54 fun to look at. So the I will start with
1:58 a I'll give you sort of like the outline
2:01 of um
2:03 people's
2:05 desire to set up perfect cryptographic
2:08 system how to communicate with perfect
2:10 security how people did it over the time
2:12 what were the main trends and then we'll
2:15 talk about you know of course the the
2:18 key problem the key distribution thing
2:20 and then how quantum physics comes to
2:22 rescue and uh and few other ideas there.
2:26 So essentially as I said there's going
2:28 to be two narratives here. One was
2:30 curiositydriven research. So that was
2:33 when people uh tried to understand what
2:37 really this new physical theory quantum
2:39 theory that was you know as we know was
2:42 cooked up about 100 years ago. What is
2:45 it really about? What are the
2:47 implications? Is it a in particular one
2:50 one thing that dominated discussion at
2:53 the time was is it complete and that was
2:56 Einstein think is it like is it really
3:00 the the real thing or is it the first
3:02 approximation to something deeper and
3:04 more profound so the therefore Einstein
3:06 worry about the completeness of quantum
3:08 theory and then we have the whole
3:09 narrative of people trying to understand
3:12 this will take us later to John Bell who
3:15 who kind of tried to answer this
3:17 question in terms of more in in sort of
3:20 more um
3:23 uh concrete way sort of trying to
3:25 propose experiment where this can happen
3:28 and then it will go to experiments and
3:29 as you know that resulted in Nobel prize
3:32 in 2022. So there was a one line of
3:35 research but that surprisingly emerged
3:39 with another line of research completely
3:42 different at the very beginning when
3:44 people were interested in the notion of
3:45 security. So we can go to ancient Greeks
3:48 and talk about how people wanted to
3:50 protect information then and then how
3:52 people uh moved on and with the
3:55 sophisticated technology people still
3:57 trying to protect information because it
3:59 was of value and you know like 50 years
4:04 ago or earlier than than that it was
4:07 just it was just completely two
4:09 different fields. there was just no
4:12 overlap whatsoever between people
4:14 working on the foundations of quantum
4:16 theory and people working on
4:17 cryptography. And then those things
4:19 changed slowly. So one development was
4:22 Steven Visner who came up with the idea
4:25 of conjugate coding. Then Charlie
4:27 Bennett and Jil Brasard um had idea how
4:30 to use this uncertainty principle to
4:33 encode information in such a way that it
4:36 may be used for the key distribution.
4:38 And then in my work on the bell
4:40 inequality and quantum crypto sort of
4:44 managed to bring the two branches
4:46 together. And then then sort of they
4:49 started feeding each other in a very
4:51 nice way that um for example people
4:54 working on the bell inequality side had
4:57 to now look into a certain problems like
4:59 for example certain loopholes which were
5:03 optional when when you talk about nature
5:05 but not so optional when you take
5:07 adversarial scenario and think oh okay
5:09 we are not talking about how nature
5:11 behaves but maybe we are talking about
5:12 how your adversary behaves. So so this
5:15 we will talk a little bit. So this is
5:17 like the the overview of what's going to
5:20 come in the next hour and a half or so.
5:24 So I I think if it is okay with you, I
5:26 will just go maybe for one one hour
5:29 class without
5:32 break unless you want me to just do 45
5:34 plus something
5:37 but maybe it's easier just if we just
5:40 have one hour plus. We'll see how it
5:42 goes.
5:44 Okay. So let me start with a brief
5:47 overview of uh crypto how people uh
5:53 encrypted and protected information that
5:55 uh many many years ago. So essentially
6:00 um when you look at the origin of
6:02 cryptography we more or less go to the
6:06 origin of human writing and the way
6:08 people started using symbols to
6:10 communicate with each other. So when you
6:12 have a finite set of symbols and I
6:14 stress finite because here we are in
6:17 Asia where you have a slightly different
6:20 way or different set of symbols to
6:23 communicate. So it's a uh but but when
6:26 you sort of stick to say 35 the Roman
6:29 alphabet or Greek alphabet or whatever
6:31 Phoians sort of came up with a finite
6:34 set of symbols used to communicate
6:38 messages then it's very easy to play
6:41 with those symbols to distort those
6:43 messages to protect them. So what you
6:45 can do, you can permute characters in
6:47 your message, right? So you just place
6:49 the symbols in a different location or
6:51 you can also do the substitution. You
6:53 can take one symbol and substitute
6:54 another symbol for that symbol. So so
6:57 that is the the two techniques
6:59 permutation and substitutions
7:02 were used as early as you know 400 BC
7:08 or in the early days of the Roman
7:10 Republic.
7:12 Well, Julian Caesar took it from the
7:14 republic to the Roman Empire.
7:17 Um so so
7:19 we have those two things and it's
7:21 interesting to there's still among
7:23 historians of science there's
7:24 interesting debate why was it that uh
7:29 for example the Chinese didn't develop
7:31 such a system uh earlier but most likely
7:35 it is related to the fact that the
7:38 number of the Chinese character was huge
7:40 and to come up with a method for
7:41 substitution and permutation was
7:43 difficult so the Asian Chinese
7:46 cryptography relied mostly on
7:49 well actually
7:52 there wasn't as such but relied mostly
7:54 on on protecting information relied on
7:57 hiding messages in some clever
7:59 mechanical devices rather than playing
8:02 with those characters.
8:05 So the first device we know that was
8:08 used for cryptographic purposes and it
8:11 was used in ancient Greece in Sparta was
8:14 called skittley. So skittleily was a
8:17 wooden button of a certain diameter
8:20 and then you have two guys. You have two
8:23 military commander and they would have
8:25 wooden buttons of the same diameter. So
8:28 if you want to send a message from if
8:30 one commander military commander wants
8:32 to send a message to the other one would
8:34 take a strip of parchment just wrap it
8:38 around this wooden button and then you
8:40 write your message lengthwise. So say
8:43 attack tomorrow and then you unwrap it.
8:46 So when you unwrap it, it's just you
8:49 know the the the location of the letters
8:52 is somewhat different modular the
8:54 rotation of those letters but um but you
8:58 know letter A is letter A letter T is
9:00 still letter T but the placement is
9:02 different and you give this parchment to
9:05 a courier that takes it to a military
9:07 commander at some other location. So the
9:10 other guy gets the parchments, takes a
9:12 wooden button that is of the same
9:14 diameter as the other one, wrap it
9:16 around and the message would reappear.
9:19 So that's the first example of a first
9:22 historical record that we have of using
9:25 um mechanical devices, simplistic
9:29 devices like this for secure
9:31 communication. So that was about 400 BC.
9:36 um another method that allegedly was
9:39 used by Julius Caesar. So it's we are
9:41 talking about 50 BC here was used was
9:45 based on substitution. So you take your
9:49 your alphabet so letters from the
9:51 alphabet say Roman alphabet and you
9:54 shift the whole alphabet by say three
9:57 characters to the left. So a, b and c
10:00 are sticking out here as you can see and
10:02 you append them to the end of this
10:04 alphabet. So then you have a
10:06 substitution rule which essentially says
10:10 let's see whether this works here which
10:12 says for a substitute d for b substitute
10:15 e for c substitute f and so on so forth.
10:18 So you take the same message that we saw
10:20 before attack tomorrow and now we are
10:24 not replacing the we are not sort of
10:27 shifting the placement of the characters
10:28 but what we are doing here we are
10:31 replacing one character with another
10:33 character. So that's a very very simple
10:35 substitution method apparently was used
10:37 by Julius Caesar um to communicate with
10:40 his military commander.
10:44 So the the two methods that you saw well
10:48 not so much different. You may say that
10:50 all they all rely on sort of like taking
10:53 a mapping from if you look at the
10:55 substitution. So substitution in a way
10:58 is a permutation as a map, right? So you
11:00 take the whole alphabet and you map it.
11:03 It's a onetoone mapping to to the
11:06 alphabet. And the the sort of shifting
11:09 the whole by three characters is a very
11:11 simple one. Um but there could be many
11:14 many of them. Um but of course you know
11:17 if you have to agree on the rule uh what
11:20 kind of substitution we are going to use
11:23 then it's good to take a simple one so
11:25 that you can explain to military
11:27 commander I'm going to communicate with
11:29 you using substitution cipher and the
11:32 rule is shift all the characters by say
11:35 three or five or 42 oh maybe not 42
11:38 because I'm not
11:41 um but then but the number of
11:44 substitution nonetheless is huge
11:46 And it's interesting that um
11:50 it took people a while to have a
11:53 systematic method of breaking this. And
11:55 to the best of our knowledge, the first
11:57 person who managed to crack substitution
12:00 ciphers uh was a philosopher of the
12:04 Arabs, a guy by the name of Al Kindi who
12:06 lived in the 9th century in what is
12:08 today Baghdad essentially. But this was
12:11 sort of like the Persian and Arabic
12:13 golden age of science. And so he was one
12:16 of those who belong to this house of
12:18 wisdom and so forth. So he was the one
12:21 that figured out that something that is
12:25 almost obvious to us, right? that a
12:27 natural language is not
12:30 be it written or spoken but but a
12:32 natural language is not a random set of
12:35 characters that characters appear with a
12:37 certain natural frequencies in any
12:39 single language.
12:41 So if you take English for example you
12:44 can see here the frequency chart of
12:47 English language here. So if you take a
12:50 text, a typical text in English and look
12:54 how often a given letter appears. So
12:57 it's not that they appear with the same
12:59 frequency. So you'll find that the
13:00 letter E is the most frequent one in
13:03 most Indo-Uropean languages. In fact, uh
13:06 the letter E is the most uh common one.
13:09 And then certain pairs of letters appear
13:12 quite frequently. So in English, th is a
13:14 common combination. Right? So a simple
13:17 statistical analysis is enough to break
13:20 substitution cipher. So if if you given
13:23 a piece of text, right? And you look and
13:25 you know that it was encrypted so to
13:28 speak with a substitution cipher. So
13:29 there was a one to one substitution. So
13:31 what you do, you look for the most
13:33 frequent character. You find the most
13:35 frequent character. Most likely it's the
13:37 letter E. So you try it's the letter E.
13:40 And then you look for the second most
13:41 frequent character and the the pairs of
13:44 letters and sensors and you know the
13:47 language is very redundant. So you see
13:49 the message sort of almost popping up
13:51 immediately. You can fill the gaps very
13:53 easily later.
13:56 So that is when you lose a when you use
14:00 a typical um set of text and messages.
14:04 But what is interesting as a sort of a
14:06 side remark I couldn't help just to give
14:09 you this example. I always find it
14:10 amusing. Some writers
14:14 um are very proud of the skills of the
14:17 command of language, right? And then
14:18 they there is a genre that is called
14:21 lipograms. Leoggrams are pieces of text
14:25 where you distort this frequency on
14:27 purpose.
14:28 So for example, if you read this first
14:32 paragraph, it's written without the
14:34 letter E, the most frequent character in
14:36 English.
14:38 And the the ma the most famous lipogram
14:42 in the history is uh is was written by
14:44 the French guy George Perk. Um in as it
14:49 happens in French the letter E is also
14:51 the most frequent one. And so he managed
14:54 to write the whole book called Laarion
14:58 without the letter E. And it's you know
15:01 it's 85,000 words. Really amazing. So
15:06 you can just read this book and you it's
15:08 mindboggling. And what is even more
15:10 mind-boggling that it was translated to
15:12 English and was also translated in a way
15:15 that avoid the letter E.
15:18 Of course, George Pere shouldn't put his
15:21 name on the book.
15:24 Um, and then there was a a weird German
15:27 guy, a poet who hated he had obsessive
15:30 dislike for the letter R. Not only he
15:34 was writing his poetry without the
15:36 letter but for something. So he wrote
15:39 130 poems in German without the letter
15:41 but he also tried to avoid it from the
15:44 daily conversation. So you can imagine
15:50 so the today of course except lipograms
15:55 when we talk about onetoone substitution
15:58 it's quite clear that um they kind of
16:01 simplistic right. So simple frequency
16:04 analysis and and and you're done. So
16:06 onetoone substitution
16:08 is a very is is not even considered
16:11 today as an encryption. It just change
16:14 of the alphabet. You just take something
16:17 and you substitute something else for
16:19 it.
16:21 So the it was recognized
16:24 not you know after alkindi or
16:28 people realized that one to one is not
16:30 the way to go. So the next step in the
16:33 history of encryption was one to many
16:36 right so if one to one doesn't work so
16:38 they they called monoalphabetic cipher
16:41 that where you have one to one
16:42 substitution for one alphabet another
16:44 alphabet here you have a polyalphabetic
16:48 cipher so that means one alphabet and
16:50 you try to make different substitution
16:53 as you go on in your encryption.
16:56 So that came and again you know
16:58 historians if you were to believe
17:00 historians they have all kind of
17:02 different answers who did it first it's
17:05 not entirely clear the idea popped up
17:07 somewhere in 15th century or so at the
17:11 end of the 15th century early 16th
17:13 century in Europe um somewhere in Italy
17:16 renaissance was the time there were lots
17:18 of intrigues and plots and all kind of
17:20 things so that uh one person who is
17:24 attributed to um with with inventing
17:28 those polyalphabetic cipher is Lon
17:31 Batista Alberti. He you may know him as
17:34 a famous architect and
17:36 true Renaissance guy, but other
17:39 contenders are Johannes Treatius and
17:42 Bless Deigner. Um anyway, let's take
17:46 Alberti. Alberti at least is credited
17:49 with coming up with another mechanical
17:51 device that was uh supposed to
17:54 revolutionize the whole
17:57 cryptography later on. So he came up
17:59 with what is called Albert's disc.
18:03 So that disc which you can see here is
18:07 um so you have actually two concentric
18:09 discs and on the parameter of the disk
18:13 you write the alphabet the letters from
18:15 the alphabet on the inner and the outer
18:18 disc and the relative rotation of the
18:20 two disk gives you the substitution
18:22 rule. So that's a simple shift, right?
18:25 So you can shift it by three, four,
18:27 five, whatever.
18:29 And then as you go along, so for you
18:32 then for example, if you want to encrypt
18:34 the message, you can use a sequence of
18:38 substitutions. So you can c suddenly for
18:40 example I want to send a message to
18:41 Bill. I can agree with him that you know
18:44 I use encryption
18:46 um in which I will encrypt with a
18:50 sequence of substitutions which I define
18:52 as 71419.
18:54 So I shift the alphabet
18:57 by seven characters for the first
18:59 letter. I shift then I use another
19:02 substitution. I shift the alphabet by 14
19:05 characters for the second letter. And
19:08 then I shift it by 19 characters for the
19:11 third letter. For the fourth letter, I
19:14 go back to the first substitution.
19:15 That's seven, 14, 19. And I keep on
19:18 repeating. So every third letter is
19:22 encrypted with the same shift. Right? So
19:26 what I need to communicate to Bill is of
19:28 course this sequence. I said 71419.
19:32 And Bill remembers this and this is our
19:34 cryptographic key so to speak. So he
19:37 knows how to decrypt and Albert's disk.
19:41 Of course you can do it without Alberti
19:42 disk but it was a useful device where
19:44 you do all those shifts and you simply
19:46 just write your um your cipher. So this
19:51 this had some advantage that sometimes
19:54 you know the like in monoalphabetic
19:57 ciphers the reason why it's very easy to
19:59 use statistical analysis that the
20:01 mapping of a given letter
20:04 so a given letter is always substituted
20:07 by the same character. So for example if
20:09 you have the letter L in monoalphabetic
20:12 science there will be always something
20:15 and will not change whether here with
20:18 this kind of substitution um if you have
20:21 a plain text cell you have two letters L
20:24 next to each other they will be mapped
20:26 into different characters. So that makes
20:28 the whole statistical analysis much more
20:31 difficult
20:32 but not you know again if it is a short
20:38 key. It is just only if you use only
20:40 three substitute three substitutions
20:42 then then it's it's not that difficult
20:44 to break it and the person who is
20:47 credited with breaking polyphabetic
20:49 ciphers Charles Babage you know again a
20:52 very interesting character um from the
20:56 you know the
20:58 in the early 19th century he managed to
21:00 work out among many other things he was
21:03 working as you probably know on the
21:04 first analytical engine the sort of he
21:07 was a pioneer of computing but he was
21:09 also interested in in breaking ciphers.
21:13 So as you can see it actually took
21:15 people a while to break polyalphabetic
21:17 ciphers in in systematic way few
21:20 centuries right
21:22 and then
21:24 the the concept of alberti disc actually
21:28 picked up and when when
21:32 we had sort of more complicated
21:34 electromechanical machines the albert's
21:37 disc was sort of put together and evolve
21:40 into a rotor so you have a several
21:43 Albert's disc on one road and then you
21:46 can implement more and more and more
21:48 complicated poly alphabetic ciphers.
21:51 So the more sort of substitutions you
21:53 have uh the more difficult is to break
21:56 it. And uh as probably most of you know
22:00 the story the the most famous machine
22:03 probably of this type uh was designed by
22:06 a Dutch engineer Arthur Shrius. It was
22:09 called Enigma. And Enigma was used
22:12 during World War II. And what was
22:16 another spectacular thing? It was simply
22:19 broken by Polish cryptologists
22:22 led by Marian Ryski
22:25 who shortly before the outbreak of World
22:27 War II, the Poles managed to read
22:30 essentially all German uh communication.
22:33 it didn't help them that much to be uh
22:37 the you know at the end of the day and
22:40 but but the the work that started in
22:42 Poland continued in the United Kingdom
22:44 and Bletchley with some further
22:46 development and that was actually quite
22:48 essential for um finishing or sort of
22:52 like winning the war on the allied side.
22:55 So that the poles who broke Enigma are
22:58 sort of one of those who managed. It was
23:01 it was a very spectacular
23:05 way of implementing um
23:09 applying some ideas from permutation
23:11 from the group theory to to break those
23:13 ciphers. So it's it's very nice. I I
23:16 usually like when I give lectures to
23:18 illustrate in group theory. It's very
23:20 nice to illustrate with the way
23:23 Ryfki in particular but also the two
23:25 other guys managed to they were they
23:28 were just mathematicians right so then
23:30 they they use all those tools they had
23:32 to break to break enigma and it's a
23:34 beautiful illustration how mathematics
23:36 can actually help in real situation so
23:39 when you see this evolution right when
23:42 we when we go from skittley to Alberti
23:45 disk to enigma the moral of the story is
23:49 okay. There are many clever inventions
23:51 like monoalphabetic ciphers,
23:53 polyalphabetic ciphers. Then you have
23:57 enigma that is like super polyalphabetic
24:00 cipher. But every single time there's a
24:03 ingenious device or ingenious method for
24:06 encryption, there's ingenious method for
24:09 breaking the cipher. So the question is,
24:12 is there a way to design something that
24:14 cannot be broken?
24:16 So that was like the problem in crypto
24:19 right and the answer is actually yes
24:23 the the so if you take the poly
24:25 alphabetic cipher to the limit so for
24:28 for each character you have a different
24:30 substitution so that's the limit so then
24:33 you end up with something that is called
24:35 a one-time pad and one time pad probably
24:38 the easiest way to explain it is is
24:40 maybe not as a limit for polyalphabetic
24:42 cipher but as as sort of a simple
24:46 encryption of binary sequences. So you
24:49 take a message that you have, you use
24:51 ASKI code or whatever, turn it into a
24:53 binary. So we changed the alphabet,
24:56 write your message in binary and then we
25:00 have those two characters, our two uh
25:04 protagonist in in in quantum information
25:08 for sure in in quantum cryptography in
25:10 particular we have Alice and Bob usually
25:12 two good guys who want to communicate
25:15 and they have some secrets to share
25:19 and in order to do that they're going to
25:20 use one-time pad and one-time pad relies
25:23 on the fact that Alice and Bob met and
25:27 managed to establish a random sequence
25:30 of zeros and one which is identical. So
25:33 they have identical they share identical
25:35 truly random and secret sequence of
25:37 zeros and one and that's called a
25:39 cryptographic key. So that's written in
25:43 red characters here. So then um they go
25:47 into two distant locations and whenever
25:49 they want to whenever one of them say
25:52 Alice wants to send a message to the dog
25:53 well what she can do she can take the
25:56 message write it in binary and do bit by
26:00 bit addition to the key right so the the
26:03 bitby-bit addition is just like a
26:05 regular addition apart from fact that 1
26:08 + 1 becomes zero
26:11 so then by adding so you can see it on
26:15 this side. So one time P you take the
26:17 message take the key generate the
26:19 cryptogram. So the cryptogram because
26:22 the key is truly random like if it is
26:24 randomly generated the message is not
26:27 the message has a natural the pattern of
26:29 a natural language we know that right?
26:31 So now you add those two and the
26:34 randomness from the key is translated to
26:37 the cryptogram. So the cryptogram is
26:39 truly random. If the key is random, this
26:42 randomness sort of transfers to the
26:44 cryptogram. So the cryptogram if you
26:46 look at it then doesn't have any pattern
26:49 because it it inherited randomness from
26:51 the key. So then you send this message
26:54 over any unprotected channel and
26:56 frequency analysis and statistical
26:59 analysis doesn't work because the any
27:02 pattern natural pattern from a natural
27:05 language is completely wiped out at this
27:07 point. So you have just a a random
27:09 string of characters unless you have the
27:13 key. So Bob is here. The cryptogram
27:15 arrives. Bob takes the key and he's
27:19 substracting this randomness from
27:21 cryptogram and recovering the message
27:23 with the same binary addition. So this
27:26 scheme here uh which was proposed in the
27:31 30s and 20s
27:33 um was shown to be absolutely secure
27:39 um as long as certain conditions are
27:41 satisfied. So the conditions are that
27:44 the key is truly random
27:48 is truly secret. So it's only known to
27:50 Alice and Bob. It's as long as the
27:53 message. So you you you cannot just use
27:57 part of the key and reuse it again. And
27:59 the key is never used again. So you only
28:02 use it once. So that's why it's called
28:03 one time path. You use it once, it's
28:06 gone, right?
28:08 If you start using it again, so you're
28:11 going into sort of like a polyalphabetic
28:13 cipher regime where things are not
28:16 entirely secure. In fact, there are
28:18 there are very good example in the
28:20 history of cryptologology where in
28:24 particular the Russians after the war
28:26 and the the Soviets tried to uh they
28:30 they had some issues with the they use
28:33 one time pad and they reuse the keys in
28:35 in several occasions and American
28:37 exploited this. So there was there was a
28:40 whole program called venoma that managed
28:43 to decrypt one time the so-called
28:46 one-time path where certain assumptions
28:48 regarding the key managements were not
28:50 satisfied. But anyway so so Shalon
28:53 managed to prove in the in the 1930s
28:56 that this kind of system is absolutely
28:58 secure. There is a perfect cipher. You
29:00 cannot break it as long as those
29:02 assumptions are satisfied. So what's the
29:04 problem? So you know what the problem
29:06 is? The problem is that
29:10 somehow we made this assumption that
29:12 Alice and Bob have the key and this one
29:16 time path. We also said we use it we use
29:19 it once the key is gone. We cannot reuse
29:22 the key again. So there's a need for the
29:25 key distribution. So here we come to
29:28 crypto. The big problem is okay fine we
29:31 can solve the we can have a perfect
29:35 cipher as as long as we can solve the
29:37 key distribution problem
29:40 and um so what kind of
29:44 solutions do we have today to the key
29:46 distribution problem so one come under
29:51 um the label public key crypto systems
29:54 I'm not going to talk about it's a
29:56 fascinating as a topic from
29:59 the series of lectures I would say. But
30:01 the idea that mathematicians came up in
30:04 the in the 1970s or so was that
30:10 maybe we can avoid the key distribution
30:12 as long as we can somehow introduce two
30:15 keys. one of them is public, one of them
30:17 is private and base the whole security
30:21 not on what they call information
30:23 security where there's not enough
30:24 information to break this the system but
30:27 on computational complexity. I talked
30:29 about computational complexity
30:31 yesterday. So the fact that there are
30:34 certain mathematical problems
30:36 that relate to the two keys and
30:40 essentially
30:42 the the the security there relies on the
30:45 difficulty of performing certain
30:47 computational tasks. So the public key
30:50 crypto systems um
30:54 is is not really a way of fixing the key
30:57 distribution problem but it's sort of
30:58 like avoiding this in a very elegant
31:00 mathematical way. It's not known to be
31:04 it's not provably secure because many of
31:07 those results in uh as we talked
31:10 yesterday in in computational complexity
31:13 cannot be or we don't we don't have any
31:16 proofs that certain assumptions that
31:17 there are certain complexity classes and
31:19 there are certain relations between
31:20 those complexity classes
31:23 but nonetheless they work and but but
31:26 but but still we know that some of them
31:30 uh may not work in when we have quantum
31:33 technologies. So because of again those
31:35 complexity classes for example if you
31:37 take factory it's difficult for
31:40 classical computers but it's not
31:42 difficult for quantum computers. So it
31:44 belongs to this class BQP that we talked
31:47 about yesterday and therefore once we
31:49 have a quantum computer of um of
31:53 sufficient computational power we will
31:55 be able to break those ciphers.
31:58 So then then we have some issues with
32:01 public key crypto systems and therefore
32:03 today um there is an effort to establish
32:08 a set of new public key crypto system
32:12 going beyond RSA going beyond those who
32:15 that depend in their security on on say
32:19 factoring or discrete log and looking
32:21 for another mathematical problems which
32:24 are difficult even for quantum
32:26 computers. So the idea is okay maybe we
32:32 it will take some time to build quantum
32:34 computers but let's be prepared and
32:36 let's use conventional classical
32:39 methods but make those methods resilient
32:42 to quantum attacks in the future. It's
32:45 very difficult to do that. In fact you
32:46 know there is an American now Americans
32:49 establish a certain set of standards. Um
32:52 there are certain mathematical problems
32:55 based on vectors on latises and so on so
32:58 forth. We will not go into this but it's
33:00 possible but to prove security is
33:03 extremely difficult and it's not
33:04 entirely clear whether those that were
33:07 proposed will will be secure in years to
33:10 come. But certainly they have an
33:12 enormous advantage that they're very
33:14 flexible in zillions of applications and
33:17 and we can implement them essentially
33:20 now without even quantum technology
33:22 hoping that they will be resilient to
33:24 quantum technologies in the future. So
33:27 that's that's sort of one way to avoid
33:29 key distribution problem. The other way
33:31 is to fix it trying to fix it. And this
33:33 is actually what quantum crypto is
33:35 trying to do. So quantum cryptography
33:38 basically says well um we find a way of
33:43 distributing the key and uh and that
33:47 that that way works even if we have
33:50 quantum computers. So so quantum crypto
33:53 is secure even against quantum attack.
33:56 The problem here is of course that
33:58 requires quantum technology and may not
34:01 be good for all computational task.
34:03 there's a variety the whole spectrum of
34:06 uh cryptographic or information
34:09 protection scenarios. So usually quantum
34:11 crypto is used for pointto-point
34:13 communication but uh a few others as
34:16 well but certainly is not as flexible as
34:19 something that we can do with public key
34:21 crypto systems but nonetheless this is
34:24 what we are going to talk about.
34:27 Um so every now and then um I drop some
34:31 topics so I decided to insert the slide
34:33 for you saying okay it's your homework
34:35 you know I'm not going to talk about it
34:37 but it's interesting so take a look at
34:39 this so I encourage you to look at
34:41 public key crypto system RSA elliptic
34:43 curves and latis base latis base are
34:46 interested
34:47 interesting because um
34:50 because they are proposed as sort of a
34:55 new generation of cryptographics systems
34:57 that's supposed to be resilience against
35:00 quantum mech and it's a growing
35:02 controversy you know that uh shortly
35:05 after Peter Shaw published his uh paper
35:08 on quantum factoring I think maybe two
35:12 or three years later I don't remember he
35:15 had another paper where he claimed that
35:17 the latisbased crypto is not secure so
35:20 there was a an attack on latis base that
35:23 paper all like rev showed is not correct
35:27 was withdrawn. But then there were few
35:29 other papers and even you know last year
35:32 there was a very interesting paper from
35:35 our Chinese colleagues showing that um
35:38 latisbased crypto can be broken on a
35:41 quantum computer. Again it it took but
35:44 you know it took all community all over
35:46 the world about three months to figure
35:48 out where is the mistake. there was a
35:50 mistake so it doesn't work but but it's
35:53 it's sort of like makes you if you into
35:56 this if you you know if you entered this
35:59 business would you put your money on
36:01 latisbased crypto if you every now and
36:03 then you you see how close it is and
36:06 it's coming closer and closer to come up
36:08 with a quantum algorithm may eventually
36:10 break latisbased crypto um so it's
36:13 interesting to see this and and I don't
36:15 know whether latisbased crypto will
36:18 survive for a long time yes
36:29 They can
36:30 >> they can fix that
36:35 >> the the Chinese
36:38 >> Wow. I wish them good luck. That would
36:40 be a breakthrough.
36:43 I don't think
36:48 >> well I I you know I haven't I
36:52 communicated with that person from
36:54 Sinhoa who came up with this algorithm.
36:57 He was a young guy you know just he came
37:00 up with a very nice paper that took us
37:03 about three months to figure out the
37:05 mistake. Tom Vidig was the first one who
37:07 actually pointed out what the mistake
37:09 was. Um but uh and then it's interesting
37:12 that uh I like this this this young
37:15 researcher because you know he was very
37:19 unhappy that this mistake was found but
37:21 he was also very honest about it. He he
37:23 he posted on the website that you know
37:26 there is a problem here and uh and then
37:29 I said well look you should talk about
37:31 this algorithm anyway because it doesn't
37:33 matter that it's doesn't work. It just
37:36 shows that you know you use a set of
37:38 interesting techniques and tools and
37:40 maybe eventually it will something will
37:42 come up. But he went into sort of like
37:45 um um
37:49 yeah he he decided to disconnect from
37:51 for a while and work hard on fixing this
37:54 problem. So if he fixed that would be
37:57 great but I think that will be a real
37:59 breakthrough. So it requires certain
38:00 degree of scrutiny.
38:06 Say again. Sorry.
38:12 >> I don't know. I haven't yet.
38:14 >> Oh, the you say the Danish guy. Yeah,
38:16 the the
38:18 well that's he's he's a very serious and
38:21 well established cryptologologist.
38:23 Okay. Well, look guys. So, there's
38:25 something else to look at. You know,
38:26 look at look and find a mistake. Okay.
38:29 That's the homework for you.
38:34 So by the end of the school, you'll be
38:36 judged on your on your progress.
38:40 >> So Arthur, you want him to do it in an
38:42 afternoon or in two days and it took you
38:45 three months?
38:46 >> Yeah. Well, that's that's you know, it
38:48 took me sort of like it was not even it
38:51 probably would took me longer. Tom Vidig
38:52 was the one who founded in three months,
38:54 right? But now there's a new one coming
38:57 up. So this Ivan is he's well you know
39:02 very accomplished well established
39:04 Danish cryptologist so he says so should
39:07 be taken very seriously but okay if
39:09 latis crypto is dead I'm I don't mind
39:12 you most
39:15 um
39:17 oh anyway so they this area is known
39:20 sometimes as a I don't like this name
39:22 but it's called postquantum crypto I
39:25 don't know why so the the area where uh
39:28 you use current mathematical
39:32 techniques to defend yourself against
39:35 quantum attack. It's probably quantum
39:37 resilient would be more appropriate but
39:38 never mind. So this postquantum
39:41 managed to stick and um so there are
39:44 many interesting papers that um in in
39:48 this field and you know to what extent
39:51 that people can really come up with
39:53 quantum resilient thing is an open
39:55 question.
39:58 So the going back to the key
40:00 distribution. So when we have this
40:02 simple one-time path scenario
40:05 the
40:09 the key is is you know it's the key
40:13 distribution problem is not that the
40:16 computer scientists do not have a set of
40:19 tools to do something about it. So for
40:21 example, one thing is
40:24 as long as you can establish
40:27 how much any third party like an
40:30 eavesdropper Eve can know about the key,
40:34 computer scientists actually have a good
40:36 set of tools to extract the secret key.
40:40 So if I somehow know that Bill knows a
40:44 fraction of my key and I know how many
40:47 bits roughly or at least I can put a
40:49 bound on it then I can extract a shorter
40:52 key that Bills knows nothing about.
40:57 So
40:59 uh but the problem is that finding how
41:02 much Bill may know is is difficult for
41:05 me because he you know he's a clever guy
41:08 and he has all kind of um clever tools
41:11 to his disposal. So how do I know how
41:14 much he learned during the key
41:17 distribution that I had with my friend?
41:18 So Bill was listening very carefully and
41:21 um I really don't know what is the
41:23 signature of Bill's eavesdropping in my
41:25 data. So that's a very difficult thing
41:28 to establish. In fact, it's impossible.
41:30 However, um once
41:35 once you sort of know the the bound
41:38 there are those randomness extractors,
41:40 there's a privacy amplification that is
41:42 a set of tools that I can use. So just
41:44 to give you example how it works. So
41:46 suppose um uh so suppose
41:52 I have the key of two bits. So just take
41:55 a very simplistic case. I have two bits.
41:58 Call them X1 and X2.
42:00 And I know that somehow Bill managed to
42:03 learn one bit. But I don't know whether
42:06 it's X1 or X2. And maybe he knows some
42:09 you know I don't know which one.
42:13 But but I know that it's not more than
42:15 one bit. For some reason I I learned
42:17 somehow I managed to figure this out. So
42:20 one thing I can do I can do the binary
42:23 addition. I can add X1 to X2
42:28 and get one bit. But I know that this
42:31 one bit is secret that Bill doesn't know
42:33 this bit because he knows at most one
42:36 bit X1 or X2. So he certainly doesn't
42:38 know for him one of them is completely
42:40 random. And by doing this binary
42:43 addition I get just one bit that looks
42:45 random to him. So this is a way that you
42:48 know I had partially secure binary
42:50 string in this case of length two and by
42:55 binary addition I managed to generate a
42:58 shortage in this case one bit binary
43:01 string but I know that it's entirely
43:03 secret. So you can extend this kind of
43:06 idea in a slightly more sophisticated
43:08 way works. But you see the crucial piece
43:11 of information here was that I managed
43:13 to put an upper bound on Bill's
43:15 information on my key. If he knows two
43:19 bits then I'm I'm you know I cannot do
43:21 anything about it. He just knows the
43:23 key. But putting an upound
43:26 gives you a chance. So computer
43:28 scientist know so the key distribution
43:31 doesn't have to be perfect. It there
43:33 could be errors there. that there could
43:35 be some partial leak. As long as we can
43:38 make some estimates, then it's fine. We
43:40 can actually extract secret keys using
43:43 all kind of set of tools.
43:45 And um so the figure of merit that we
43:50 usually use here in cryptographic
43:54 scenario is the mean entropy. So as you
43:56 know there are many entropies that you
43:58 can come up the common one is of course
44:00 the shaon entropy. But when you're
44:03 looking for the worst case scenario and
44:06 uh so we use we take the probability of
44:11 guessing. So if I want to estimate so my
44:15 apologies Bill I'm going to use you as
44:17 my educational tool for a while. So I
44:19 refer to you your you you're dedicated
44:22 to science and education I know. So, so,
44:25 so if uh if sort of if Bill,
44:29 so how do I estimate
44:32 in mathematical terms Bill's information
44:35 about my key? So, one thing you can use
44:39 is the pro if you can estimate something
44:41 called probability of guessing the key.
44:45 So, that is what is the probability that
44:47 Bill can actually guess my secret. And
44:51 then what you do you take log to base 2
44:54 minus log of this probability of
44:56 guessing and that's what is called mean
44:58 entropy or we call it the conditional
45:00 mean entropy condition you know entropy
45:03 of my key condition upon his knowledge.
45:06 So this mean entropy is a figure of
45:08 merit that is important because that
45:10 tells you roughly that if I can estimate
45:13 this mean entropy that tells you roughly
45:16 how much key I can extract how much
45:18 secret key I can extract from something
45:21 that is not entirely secret. So, so we
45:25 are really after this figure of merit.
45:27 Actually, it will get more complicated
45:29 if you really want to go into this. Um,
45:32 we can talk about smooth conventional
45:36 mean entropy and so on so forth. But in
45:38 the first sort of approximation,
45:41 look, think of it this way. Probability
45:42 of guessing take minus log of that that
45:46 gives you mean entropy. And this this
45:49 number is important because it tells you
45:51 how much secret stuff I can get out of
45:54 something that may be partially secret.
45:58 So that's sort of quantified in
46:00 classical scenario into something that
46:02 is called the leftover hash lema. I just
46:04 like the name you know just I don't know
46:06 who came up with this but so where you
46:09 just if I had the raw key which is
46:12 partially secret. So this is this gray
46:14 stuff here and I managed to estimate the
46:19 mean entropy. So how much a potential
46:22 adver adversary may know or what is sort
46:24 of like uncertainty. So the mean entropy
46:27 to be more exact sort of quantifies
46:31 builds uncertainty about the key and so
46:34 then I can I can use a set of
46:38 mathematical tools to shrink the whole
46:41 thing and extract the key. We may or may
46:44 not go to this on Thursday when I talk
46:47 but this is just to give you the rough
46:49 idea how it works.
46:51 So let me add to your homework. So about
46:55 from so so you can maybe look up why
46:58 cryptographers use min entropy rather
47:00 than shonom entropy. So think about it
47:02 or look it up. Um
47:06 and if you're more ambitious, you can
47:08 try to go further define security using
47:11 cologor of trace distance between
47:13 probability distributions.
47:15 I may or may not talk about it on
47:17 Thursday. We'll see how it goes. But
47:19 that's related. If you have more
47:21 appetite to learn about how computer
47:23 scientists can extract data from
47:26 something that is partially secret to
47:28 something that is almost secret, just
47:31 you can look it up.
47:33 So we managed to pin down the problem,
47:36 right? How we we can have a pretty good
47:42 almost perfect cipher using for example
47:45 one-time part as long as in the key
47:48 distribution process.
47:50 As long as we are able to estimate how
47:53 much information leaked out in classical
47:56 scenario the you know you may you may
47:59 analyze different channels that say Bill
48:02 can eavesdrop on me you may say oh this
48:05 guy is clever he has this technology he
48:07 has another technology this allows him
48:09 to learn this this allows him to learn
48:10 that but at the end of the day you
48:13 really don't know how clever he is he
48:16 could be pretty clever and he can have
48:17 technology you never heard
48:20 So there's no fundamental.
48:25 So well that may be the case, right?
48:31 So so the thing is that there's also in
48:36 classical physics there's no law that
48:39 protects him from sort of a passive
48:41 easedropping without leaving any traces
48:43 whatsoever.
48:45 So he may even have such a technology
48:47 that he can read the whole key and I'm
48:49 not aware of this because he's not
48:51 leaving any traces of his eavesy.
48:55 So in the classical domain there's no
48:58 way you can estimate
49:01 um at least at the fundamental level you
49:03 can estimate this mean entropy. So you
49:06 can you I will never be in a position to
49:09 know for sure how much Bill knows.
49:14 So then uh well then we move to quantum
49:18 entanglement that probably it's not your
49:20 homework. I'm sure you know about it but
49:22 that's sort of like I'm sort of slowly
49:26 moving to the other the other narrative.
49:29 So we let's summarize the crypto part.
49:31 So I was I was telling you about this
49:35 one time path that was essentially sort
49:37 of invented in 1918 by this guy Jill
49:40 Vernham. than public key crypto systems.
49:43 There's an interesting story here. By
49:45 the way, they were first uh discovered
49:49 by a bunch of researchers working for
49:53 the British GCHQ. GCHQ stands for the
49:57 government communication headquarters.
50:00 And that's the bunch of um
50:03 mathematicians and researchers who work
50:05 for the British government to protect
50:07 the security of communication. But also
50:09 it's about um eavesdropping on any
50:14 anyone else and the usual stuff, right?
50:17 But they have they had a wonderful
50:20 tradition and a bunch of mathematicians
50:22 working there and bunch of misfits as
50:23 well. And one of them was this person
50:25 called James Ellis who was a half a
50:28 mathematician, half a poet and a geek
50:30 and you know one of those guys sometimes
50:33 you wonder what he's doing you know
50:35 right and he came up with this idea but
50:38 not in a very mathematical terms of
50:40 public key crypto system. So it's a
50:42 little bit like you know um sort of a
50:48 kind of having a safe box where you can
50:51 you have two keys. One is for locking
50:53 the safe box. Another one is unlocking
50:55 the safe box and he can you can say I
50:59 give everyone open safe box with a
51:02 locking key but I keep the unlocking
51:04 key. So once you lock the box with the
51:06 locking key the so-called public key you
51:09 cannot unlock it with the same one. You
51:11 have to use the private key to unlock
51:13 the safe box. So he had this kind of
51:16 idea but it had to be sort of taken
51:18 further by
51:20 some mathematicians like Phil Cox that
51:23 who actually came up with a mathematical
51:25 systems. So they were discovered
51:27 originally
51:29 um in at the GCHQ but those guys
51:33 couldn't publish it. So I feel always
51:35 very sorry for my colleagues from GCHQ
51:37 because they have good ideas but
51:40 sometimes you know they are not paid
51:42 that well but and they also don't have
51:45 this you know the vanity factor is is
51:48 also suffering because they cannot just
51:50 advertise their work to the rest of the
51:52 world. Um but but you know now we know
51:56 that they did it but at the time without
51:59 people American colleagues um from like
52:04 Rivers Adelman and Shamir who discovered
52:08 that maybe two or three years later they
52:11 came up with a very similar actually
52:14 identical ideas. So it's interesting to
52:16 see even those even those people didn't
52:19 communicate it's interesting that the
52:20 development in the field comes to a
52:23 certain point where certain ideas are
52:25 bound to emerge right so and they really
52:27 popped up um
52:30 so then I talk a little bit about uh we
52:35 are coming into sort of quantum part but
52:38 let me let me sort of now go to the
52:40 other narrative and then I'm going to
52:43 merge those two narratives active maybe
52:45 not today we'll see how it goes
52:48 so in parallel there was an interesting
52:51 development in
52:54 among physicists who try to understand
52:56 how nature works and we'll come to the
52:59 key distribution we'll see how it
53:01 eventually comes to the key distribution
53:05 so the the big thing of course the big
53:08 mystery in the early days of quantum
53:10 physics was
53:13 why we cannot make precise predictions.
53:17 So how is it that identical preparations
53:21 lead to different outcomes? So if you
53:24 take this very very simple experiment
53:27 where you take a single photon and
53:29 impinging on a beam splitter and it's
53:33 either reflected if you put a photo
53:35 detector there or transmitted if you put
53:38 another photo detector. So one of the
53:40 two detectors will click right
53:43 but you can you cannot you cannot
53:45 predict which one. So you can have
53:48 identical preparations. You have a in
53:51 this platonic at least sort of view of
53:53 this experiment. Take a zillion of those
53:55 experiments
53:57 the same momentum the same frequencies
53:59 the same placing everything is the same
54:02 and you know here goes the experiment
54:04 and the outcomes can be different.
54:07 So Einstein couldn't actually digest
54:10 this. He said look this doesn't make
54:13 sense, right? So how come
54:16 this is happening? Most likely because
54:18 the quantum theory by the way tells you
54:20 that the initial system the initial
54:23 preparation the initial state are
54:25 identical. But then Einstein says well
54:29 most likely at least I believe that this
54:32 is not the case that there is a better
54:35 description of quantum state that there
54:37 are certain variables that are not
54:40 incorporated into the quantum
54:41 descriptions and once you know those
54:44 variables
54:46 those extra quantities that describe the
54:48 state then you should be able to make
54:51 predictions. So then you you it's it's
54:53 not random. It's not inherently random
54:56 but it is sort of um it's simply it is
55:01 looks to us like this because we don't
55:03 know those hidden variables so to speak.
55:06 Once you can see those one you know
55:08 those variables on you have a theory
55:10 that allows you to interpret them in a
55:13 proper way that the outcomes will be
55:15 perfectly predictable. So you would know
55:18 what's going to happen in this case. So
55:20 that was that was a big dilemma. So
55:23 Einstein considered quantum theory not
55:26 to be complete. So he wrote um he wrote
55:30 this paper with Podolski and Rosen in
55:34 1935
55:37 under the title can quantum mechanical
55:39 description of physical reality be
55:41 considered complete
55:43 and and sort of he's he posed the
55:47 question right the title is the question
55:49 and his answer was most likely not and
55:54 he had an argument there showing that um
55:59 nicely constructed algorithm showing
56:01 that arguments showing that that most
56:04 likely that's not the case that we have
56:06 to work harder. So Aisha was not against
56:08 quantum theory. He was for it but he
56:11 thought it was not the work is not
56:13 finished yet. He said we have to work
56:15 harder. It's just like we are halfway
56:17 through. We have quantum theory but it
56:20 has some bizarre features and I'm not
56:22 taking this. you guys have to work
56:24 harder and come up with more complete
56:26 and once we have this more complete
56:28 theory then everything will be
56:29 predictable.
56:32 Um I just I want maybe to
56:36 move to and then this sort of idea
56:41 was um taken you know most people
56:44 treated this 1935 paper as a very kind
56:48 of philosophical paper because Einstein
56:50 didn't come up with any
56:53 um
56:55 any sort of uh way that you can possibly
57:00 verify this
57:03 world view that this is not complete in
57:06 in experimental terms. So you know for
57:08 most physicists if you don't if you
57:10 cannot come up with something that you
57:11 can verify or refute then it doesn't
57:15 it's just a philosophy you know you can
57:18 maybe it's true maybe it's not true who
57:20 knows you can talk about it but that's
57:22 as much as you can do about so the big
57:25 achievement and by the way most most
57:27 physicists were not so much interested
57:29 about this quantum physics was working
57:32 quantum physics was fine it was making
57:34 statistical predictions and they were
57:36 good enough explaining many things. So
57:38 that was as good as it gets. But there
57:40 were a few people who were curious about
57:43 this question posed by Einstein and one
57:46 of them was John Bell who
57:49 he John Bell was from Northern Ireland.
57:51 He was working in Geneva at CERN and his
57:55 job was essentially to design
57:57 accelerator and this is a very good
57:59 example that sometimes maybe you
58:00 shouldn't be doing what you're doing but
58:03 um and and after uh after hours he was
58:07 doing quantum foundations and so this
58:11 picture I'm told all Asper tells me that
58:14 this picture was taken during his
58:16 discussion with John Bell
58:19 and uh and John Bell came up with a way
58:23 of
58:25 actually refuting the concept of
58:29 Einstein's local hidden variables.
58:33 So he said well actually you know maybe
58:35 is a testable proposition. Maybe what
58:37 Einstein had in mind can be resolved by
58:40 experiments. So in fact
58:43 John Bell started by trying to come up
58:47 with a theory of hidden variables. So he
58:49 was taking Einstein science he was
58:51 saying okay well let's try work it out
58:53 how it can work and he realized that
58:56 there were two components if you want to
58:58 have those hidden variables local so to
59:03 speak. So if if what's going to happen
59:06 here only depends on things locally. It
59:10 doesn't depend on some specially
59:12 separated region. Um so then uh you have
59:17 to give something either you can
59:20 probably construct hidden variable
59:22 theorem but it's going to be non-local
59:24 or um
59:27 you know you can you can have if you
59:29 want to have things local there's
59:31 inherent randomness somehow involved. So
59:34 then then then he worked harder and then
59:36 he managed to show that you can
59:40 refute there are ways to refute at least
59:44 in there are ways to refute
59:46 experimentally local hidden variables.
59:50 So probably by now you all know about
59:54 bell theorem and there different
59:57 versions of it. Of course the most
59:59 popular one is this chl
1:00:04 shimony
1:00:06 ch it's John clauser I think it was horn
1:00:11 halt
1:00:14 you look it up. Okay.
1:00:17 So I know that C is certainly for
1:00:19 clauser. The first H is probably for
1:00:22 Halt. Uh then S is for Abnner Shimony
1:00:26 and uh and the last one probably for
1:00:29 Michael Horn but I'm not sure. Anyway,
1:00:32 so CHSH is a version of bell bell
1:00:35 inequalities
1:00:37 and uh there are many ways of course of
1:00:40 showing proving looking at it but
1:00:42 probably like if you look for one slide
1:00:44 and one liner is that you consider a
1:00:47 situation where you have two observers
1:00:52 of course Alice and Bob. Uh you put them
1:00:54 into two different locations.
1:00:57 um you put a source of entangled
1:00:58 particles in between and you may want to
1:01:02 measure certain not compatible
1:01:05 properties of those two particles. So
1:01:08 you have say one photon from the source
1:01:10 going to Alice, another photon from the
1:01:13 source going to Bob and say you're going
1:01:15 to measure different types of
1:01:16 polarization of this photon.
1:01:19 And um
1:01:22 if it is indeed the case that each
1:01:25 photon is then carrying a a well defined
1:01:30 polarization, right? So that the
1:01:33 measurement that you are going to take
1:01:36 is not going to make this polarization
1:01:38 happen in some mysterious way but it's
1:01:41 going to uncover the polarization that
1:01:43 already exists. So there is for every
1:01:46 single type of polarization there's a
1:01:48 value of it and working with this
1:01:50 assumption
1:01:52 uh we can just simply say that if Alice
1:01:55 for example is measuring polarization A1
1:01:58 she can get two different values plus
1:02:00 one and minus one uh in some units of H
1:02:04 bar and those values do exist prior to
1:02:08 the measurement and if she's going to
1:02:09 measure another type of polarization say
1:02:11 A2 then again this polarization also has
1:02:15 a well- definfined values prior to the
1:02:17 measurement.
1:02:19 And then the same for Bob. You assume
1:02:21 that B1 and B2 have well- definfined
1:02:25 values. Um and the experiment runs as
1:02:30 follows. So you have the source that
1:02:32 repeatedly emits um photons and the
1:02:36 polarization. And each time the toon
1:02:38 arrives at Ali's location, she's going
1:02:40 to measure either A1 or A2, choosing
1:02:43 randomly between the two. And the same
1:02:46 for Bob. Bob is going to choose either
1:02:49 B1 and B2. Now,
1:02:52 if you take this sort of like a local
1:02:55 realism view, you say that those values
1:02:58 do exist. You know, they they they are
1:03:01 predetermined values.
1:03:04 And and if this is the case, you can
1:03:06 construct a different you can you can
1:03:08 think then about a1, a2, b1, b2 as
1:03:11 random variables having values taking
1:03:14 values plus one and and minus2 and then
1:03:17 you can construct um another random
1:03:20 variable s which is a a linear
1:03:24 combination of those and you can look at
1:03:26 it. So here it is um it's um
1:03:31 a1 and we have the term b1 plus b2 here
1:03:34 and here we have term b1 minus b2. So if
1:03:38 it is the case that we have values plus
1:03:40 one minus one associated with those
1:03:42 random variables A1 A2 B1 B2 and you
1:03:46 look at this expression and you can see
1:03:48 that in this case in every single
1:03:51 realization of this experiment those
1:03:53 values all four values exist right you
1:03:56 may not be measuring all of them but
1:03:58 they do exist then one term in here has
1:04:03 to be equal to zero and the other one to
1:04:06 plus or minus two, right? So if B1 and
1:04:09 B2 are identical, both + one or both
1:04:13 minus one, this term is zero and this
1:04:16 term is equal plus or minus two and vice
1:04:19 versa. So in any case we can see that s
1:04:24 can only take two values plus two and
1:04:26 minus2 under those assumptions, right?
1:04:30 And if you run this experiment many many
1:04:33 times
1:04:35 then the the estimated average is going
1:04:39 to be somewhere between minus2 and two
1:04:42 and that's essentially ch inequality. So
1:04:46 starting with the simple assumptions
1:04:47 that those numerical that those values
1:04:50 are there they even though you know
1:04:54 prior to the measurement you'll come up
1:04:57 with inequality
1:04:59 that you can see here
1:05:02 and uh that's
1:05:05 you know that's not exactly if you then
1:05:08 repeat the whole argument using quantum
1:05:12 physics we don't have I mean there are
1:05:13 many ways of doing this we don't have to
1:05:15 go into this. If you say for example I
1:05:17 put a source of entangled photons, I
1:05:20 prepare them in a certain state and I
1:05:22 measure the polarization then I use a
1:05:24 different physical theory. So on one
1:05:26 hand the previous argument
1:05:29 was we were using the description that
1:05:33 was purely classical. We were using the
1:05:36 assumptions that those values do exist
1:05:38 that there are local hidden variables
1:05:40 and uh that led us to this inequality.
1:05:44 If you take quantum mechanical
1:05:46 description of the world then you can
1:05:49 see that this figure of merit the
1:05:51 estimated average may not be confined to
1:05:54 the interval minus 22. It may actually
1:05:56 go outside and it can go all the way up
1:05:59 to square root of two.
1:06:04 Today we when we talk about so this is
1:06:08 actually old-fashioned way of talking
1:06:09 about
1:06:11 bell inequalities or CHS inequalities
1:06:14 today and I may take this view it's it's
1:06:18 kind of interesting and maybe more
1:06:20 productive and and nicer in many
1:06:22 applications to think about what is
1:06:24 called chsh game where you consider
1:06:29 those two different boxes in two
1:06:32 different locations and you translate
1:06:34 the whole scenario into Alice and Bob
1:06:37 having devices and those devices can act
1:06:40 either according to local hidden
1:06:42 variable theorems where there is a set
1:06:45 of instructions telling each box how to
1:06:48 behave in every single round and then
1:06:51 Alice and DOPS can choose randomly
1:06:55 inputs to the boxes and boxes would
1:06:57 respond with some outputs and then
1:07:00 looking what at something the
1:07:01 conditional probability distribution of
1:07:04 outputs depending to inputs. You can
1:07:06 classify those probability distributions
1:07:09 into those conforming to local hidden
1:07:13 variable theorems and those that are not
1:07:16 conforming to them. So we'll take this
1:07:18 line when I talk about bell inequalities
1:07:21 but let me skip it. But if you look at
1:07:24 this class of conditional probability
1:07:27 distributions
1:07:29 then you can you can divide them into
1:07:31 classes. You say there are certain types
1:07:32 of correlations
1:07:34 that can be really explained in terms of
1:07:37 the local hidden variables that is sort
1:07:39 of the Einstein world and that would be
1:07:42 this sort of a classical square in the
1:07:44 middle all those sets that can be you
1:07:47 know mathematically
1:07:49 shown in a rather precise way. um the
1:07:53 sort of a set of those probability
1:07:55 distributions that are represented in um
1:07:58 higher dimensional sort of like in the
1:08:00 in the case that I'm describing you need
1:08:02 a space of at least a dimensional real
1:08:06 space um you you you describe by a point
1:08:09 that what we call probability point so
1:08:11 that that the convex sets of classical
1:08:14 correlations but what is interesting
1:08:17 here of course in our description is
1:08:19 that the set of classical correlations
1:08:21 is actually a subset. It's a strict
1:08:23 subset of the larger set of quantum
1:08:26 correlations
1:08:27 that are predicted by quantum mechanical
1:08:30 description. So, and then there's even a
1:08:33 larger set of what we call non-signaling
1:08:35 correlation that respect relativity.
1:08:38 What is interesting though is and and uh
1:08:42 and it's relatively sort of like not
1:08:44 recent but but an interesting
1:08:46 observation is that the set of
1:08:49 correlation that respect relativity is
1:08:52 strictly larger than the quantum set. So
1:08:55 quantum physics is somewhat more
1:08:56 restrictive. It respects relativity
1:08:59 but it could have respected relativity
1:09:01 in more relaxed way but it's it's it's
1:09:04 sort of like we we know about
1:09:06 non-signaling correlations which are um
1:09:10 not quantum not physical.
1:09:14 So anyway in this kind of language the
1:09:18 bell or CHSH inequality says that
1:09:24 is a certain function. It says that if I
1:09:26 measure those correlations, this figure
1:09:28 of merit that I observe can reach the
1:09:32 value two or is between minus2 and two
1:09:36 and not more. You it has to be in this
1:09:38 interval.
1:09:40 In quantum mechanical description of the
1:09:42 world, we allow this figure of merit to
1:09:44 go from minus two roo of two to two
1:09:47 square root of two. So if you observe
1:09:50 correlation somewhere here you refute
1:09:53 local hidden variable model saying that
1:09:56 you know it's it's it cannot the world
1:09:58 cannot be just explained in terms of
1:09:59 local hidden variables.
1:10:02 um we don't know about the correlations
1:10:04 which are outside the quantum there is
1:10:06 as I said there's a set of non-signaling
1:10:08 correlations one we we use them as a
1:10:10 mathematical reference point is an
1:10:12 interesting mathematical tool um but we
1:10:16 haven't observed this kind of
1:10:18 correlations
1:10:19 so so I encourage you to look at the ch
1:10:23 game but anyway the the moral of the
1:10:26 story is then then experimentalist moved
1:10:28 in and now the the sort of the thing is
1:10:33 to check what is the case and and of
1:10:35 course you know there's a a wonderful
1:10:37 story of people taking or not taking
1:10:40 bell inequality seriously most people
1:10:42 actually didn't so those we have John
1:10:44 Bell in the in the 60s writing about his
1:10:50 idea and nobody really cared that much
1:10:53 and there were few there were just
1:10:54 outliers and it's you know after John
1:10:58 Clauser who did his experiment
1:11:00 experiments. Um there was along aspect
1:11:04 he was probably the first one who
1:11:07 managed to sort of like percolate to the
1:11:10 attention of most physicists who said
1:11:12 well it's interesting you know it's it's
1:11:14 good that quantum physics works as as
1:11:17 sort of equations tell us but the
1:11:20 philosophical part of that was somehow
1:11:23 always sort of downplayed. So, so it was
1:11:25 just the case that here we have a rather
1:11:28 powerful statement that there is
1:11:30 inherent if you take you know if you
1:11:33 keep this locality in mind you you think
1:11:35 oh either there are some weird
1:11:37 communication between the particles
1:11:39 there's something truly non-local going
1:11:41 on or there is inherent randomness so
1:11:45 that means that the quantum physics in
1:11:47 this sense is complete that one cannot
1:11:50 hope for better description in this beam
1:11:53 splitter experiment that I showed told
1:11:55 you this sort of description of the
1:11:57 state is as good as it gets. You cannot
1:12:00 do anything better than that. You have
1:12:02 to leave with statistical predictions.
1:12:05 And that is actually quite to to anyone
1:12:07 who was brought up in a tradition where
1:12:11 science explained things is making
1:12:12 predictions but also makes explanations.
1:12:15 That that is really weird. It's very
1:12:17 difficult to to sort of if you really
1:12:21 really really think about it, it's
1:12:22 difficult to comprehend the fact that
1:12:25 something just pops out for no reason,
1:12:27 right? It just like happens.
1:12:31 Where's history to this event? There's
1:12:33 no history to this event. It just it
1:12:35 just happens. Okay? Many people can
1:12:38 question this view saying that there are
1:12:40 some assumptions and we divide the world
1:12:43 into classical and quantum. Maybe we
1:12:45 shouldn't be dividing. So there are ways
1:12:46 around the philosophers can keep talking
1:12:49 you know that this just that's not the
1:12:51 end of the story but in the first
1:12:52 approximation is this should have been
1:12:54 sort of like a shocking news to most
1:12:57 physicists at the time but it wasn't
1:12:59 really so people just mostly ignored it
1:13:02 and nobody cared so much about this
1:13:04 thing. I the aspect experiment was kind
1:13:08 of noticed but nobody made a sort of a
1:13:12 big hoo-ha out of that and then you know
1:13:15 those experiments where
1:13:18 uh of course repeated it was not always
1:13:21 the case after John Clauser by the way
1:13:23 who showed the violation of bell
1:13:24 inequalities there were people there
1:13:27 were some other experiments that showed
1:13:28 that the bell inequalities were
1:13:30 satisfied so at the time those
1:13:31 experiments were not so precise so
1:13:34 aspair was maybe the first one who who
1:13:36 showed that actually almost certainly
1:13:38 they have violated but then a few others
1:13:41 came along. So there are number of
1:13:42 people who contributed to the current
1:13:46 state-of-the-art where we know they have
1:13:47 violated from John Clauser to Alan
1:13:50 Aspect to Nicolola Jizang to Anton
1:13:53 Silinger John Pan and two of my heroes
1:13:57 who contributed who work for the defense
1:13:59 research agency. I used to work with
1:14:02 John Rarity and Paul Tapster. Those were
1:14:04 like, you know, it was a great time. We
1:14:07 had we were doing quantum crypto in a
1:14:09 defense research lab in Mulvin, not far
1:14:12 away from Oxford. And it was absolutely
1:14:16 fascinating to see how both difficult
1:14:20 and easy and fun it was to do research.
1:14:22 First of all, for some historical reason
1:14:25 in in the UK, um crypto, you know, this
1:14:29 this map was under the Ministry of
1:14:31 Defense and believe it or not, Ministry
1:14:34 of Defense essentially at the time was
1:14:36 not supposed to be working on crypto.
1:14:38 Crypto was one the foreign office and
1:14:40 there was another research agency, the
1:14:41 GCHQ that I mentioned that is somewhere
1:14:44 else in Chelenham and those guys were
1:14:46 supposed to be doing crypto but not
1:14:48 people in the defense research lab. But
1:14:51 you know the guy doing crypto the bunch
1:14:53 of computer scientists, mathematicians
1:14:55 and having no access to lasers or
1:14:58 anything related to something that can
1:15:02 be used to violate bell inequality which
1:15:04 I'll talk in a moment. So, so, so it was
1:15:07 it was we were not supposed to be doing
1:15:09 this kind of thing. And as John Rarity
1:15:12 put it, you know, in our lab, if I don't
1:15:15 aim my laser at a tank, I'm not doing a
1:15:18 research here. But but but of course,
1:15:20 you know, the it's it was not that bad.
1:15:24 And we um what I like also was a
1:15:28 interesting human dynamics between John
1:15:30 and Paul. So John was sort of if you
1:15:33 know John Rarity he's a rather outgoing
1:15:35 and he's very he traveled to meetings
1:15:39 and conferences. You probably never seen
1:15:42 and for good reason because Paul Tapster
1:15:45 hardly ever left Mulvin. So Paul Tapster
1:15:48 his life was essentially confined to
1:15:50 three points on the map. One was his
1:15:53 house, the other one was the lab and the
1:15:56 third one was the bridge club where he
1:15:58 he wor you know he played bridge. Um so
1:16:01 the um Paul hated going to any meetings
1:16:05 and conferences but he was he is
1:16:07 probably one of the best experimenters I
1:16:09 ever had the pleasure to work with. This
1:16:11 guy had amazing intuition and he
1:16:14 couldn't care less about anything else.
1:16:16 So that was that's Paul Tapster. And so
1:16:19 the two of them were great because uh
1:16:21 Paul was very keen to work on the
1:16:23 experiment and John was very keen to
1:16:25 travel and tell the world the world
1:16:27 about it.
1:16:31 So that's um
1:16:34 so that brings us to quantum
1:16:35 cryptography and I just bringing those
1:16:37 two narratives together. But I think
1:16:40 that as we are reaching almost one hour
1:16:42 and a half maybe maybe I'll stop here
1:16:46 just to summarize and I'll continue on
1:16:48 Thursday but but essentially what I
1:16:52 tried to do today was this to tell you
1:16:54 that
1:16:56 the there are two different branch there
1:16:58 were two different branches of
1:17:01 interesting branches one one related to
1:17:04 security the other one curiositydriven
1:17:06 research related to understanding
1:17:08 randomness
1:17:09 And uh so we went through the history of
1:17:13 security
1:17:15 of sort of crypto type research from the
1:17:18 early days of simple substitution
1:17:21 ciphers to um one-time paths and how we
1:17:25 ended up with a key distribution
1:17:27 problem. So we marked this as a problem.
1:17:29 We identify the problem there is to
1:17:32 estimate how much our adversaries can
1:17:35 possibly know about what we have and
1:17:39 once we have this number the mean
1:17:41 entropy for example we can use
1:17:43 mathematical tools to extract a secret
1:17:45 from that and we stop there and then I
1:17:48 switched to curiositydriven research
1:17:51 where Einstein unhappiness about quantum
1:17:54 theory not being complete led us to
1:17:57 recognize at the end of the say that the
1:18:00 depending how you look at reputation of
1:18:03 local hidden variables but essentially
1:18:05 you may take the view that there is
1:18:07 inherent randomness in nature that
1:18:09 there's something that nobody knows
1:18:12 nobody can know can predict Bill even
1:18:15 cannot predict with his superior
1:18:17 technology you know it's inherently
1:18:19 there Bill cannot there's no like no
1:18:23 third party not even Bill can predict
1:18:25 what's going to happen in the beam
1:18:27 splitter experiment experiment whether
1:18:29 it's going to go this way and that way
1:18:31 and that's interesting that is for the
1:18:33 first time we have a statement that it's
1:18:37 not randomness for whom it's just
1:18:39 randomness full stop right at this point
1:18:42 this event is truly random and so and we
1:18:46 are coming to the point where we are
1:18:47 going to bring together those two things
1:18:49 and you see that they are coming very
1:18:51 close together the key distribution
1:18:53 problem estimating how much randomness
1:18:56 or lack of knowledge is there with a
1:18:58 physical statement that there is a truly
1:19:01 random thing in nature. Now we just have
1:19:04 to bring them together and that was the
1:19:07 origin of quantum cryptography came from
1:19:10 sort of my side. Of course, Charlie Ben
1:19:14 and J Brasad were looking at it from a
1:19:16 different perspective with this
1:19:18 Heisenberg uncensored principle, but um
1:19:22 I you know at the time um we didn't know
1:19:25 each other and also they published it
1:19:28 was all before the internet and before
1:19:31 um rapid dissemination of work and and
1:19:34 their work was published in um
1:19:37 proceedings of some Indian conference
1:19:40 that the proceeding readings were
1:19:42 published and I don't know maybe 100
1:19:44 copies or so and and Jill was so unhappy
1:19:47 about this fact that it was not
1:19:49 documented early enough that he decided
1:19:52 to take this and have it reprinted and I
1:19:55 think it was it was it finally appeared
1:19:58 in in in in journal later in much much
1:20:01 much later um so my work was essentially
1:20:05 I didn't know about their work and it
1:20:07 was interesting to for me to learn about
1:20:10 it at some point when when I published
1:20:12 the paper and sort of in the process of
1:20:14 referring the paper I learned about this
1:20:17 work it was I was both happy and unhappy
1:20:19 at the same time so the reason I was
1:20:22 unhappy of course was that okay well
1:20:24 someone else had this idea not not so
1:20:27 not so happy about that but but the it's
1:20:30 interesting thing you know when you do
1:20:32 those things and you're I was not very
1:20:34 secure with uh with not very sort of
1:20:37 confident that what I'm actually doing
1:20:39 makes any sense whatsoever
1:20:41 And if you're a student, a young
1:20:43 researcher, you don't have that much
1:20:45 confidence in your work and you don't
1:20:46 know whether it's important, not
1:20:48 important, maybe rubbish. Maybe there's
1:20:49 a problem there. So to see that
1:20:51 wellestablished researchers like Charlie
1:20:53 Bennett were doing something along those
1:20:57 line was actually a sort of like a boost
1:20:59 of morale in some sense. So, and um but
1:21:02 I'll tell you this story um on Thursday
1:21:06 and we'll see um I think that it would
1:21:10 be good to if you have any questions
1:21:12 that uh you can send you want me or you
1:21:16 want me to elaborate on something. I'm
1:21:18 quite happy to to go in any direction.
1:21:21 I'm happy to go on the whiteboard and
1:21:23 and do some equations if you have some
1:21:25 specific questions. But
1:21:29 but I don't know maybe I'll just at
1:21:31 least the first lecture maybe I'll just
1:21:32 go on slide and finish the story. I
1:21:34 wanted to finish today but I don't think
1:21:37 I will do that today. Um anyway so any
1:21:40 questions about what I said today?
1:21:44 >> Yes.
1:21:45 >> How do we exploit
1:21:48 two?
1:21:49 >> How do I exploit
1:21:50 >> how do we exploit
1:21:52 >> to this car is greater than 22? Oh,
1:21:55 greater than 2 2, right?
1:21:57 >> It seems to be a powerful resource.
1:21:58 Great.
1:21:59 >> Yes. Yes. Yes. So, so we um there Yeah,
1:22:02 it's a very good in fact you know it's
1:22:05 interesting
1:22:07 if you look at uh correlation
1:22:09 mathematical correlations non-signaling
1:22:12 correlations
1:22:13 um which are
1:22:17 which are non-signaling but cannot be
1:22:20 explained by quantum. So, so they are
1:22:24 sort of this value of s goes up to four
1:22:28 for this particular type of correlations
1:22:31 and the way you even though it's sort of
1:22:34 like a mathematical thing that you can
1:22:36 never reach the ch inequality can be
1:22:39 viewed as trying to approximate those
1:22:43 correlations.
1:22:44 So you can see that you can write those
1:22:47 correlations if you use the
1:22:50 a certain mathematical approach if you
1:22:52 which I can maybe explain next time. You
1:22:55 can you can see that the
1:22:58 probability of winning in CHSH game
1:23:03 is essentially the overlap of
1:23:06 probability distributions that you have
1:23:09 with those unrealistic correlations. So
1:23:12 this mathematical correlation serves as
1:23:14 a sort of like a reference point to you
1:23:18 and the probability of winning CHSH
1:23:21 game. If you have those unrealistic
1:23:23 corations would be one but we don't have
1:23:26 them. So the question is if you cannot
1:23:28 just win this CHSH game all the time you
1:23:32 could only do it with unrealistic
1:23:35 those unrealistic correlations. how well
1:23:39 you can perform and you can show that if
1:23:41 you use classical correlations that the
1:23:44 best you can do is to win this game
1:23:46 roughly 75%.
1:23:49 So up to three quarters of cases you can
1:23:52 get it right. So 75% is your success
1:23:55 rate. If you use quantum correlations
1:23:58 you can go further. You can go something
1:24:00 like 86%.
1:24:02 But not any further. There's something
1:24:04 called serial unbound which bounds your
1:24:06 performance in quantum thing and then
1:24:10 you would have to have other resources
1:24:12 to be able to win this with probability
1:24:15 100%. So having this helped actually to
1:24:20 not only to sort of like put a
1:24:22 perspective. So this serves as an
1:24:24 interesting mathematical
1:24:26 um reference points for many
1:24:28 considerations.
1:24:29 And the other thing is that you can also
1:24:33 do all kind of easy bounds uh because
1:24:36 the the structure of those non-local
1:24:38 correlations is somewhat easier than the
1:24:40 quantum set. The quantum set of
1:24:41 correlations is horrible. Even in the
1:24:44 simplest possible case, we know it's a
1:24:46 convex set. We know it's smooth here,
1:24:48 but it has sharp edges then there. So it
1:24:51 is it gets it's a it's a monster. It's a
1:24:54 sort of it leaves in and I'm talking
1:24:56 about the simplest possible scenario the
1:24:58 simplest bell scenario where we have two
1:25:01 binary input binary outputs two parties
1:25:04 involved even in this case the set of
1:25:07 quantum correlations can be sort of
1:25:11 placed into a dimensional real space and
1:25:14 it's convex but it is complicated and
1:25:18 those crosssections you can reveal all
1:25:21 kind of complexities there. But the set
1:25:25 of non-local correlations is actually
1:25:28 simpler because it's a it's a polytop
1:25:30 and uh and then you can take all kind of
1:25:34 you can do all kind of bounds by working
1:25:37 with those not achievable correlations
1:25:40 but at least they put an you know some
1:25:42 bounds on what you can achieve in
1:25:43 quantum cases. So I think that we gained
1:25:46 lots of insight into the nature of the
1:25:50 CHSH inequality. Even the CHSH guys, I
1:25:52 don't think they had this insight that
1:25:54 we have looking at those non-realistic
1:25:56 but nonetheless very useful
1:25:58 mathematically correlations.
1:26:02 >> Yes,
1:26:03 >> we talked about the party version
1:26:09 there. Are there three party extensions?
1:26:12 >> Oh yeah yeah yeah. So, so the the
1:26:14 scenario
1:26:17 that I was talking here I taking the the
1:26:21 simplest one is is called two two
1:26:25 scenario that means like you have two
1:26:27 parties
1:26:29 you have two inputs. So the binary input
1:26:32 input is X and Y inputs are binary and
1:26:36 binary output. But you may consider
1:26:39 having n parties. So there are n
1:26:42 different individuals and then they may
1:26:45 put inputs that cons you know any number
1:26:48 of inputs and consider any number of
1:26:50 outputs finite but any number of those
1:26:54 and so those scenarios are more
1:26:55 difficult but as you can imagine
1:26:57 especially mathematical physicists they
1:26:59 love it you know just have something two
1:27:01 two then the first question comes to
1:27:04 your mind how about generalizing this
1:27:05 right so just um so yes so that's that's
1:27:10 being considered. But the two two
1:27:13 scenario is is kind of interesting
1:27:15 because it it has many there are certain
1:27:19 things that you can only do in this
1:27:20 particular scenario. For example, there
1:27:22 are certain deal dealing with binary
1:27:25 observables
1:27:26 um is kind of special. You can you can
1:27:30 there's something called Jordan's lema
1:27:32 which you can show that in the
1:27:36 that is actually quite important when we
1:27:38 talk about device independent crypto you
1:27:40 can you can show that
1:27:44 you don't have to go
1:27:46 if you okay let me just so you have this
1:27:49 box right in this sort of box scenario
1:27:51 there's Alice and Bob and they have
1:27:53 those boxes and they put uh inputs which
1:27:56 is a binary input it's either zero or
1:27:59 one and out of the box comes either zero
1:28:02 or one and you can just think about the
1:28:04 whole thing as having a quantum systems
1:28:07 inside and zero and one is going to
1:28:10 choose which observable you are going to
1:28:12 measure and the output the result of the
1:28:15 measurement just comes as the output
1:28:17 from the box. So the fact that those
1:28:19 observables have two outputs.
1:28:24 So so but but the the fact that the
1:28:26 system inside could be very complicated.
1:28:30 So your observable could be n by n
1:28:32 matrix but has only two out outcomes.
1:28:36 Right? So so the en values are the
1:28:38 generate plus one or minus one. It turns
1:28:40 out that you don't have to consider what
1:28:45 is inside to be a highly dimensional
1:28:48 system. A cubit will be enough. And
1:28:50 that's that's you know that's great
1:28:52 because then you can show you can show
1:28:54 all kind of interesting simplification
1:28:56 in this case and that's that's why we
1:28:59 like this system. It gives us all kind
1:29:01 of interesting stuff.
1:29:03 I'm not saying it's not worth
1:29:05 investigating more complex scenario. I'm
1:29:07 sure there is maybe something
1:29:08 interesting will come out of that. But
1:29:10 we can get such a long mileage out of
1:29:12 the simplest two two scenario which is
1:29:15 why we are studying this.
1:29:20 Yes,
1:29:21 >> I know that recently a number of
1:29:24 agencies
1:29:26 have decided
1:29:39 you have any
1:29:44 secure processes in Europe.
1:29:50 Yeah. So the um it's you know it's it's
1:29:55 an interesting and very very interesting
1:29:57 and very difficult question to answer in
1:30:00 precise terms because it's it's a
1:30:02 combination of science and policy and
1:30:06 politics and sort of even some aspects
1:30:11 of social sciences I would say and
1:30:12 trends and and things. So you the
1:30:20 that
1:30:22 so is you know the question is why
1:30:24 should we bother about quantum crypto
1:30:26 that requires quantum technologies and
1:30:29 it's somewhat limited in its usage at
1:30:31 the moment right when we can actually
1:30:34 look at the in the quantum era we can
1:30:36 protect information not with quantum
1:30:38 crypto but with um classical tools that
1:30:42 are good enough to protect information
1:30:45 even against quantum attacks.
1:30:49 And the the first sort of the the first
1:30:53 country that took that became proactive
1:30:56 was United States where there are this
1:31:01 national institute of standards and
1:31:02 technology and so this agency in United
1:31:05 States is responsible for setting up the
1:31:07 standards for future communication. So
1:31:09 that you know it's not it's not good
1:31:12 enough to have a good way of doing this.
1:31:14 You also want to stand make some sort of
1:31:16 standards that you can sometimes even
1:31:18 communicate with your enemy who's using
1:31:21 the same kind of system.
1:31:24 And then so this agency recognized the
1:31:26 fact that there is a need for well doing
1:31:30 something and having a tradition in
1:31:34 setting up standards for communication
1:31:36 in public key crypto system. It was a
1:31:38 natural extension is to go to community
1:31:41 of hardcore
1:31:43 cryptologists, people, engineers who who
1:31:46 know how the security works in a real
1:31:48 scenario, you know, and and in this
1:31:51 community there's interesting spectrum
1:31:52 of characters. So there are those who we
1:31:55 know how those things work in the real
1:31:57 world. You mathematicians don't tell us
1:31:59 about this nonsense. you know there's
1:32:00 this super pragmatic approach very
1:32:03 dismissive about all these sigas deltas
1:32:06 alphas on the whiteboard right um so
1:32:09 that you know there is a merit to this
1:32:11 of course because there is sometimes you
1:32:14 know people working on the other side of
1:32:16 the spectrum on the theory they think
1:32:18 that they discovered absolutely
1:32:20 something fantastic and they don't
1:32:21 realize that if you take it through the
1:32:23 hoops of implementations there are
1:32:25 issues at every single stage and those
1:32:27 guys engineers have to face those issues
1:32:30 implement them and they know that the
1:32:32 real world is not the platonic world
1:32:33 that I was describing here. So, so there
1:32:36 is sort of like interesting spectrum but
1:32:40 it's fair to say that in many of those
1:32:42 committees the hardcore pragmatist
1:32:44 dominate because they also people once
1:32:47 they have a good track record the
1:32:50 government agencies trust them they pro
1:32:52 you know they may not be using the most
1:32:53 sophisticated tools in the world but
1:32:55 they effective they protected things
1:32:57 they they have something to show so that
1:33:00 created a really very weird dynamics in
1:33:02 the US on the committee so that as You
1:33:05 probably know that um um the the
1:33:09 government that there was a public
1:33:11 competition for and this is always a
1:33:14 good idea to announce to the world look
1:33:16 we are collecting ideas for the next
1:33:19 generation classical public key crypto
1:33:21 systems. So the people started
1:33:24 submitting those ideas and there was a
1:33:26 committee that was selecting them and
1:33:29 that was a bit um there was an
1:33:32 interesting sort of a combination of
1:33:34 characters and people and attitudes
1:33:37 and uh and the evaluation process
1:33:42 um was a bit embarrassing I have to say
1:33:44 because um there were some of the crypto
1:33:48 systems that were selected not to the
1:33:51 final stage but they were sort of
1:33:53 shortsh shortlisted at some point and
1:33:55 some of them failed in a very
1:33:57 spectacular way. So there were at least
1:33:59 two cases where if something that was
1:34:03 supposed to be secure against quantum
1:34:05 attack was broken on a PC computer in
1:34:08 Sururik by someone who works for IBM and
1:34:10 said okay well for the weekend I just
1:34:12 have this challenge let me check this
1:34:14 system and you know so this is
1:34:16 embarrassment where you have something
1:34:17 that is already shortlisted to be secure
1:34:20 against quantum attack and there's a guy
1:34:22 in Turi who goes on a PC and breaks the
1:34:25 system without any quantum technology
1:34:27 right so that that hap that shows that
1:34:30 in this kind of community there was a
1:34:34 bit of a those who knew about
1:34:37 conventional tools knew very little
1:34:39 about quantum those who knew about
1:34:41 quantum probably didn't know about those
1:34:43 conventional tools that you needed so
1:34:46 that that is a generation problem I
1:34:48 think that there's just a lack of
1:34:49 education in those fields and I think as
1:34:51 I said yesterday I think you guys in a
1:34:53 much better position to judge in the
1:34:55 future so finally we have a set of
1:34:58 standards that US imposed um for
1:35:01 postquantum crypto mostly featuring
1:35:05 latisbased cryptography but as I
1:35:07 mentioned earlier this latisbased if you
1:35:10 like if you ask mathematicians at least
1:35:13 you know they they're not so sure that
1:35:15 they will last for a long period of time
1:35:17 I myself I'm not sure I wouldn't put my
1:35:19 money on latis base even though I like
1:35:21 mathematics I think it's pretty cool and
1:35:24 I think it may work for a while but I
1:35:26 don't think a long term is a is this is
1:35:28 a solution. Now you ask about the
1:35:30 European thing. Europeans usually follow
1:35:32 Americans, right? Because it's just what
1:35:34 can we do, you know, just there's a big
1:35:38 guy there and then there's not that much
1:35:41 we can do about it. So I don't think we
1:35:44 will just come with anything. We may
1:35:45 have our views and ideas and sometimes
1:35:47 whenever in the in the past we tried to
1:35:50 push European solutions. Sometimes we
1:35:52 failed because we claimed that they were
1:35:55 better than Americans but the American
1:35:57 imposed some standards and unwillingly
1:36:00 we had to follow them. Um so but but but
1:36:04 you know
1:36:06 I have to say that on some of those
1:36:09 European comedies at least those that
1:36:11 I'm familiar with the same dynamics
1:36:13 happen as happen in the US. So I think
1:36:17 it's it's interesting you know because
1:36:19 it just sometimes you go as a scientist
1:36:21 you go to a meeting and you'll be
1:36:24 surprised how immune people can be to
1:36:27 scientific arguments. you know, it's
1:36:29 just sometimes other factors decide upon
1:36:33 certain things and just I you know, this
1:36:35 is a this is sort of goes beyond the
1:36:37 point of this lecture, but it's an
1:36:39 interesting story. So, it's just
1:36:42 thanks.
1:36:46 >> Yes.
1:36:53 >> Yes. Is there similar stories in quantum
1:36:57 that we found out later that some kind
1:37:00 of secret service already?
1:37:03 >> Not that I mean if that is the case it's
1:37:06 so secret that nobody knows it. I don't
1:37:08 know. I think that the story um I think
1:37:12 that the story of so far you know maybe
1:37:18 there's a sort of a someone you know
1:37:22 like I some early days of I think I my
1:37:28 life I went to some quantum optics
1:37:29 conferences and atomic and laser
1:37:32 physicists talk about things it's I
1:37:34 wanted to learn the field it was it was
1:37:36 interesting for me because I wanted to
1:37:37 know the techniques and there was always
1:37:39 it was always fascinating to watch that
1:37:42 someone talking about the lasers and
1:37:44 something being developed here and there
1:37:46 was always a Russian guy in the audience
1:37:47 who said oh that was invented you know
1:37:49 long before somewhere noir somewhere so
1:37:52 I always had this vision that there was
1:37:54 a snow hat in Nova but everything that
1:37:57 was invented later was invented there
1:37:59 before and so whether I'm not trying to
1:38:02 I mean our Russian colleagues for sure
1:38:05 you know contributed immensely to this
1:38:07 field so it's Not that I'm not making
1:38:09 fun of that. Um, but when you have those
1:38:13 sort of geopolitical divisions, it's
1:38:15 possible sometimes that something
1:38:17 especially something that is relevant to
1:38:19 national security could be invented.
1:38:21 Elliot John Ellis is a good example in
1:38:24 quantum crypto. I think it's very
1:38:26 unlikely. So the story we have so far is
1:38:30 that there is an interesting guy Steven
1:38:32 Vizner who is a son of Jeremy Vizner.
1:38:35 Jeremy Vner, his father was a head of
1:38:37 MIT and he was like, you know, a very
1:38:40 powerful political character. Stephen,
1:38:42 in contrast, was a was just super shy.
1:38:45 This guy was absolutely like a bit of a
1:38:48 misfit. He had some ideas and he didn't
1:38:52 fit into academic community that well.
1:38:55 He ended up by the way he passed away a
1:38:57 few years ago sadly but at some point he
1:39:00 left us. he went to Israel and he was
1:39:04 trying to devote the rest of his life to
1:39:07 um to solar energy and
1:39:11 and so I knowing Steve was was a real
1:39:14 pleasure and so he would just be calling
1:39:16 you sometimes in the middle of the night
1:39:19 asking questions that were completely
1:39:20 unrelated to anything like sometimes
1:39:23 about politics sometimes about something
1:39:26 and but extremely extremely shy. So, so
1:39:29 he is the one who had this idea of
1:39:31 conjugate coding and he wrote something
1:39:35 about it but it was neglected rejected
1:39:38 but he when he was a student in in New
1:39:41 York he was sharing an apartment with
1:39:43 Charlie Bennett. So Charlie Bennett
1:39:46 learned from Steve Eisner about the
1:39:48 whole thing about this conjugate coding
1:39:50 and was sort of talking and talking to
1:39:52 people. Charlie likes talking to
1:39:53 everyone. So and Jill Brasad happened to
1:39:57 be one of those who listened to Charlie
1:40:00 Bennett and uh and then Steve Vner wrote
1:40:03 he his sort of idea for conjugate coding
1:40:06 was to use Heisenber uncertainty
1:40:08 principle and to generate sequences
1:40:12 um to authenticate things like for
1:40:15 example bank nodes but that was
1:40:17 unrealistic and and Charlie Wil had this
1:40:20 idea that well you know it may work for
1:40:22 something else so they adapted Steven
1:40:24 Visner's idea for the key distribution
1:40:27 and then they talk about it somewhere in
1:40:30 in 84 I guess in in Bangal or in India
1:40:33 at the conference that was you know
1:40:36 before my time and then this sort of
1:40:39 stayed as the idea that only like maybe
1:40:41 you know a handful people in the
1:40:43 universe knew about it in Europe we
1:40:46 didn't know about it at all um I think
1:40:49 at the time so when I came into this
1:40:53 through a different path path in a
1:40:54 different route. didn't know about that
1:40:56 work until um
1:41:00 until um
1:41:02 David Deutsch who was my supervisor he
1:41:05 said you know what Charlie Bennett
1:41:07 talked to me some time ago and they were
1:41:09 talking about this and this maybe it's
1:41:10 worth checking and then it was somehow
1:41:14 when I wrote my paper it was a referee
1:41:16 that was pointed out that maybe I should
1:41:18 actually refer to this idea it's not
1:41:20 entirely new so then I just realized
1:41:22 that uh talking Then I met Charlie
1:41:25 Bennett then I talked to him. So you see
1:41:27 at the time there was no internet as
1:41:28 such. So we had to really travel meet
1:41:30 and talk to people in person or ask for
1:41:33 some kind of preprints to be mailed so
1:41:36 that you can you can read that that
1:41:38 work. So that's the so somehow the the
1:41:41 European part of the story is is is you
1:41:44 know my part of the story and the the
1:41:46 American is is the Canadian and the US
1:41:49 part is Charlie Benner Brard and Steve
1:41:51 Ener who should be given lots of credit
1:41:53 here and there were maybe other people
1:41:56 who had similar ideas at some point but
1:41:58 I simply don't know about it and nobody
1:42:00 came up so I'm sort of waving the flag
1:42:03 saying look guys I did it all before you
1:42:05 did but it was so secret that I couldn't
1:42:07 publish it I doubt
1:42:15 Well, I think that you deserve coffee
1:42:17 break.
```
