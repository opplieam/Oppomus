Parallel web crawler (Oppomus)
=======
- Take full advantage of multiple cores/CPU
- Suitable for normal to huge crawling scale
- Easy to use

Prerequisites
=======
- [requests][1]
- [beautifulsoup=3.2.1][2]

Oppomus crawl method
=======
Normal scale
- line -> Just a simple crawl method. Nothing surprise, You can see an example in the `bots/exline.py`
- nested -> In the case you need to travel into a deep structure. Oppomus let you divide the task and
  solving in a parallel way. Basic ex. You need to extract all product names in amazon. First task; collect all
  the item urls. Second task; get urls, travel and extract the name.

How to
=======
- Choose crawl method and write a bot in `bots/` package
- Customize your output style in `output.py`, e.g., write to file or CSV or JSON
- Go to `config.py` and add your bot
  - You can balance the process, delay time by yourself in advanced configuration
- Start the program by `python run.py`
- The program will automatic terminated in 30 seconds if there is no job in Output process
- You can see the logs in `logs/` directory.

To do
=======
core
- MySql config
- Beautyfulsoup4 and lxml support
- Be able to run specific bot
- Add Huge scale (Reliable and Speed crawling method)
- Change multithreading to stackless (round robin)
- Add more useful library

output support
- write to file, csv, xml, json (Library)
- output to mongodb (example)
- output to mysql (example)

future
- Cluster/Cloud support or Web interface or NLProcessing :)

Change log
=======
v0.0.1
- Automatic create `logs/` director if it doesn't exists

[1]: http://docs.python-requests.org/en/latest/
[2]: http://www.crummy.com/software/BeautifulSoup/