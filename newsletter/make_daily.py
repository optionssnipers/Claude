#!/usr/bin/env python3
"""Daily newsletter builder. Edit ONLY the content fields in dict v (and the plain-text replacements) for today, then run:
   python3 make_daily.py   -> writes /mnt/user-data/outputs/newsletter-<DATE>.html/.txt/-subject.txt/.png
Needs: npm i playwright @fontsource/archivo-black @fontsource/outfit @fontsource/jetbrains-mono in /tmp/sc (done below if missing).
Repo path: /home/claude/wall-street-awards. DATE_TAG below must be today's YYYY-MM-DD."""
import os,subprocess
DATE_TAG='2026-11-27'
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
v={'SUBJ':'Stocks reopen for a half day','PRE':'Short session today. Stocks close at 1:00 PM ET.','DATE':'FRI NOV 27, 2026','ALT':'Stocks reopen for a half day',
'HEADLINE':f'Stocks {G}reopen for a half day</span> as tech tries to rebound.',
'NEWS':'U.S. stocks reopen today after the Thanksgiving break for a short session that ends at 1:00 PM ET, per TipRanks and Oninvest. Futures pointed higher before the open, led by tech, per TipRanks. Wednesday was split. The Dow closed up 0.3%, while the S&P 500 fell 0.3% and the Nasdaq Composite fell 0.6%, per Zacks and Oninvest. A proposal for new tariffs on 14 economies hit AI stocks, per Zacks and Oninvest.',
'T1':('DOW WED','+0.3%',GREEN),'T2':('S&amp;P 500 WED','-0.3%',RED),'T3':('NASDAQ WED','-0.6%',RED),
'NUMNOTE':'Wednesday closing figures, per Zacks and Oninvest. Markets were closed Thursday.',
'BUL':['Watch the clock. Stocks trade 9:30 AM to 1:00 PM ET today, per TipRanks and Oninvest. Thin volume can make moves jumpy.','Study the AI names. Nvidia, Micron and Oracle each fell roughly 4% to 5% on Wednesday after the tariff headlines, per Zacks and Oninvest. Watch whether they bounce or fade.'],
'QA':[('Why is today a short day?','Stocks close early at 1:00 PM ET the day after Thanksgiving, per TipRanks. Fewer traders are around, so volume is light.')],
'MIDBTN':'BOOK A CALL','NOTE':'Sniper, today is a half day. Trading runs 9:30 AM to 1:00 PM ET, per TipRanks and Oninvest. Thin volume can make price jump on small orders. Wednesday showed a split tape. The Dow closed higher while the Nasdaq fell, per Zacks and Oninvest. That tells me money is picking spots, not buying everything. I do not chase a gap in a short session. I wait for the data, then I watch the reaction. Emotions run the tape. Problem solvers do not panic. They pivot. Hit reply and tell me what you are watching.',
'CTATEXT':'Join our community and learn how to profit from the news. Book a call to get started.','TRUST':'2,000+ students have learned with us. On the call, we show you your next step.','CTABTN':'BOOK A CALL','CTAURL':'https://www.optionssnipersuniversity.com/book-call-now','PS':'Not sure where to start? We will point you to your next step.','PSLINK':'Book your call here.','SRC':'TipRanks, Zacks and Oninvest'}
logo='https://raw.githubusercontent.com/optionssnipers/wall-street-awards/main/newsletter/osu-logo.png'
open(f'/mnt/user-data/outputs/newsletter-{DATE_TAG}.html','w').write(page(v,logo,'',fonts='',ICON=''))
open('/tmp/nl/render.html','w').write(page(v,'/home/claude/wall-street-awards/newsletter/osu-logo.png','',fonts=fonts,ICON=''))
t=open('/home/claude/wall-street-awards/newsletter/email-plain-text.txt').read()
rep={'[[DATE]]':v['DATE'],'[[HEADLINE]]':'Stocks reopen for a half day as tech tries to rebound.',
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
