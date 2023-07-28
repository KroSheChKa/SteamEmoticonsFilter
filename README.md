# SteamEmoticonsFilter

A program that filters your emoticons in Steam
------

I have **a lot of** Steam emoticons that I make a gradient out of and put in a showcase in my profile like this:

![image](https://github.com/KroSheChKa/SteamEmoticonsFilter/assets/104899233/8769114b-2938-44cc-a41e-e8ab313a2b28)

> Emoticons were passed through the algorithm 

To do this, I use [steam.tools](https://steam.tools/mosaticon/) to get a string of Hue-sorted emoticons (I can't say it's done in a cool way tho. **So I think I will add a new hue-sorting method in future commits**). But every time I *get new ones*/*sell some*, I have to do it all over again - removing the "terrible" emoticons from the string. I also have to remove duplicates manually.

----

**What the program can do:**
- removes duplicates
- removes blacklist emoticons
- сhange the order of emoticons and distribute them to different number of showcases by changing [this](https://github.com/KroSheChKa/SteamEmoticonsFilter/edit/main/README.md#setting-preferences) preferences

# Setting preferences
You can change them in the beginning of the main() function.

***invert_emoticons*** - Inverts the order of emoticons no matter how you sort them.
- `1` - keep unchanged
- `-1` - invert emoticons

***showcase_count*** - Number of desired showcases. 

***split_type*** - Different types of distribution of emoticons in the storefront
- `0` - Cuts the emoticons right under the ***character limit***.
  > **It may not fill all desired showcases**, as there might be *not enough* emoticons to completely *cover* all of them.
- `1` - Distributes the emoticons equally among all showcases.


***character_limit*** - Limitation of the number of emoticons in one showcase. 8000 - default value.
> Works only if `split_type = 0`

# How to launch

A few steps:
- Make sure you have installed [python 3.X](https://www.python.org/downloads/) (Better to download 3.10)
- Clone this project by command below or you can just download it as **.zip**:
```
git clone https://github.com/KroSheChKa/SteamEmoticonsFilter.git
```
> **Make sure you have downloaded [git](https://git-scm.com/downloads)!**
- Open cmd and paste this:
```
pip install numpy
```
- There are **2 files** you need to **modify** in `Text Files` folder:
  
  - In `Emoticons.txt` paste string from [steam.tools](https://steam.tools/mosaticon/) in **one line** (Here will be Steam guide in future)
  - In `BlackList` add emoticons that you don't want to see in result string (also paste in **one line** without spaces) like this:

    ```
    :example::example1::example2::ect_examples:
    ```

- The final step. Just double-click on the `SEF.py` and **copy** the result string in the `Results.txt` file :)

---
  
*Any suggestions? You found a flaw?*

-> Welcome to [Discussions](https://github.com/KroSheChKa/SteamEmoticonsFilter/discussions)
