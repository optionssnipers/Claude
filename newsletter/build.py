import re
LOGO='osu-logo.png'
def sec(label,body,pad='20px 24px'):
    return f'''<tr><td style="padding:{pad};border-top:1px solid #243040;"><div style="font-family:Impact,'Anton',Arial,sans-serif;font-size:15px;letter-spacing:2px;color:#F5C542;margin-bottom:10px;">{label}</div>{body}</td></tr>'''
def chip(n,m,c='#E63946'):
    return f'<td width="33%" style="padding:4px;"><div style="background:#1a222d;border-radius:8px;padding:12px;text-align:center;"><div style="font-size:11px;color:#9aa7b4;">{n}</div><div style="font-size:24px;font-weight:bold;color:{c};">{m}</div></div></td>'
def page(v,logo,cover):
    p='font-size:17px;line-height:1.6;color:#d5dde5;margin:0;'
    rows=[]
    rows.append(f'''<tr><td style="padding:18px 24px;border-bottom:3px solid #F5C542;"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td width="60"><img src="{logo}" width="48" height="48" alt="Options Snipers University" style="display:block;border:0;"></td><td style="font-family:Impact,'Anton',Arial,sans-serif;font-size:20px;letter-spacing:2px;color:#ffffff;">OPTIONS SNIPERS <span style="color:#F5C542;">UNIVERSITY</span><div style="font-family:Arial,sans-serif;font-size:11px;letter-spacing:2px;color:#9aa7b4;">DAILY NEWS THAT HITS YOUR WALLET &nbsp;|&nbsp; {v['DATE']}</div></td></tr></table></td></tr>''')
    rows.append(f'<tr><td><img src="{cover}" width="600" alt="{v["ALT"]}" style="display:block;width:100%;height:auto;border:0;"></td></tr>')
    rows.append(f'''<tr><td style="padding:24px 24px 16px;"><div style="font-size:14px;color:#9aa7b4;">Hi {{{{contact.first_name}}}},</div><h1 style="margin:8px 0 0;font-family:Impact,'Anton',Arial,sans-serif;font-weight:normal;letter-spacing:.5px;font-size:32px;line-height:1.15;color:#ffffff;">{v['HEADLINE']}</h1></td></tr>''')
    rows.append(sec('1 &nbsp;THE NEWS',f'<p style="{p}">{v["NEWS"]}</p>'))
    rows.append(sec('2 &nbsp;THE NUMBERS',f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{chip(*v["T1"])}{chip(*v["T2"])}{chip(*v["T3"])}</tr></table><p style="font-size:12px;color:#7d8996;margin:8px 4px 0;">{v["NUMNOTE"]}</p>',pad='20px 20px'))
    li=''.join(f'<li style="margin-bottom:8px;">{b}</li>' for b in v['BUL'])
    rows.append(sec('3 &nbsp;HOW TO MAKE MONEY FROM THIS',f'<ul style="{p}padding-left:22px;">{li}</ul>'))
    qa=''.join(f'<div style="margin-bottom:14px;"><div style="font-size:17px;font-weight:bold;color:#ffffff;">{q}</div><div style="{p}">{a}</div></div>' for q,a in v['QA'])
    rows.append(sec('4 &nbsp;QUICK QUESTIONS',qa))
    rows.append(f'''<tr><td align="center" style="padding:24px;border-top:1px solid #243040;background:#0e131a;"><div style="font-family:Impact,'Anton',Arial,sans-serif;font-size:15px;letter-spacing:2px;color:#F5C542;margin-bottom:6px;">5 &nbsp;YOUR NEXT STEP</div><div style="font-size:16px;color:#d5dde5;margin-bottom:14px;">{v['CTATEXT']}</div><a href="{v['CTAURL']}" style="display:inline-block;background:#F5C542;color:#0b0f14;font-weight:bold;font-size:17px;text-decoration:none;padding:14px 30px;border-radius:8px;">{v['CTABTN']}</a></td></tr>''')
    rows.append(f'''<tr><td style="padding:18px 24px;background:#080b10;font-size:11px;line-height:1.6;color:#7d8996;">Where we got this: {v['SRC']}.<br>This is for learning only. It is not money advice. Trading options is risky and you can lose money.<br><br><strong style="color:#F5C542;">OPTIONS SNIPERS UNIVERSITY</strong> &nbsp;|&nbsp; @optionssnipersuniversity<br>{{{{location.name}}}} · {{{{location.full_address}}}}<br>You get this email because you signed up for our training. <a href="{{{{unsubscribe_link}}}}" style="color:#9aa7b4;">Unsubscribe</a></td></tr>''')
    return f'''<!DOCTYPE html>
<html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Options Snipers University Daily</title></head>
<body style="margin:0;padding:0;background:#0b0f14;">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:#0b0f14;">{v['PRE']}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:#0b0f14;"><tr><td align="center" style="padding:16px 8px;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="width:100%;max-width:600px;background:#121821;border-radius:12px;overflow:hidden;font-family:Arial,Helvetica,sans-serif;color:#e8edf2;">
{chr(10).join(rows)}
</table></td></tr></table></body></html>'''
ph={'PRE':'[[PREHEADER: one short sentence]]','DATE':'[[DATE]]','ALT':'[[ALT: headline]]','HEADLINE':'[[HEADLINE: short and plain]]','NEWS':'[[THE NEWS: 3 short sentences. Who, what, when.]]',
'T1':('[[T1_NAME]]','[[T1_MOVE]]'),'T2':('[[T2_NAME]]','[[T2_MOVE]]'),'T3':('[[T3_NAME]]','[[T3_MOVE]]'),'NUMNOTE':'[[NUMBERS NOTE: what the numbers are, e.g. Change on Tuesday]]',
'BUL':['[[MONEY_IDEA_1: a way traders can profit, plain words]]','[[MONEY_IDEA_2: another way]]','[[MONEY_IDEA_3: the risk to know]]'],'QA':[('[[Q1]]','[[A1: 1-2 short sentences]]'),('[[Q2]]','[[A2: 1-2 short sentences]]')],
'CTATEXT':'[[CTA_TEXT: one friendly sentence]]','CTABTN':'[[BUTTON TEXT]]','CTAURL':'[[CTA_URL]]','SRC':'[[SOURCES]]'}
open('email-template.html','w').write(page(ph,'osu-logo.png','[[COVER_URL]]'))
sm={'PRE':'The biggest AI stock sale of the year just dipped. Here is what it means for you.','DATE':'TUE NOV 24, 2026','ALT':'Anthropic fell below its IPO price','HEADLINE':'Anthropic\'s stock fell below its starting price',
'NEWS':'Anthropic is an AI company. It sold its stock to the public at $83 a share. On Tuesday, the stock fell below $83. Nvidia and the Nasdaq went down too.',
'T1':('ANTHROPIC','-6.5%'),'T2':('NVIDIA','-5.9%'),'T3':('NASDAQ','-1.5%'),'NUMNOTE':'How much each one went down on Tuesday.',
'BUL':['Bet on the drop: a trader can buy a "put option." It gains value if the stock keeps going down.','Wait for the dip: some traders watch for the price to stop falling, then buy a "call option" to bet on a bounce back.','Know the risk: options can lose all the money you put in. Only use money you can afford to lose.'],
'QA':[('Why did it fall?','People got less excited about AI stocks, and many of them sold.'),('Is this true?','Yes. Two news sources reported the same numbers.')],
'CTATEXT':'Want to learn how traders look for chances when stocks move?','CTABTN':'Watch the free class','CTAURL':'https://example.com','SRC':'AP and Reuters'}
open('sample/preview.html','w').write(page(sm,'../osu-logo.png','cover.jpg'))
