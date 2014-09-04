#[Challenge #177 Hard - Stats on movie transcript](http://www.reddit.com/r/dailyprogrammer/comments/2exnal/8292014_challenge_177_hard_script_it_language/)

**Python 3.4**

The obvious language for this challenge is indeed Python. Here's my solution.

#Output

    Scene 1 :
     Number of words:  365
     Top 5 words: 
        * the (17 times)
        * of (15 times)
        * a (14 times)
        * it (8 times)
        * not (8 times)
        * swallow (6 times)
     Top 5 words make up:  18.63 % of that scene
     List of characters (sorted by # of words spoken): 
        * ARTHUR (174 words)
        * GUARD #1 (154 words)
        * GUARD #2 (37 words)
     List of characters (sorted by # lines spoken): 
        * GUARD #1 (18 lines)
        * ARTHUR (15 lines)
        * GUARD #2 (6 lines)
    ================================================================================
    Scene 2 :
     Number of words:  229
     Top 5 words: 
        * dead (16 times)
        * your (14 times)
        * out (12 times)
        * bring (12 times)
        * i (10 times)
        * not (7 times)
     Top 5 words make up:  31.0 % of that scene
     List of characters (sorted by # of words spoken): 
        * MORTICIAN (110 words)
        * CUSTOMER (84 words)
        * DEAD PERSON (35 words)
     List of characters (sorted by # lines spoken): 
        * CUSTOMER (14 lines)
        * MORTICIAN (13 lines)
        * DEAD PERSON (8 lines)
    ================================================================================
    Scene 3 :
     Number of words:  545
     Top 5 words: 
        * the (23 times)
        * you (23 times)
        * i (20 times)
        * in (13 times)
        * a (13 times)
        * king (9 times)
        * of (9 times)
        * to (9 times)
        * well (9 times)
        * that (9 times)
        * what (7 times)
     Top 5 words make up:  26.42 % of that scene
     List of characters (sorted by # of words spoken): 
        * DENNIS (297 words)
        * ARTHUR (174 words)
        * WOMAN (74 words)
     List of characters (sorted by # lines spoken): 
        * ARTHUR (25 lines)
        * DENNIS (19 lines)
        * WOMAN (10 lines)
    ================================================================================
    Scene 4 :
     Number of words:  258
     Top 5 words: 
        * you (17 times)
        * the (8 times)
        * i (8 times)
        * come (7 times)
        * have (6 times)
        * then (5 times)
     Top 5 words make up:  19.77 % of that scene
     List of characters (sorted by # of words spoken): 
        * ARTHUR (158 words)
        * BLACK KNIGHT (100 words)
     List of characters (sorted by # lines spoken): 
        * ARTHUR (20 lines)
        * BLACK KNIGHT (20 lines)
    ================================================================================
    Scene 5 :
     Number of words:  378
     Top 5 words: 
        * a (26 times)
        * witch (18 times)
        * burn (15 times)
        * the (11 times)
        * her (11 times)
        * you (10 times)
     Top 5 words make up:  24.07 % of that scene
     List of characters (sorted by # of words spoken): 
        * BEDEMIR (142 words)
        * CROWD (63 words)
        * VILLAGER #1 (61 words)
        * ARTHUR (41 words)
        * WITCH (27 words)
        * VILLAGER #3 (22 words)
        * VILLAGER #2 (22 words)
     List of characters (sorted by # lines spoken): 
        * BEDEMIR (25 lines)
        * CROWD (14 lines)
        * VILLAGER #1 (13 lines)
        * VILLAGER #2 (10 lines)
        * VILLAGER #3 (5 lines)
        * ARTHUR (5 lines)
        * WITCH (4 lines)
    ================================================================================
    [Narrative Interlude] :
     Number of words:  92
     Top 5 words: 
        * the (12 times)
        * sir (5 times)
        * and (4 times)
        * of (4 times)
        * to (4 times)
        * had (3 times)
        * who (3 times)
        * knights (2 times)
     Top 5 words make up:  40.22 % of that scene
     List of characters (sorted by # of words spoken): 
        * NARRATOR (92 words)
     List of characters (sorted by # lines spoken): 
        * NARRATOR (1 lines)
    ================================================================================
    Scene 6 :
     Number of words:  176
     Top 5 words: 
        * camelot (8 times)
        * we (8 times)
        * to (6 times)
        * and (6 times)
        * a (6 times)
        * the (5 times)
        * we're (5 times)
        * knights (3 times)
        * in (3 times)
        * lot (3 times)
        * our (2 times)
     Top 5 words make up:  31.25 % of that scene
     List of characters (sorted by # of words spoken): 
        * ARTHUR (151 words)
        * BEDEMIR (16 words)
        * LAUNCELOT (4 words)
        * PATSY (4 words)
        * GALAHAD (1 words)
     List of characters (sorted by # lines spoken): 
        * ARTHUR (4 lines)
        * LAUNCELOT (2 lines)
        * BEDEMIR (2 lines)
        * GALAHAD (1 lines)
        * PATSY (1 lines)
    ================================================================================
    Scene 7 :
     Number of words:  146
     Top 5 words: 
        * the (7 times)
        * arthur (6 times)
        * a (4 times)
        * to (4 times)
        * it's (4 times)
        * lord (4 times)
        * oh (3 times)
        * don't (3 times)
        * of (3 times)
        * grail (3 times)
        * your (3 times)
        * and (3 times)
        * is (3 times)
        * it (2 times)
     Top 5 words make up:  35.62 % of that scene
     List of characters (sorted by # of words spoken): 
        * GOD (123 words)
        * ARTHUR (15 words)
        * LAUNCELOT (5 words)
        * GALAHAD (3 words)
     List of characters (sorted by # lines spoken): 
        * GOD (5 lines)
        * ARTHUR (5 lines)
        * LAUNCELOT (1 lines)
        * GALAHAD (1 lines)
    ================================================================================
    Scene 8 :
     Number of words:  419
     Top 5 words: 
        * you (15 times)
        * and (11 times)
        * i (11 times)
        * your (9 times)
        * the (9 times)
        * a (9 times)
        * of (7 times)
        * is (7 times)
        * uh (6 times)
     Top 5 words make up:  20.05 % of that scene
     List of characters (sorted by # of words spoken): 
        * GUARD (157 words)
        * ARTHUR (137 words)
        * BEDEMIR (60 words)
        * GALAHAD (26 words)
        * MUTTERING GUARDS (19 words)
        * ALL (11 words)
        * LAUNCELOT (5 words)
        * GUARDS (4 words)
        * OTHER GUARDS (0 words)
     List of characters (sorted by # lines spoken): 
        * ARTHUR (15 lines)
        * GUARD (14 lines)
        * GALAHAD (4 lines)
        * BEDEMIR (4 lines)
        * ALL (3 lines)
        * LAUNCELOT (1 lines)
        * MUTTERING GUARDS (1 lines)
        * GUARDS (1 lines)
        * OTHER GUARDS (1 lines)
    ================================================================================
    Scene 9 :
     Number of words:  72
     Top 5 words: 
        * the (6 times)
        * arthur (3 times)
        * to (3 times)
        * grail (2 times)
        * a (2 times)
        * and (2 times)
        * that (2 times)
        * for (2 times)
        * they (2 times)
        * consulted (1 times)
        * utterly (1 times)
        * king (1 times)
        * disheartened (1 times)
        * knights (1 times)
        * required (1 times)
        * now (1 times)
        * conclusion (1 times)
        * strategy (1 times)
        * have (1 times)
        * his (1 times)
        * took (1 times)
        * if (1 times)
        * new (1 times)
        * should (1 times)
        * ferocity (1 times)
        * him (1 times)
        * brought (1 times)
        * taunting (1 times)
        * greg (1 times)
        * having (1 times)
        * is (1 times)
        * of (1 times)
        * defeat (1 times)
        * decided (1 times)
        * at (1 times)
        * completely (1 times)
        * seems (1 times)
        * was (1 times)
        * french (1 times)
        * this (1 times)
        * were (1 times)
        * by (1 times)
        * convinced (1 times)
        * did-- (1 times)
        * separate (1 times)
        * surprise (1 times)
        * be (1 times)
        * what (1 times)
        * action (1 times)
        * became (1 times)
        * castle (1 times)
        * quest (1 times)
        * search (1 times)
        * holy (1 times)
        * individually (1 times)
        * successful (1 times)
        * closest (1 times)
     Top 5 words make up:  100.0 % of that scene
     List of characters (sorted by # of words spoken): 
        * NARRATOR (70 words)
        * WOMAN (1 words)
        * DIRECTOR (1 words)
        * Pictures for Schools, take 8. (0 words)
     List of characters (sorted by # lines spoken): 
        * NARRATOR (1 lines)
        * Pictures for Schools, take 8. (1 lines)
        * WOMAN (1 lines)
        * DIRECTOR (1 lines)
    ================================================================================
    Scene 10 :
     Number of words:  457
     Top 5 words: 
        * his (16 times)
        * and (16 times)
        * i (14 times)
        * to (13 times)
        * sir (12 times)
        * brave (12 times)
        * robin (11 times)
     Top 5 words make up:  20.57 % of that scene
     List of characters (sorted by # of words spoken): 
        * MINSTREL  (172 words)
        * ROBIN (73 words)
        * LEFT HEAD (71 words)
        * RIGHT HEAD (39 words)
        * MIDDLE HEAD (37 words)
        * NARRATOR (29 words)
        * ALL HEADS (19 words)
        * WOMAN (10 words)
        * DENNIS (7 words)
     List of characters (sorted by # lines spoken): 
        * ROBIN (12 lines)
        * LEFT HEAD (10 lines)
        * MINSTREL  (10 lines)
        * MIDDLE HEAD (9 lines)
        * RIGHT HEAD (7 lines)
        * ALL HEADS (5 lines)
        * NARRATOR (1 lines)
        * DENNIS (1 lines)
        * WOMAN (1 lines)
    ================================================================================
    Scene 11 :
     Number of words:  756
     Top 5 words: 
        * the (28 times)
        * you (24 times)
        * and (23 times)
        * oh (20 times)
        * i (18 times)
     Top 5 words make up:  14.95 % of that scene
     List of characters (sorted by # of words spoken): 
        * ZOOT (231 words)
        * GALAHAD (229 words)
        * DINGO (157 words)
        * LAUNCELOT (66 words)
        * PIGLET (27 words)
        * GIRLS (21 words)
        * VARIOUS GIRLS (19 words)
        * NARRATOR (5 words)
        * ALL (1 words)
     List of characters (sorted by # lines spoken): 
        * GALAHAD (37 lines)
        * LAUNCELOT (14 lines)
        * ZOOT (14 lines)
        * DINGO (12 lines)
        * GIRLS (7 lines)
        * PIGLET (6 lines)
        * VARIOUS GIRLS (2 lines)
        * NARRATOR (1 lines)
        * ALL (1 lines)
    ================================================================================
    Narrative Interlude 2 :
     Number of words:  114
     Top 5 words: 
        * a (5 times)
        * were (3 times)
        * sir (3 times)
        * swallow's (3 times)
        * i (3 times)
        * which (3 times)
        * they (3 times)
        * if (2 times)
        * mean (2 times)
        * and (2 times)
        * with (2 times)
        * the (2 times)
        * scene (2 times)
        * had (2 times)
        * flight (2 times)
        * than (2 times)
        * arthur (2 times)
        * oh (2 times)
        * in (2 times)
        * on (2 times)
        * away (2 times)
        * more (2 times)
        * it (1 times)
        * temptation (1 times)
        * any (1 times)
        * but (1 times)
        * you (1 times)
        * can (1 times)
        * four (1 times)
        * dragging-- (1 times)
        * lovely (1 times)
        * twenty-four (1 times)
        * of (1 times)
        * grail (1 times)
        * starling (1 times)
        * cord (1 times)
        * them (1 times)
        * discovered (1 times)
        * aren't (1 times)
        * hadn't (1 times)
        * anyway (1 times)
        * birds (1 times)
        * acting (1 times)
        * between (1 times)
        * clue (1 times)
        * something (1 times)
        * not (1 times)
        * launcelot (1 times)
        * get (1 times)
        * unladen (1 times)
        * no (1 times)
        * swallows (1 times)
        * some (1 times)
        * to (1 times)
        * -oolp (1 times)
        * although (1 times)
        * two (1 times)
        * hear (1 times)
        * an (1 times)
        * line (1 times)
        * king (1 times)
        * saved (1 times)
        * certain (1 times)
        * laden (1 times)
        * that's (1 times)
        * flights (1 times)
        * galahad (1 times)
        * discovers (1 times)
        * meanwhile (1 times)
        * nearer (1 times)
        * obviously (1 times)
        * is (1 times)
        * there (1 times)
        * think (1 times)
        * vital (1 times)
        * -- (1 times)
        * almost (1 times)
        * walking (1 times)
        * from (1 times)
        * bedemir (1 times)
        * really (1 times)
        * still (1 times)
        * smashing (1 times)
     Top 5 words make up:  100.0 % of that scene
     List of characters (sorted by # of words spoken): 
        * NARRATOR (110 words)
        * CROWD (4 words)
     List of characters (sorted by # lines spoken): 
        * NARRATOR (2 lines)
        * CROWD (1 lines)
    ================================================================================
    Scene 24 :
     Number of words:  97
     Top 5 words: 
        * the (10 times)
        * he (10 times)
        * grail (6 times)
        * ha (5 times)
        * of (5 times)
        * where (3 times)
        * man (3 times)
        * hee (3 times)
        * which (3 times)
        * cave (3 times)
        * has (3 times)
        * live (2 times)
     Top 5 words make up:  57.73 % of that scene
     List of characters (sorted by # of words spoken): 
        * OLD MAN (52 words)
        * ARTHUR (45 words)
     List of characters (sorted by # lines spoken): 
        * OLD MAN (6 lines)
        * ARTHUR (5 lines)
    ================================================================================
    Scene 25 :
     Number of words:  170
     Top 5 words: 
        * nee (16 times)
        * the (8 times)
        * who (8 times)
        * you (7 times)
        * we (7 times)
        * and (6 times)
        * are (6 times)
        * a (6 times)
        * knights (5 times)
     Top 5 words make up:  40.59 % of that scene
     List of characters (sorted by # of words spoken): 
        * HEAD KNIGHT (91 words)
        * ARTHUR (73 words)
        * BEDEMIR (3 words)
        * HEAD KNIGHTS (2 words)
        * RANDOM (1 words)
     List of characters (sorted by # lines spoken): 
        * HEAD KNIGHT (12 lines)
        * ARTHUR (10 lines)
        * RANDOM (1 lines)
        * HEAD KNIGHTS (1 lines)
        * BEDEMIR (1 lines)
    ================================================================================
    Scene 26 :
     Number of words:  591
     Top 5 words: 
        * the (25 times)
        * no (18 times)
        * i (18 times)
        * and (15 times)
        * you (14 times)
        * get (13 times)
     Top 5 words make up:  17.43 % of that scene
     List of characters (sorted by # of words spoken): 
        * FATHER (379 words)
        * GUARD #1 (145 words)
        * HERBERT (53 words)
        * GUARD #2 (6 words)
        * NARRATOR (5 words)
        * ERBERT (3 words)
     List of characters (sorted by # lines spoken): 
        * FATHER (32 lines)
        * GUARD #1 (20 lines)
        * HERBERT (9 lines)
        * GUARD #2 (6 lines)
        * NARRATOR (1 lines)
        * ERBERT (1 lines)
    ================================================================================
    Scene 27 :
     Number of words:  183
     Top 5 words: 
        * i (9 times)
        * sir (7 times)
        * concorde (7 times)
        * the (4 times)
        * have (4 times)
        * and (4 times)
        * to (4 times)
        * you (4 times)
        * in (4 times)
        * not (3 times)
        * no (3 times)
        * me (3 times)
        * please (3 times)
        * shall (3 times)
        * a (3 times)
        * uh (3 times)
        * my (3 times)
        * come (3 times)
        * vain (2 times)
     Top 5 words make up:  41.53 % of that scene
     List of characters (sorted by # of words spoken): 
        * LAUNCELOT (131 words)
        * CONCORDE (52 words)
     List of characters (sorted by # lines spoken): 
        * CONCORDE (8 lines)
        * LAUNCELOT (8 lines)
    ================================================================================
    Scene 28 :
     Number of words:  320
     Top 5 words: 
        * i (15 times)
        * you (14 times)
        * to (10 times)
        * uh (9 times)
        * well (8 times)
     Top 5 words make up:  17.5 % of that scene
     List of characters (sorted by # of words spoken): 
        * LAUNCELOT (146 words)
        * FATHER (103 words)
        * HERBERT (61 words)
        * GUARD #1 (10 words)
     List of characters (sorted by # lines spoken): 
        * LAUNCELOT (17 lines)
        * FATHER (13 lines)
        * HERBERT (12 lines)
        * GUARD #1 (1 lines)
    ================================================================================
    Scene 29 :
     Number of words:  367
     Top 5 words: 
        * to (16 times)
        * the (16 times)
        * he's (15 times)
        * going (11 times)
        * tell (11 times)
        * of (9 times)
        * i (9 times)
        * and (8 times)
     Top 5 words make up:  25.89 % of that scene
     List of characters (sorted by # of words spoken): 
        * FATHER (227 words)
        * LAUNCELOT (47 words)
        * SINGING (40 words)
        * RANDOM (26 words)
        * HERBERT (17 words)
        * CONCORDE (10 words)
     List of characters (sorted by # lines spoken): 
        * FATHER (12 lines)
        * RANDOM (7 lines)
        * LAUNCELOT (6 lines)
        * CONCORDE (3 lines)
        * HERBERT (3 lines)
        * SINGING (2 lines)
    ================================================================================
    Scene 30 :
     Number of words:  193
     Top 5 words: 
        * no (15 times)
        * nee (7 times)
        * say (5 times)
        * you (5 times)
        * shrubberies (5 times)
        * it (4 times)
        * is (4 times)
        * will (4 times)
        * are (4 times)
        * not (4 times)
        * noo (4 times)
        * we (4 times)
        * and (4 times)
        * a (4 times)
        * 'nee' (3 times)
     Top 5 words make up:  39.38 % of that scene
     List of characters (sorted by # of words spoken): 
        * ARTHUR (94 words)
        * ROGER (74 words)
        * CRONE (19 words)
        * BEDEMIR (6 words)
     List of characters (sorted by # lines spoken): 
        * ARTHUR (11 lines)
        * CRONE (4 lines)
        * BEDEMIR (4 lines)
        * ROGER (3 lines)
    ================================================================================
    Scene 31 :
     Number of words:  342
     Top 5 words: 
        * the (16 times)
        * it (14 times)
        * you (10 times)
        * is (9 times)
        * a (9 times)
        * aaaaugh (8 times)
     Top 5 words make up:  19.3 % of that scene
     List of characters (sorted by # of words spoken): 
        * HEAD KNIGHT (170 words)
        * ARTHUR (91 words)
        * MINSTREL  (34 words)
        * ROBIN (26 words)
        * KNIGHTS (9 words)
        * RANDOM (7 words)
        * BEDEMIR (5 words)
     List of characters (sorted by # lines spoken): 
        * HEAD KNIGHT (16 lines)
        * ARTHUR (14 lines)
        * KNIGHTS (7 lines)
        * ROBIN (4 lines)
        * RANDOM (3 lines)
        * MINSTREL  (2 lines)
        * BEDEMIR (1 lines)
    ================================================================================
    Narrative Interlude 3 :
     Number of words:  94
     Top 5 words: 
        * and (9 times)
        * the (4 times)
        * into (4 times)
        * changed (3 times)
        * spring (3 times)
        * summer (3 times)
        * winter (3 times)
        * yay (3 times)
        * much (2 times)
        * rejoicing (2 times)
        * there (2 times)
        * of (2 times)
        * a (2 times)
        * was (2 times)
        * they (2 times)
        * in (2 times)
        * on (2 times)
        * to (2 times)
        * out (1 times)
     Top 5 words make up:  56.38 % of that scene
     List of characters (sorted by # of words spoken): 
        * NARRATOR (91 words)
        * ALL (3 words)
     List of characters (sorted by # lines spoken): 
        * NARRATOR (3 lines)
        * ALL (2 lines)
    ================================================================================
    Scene 32 :
     Number of words:  326
     Top 5 words: 
        * you (13 times)
        * the (12 times)
        * a (11 times)
        * yes (9 times)
        * of (8 times)
     Top 5 words make up:  16.26 % of that scene
     List of characters (sorted by # of words spoken): 
        * TIM (148 words)
        * ARTHUR (142 words)
        * KNIGHTS (23 words)
        * GALAHAD (6 words)
        * BEDEMIR (6 words)
        * ROBIN (1 words)
     List of characters (sorted by # lines spoken): 
        * ARTHUR (14 lines)
        * TIM (11 lines)
        * KNIGHTS (5 lines)
        * GALAHAD (1 lines)
        * ROBIN (1 lines)
        * BEDEMIR (1 lines)
    ================================================================================
    Scene 33 :
     Number of words:  515
     Top 5 words: 
        * the (21 times)
        * and (16 times)
        * you (12 times)
        * it (11 times)
        * three (10 times)
     Top 5 words make up:  13.59 % of that scene
     List of characters (sorted by # of words spoken): 
        * BROTHER (153 words)
        * ARTHUR (132 words)
        * TIM (121 words)
        * ROBIN (34 words)
        * KNIGHT (19 words)
        * GALAHAD (18 words)
        * MAYNARD (12 words)
        * BORIS (11 words)
        * KNIGHTS (8 words)
        * LAUNCELOT (6 words)
        * ALL (1 words)
     List of characters (sorted by # lines spoken): 
        * ARTHUR (21 lines)
        * TIM (16 lines)
        * KNIGHT (9 lines)
        * ROBIN (5 lines)
        * GALAHAD (3 lines)
        * MAYNARD (3 lines)
        * KNIGHTS (3 lines)
        * BROTHER (2 lines)
        * BORIS (2 lines)
        * LAUNCELOT (1 lines)
        * ALL (1 lines)
    ================================================================================
    Scene 34 :
     Number of words:  234
     Top 5 words: 
        * the (14 times)
        * of (10 times)
        * no (9 times)
        * it (7 times)
        * he (6 times)
     Top 5 words make up:  19.66 % of that scene
     List of characters (sorted by # of words spoken): 
        * MAYNARD (67 words)
        * NARRATOR (38 words)
        * LAUNCELOT (37 words)
        * ARTHUR (36 words)
        * BEDEMIR (26 words)
        * GALAHAD (13 words)
        * KNIGHT (12 words)
        * ALL (4 words)
        * SEVERAL (1 words)
     List of characters (sorted by # lines spoken): 
        * LAUNCELOT (8 lines)
        * MAYNARD (8 lines)
        * KNIGHT (6 lines)
        * ARTHUR (6 lines)
        * BEDEMIR (6 lines)
        * GALAHAD (3 lines)
        * NARRATOR (1 lines)
        * ALL (1 lines)
        * SEVERAL (1 lines)
    ================================================================================
    Scene 35 :
     Number of words:  375
     Top 5 words: 
        * the (22 times)
        * is (17 times)
        * what (16 times)
        * of (12 times)
        * you (11 times)
     Top 5 words make up:  20.8 % of that scene
     List of characters (sorted by # of words spoken): 
        * ARTHUR (128 words)
        * KEEPER (110 words)
        * LAUNCELOT (51 words)
        * ROBIN (48 words)
        * GALAHAD (13 words)
        * KNIGHT (13 words)
        * BEDEMIR (12 words)
     List of characters (sorted by # lines spoken): 
        * KEEPER (16 lines)
        * ARTHUR (15 lines)
        * ROBIN (10 lines)
        * LAUNCELOT (7 lines)
        * KNIGHT (5 lines)
        * GALAHAD (3 lines)
        * BEDEMIR (2 lines)
    ================================================================================
    Scene 36 :
     Number of words:  281
     Top 5 words: 
        * you (15 times)
        * of (12 times)
        * the (10 times)
        * launcelot (9 times)
        * your (7 times)
     Top 5 words make up:  18.86 % of that scene
     List of characters (sorted by # of words spoken): 
        * GUARD (154 words)
        * ARTHUR (120 words)
        * BEDEMIR (7 words)
     List of characters (sorted by # lines spoken): 
        * ARTHUR (9 lines)
        * GUARD (5 lines)
        * BEDEMIR (3 lines)
    ================================================================================
    ANALYSIS OF THE WHOLE MOVIE:
     Number of words: 8095
     Number of lines: 953
     Number of stage directions: 134
     Number of characters: 57
     Characters (sorted by number of words):
        * ARTHUR has spoken 1711 words and 194 lines ( 20.36 %)
        * FATHER has spoken 709 words and 57 lines ( 5.98 %)
        * LAUNCELOT has spoken 498 words and 65 lines ( 6.82 %)
        * NARRATOR has spoken 440 words and 11 lines ( 1.15 %)
        * GUARD has spoken 311 words and 19 lines ( 1.99 %)
        * GALAHAD has spoken 309 words and 53 lines ( 5.56 %)
        * GUARD #1 has spoken 309 words and 39 lines ( 4.09 %)
        * DENNIS has spoken 304 words and 20 lines ( 2.1 %)
        * BEDEMIR has spoken 283 words and 49 lines ( 5.14 %)
        * TIM has spoken 269 words and 27 lines ( 2.83 %)
        * HEAD KNIGHT has spoken 261 words and 28 lines ( 2.94 %)
        * ZOOT has spoken 231 words and 14 lines ( 1.47 %)
        * MINSTREL  has spoken 206 words and 12 lines ( 1.26 %)
        * ROBIN has spoken 182 words and 32 lines ( 3.36 %)
        * DINGO has spoken 157 words and 12 lines ( 1.26 %)
        * BROTHER has spoken 153 words and 2 lines ( 0.21 %)
        * HERBERT has spoken 131 words and 24 lines ( 2.52 %)
        * GOD has spoken 123 words and 5 lines ( 0.52 %)
        * KEEPER has spoken 110 words and 16 lines ( 1.68 %)
        * MORTICIAN has spoken 110 words and 13 lines ( 1.36 %)
        * BLACK KNIGHT has spoken 100 words and 20 lines ( 2.1 %)
        * WOMAN has spoken 85 words and 12 lines ( 1.26 %)
        * CUSTOMER has spoken 84 words and 14 lines ( 1.47 %)
        * MAYNARD has spoken 79 words and 11 lines ( 1.15 %)
        * ROGER has spoken 74 words and 3 lines ( 0.31 %)
        * LEFT HEAD has spoken 71 words and 10 lines ( 1.05 %)
        * CROWD has spoken 67 words and 15 lines ( 1.57 %)
        * CONCORDE has spoken 62 words and 11 lines ( 1.15 %)
        * VILLAGER #1 has spoken 61 words and 13 lines ( 1.36 %)
        * OLD MAN has spoken 52 words and 6 lines ( 0.63 %)
        * KNIGHT has spoken 44 words and 20 lines ( 2.1 %)
        * GUARD #2 has spoken 43 words and 12 lines ( 1.26 %)
        * KNIGHTS has spoken 40 words and 15 lines ( 1.57 %)
        * SINGING has spoken 40 words and 2 lines ( 0.21 %)
        * RIGHT HEAD has spoken 39 words and 7 lines ( 0.73 %)
        * MIDDLE HEAD has spoken 37 words and 9 lines ( 0.94 %)
        * DEAD PERSON has spoken 35 words and 8 lines ( 0.84 %)
        * RANDOM has spoken 34 words and 11 lines ( 1.15 %)
        * PIGLET has spoken 27 words and 6 lines ( 0.63 %)
        * WITCH has spoken 27 words and 4 lines ( 0.42 %)
        * VILLAGER #3 has spoken 22 words and 5 lines ( 0.52 %)
        * VILLAGER #2 has spoken 22 words and 10 lines ( 1.05 %)
        * GIRLS has spoken 21 words and 7 lines ( 0.73 %)
        * ALL has spoken 20 words and 8 lines ( 0.84 %)
        * MUTTERING GUARDS has spoken 19 words and 1 lines ( 0.1 %)
        * CRONE has spoken 19 words and 4 lines ( 0.42 %)
        * ALL HEADS has spoken 19 words and 5 lines ( 0.52 %)
        * VARIOUS GIRLS has spoken 19 words and 2 lines ( 0.21 %)
        * BORIS has spoken 11 words and 2 lines ( 0.21 %)
        * PATSY has spoken 4 words and 1 lines ( 0.1 %)
        * GUARDS has spoken 4 words and 1 lines ( 0.1 %)
        * ERBERT has spoken 3 words and 1 lines ( 0.1 %)
        * HEAD KNIGHTS has spoken 2 words and 1 lines ( 0.1 %)
        * SEVERAL has spoken 1 words and 1 lines ( 0.1 %)
        * DIRECTOR has spoken 1 words and 1 lines ( 0.1 %)
        * OTHER GUARDS has spoken 0 words and 1 lines ( 0.1 %)
        * Pictures for Schools, take 8. has spoken 0 words and 1 lines ( 0.1 %)
     Top 10 words:
        * the (308 times)
        * you (218 times)
        * a (192 times)
        * i (182 times)
        * and (166 times)
        * of (156 times)
        * to (145 times)
        * no (111 times)
        * is (98 times)
        * oh (95 times)
     Top 3 scenes (sorted by number of words):
        * Scene 11 (756 words 9.34 %)
        * Scene 26 (591 words 7.3 %)
        * Scene 3 (545 words 6.73 %)
     The forbidden word has been spoken 121 times