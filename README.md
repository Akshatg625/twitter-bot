# Twitter-Bot

<b>Languages Used :</b>Python

## Features Currently available:
<pre>
    1) Automatic retweet, like and follow
    2) Find trending
    3) Hashtags to search
    4) Find people and information about them
</pre>
<h1><u>Installing Instructions</h1></u>
<code><pre>
git clone https://github.com/ashwani-rathee/Twitter-Bot.git
cd Twitter-Bot
#Update the credentials you found from your Twitter Developer Website
pip install requirements.txt
python3 Twitter-Bot.py
</pre>
</code>
<h1>Exploring GPT-2</h1>
We fine-tuned the GPT-2 language model (345 and 124 million parameters) on quotes,shakespeare text to create AI versions of them.
###(Yet to DO)and then had the bots rewrite real tweets or complete tweets based on various prompts (short sentence starters like “The meaning of life is”).

Some of these are funny, some are profound, some are dark in a way that make us pause for a second.
## On Ubuntu 20.04
-mkdir gpt-2
-cd gpt-2
- conda create --name gpt-2 python=3.6
- conda activate gpt-2
- git clone https://github.com/openai/gpt-2.git && cd gpt-2
- pip3 install tensorflow==1.12.0 #won't install as not available
- ##instead install any tensorflow==1.x
- #closest to original
- pip3 install tensorflow==1.13.0rc1
- #tensorflow.__version__
- '1.13.0-rc1'
- pip3 install -r requirements.txt
- python3 download_model.py  modelname#124M,355M...




<h1>Contributors</h1>
See ![Contributions.md](https://github.com/ashwani-rathee/Twitter-Bot/blob/main/contributions.md)
<br>
<ol>
    <li>Ashwani Rathee</li>
    <li>Akshat Gupta</li>
</ol>
<br>
<h1><u>References</u></h1>
<ol>
    <li>Notebook by Max Woolf:https://colab.research.google.com/drive/1VLG8e7YSEwypxU-noRNhsv5dW4NfTGce#scrollTo=H7LoMj4GA4n_</li>
    <li>Blog Post:https://minimaxir.com/2020/01/twitter-gpt2-bot</li>
    <li>https://minimaxir.com/2019/09/howto-gpt2/</li>
    <li>GPT-2 Twitter Bot:https://github.com/ShaneZhong/gpt-2-twitter-bot</li>
</ol>
