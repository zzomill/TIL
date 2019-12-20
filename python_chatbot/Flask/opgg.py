from flask import Flask, escape, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgg2')
def opgg2():
    userName = request.args.get('userName')
    url = f'http://www.op.gg/summoner/userName={userName}'
    req = requests.get(url).text

    soup = BeautifulSoup(req, 'html.parser')
    tier = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank')
    win = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
#    win = win[:-1]
    return render_template('opgg2.html', userName = userName, tier = tier.text, win = win.text[:-1])

if __name__ == ("__main__"):
    app.run(debug=True) 