#!/usr/bin/env python3
"""Daily newsletter builder. Edit ONLY the content fields in dict v (and the plain-text replacements) for today, then run:
   python3 make_daily.py   -> writes /mnt/user-data/outputs/newsletter-<DATE>.html/.txt/-subject.txt/.png
Needs: npm i playwright @fontsource/archivo-black @fontsource/outfit @fontsource/jetbrains-mono in /tmp/sc (done below if missing).
Repo path: /home/claude/wall-street-awards. DATE_TAG below must be today's YYYY-MM-DD."""
import os,subprocess
DATE_TAG='2026-11-25'
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
v={'SUBJ':'Futures sink as the AI selloff spreads','PRE':'Tariff news and a big inflation report hit this morning.','DATE':'WED NOV 25, 2026','ALT':'Stock futures fall before the open',
'HEADLINE':f'Stock futures are {G}down big</span> before the open.',
'NEWS':'U.S. stock futures fell early Wednesday as the AI selloff spread. Nasdaq-100 futures were down more than 2%, per Yahoo Finance and TipRanks. Reports say new tariffs on 16 trading partners are coming.',
'T1':('NASDAQ FUTURES','-2%+',RED),'T2':('NASDAQ TUE','-1.5%',RED),'T3':('S&amp;P 500 TUE','-0.5%',RED),
'NUMNOTE':'Tuesday figures are closes. Futures are early signals, not final prices.',
'BUL':['Watch 8:30 AM ET. The PCE inflation report is due. It is expected to show prices up 0.3% in October and 3.8% from a year ago.','Pick a side. A put option may gain if stocks keep falling. A call option may gain if they bounce. Many traders wait until the report is out.','Know the risk. Options can lose all the money you put in. Only use money you can afford to lose.'],
'QA':[('Will prices go up because of tariffs?','Reports say new tariffs are coming, but rates and dates are not confirmed. Prices may rise on some imported goods if they go ahead.')],
'MIDBTN':'BOOK A CALL','NOTE':'Here is how I see it. One red morning does not change the plan. I wait for the report, then I watch my level. Hit reply and tell me what you are watching.',
'CTATEXT':'Join our community and learn how to profit from the news. Book a call to get started.','TRUST':'2,000+ students have learned with us. On the call, we show you your next step.','CTABTN':'BOOK A CALL','CTAURL':'https://www.optionssnipers.ai','PS':'Not sure where to start? We will point you to your next step.','PSLINK':'Book your call here.','SRC':'Yahoo Finance, TipRanks and Rallies.ai'}
logo='https://raw.githubusercontent.com/optionssnipers/wall-street-awards/main/newsletter/osu-logo.png'
open(f'/mnt/user-data/outputs/newsletter-{DATE_TAG}.html','w').write(page(v,logo,'',fonts='',ICON=''))
open('/tmp/nl/render.html','w').write(page(v,'/home/claude/wall-street-awards/newsletter/osu-logo.png','',fonts=fonts,ICON=''))
t=open('/home/claude/wall-street-awards/newsletter/email-plain-text.txt').read()
rep={'[[DATE]]':v['DATE'],'[[HEADLINE]]':'Stock futures are down big before the open.',
'[[One sentence per line.]]':v['NEWS'].replace('. ','.\n'),
'[[T1_NAME]] [[T1_MOVE]]':'NASDAQ FUTURES -2%+','[[T2_NAME]] [[T2_MOVE]]':'NASDAQ TUE -1.5%','[[T3_NAME]] [[T3_MOVE]]':'S&P 500 TUE -0.5%',
'[[MONEY_IDEA_1: level or event to watch, with a number]]':v['BUL'][0],'[[MONEY_IDEA_2: how a trader plays it]]':v['BUL'][1],
'[[Q1]]':v['QA'][0][0],'[[A1]]':v['QA'][0][1],'[[WASI NOTE]] Hit reply and tell me what you are watching.':v['NOTE'],
'[[BOOKING_LINK]]':v['CTAURL'],'[[SOURCES]]':v['SRC']}
for k,x in rep.items(): t=t.replace(k,x)
t=t.replace('- Know the risk. Options can lose all the money you put in. Only use money you can afford to lose.','- '+v['BUL'][2])
open(f'/mnt/user-data/outputs/newsletter-{DATE_TAG}.txt','w').write(t)
open(f'/mnt/user-data/outputs/newsletter-{DATE_TAG}-subject.txt','w').write('SUBJECT: '+v['SUBJ']+'\nPREHEADER: '+v['PRE']+'\n')
print(re.findall(r'\[\[.*?\]\]',t))

shot=open('/tmp/nl/shot.js').read().replace('newsletter-2026-11-25.png','newsletter-%s.png'%DATE_TAG)
open('/tmp/nl/shot.js','w').write(shot)
subprocess.run(['node','/tmp/nl/shot.js'],check=True)
print('done',DATE_TAG)
