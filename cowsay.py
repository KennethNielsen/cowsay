#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python version of the cowsay program. The cows are nicked from the
cow files from the original program. All credits for those go to the
authors of the original cowsay.
"""

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""

from __future__ import print_function, unicode_literals
from textwrap import wrap


COWS = {
    'apt':
r"""
       \ (__)
         ({eyes})
   /------\/
  / |    ||
 *  /\---/\
    ~~   ~~
""".lstrip('\n'),
    'beavis.zen':
r"""
   \         __------~~-,
    \      ,'            ,
          /               \
         /                :
        |                  '
        |                  |
        |                  |
         |   _--           |
         _| =-.     .-.   ||
         o|/o/       _.   |
         /  ~          \ |
       (____@)  ___~    |
          |_===~~~.`    |
       _______.--~     |
       \________       |
                \      |
              __/-___-- -__
             /            _ \
""".lstrip('\n'),
    'bong':
r"""
         \
          \
            ^__^ 
    _______/(oo)
/\/(       /(__)
   | W----|| |~|
   ||     || |~|  ~~
             |~|  ~
             |_| o
             |#|/
            _+#+_
""".lstrip('\n'),
    'bud-frogs':
r"""
     \
      \
          oO)-.                       .-(Oo
         /__  _\                     /_  __\
         \  \(  |     ()~()         |  )/  /
          \__|\ |    (-___-)        | /|__/
          '  '--'    ==`-'==        '--'  '
""".lstrip('\n'),
    'bunny':
r"""
  \
   \   \
        \ /\
        ( )
      .( o ).
""".lstrip('\n'),
    'calvin':
r"""
 \                   .,
   \         .      .TR   d'
     \      k,l    .R.b  .t .Je
       \   .P q.   a|.b .f .Z%		
           .b .h  .E` # J: 2`     .
      .,.a .E  ,L.M'  ?:b `| ..J9!`.,
       q,.h.M`   `..,   ..,""` ..2"`
       .M, J8`   `:       `   3;
   .    Jk              ...,   `^7"90c.
    j,  ,!     .7"'`j,.|   .n.   ...
   j, 7'     .r`     4:      L   `...
  ..,m.      J`    ..,|..    J`  7TWi
  ..JJ,.:    %    oo      ,. ....,
    .,E      3     7`g.M:    P  41
   JT7"'      O.   .J,;     ``  V"7N.
   G.           ""Q+  .Zu.,!`      Z`
   .9.. .         J&..J!       .  ,:
      7"9a                    JM"!
         .5J.     ..        ..F`
            78a..   `    ..2'
                J9Ksaw0"'
               .EJ?A...a.
               q...g...gi
              .m...qa..,y:
              .HQFNB&...mm
               ,Z|,m.a.,dp
            .,?f` ,E?:"^7b
            `A| . .F^^7'^4,
             .MMMMMMMMMMMQzna,
         ...f"A.JdT     J:    Jp,
          `JNa..........A....af`
               `^^^^^'`
""".lstrip('\n'),
    'cheese':
r"""
   \
    \
      _____   _________
     /     \_/         |
    |                 ||
    |                 ||
   |    ###\  /###   | |
   |     0  \/  0    | |
  /|                 | |
 / |        <        |\ \
| /|                 | | |
| |     \_______/   |  | |
| |                 | / /
/||                 /|||
   ----------------|
        | |    | |
        ***    ***
       /___\  /___\
""".lstrip('\n'),
    'cock':
r"""
    \
     \  /\/\
       \   /
       |  0 >>
       |___|
 __((_<|   |
(          |	
(__________)	
   |      |
   |      |
   /\     /\
""".lstrip('\n'),
    'cower':
r"""
     \
      \
        ,__, |    | 
        (oo)\|    |___
        (__)\|    |   )\_
             |    |_w |  \
             |    |  ||   *

             Cower....
""".lstrip('\n'),
    'daemon':
r"""
   \         ,        ,
    \       /(        )`
     \      \ \___   / |
            /- _  `-/  '
           (/\/ \ \   /\
           / /   | `    \
           O O   ) /    |
           `-^--'`<     '
          (_.)  _  )   /
           `.___/`    /
             `-----' /
<----.     __ / __   \
<----|====O)))==) \) /====
<----'    `--' `.__,' \
             |        |
              \       /
        ______( (_  / \______
      ,'  ,-----'   |        \
      `--{__________)        \/
""".lstrip('\n'),
    'default':
r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
""".lstrip('\n'),
    'dragon':
r"""
      \                    / \  //\
       \    |\___/|      /   \//  \\
            /0  0  \__  /    //  | \ \    
           /     /  \/_/    //   |  \  \  
           @_^_@'/   \/_   //    |   \   \ 
           //_^_/     \/_ //     |    \    \
        ( //) |        \///      |     \     \
      ( / /) _|_ /   )  //       |      \     _\
    ( // /) '/,_ _ _/  ( ; -.    |    _ _\.-~        .-~~~^-.
  (( / / )) ,-{        _      `-.|.-~-.           .~         `.
 (( // / ))  '/\      /                 ~-. _ .-~      .-~^-.  \
 (( /// ))      `.   {            }                   /      \  \
  (( / ))     .----~-.\        \-'                 .~         \  `. \^-.
             ///.----..>        \             _ -~             `.  ^-`  ^-_
               ///-._ _ _ _ _ _ _}^ - - - - ~                     ~-- ,.-~
                                                                  /.-~
""".lstrip('\n'),
    'dragon-and-cow':
r"""
                       \                    ^    /^
                        \                  / \  // \
                         \   |\___/|      /   \//  .\
                          \  /O  O  \__  /    //  | \ \           *----*
                            /     /  \/_/    //   |  \  \          \   |
                            @___@`    \/_   //    |   \   \         \/\ \
                           0/0/|       \/_ //     |    \    \         \  \
                       0/0/0/0/|        \///      |     \     \       |  |
                    0/0/0/0/0/_|_ /   (  //       |      \     _\     |  /
                 0/0/0/0/0/0/`/,_ _ _/  ) ; -.    |    _ _\.-~       /   /
                             ,-}        _      *-.|.-~-.           .~    ~
            \     \__/        `/\      /                 ~-. _ .-~      /
             \____(oo)           *.   }            {                   /
             (    (--)          .----~-.\        \-`                 .~
             //__\\  \__ Ack!   ///.----..<        \             _ -~
            //    \\               ///-._ _ _ _ _ _ _{^ - - - - ~
""".lstrip('\n'),
    'duck':
r"""
 \
  \
   \ >()_
      (__)__ _
""".lstrip('\n'),
    'elephant':
r"""
 \     /\  ___  /\
  \   // \/   \/ \\
     ((    O O    ))
      \\ /     \ //
       \/  | |  \/ 
        |  | |  |  
        |  | |  |  
        |   o   |  
        | |   | |  
        |m|   |m|  
""".lstrip('\n'),
    'elephant-in-snake':
r"""
       \
        \  ....
          .    ........
          .            .
          .             .
    .......              .........
    ..............................
Elephant inside ASCII snake
""".lstrip('\n'),
    'eyes':
r'''
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$ 
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P 
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$# 
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$* 
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R" 
        "*$bd$$$$      '*$$$$$$$$$$$o+#" 
             """"          """"""" 
'''.lstrip('\n'),
    'flaming-sheep':
r"""
  \            .    .     .   
   \      .  . .     `  ,     
    \    .; .  : .' :  :  : . 
     \   i..`: i` i.i.,i  i . 
      \   `,--.|i |i|ii|ii|i: 
           UooU\.'@@@@@@`.||' 
           \__/(@@@@@@@@@@)'  
                (@@@@@@@@)    
                `YY~~~~YY'    
                 ||    ||     
""".lstrip('\n'),
    'ghostbusters':
r"""
          \
           \
            \          __---__
                    _-       /--______
               __--( /     \ )XXXXXXXXXXX\v.
             .-XXX(   O   O  )XXXXXXXXXXXXXXX-
            /XXX(       U     )        XXXXXXX\
          /XXXXX(              )--_  XXXXXXXXXXX\
         /XXXXX/ (      O     )   XXXXXX   \XXXXX\
         XXXXX/   /            XXXXXX   \__ \XXXXX
         XXXXXX__/          XXXXXX         \__---->
 ---___  XXX__/          XXXXXX      \__         /
   \-  --__/   ___/\  XXXXXX            /  ___--/=
    \-\    ___/    XXXXXX              '--- XXXXXX
       \-\/XXX\ XXXXXX                      /XXXXX
         \XXXXXXXXX   \                    /XXXXX/
          \XXXXXX      >                 _/XXXXX/
            \XXXXX--__/              __-- XXXX/
             -XXXXXXXX---------------  XXXXXX-
                \XXXXXXXXXXXXXXXXXXXXXXXXXX/
                  ""VXXXXXXXXXXXXXXXXXXV""
""".lstrip('\n'),
    'gnu':
r"""
    \               ,-----._
  .  \         .  ,'        `-.__,------._
 //   \      __\\'                        `-.
((    _____-'___))                           |
 `:='/     (alf_/                            |
 `.=|      |='                               |
    |)   O |                                  \
    |      |                               /\  \
    |     /                          .    /  \  \
    |    .-..__            ___   .--' \  |\   \  |
   |o o  |     ``--.___.  /   `-'      \  \\   \ |
    `--''        '  .' / /             |  | |   | \
                 |  | / /              |  | |   mmm
                 |  ||  |              | /| |
                 ( .' \ \              || | |
                 | |   \ \            // / /
                 | |    \ \          || |_|
                /  |    |_/         /_|
               /__/
""".lstrip('\n'),
    'head-in':
r"""
    \
     \
    ^__^         /
    (oo)\_______/  _________
    (__)\       )=(  ____|_ \_____
        ||----w |  \ \     \_____ |
        ||     ||   ||           ||
""".lstrip('\n'),
    'hellokitty':
r"""
  \
   \
      /\_)o<
     |      \
     | O . O|
      \_____/
""".lstrip('\n'),
    'kiss':
r"""
     \
      \
             ,;;;;;;;,
            ;;;;;;;;;;;,
           ;;;;;'_____;'
           ;;;(/))))|((\
           _;;((((((|))))
          / |_\\\\\\\\\\\\
     .--~(  \ ~))))))))))))
    /     \  `\-(((((((((((\\
    |    | `\   ) |\       /|)
     |    |  `. _/  \_____/ |
      |    , `\~            /
       |    \  \           /
      | `.   `\|          /
      |   ~-   `\        /
       \____~._/~ -_,   (\
        |-----|\   \    ';;
       |      | :;;;'     \
      |  /    |            |
      |       |            |
""".lstrip('\n'),
    'kitty':
r"""
     \
      \
       ("`-'  '-/") .___..--' ' "`-._
         ` *_ *  )    `-.   (      ) .`-.__. `)
         (_Y_.) ' ._   )   `._` ;  `` -. .-'
      _.. `--'_..-_/   /--' _ .' ,4
   ( i l ),-''  ( l i),'  ( ( ! .-'    
""".lstrip('\n'),
    'koala':
r"""
  \
   \
       ___  
     {~._.~}
      ( Y )
     ()~*~()   
     (_)-(_)   
""".lstrip('\n'),
    'kosh':
r"""
    \
     \
      \
  ___       _____     ___
 /   \     /    /|   /   \
|     |   /    / |  |     |
|     |  /____/  |  |     |     
|     |  |    |  |  |     |
|     |  | {} | /   |     |
|     |  |____|/    |     |
|     |    |==|     |     |
|      \___________/      |
|                         |
|                         |
""".lstrip('\n'),
    'luke-koala':
r"""
  \
   \          .
       ___   //
     {~._.~}// 
      ( Y )K/  
     ()~*~()   
     (_)-(_)   
     Luke    
     Skywalker
     koala   
""".lstrip('\n'),
    'mech-and-cow':
r"""
                                   ,-----.
                                   |     |
                                ,--|     |-.
                         __,----|  |     | |
                       ,;::     |  `_____' |
                       `._______|    i^i   |
                                `----| |---'| .
                           ,-------._| |== ||//
                           |       |_|P`.  /'/
                           `-------' 'Y Y/'/'
                                     .== /_
   ^__^                             /   /'|  `i
   (oo)_______                   /'   /  |   |
   (__)       )/             /'    /   |   `i
       ||----w |           ___,;`----'.___L_,-'`__
       ||     ||          i_____;----.____i""____
""".lstrip('\n'),
    'meow':
r"""
  \
   \ ,   _ ___.--'''`--''//-,-_--_.
      \`"' ` || \\ \ \\/ / // / ,-\\`,_
     /'`  \ \ || Y  | \|/ / // / - |__ `-,
    /@"\  ` \ `\ |  | ||/ // | \/  \  `-._`-,_.,
   /  _.-. `.-\,___/\ _/|_/_\_\/|_/ |     `-._._)
   `-'``/  /  |  // \__/\__  /  \__/ \
        `-'  /-\/  | -|   \__ \   |-' |
          __/\ / _/ \/ __,-'   ) ,' _|'
         (((__/(((_.' ((___..-'((__,'
""".lstrip('\n'),
    'milk':
r"""
 \     ____________ 
  \    |__________|
      /           /\
     /           /  \
    /___________/___/|
    |          |     |
    |  ==\ /== |     |
    |   O   O  | \ \ |
    |     <    |  \ \|
   /|          |   \ \
  / |  \_____/ |   / /
 / /|          |  / /|
/||\|          | /||\/
    -------------|   
        | |    | | 
       <__/    \__>
""".lstrip('\n'),
    'moofasa':
r"""
       \    ____
        \  /    \
          | ^__^ |
          | (oo) |______
          | (__) |      )\/\
           \____/|----w |
                ||     ||

	         Moofasa
""".lstrip('\n'),
    'moose':
r"""
  \
   \   \_\_    _/_/
    \      \__/
           (oo)\_______
           (__)\       )\/\
               ||----w |
               ||     ||
""".lstrip('\n'),
    'mutilated':
r"""
       \   \_______
 v__v   \  \   O   )
 (oo)      ||----w |
 (__)      ||     ||  \/\
""".lstrip('\n'),
    'pony':
r"""
       \          /\/\
        \         \/\/
         \        /   -\
          \     /  oo   -\
           \  /           \
             |    ---\    -\
             \--/     \     \
                       |      -\
                        \       -\         -------------\    /-\
                         \        \-------/              ---/    \
                          \                                  |\   \
                           |                                 / |  |
                           \                                |  \  |
                            |                              /    \ |
                            |                             /     \ |
                             \                             \     \|
                              -              /--------\    |      o
                               \+   +---------          \   |
                                |   |                   |   \
                                |   |                    \   |
                                |   |                    |   \
                                |   |                     \   |
                                 \  |                     |   |
                                 |  |                      \  \
                                 |  |                      |   |
                                 +--+                       ---+
""".lstrip('\n'),
    'pony-smaller':
r"""
     \      _^^
      \   _- oo\
          \----- \______
                \       )\
                ||-----|| \
                ||     ||
""".lstrip('\n'),
    'ren':
r"""
   \
    \
    ____  
   /# /_\_
  |  |/o\o\
  |  \\_/_/
 / |_   |  
|  ||\_ ~| 
|  ||| \/  
|  |||_    
 \//  |    
  ||  |    
  ||_  \   
  \_|  o|  
  /\___/   
 /  ||||__ 
    (___)_)
""".lstrip('\n'),
    'sheep':
r"""
  \
   \
       __     
      UooU\.'@@@@@@`.
      \__/(@@@@@@@@@@)
           (@@@@@@@@)
           `YY~~~~YY'
            ||    ||
""".lstrip('\n'),
    'skeleton':
r"""
          \      (__)      
           \     /oo|  
            \   (_"_)*+++++++++*
                   //I#\\\\\\\\I\
                   I[I|I|||||I I `
                   I`I'///'' I I
                   I I       I I
                   ~ ~       ~ ~
                     Scowleton
""".lstrip('\n'),
    'snowman':
r'''
   \
 ___###
   /oo\ |||
   \  / \|/
   /""\  I
()|    |(I)
   \  /  I
  /""""\ I
 |      |I
 |      |I
  \____/ I
'''.lstrip('\n'),
    'sodomized-sheep':
r"""
  \                 __ 
   \               (oo)
    \              (  )
     \             /--\
       __         / \  \ 
      UooU\.'@@@@@@`.\  )
      \__/(@@@@@@@@@@) /
           (@@@@@@@@)(( 
           `YY~~~~YY' \\
            ||    ||   >> 
""".lstrip('\n'),
    'stegosaurus':
r"""
\                             .       .
 \                           / `.   .' " 
  \                  .---.  <    > <    >  .---.
   \                 |    \  \ - ~ ~ - /  /    |
         _____          ..-~             ~-..-~
        |     |   \~~~\.'                    `./~~~/
       ---------   \__/                        \__/
      .'  O    \     /               /       \  " 
     (_____,    `._.'               |         }  \/~~~/
      `----.          /       }     |        /    \__/
            `-.      |       /      |       /      `. ,~~|
                ~-.__|      /_ - ~ ^|      /- _      `..-'   
                     |     /        |     /     ~-.     `-. _  _  _
                     |_____|        |_____|         ~ - . _ _ _ _ _>
""".lstrip('\n'),
    'stimpy':
r"""
  \     .    _  .    
   \    |\_|/__/|    
       / / \/ \  \  
      /__|O||O|__ \ 
     |/_ \_/\_/ _\ |  
     | | (____) | ||  
     \/\___/\__/  // 
     (_/         ||
      |          ||
      |          ||\   
       \        //_/  
        \______//
       __ || __||
      (____(____)
""".lstrip('\n'),
    'suse':
r"""
  \
   \____
  /@    ~-.
  \/ __ .- |
   // //  @
""".lstrip('\n'),
    'three-eyes':
r"""
        \  ^___^
         \ (ooo)\_______
           (___)\       )\/\
                ||----w |
                ||     ||
""".lstrip('\n'),
    'turkey':
r"""
  \                                  ,+*^^*+___+++_
   \                           ,*^^^^              )
    \                       _+*                     ^**+_
     \                    +^       _ _++*+_+++_,         )
              _+^^*+_    (     ,+*^ ^          \+_        )
             {{       )  (    ,(    ,_+--+--,      ^)      ^\
            {{ (@)    }} f   ,(  ,+-^ __*_*_  ^^\_   ^\       )
           {{:;-/    (_+*-+^^^^^+*+*<_ _++_)_    )    )      /
          ( /  (    (        ,___    ^*+_+* )   <    <      \
           U _/     )    *--<  ) ^\-----++__)   )    )       )
            (      )  _(^)^^))  )  )\^^^^^))^*+/    /       /
          (      /  (_))_^)) )  )  ))^^^^^))^^^)__/     +^^
         (     ,/    (^))^))  )  ) ))^^^^^^^))^^)       _)
          *+__+*       (_))^)  ) ) ))^^^^^^))^^^^^)____*^
          \             \_)^)_)) ))^^^^^^^^^^))^^^^)
           (_             ^\__^^^^^^^^^^^^))^^^^^^^)
             ^\___            ^\__^^^^^^))^^^^^^^^)\\
                  ^^^^^\u005cuuu/^^\u005cuuu/^^^^\^\^\^\^\^\^\^\
                     ___) >____) >___   ^\_\_\_\_\_\_\)
                    ^^^//\\_^^//\\_^       ^(\_\_\_\)
                      ^^^ ^^ ^^^ ^
""".lstrip('\n'),
    'turtle':
r"""
    \                                  ___-------___
     \                             _-~~             ~~-_
      \                         _-~                    /~-_
             /^\__/^\         /~  \                   /    \
           /|  O|| O|        /      \_______________/        \
          | |___||__|      /       /                \          \
          |          \    /      /                    \          \
          |   (_______) /______/                        \_________ \
          |         / /         \                      /            \
           \         \^\\         \                  /               \     /
             \         ||           \______________/      _-_       //\__//
               \       ||------_-~~-_ ------------- \ --/~   ~\    || __/
                 ~-----||====/~     |==================|       |/~~~~~
                  (_(__/  ./     /                    \_\      \.
                         (_(___/                         \_____)_)
""".lstrip('\n'),
    'tux':
r"""
   \
    \
        .--.
       |o_o |
       |:_/ |
      //   \ \
     (|     | )
    /'\_   _/`\
    \___)=(___/
""".lstrip('\n'),
    'unipony':
r"""
   \             \
    \             \_
     \             \\
      \             \\/\
       \            _\\/
        \         /   -\
         \      /  oo   -\
          \   /           \
             |    ---\    -\
             \--/     \     \
                       |      -\
                        \       -\         -------------\    /-\
                         \        \-------/              ---/    \
                          \                                  |\   \
                           |                                 / |  |
                           \                                |  \  |
                            |                              /    \ |
                            |                             /     \ |
                             \                             \     \|
                              -              /--------\    |      o
                               \+   +---------          \   |
                                |   |                   |   \
                                |   |                    \   |
                                |   |                    |   \
                                |   |                     \   |
                                 \  |                     |   |
                                 |  |                      \  \
                                 |  |                      |   |
                                 +--+                       ---+
""".lstrip('\n'),
    'unipony-smaller':
r"""
   \        \
    \        \
     \       _\^
      \    _- oo\
           \---- \______
                 \       )\
                ||-----||  \
                ||     ||
""".lstrip('\n'),
    'vader':
r"""
        \    ,-^-.
         \   !oYo!
          \ /./=\.\______
               ##        )\/\
                ||-----w||
                ||      ||

               Cowth Vader
""".lstrip('\n'),
    'vader-koala':
r"""
   \
    \        .
     .---.  //
    Y|o o|Y// 
   /_(i=i)K/ 
   ~()~*~()~  
    (_)-(_)   

     Darth 
     Vader    
     koala        
""".lstrip('\n'),
    'www':
r"""
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||--WWW |
                ||     ||
""".lstrip('\n'),
}


#eyes


def list_cows():
    """List the available cow avatars"""
    return COWS.keys()


class Cowsay(object):
    """"""

    def __init__(self, cow='default', eyes='oo', width=40):
        """Initialize the internal variables.

        Args:
            cow (str): The cow to use. Use the module functions list_cows to
                see which avatars can be used
        """
        try:
            self.cow = COWS[cow]
        except KeyError:
            message = 'Cow \'{}\' is unknown. Only {} are allowed'\
                .format(cow, list(COWS.keys()))
            raise ValueError(message)

        self.width = width
        if not isinstance(eyes, unicode) or len(eyes) != 2:
            message = 'eyes must be str of lenght 2'
            raise ValueError(message)
        self.eyes = eyes

    def say(self, text):
        """Make the cow say something"""
        wrapped_lines = wrap(text, self.width)
        text_width = max(len(line) for line in wrapped_lines)
        print(' {}'.format('_' * (text_width + 2)))
        template = '{{}} {{: <{}}} {{}}'.format(text_width)
        if len(wrapped_lines) == 1:
            print(template.format('<', wrapped_lines[0], '>'))
        else:
            for line_num, line in enumerate(wrapped_lines):
                if line_num == 0:
                    left, right = '/', '\\'
                elif line_num == len(wrapped_lines) - 1:
                    left, right = '\\', '/'
                else:
                    left, right = '|', '|'
                print(template.format(left, line, right))

        print(' {}'.format('-' * (text_width + 2)))
        print(self.cow.format(eyes=self.eyes))

    


if __name__ == '__main__':
    COW = Cowsay(cow='turkey')
    COW.say("Live long and prosper")
