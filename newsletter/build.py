import base64,re
def nl(t): return re.sub(r'(?<=[.?!])\s+(?=[A-Z"\[])','<br>',t)
GOLD='#F5C842'; GOLD2='#D4A437'; BG='#0A0A0A'; PANEL='#141414'; LINE='#3a2f14'; TXT='#E9E9E9'; MUTED='#9a9a9a'; RED='#E63946'; GREEN='#06D6A0'
H="font-family:'Archivo Black','Arial Black',Arial,sans-serif;"
B="font-family:'Outfit',Arial,Helvetica,sans-serif;"
M="font-family:'JetBrains Mono','Courier New',monospace;"
def sec(n,label,body,pad='22px 26px'):
    return f'''<tr><td style="padding:{pad};border-top:1px solid {LINE};"><div style="{M}font-size:12px;font-weight:bold;letter-spacing:3px;color:{GOLD};margin-bottom:12px;">[{n}] &nbsp;{label}</div>{body}</td></tr>'''
def chip(n,m,c=RED):
    return f'<td width="33%" style="padding:4px;"><div style="background:{PANEL};border:1px solid {LINE};border-radius:6px;padding:12px 6px;text-align:center;"><div style="{M}font-size:11px;letter-spacing:2px;color:{MUTED};">{n}</div><div style="{M}font-size:24px;font-weight:bold;color:{c};">{m}</div></div></td>'
def corners(top=True):
    b='border-top' if top else 'border-bottom'
    return f'<tr><td style="padding:10px 10px 0;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td width="22" height="22" style="{b}:2px solid {GOLD2};border-left:2px solid {GOLD2};font-size:0;line-height:0;">&nbsp;</td><td>&nbsp;</td><td width="22" height="22" style="{b}:2px solid {GOLD2};border-right:2px solid {GOLD2};font-size:0;line-height:0;">&nbsp;</td></tr></table></td></tr>'
def page(v,logo,cover,fonts='',ICON=''):
    p=f'{B}font-size:18px;line-height:1.55;color:{TXT};margin:0;'
    r=[corners(True)]
    r.append(f'''<tr><td style="padding:8px 26px 18px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td width="64" valign="middle"><img src="{logo}" width="52" alt="Options Snipers University" style="display:block;border:0;height:auto;"></td><td valign="middle" style="{H}font-size:19px;letter-spacing:-0.025em;color:#ffffff;line-height:1;">OPTIONS SNIPERS <span style="color:{GOLD};">UNIVERSITY</span><div style="{M}font-size:10px;font-weight:normal;letter-spacing:2px;color:{MUTED};margin-top:7px;">DAILY NEWS THAT HITS YOUR WALLET &nbsp;/&nbsp; {v['DATE']}</div></td></tr></table></td></tr>''')
    r.append(f'<tr><td style="padding:0 14px;"><img src="{cover}" width="572" alt="{v["ALT"]}" style="display:block;width:100%;height:auto;border:0;"></td></tr>')
    r.append(f'''<tr><td style="padding:24px 26px 18px;"><div style="{B}font-size:15px;color:{MUTED};">Hi {{{{contact.first_name}}}},</div><h1 style="margin:10px 0 0;{H}font-weight:normal;letter-spacing:-0.025em;font-size:34px;line-height:0.98;color:#ffffff;">{v['HEADLINE']}</h1></td></tr>''')
    r.append(sec('01','THE NEWS',f'<p style="{p}">{nl(v["NEWS"])}</p>'))
    r.append(sec('02','THE NUMBERS',f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{chip(*v["T1"])}{chip(*v["T2"])}{chip(*v["T3"])}</tr></table><p style="{M}font-size:11px;color:{MUTED};margin:10px 4px 0;">{v["NUMNOTE"]}</p>',pad='22px 22px'))
    li=''.join(f'<li style="margin-bottom:12px;">{nl(b)}</li>' for b in v['BUL'])
    r.append(sec('03','HOW TO MAKE MONEY FROM THIS',f'<ul style="{p}padding-left:22px;">{li}</ul>'))
    r.append(f'''<tr><td align="center" style="padding:0 26px 22px;"><a href="{v['CTAURL']}" style="display:inline-block;border:2px solid {GOLD};color:{GOLD};{H}font-size:13px;letter-spacing:0.02em;text-decoration:none;padding:10px 22px;border-radius:4px;">{v['MIDBTN']}</a></td></tr>''')
    qa=''.join(f'<div style="margin-bottom:16px;"><div style="{B}font-size:18px;font-weight:bold;color:{GOLD};">{q}</div><div style="{p}">{nl(a)}</div></div>' for q,a in v['QA'])
    r.append(sec('04','QUICK QUESTION',qa))
    r.append(f'''<tr><td style="padding:6px 26px 24px;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="border-left:3px solid {GOLD};padding:4px 0 4px 16px;"><div style="{M}font-size:11px;letter-spacing:3px;color:{MUTED};margin-bottom:8px;">FROM WASI</div><div style="{p}">{nl(v['NOTE'])}</div><div style="{H}font-size:15px;color:{GOLD};margin-top:10px;">Wasi Akin</div></td></tr></table></td></tr>''')
    r.append(f'''<tr><td align="center" style="padding:26px;border-top:1px solid {LINE};background:{PANEL};"><div style="{M}font-size:12px;font-weight:bold;letter-spacing:3px;color:{GOLD};margin-bottom:8px;">[05] &nbsp;JOIN THE COMMUNITY</div><div style="{B}font-size:17px;color:{TXT};margin-bottom:16px;">{nl(v['CTATEXT'])}</div><a href="{v['CTAURL']}" style="display:inline-block;background:{GOLD};color:#0A0A0A;{H}font-size:16px;letter-spacing:-0.01em;text-decoration:none;padding:15px 32px;border-radius:4px;">{v['CTABTN']}</a></td></tr>''')
    r.append(f'''<tr><td align="center" style="padding:22px 26px 4px;border-top:1px solid {LINE};"><div style="{M}font-size:11px;letter-spacing:3px;color:{MUTED};margin-bottom:12px;">SEE MORE FROM THE SNIPERS</div><table role="presentation" cellpadding="0" cellspacing="0"><tr><td style="padding:0 10px;" align="center"><a href="https://www.instagram.com/optionssnipersuniversity" style="text-decoration:none;"><img src="{ICON}icon-instagram.png" width="44" height="44" alt="Instagram" style="display:block;border:0;margin:0 auto;"><div style="{M}font-size:11px;color:{GOLD};margin-top:6px;">INSTAGRAM</div></a></td><td style="padding:0 10px;" align="center"><a href="https://www.youtube.com/channel/UCYdhQjWVViYLeouiSkUQpXQ" style="text-decoration:none;"><img src="{ICON}icon-youtube.png" width="44" height="44" alt="YouTube" style="display:block;border:0;margin:0 auto;"><div style="{M}font-size:11px;color:{GOLD};margin-top:6px;">YOUTUBE</div></a></td></tr></table></td></tr>''')
    r.append(f'''<tr><td style="padding:20px 26px 6px;{B}font-size:11px;line-height:1.6;color:#7c7c7c;">Where we got this: {v['SRC']}.<br>This is for learning only.<br>It is not money advice.<br>Trading options is risky and you can lose money.<br><br><strong style="color:{GOLD};">OPTIONS SNIPERS UNIVERSITY</strong> &nbsp;/&nbsp; @optionssnipersuniversity<br>{{{{location.name}}}} · {{{{location.full_address}}}}<br>You get this email because you signed up for our training. <a href="{{{{unsubscribe_link}}}}" style="color:{MUTED};">Unsubscribe</a></td></tr>''')
    r.append(corners(False).replace('padding:10px 10px 0','padding:0 10px 10px'))
    return f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Options Snipers University Daily</title>
<link href="https://fonts.googleapis.com/css2?family=Archivo+Black&family=Outfit:wght@400;700&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">{fonts}</head>
<body style="margin:0;padding:0;background:{BG};">
<!-- SUBJECT: {v['SUBJ']} -->
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:{BG};">{v['PRE']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{BG};"><tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:100%;max-width:600px;background:{BG};border:1px solid {GOLD2};color:{TXT};">
{chr(10).join(r)}
</table></td></tr></table></body></html>'''
def fontcss():
    d='/tmp/w/node_modules/@fontsource/'
    def f(fam,path,w):
        b=base64.b64encode(open(d+path,'rb').read()).decode()
        return f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b}) format('woff2');}}"
    return '<style>'+f('Archivo Black','archivo-black/files/archivo-black-latin-400-normal.woff2',400)+f('Outfit','outfit/files/outfit-latin-400-normal.woff2',400)+f('Outfit','outfit/files/outfit-latin-700-normal.woff2',700)+f('JetBrains Mono','jetbrains-mono/files/jetbrains-mono-latin-400-normal.woff2',400)+f('JetBrains Mono','jetbrains-mono/files/jetbrains-mono-latin-700-normal.woff2',700)+'</style>'
G=f'<span style="color:{GOLD};">'
ph={'SUBJ':'[[SUBJECT: under 50 characters, plain, names the stock or event]]','MIDBTN':'BOOK A CALL','NOTE':'[[WASI NOTE: 2-3 short sentences in Wasi\'s voice. Each sentence on its own line.]]','PRE':'[[PREHEADER: the so-what in one short sentence]]','DATE':'[[DATE]]','ALT':'[[ALT: headline]]','HEADLINE':'[[HEADLINE: short and plain. Wrap the key words in a gold span.]]','NEWS':'[[THE NEWS: 3 short sentences. Who, what, when. Each sentence goes on its own line.]]',
'T1':('[[T1_NAME]]','[[T1_MOVE]]'),'T2':('[[T2_NAME]]','[[T2_MOVE]]'),'T3':('[[T3_NAME]]','[[T3_MOVE]]'),'NUMNOTE':'[[NUMBERS NOTE]]  Green #06D6A0 = up. Red #E63946 = down.',
'BUL':['[[MONEY_IDEA_1: the exact level or event to watch today, with a number]]','[[MONEY_IDEA_2: how a trader plays it, plain words]]','[[MONEY_IDEA_3: the risk to know]]'],'QA':[('[[Q1]]','[[A1: 1-2 short sentences]]')],
'CTATEXT':'Join our community and learn how to profit from the news. Book a call to get started.','CTABTN':'BOOK A CALL','CTAURL':'[[BOOKING_LINK]]','SRC':'[[SOURCES]]'}
open('email-template.html','w').write(page(ph,'osu-logo.png','[[COVER_URL]]',ICON='https://raw.githubusercontent.com/optionssnipers/wall-street-awards/main/newsletter/'))
sm={'SUBJ':'Anthropic fell under its $83 price','MIDBTN':'BOOK A CALL','NOTE':'Here is how I see it. One red day does not change the plan. I watch the level and wait for my setup.','PRE':'The level to watch, and how traders play it.','DATE':'TUE NOV 24, 2026','ALT':'Anthropic fell below its IPO price','HEADLINE':f'Anthropic\'s stock fell {G}below its starting price.</span>',
'NEWS':'Anthropic sold its stock at $83 a share. On Tuesday, it closed below $83. Nvidia and the Nasdaq fell too.',
'T1':('ANTHROPIC','-6.5%'),'T2':('NVIDIA','-5.9%'),'T3':('NASDAQ','-1.5%'),'NUMNOTE':'How much each one went down on Tuesday.',
'BUL':['Watch the $83 line. Below it, sellers are in control. Back above it, buyers may return.','Pick a side. A "put option" gains if the stock keeps falling. A "call option" gains if it bounces back.','Know the risk. Options can lose all the money you put in. Only use money you can afford to lose.'],
'QA':[('Why did it fall?','People got less excited about AI stocks. Many of them sold.')],
'CTATEXT':'Join our community and learn how to profit from the news. Book a call to get started.','CTABTN':'BOOK A CALL','CTAURL':'https://example.com/book','SRC':'AP and Reuters'}
open('sample/preview.html','w').write(page(sm,'../osu-logo.png','cover.jpg',fontcss(),ICON='../'))
