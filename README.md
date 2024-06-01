# Nihongo Con Teppei RSS Feed Parser
This is a simple script that takes the RSS feed (named "rss") of the Nihongo Con Teppei podcast, iterates through the enclosures within, extracts the links, and saves them to a file that's named based on what number release it is.
I created this so that I could shuffle through it easily while I commute to work, and I figured someone else might find it useful, so here it is. It probably could be written in 2 or 3 lines of bash, but 🤷.

# Usage

```bash
# Make sure you're working in the repo directory
mv RSS/FEED/FILE ./rss
pip install -r requirements.txt
python main.py
```