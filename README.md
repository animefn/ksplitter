# ksplitter
A python tool to split karaoke songs (romaji syl, char, words) for Aegisub without having to know the splitting rules for jp romaji. It saves about 10-15 minutes per song, and avoids you the annoying process of having to go through each word and having to split it. the syl splitting mode is intended for use with Japanese romaji and thus follows rules suitable for Japanese only, the result will be weird with other languages.

**Please note: you Still have to adjust the timing of each syllable by yourself, this really just a replacement for the annoying process of going through each line, put separtors and clicking "accept split" in Aegisub**

## motivation
1. it saves a few minutes if you're lazy
2. You don't need to know the splitting rules. For example, I see people splitting "tsuki" to t.su.ki or "shinjiru" to shin.ji.ru which is wrong since tsu/n should be 1 syllable (correct form: tsu.ki shi.n.ji.ru). There are some other mistakes I see in  Karaoke too, so this tool should help eliminate those mistakes.

## Easiest and simplest: Run online without installation
If you don't want to download the tool just use our web version available here: https://fansubbers.animefn.com/webkarasplitter/   
video demo: https://streamable.com/0j6uf2  or  https://youtu.be/-M_bBIHPhzc or https://fansubbers.animefn.com/webkarasplitter/demo.asf



## Run on windows:
If you want to run it on widnows without installing python just grab the .exe from releases.

## Run
Just download the .py file and run it with python 3. No special requirements.

## Usage 
>>> python ksplitter.py -h

```usage: ksplitter.py [-h] -s  [-sv] [-syl | -char | -word] -f

does the k-split for aegisub karaoke (you have to adjust the timing by
yourself after splitting)

optional arguments:
  -h, --help            show this help message and exit
  -s , --selector       criteria of lines to apply the script on: all , actor
                        or style
  -sv , --selectorvalue
                        if you choose actor or style, specify the name here,
                        use "" for names with spaces "op kara"
  -syl, --syllables     makes splitting by romaji syl (default) [only pick one
                        the three char,syl,word]
  -char, --characters   makes splitting after each character[only pick one the
                        three char,syl,word]
  -word, --word         makes splitting after each word[only pick one the
                        three char,syl,word]
  -f , --filename       rel or abs path for the .ass file
```
### usage examples
if you're using the .py script 
you will have to run it with `python3 ksplitter.py ...` if you're using the exe provided in releases just replace it with `ksplitter.exe ...`

if you have a file that only contains the song lyrics that you want to split you don't need to specify a style name or an actor
`python ksplitter.py  -f sc.ass -s all  `

if sc.ass is in the same folder as the script, and you want to run the script on all lines with the style called op kara (the syl option will be used by default):
`python ksplitter.py  -f sc.ass -s style -sv "op kara"  `

If you want to split after each words (for example for English) you can use -word option:
`python ksplitter.py  -f sc.ass -s style -sv "op kara" -word `



### Batch usage 
Sometimes you might have multiple files each containing the lyrics of a song so You might want to apply it on all files at once. Just gather all your .ass 
#### Batch usage on Windows (for multiple files)
save this in a batch.bat file in the same folder as ksplitter.exe avaliable in releases section
` for %%A IN (*.ass) DO ksplitter.exe -f "%%A" -s all"`

#### batch usage on Linux/bash (for multiple files)
`for file in *.ass; do python ksplitter.py  -f "$file" -s all; done`



## known isses + workaround/tricks
In some Japanese songs they use English.
If you have some lines that are fully in English, they will be splitted following the Romaji splitting method, resulting in a weird split that does not make sense. So instead of applying the script to all lines of your karaoke manually add actors in Aegisub for English lines for example add "karaEN" and for Japanese lines "karaJP"

Then:
Split the Japanese words with nomral syl split (you don't have to specify -syl since it's the mode by default)
`python ksplitter.py  -f sc.ass -s actor -sv "karaJP" -syl `
Split the English words with  -word split (you  have to specify -word since it's not the mode by default)
`python ksplitter.py  -f sc.ass -s actor -sv "karaEN" -word `

For Hyrbid lines containing 

## Disclaimer

This tool is provided as is without warrant of any kind.
Feel free to report bugs.

Provided to you with love by Animefn.com :) 
