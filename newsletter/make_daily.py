#!/usr/bin/env python3
"""Daily newsletter builder. Edit ONLY the content fields in dict v (and the plain-text replacements) for today, then run:
   python3 make_daily.py   -> writes /mnt/user-data/outputs/newsletter-<DATE>.html/.txt/-subject.txt/.png
Needs: npm i playwright @fontsource/archivo-black @fontsource/outfit @fontsource/jetbrains-mono in /tmp/sc (done below if missing).
Repo path: /home/claude/wall-street-awards. DATE_TAG below must be today's YYYY-MM-DD."""
import os,subprocess
DATE_TAG='2026-11-26'
if not os.path.exists('/tmp/sc/node_modules/@fontsource'):
    os.makedirs('/tmp/sc',exist_ok=True)
    subprocess.run('cd /tmp/sc && npm i playwright @fontsource/archivo-black @fontsource/outfit @fontsource/jetbrains-mono >/dev/null 2>&1',shell=True)
os.makedirs('/tmp/nl',exist_ok=True)
SHOT="const {chromium}=require('/tmp/sc/node_modules/playwright');\n(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium',args:['--no-sandbox']});\nconst p=await b.newPage({viewport:{width:600,height:900},deviceScaleFactor:2});\nawait p.goto('file:///tmp/nl/render.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(400);\nawait p.screenshot({path:'/mnt/user-data/outputs/newsletter-2026-11-25.png',fullPage:true});await b.close();})();\n"
open('/tmp/nl/shot.js','w').write(SHOT.replace('newsletter-2026-11-25',"newsletter-'+DATE_TAG+'") if False else SHOT)
import re
src=open('/home/claude/wall-street-awards/newsletter/build.py').read()
src=src.split('def fontcss')[0]
exec(src)
import base64
G=f'<span style="color:{GOLD};">'
d='/tmp/sc/node_modules/@fontsource/'
def f(fam,path,w):
    b=base64.b64encode(open(d+path,'rb').read()).decode()
    return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"
fonts='<style>'+f('Archivo Black','archivo-black/files/archivo-black-latin-400-normal.woff2',400)+f('Outfit','outfit/files/outfit-latin-400-normal.woff2',400)+f('Outfit','outfit/files/outfit-latin-700-normal.woff2',700)+f('JetBrains Mono','jetbrains-mono/files/jetbrains-mono-latin-400-normal.woff2',400)+f('JetBrains Mono','jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2',700)+'</style>'
v={'SUBJ':'Dow erases a 1,100-point drop','PRE':'Markets are closed today. Here is what happened Wednesday.','DATE':'THU NOV 26, 2026','ALT':'Dow recovers from a 1,100-point drop',
'HEADLINE':f'Dow {G}erases a 1,100-point drop</span> in a wild reversal.',
'NEWS':'U.S. stocks reversed hard on Wednesday. The Dow was down more than 1,100 points at its low, per GSM Global News, then closed up 0.3%, per AP and Yahoo Finance. The Nasdaq ended down about 0.6%. An AI selloff, a hot inflation report and new tariff plans all hit the tape. U.S. markets are closed today for Thanksgiving.',
'T1':('DOW WED','+0.3%',GREEN),'T2':('S&amp;P 500 WED','-0.3%',RED),'T3':('NASDAQ WED','-0.6%',RED),
'NUMNOTE':'Wednesday closing figures, per AP and Yahoo Finance. Markets are closed Thursday.',
'BUL':['Watch Friday. Markets reopen for a half day and close at 1:00 PM ET, per Yahoo Finance and GSM Global News. Thin volume can make moves jumpy.','Study the reversal. Core PCE rose 3.3% from a year ago against 3.2% expected, per Yahoo Finance. Traders also price about a 98% chance of a December Fed rate hike, per Yahoo Finance. Watch how stocks react to that.'],
'QA':[('Why are markets closed today?','U.S. stock and bond markets are closed for Thanksgiving, per Yahoo Finance. They reopen Friday for a half day.')],
'MIDBTN':'BOOK A CALL','NOTE':'Sniper, Wednesday was a lesson in the tape. The Dow fell more than 1,100 points, then closed higher. Same day. Same headlines. The number that mattered was the reaction, not the first move. Core PCE came in at 3.3% against 3.2% expected, per Yahoo Finance. Rate-hike odds for December sit near 98%, per the same source. That is what the market is pricing, and it can hit tech first. I do not chase the panic candle. I wait for the data, then I watch who buys the dip. Emotions run the tape. Problem solvers do not panic. They pivot. Hit reply and tell me what you are watching.',
'CTATEXT':'Join our community and learn how to profit from the news. Book a call to get started.','TRUST':'2,000+ students have learned with us. On the call, we show you your next step.','CTABTN':'BOOK A CALL','CTAURL':'https://www.optionssnipersuniversity.com/book-call-now','PS':'Not sure where to start? We will point you to your next step.','PSLINK':'Book your call here.','SRC':'AP, Yahoo Finance and GSM Global News'}
logo='https://raw.githubusercontent.com/optionssnipers/wall-street-awards/main/newsletter/osu-logo.png'
open(f'/mnt/user-data/outputs/newsletter-{DATE_TAG}.html','w').write(page(v,logo,'',fonts='',ICON=''))
open('/tmp/nl/render.html','w').write(page(v,'/home/claude/wall-street-awards/newsletter/osu-logo.png','',fonts=fonts,ICON=''))
t=open('/home/claude/wall-street-awards/newsletter/email-plain-text.txt').read()
rep={'[[DATE]]':v['DATE'],'[[HEADLINE]]':'Dow erases a 1,100-point drop in a wild reversal.',
'[[One sentence per line.]]':v['NEWS'].replace('. ','.\n'),
'[[T1_NAME]] [[T1_MOVE]]':'DOW WED +0.3%','[[T2_NAME]] [[T2_MOVE]]':'S&P 500 WED -0.3%','[[T3_NAME]] [[T3_MOVE]]':'NASDAQ WED -0.6%',
'[[MONEY_IDEA_1: level or event to watch, with a number]]':v['BUL'][0],'[[MONEY_IDEA_2: how a trader plays it]]':v['BUL'][1],
'[[Q1]]':v['QA'][0][0],'[[A1]]':v['QA'][0][1],'[[WASI NOTE]] Hit reply and tell me what you are watching.':v['NOTE'],
'[[BOOKING_LINK]]':v['CTAURL'],'[[SOURCES]]':v['SRC']}
for k,x in rep.items(): t=t.replace(k,x)
t=t.replace('- Know the risk. Options can lose all the money you put in. Only use money you can afford to lose.\n','')
open(f'/mnt/user-data/outputs/newsletter-{DATE_TAG}.txt','w').write(t)
open(f'/mnt/user-data/outputs/newsletter-{DATE_TAG}-subject.txt','w').write('SUBJECT: '+v['SUBJ']+'\nPREHEADER: '+v['PRE']+'\n')
print(re.findall(r'\[\[.*?\]\]',t))

shot=open('/tmp/nl/shot.js').read().replace('newsletter-2026-11-25.png','newsletter-%s.png'%DATE_TAG)
open('/tmp/nl/shot.js','w').write(shot)
subprocess.run(['node','/tmp/nl/shot.js'],check=True)
print('done',DATE_TAG)
