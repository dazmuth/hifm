#!/usr/bin/env python3
"""Builds the HIFM v2 pages. Output: /home/claude/hifm-v2/*.html
Run:  python3 build_v2.py
"""
import html, os
from PIL import Image

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = f"{SITE}/assets/img"
AD_EMAIL = "Magazine.HiFEX@gmail.com"   # from the magazine masthead; swap when the ad-sales address is known
esc = html.escape

# Defaults baked into the HTML (site-info.js can override them; same values here so the pages work without JavaScript)
CUR_ISSUE, CUR_SEASON = 31, "Fall 2026"
CATCH = "Hooray for Hollywood"
CUR_PDF = "archive/Issue 031.pdf"

def pdf_href(num):
    return f"archive/Issue {num:03d}.pdf".replace(" ", "%20")

_dims = {}
def dims(name):
    if name not in _dims:
        with Image.open(f"{IMG}/{name}") as im:
            _dims[name] = im.size
    return _dims[name]

def img(name, alt, cls="", eager=False):
    w, h = dims(name)
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    c = f' class="{cls}"' if cls else ""
    return f'<img src="assets/img/{name}" width="{w}" height="{h}" alt="{esc(alt)}" {load}{c}>'

# ------------------------------------------------------------------ data
STORIES = {
 "willis": dict(file="story-willis.html", kicker="Cover Story", title="Bruce Willis: Hollywood Hero",
   dek="Few stars have ever redefined an entire genre with a single performance.", byline="Sandro Monetti", pages="Pages 2–7",
   lead="i31-willis2.jpg", lead_alt="Bruce Willis smiling, with Die Hard and Live Free or Die Hard posters behind him",
   thumb="i31-willis2.jpg",
   spreads=[("sp31-02.jpg", "Pages 2–3 as printed", "Spread from the printed magazine: cover story opener for Bruce Willis"),
            ("sp31-04.jpg", "Pages 4–5 as printed", "Spread from the printed magazine: Bruce Willis film posters and his Hollywood Walk of Fame cement block"),
            ("sp31-06.jpg", "Pages 6–7 as printed", "Spread from the printed magazine: Bruce Willis photo collage")],
   body=[
    "Few stars have ever redefined an entire genre with a single performance, but Bruce Willis did exactly that in 1988 with Die Hard. Before John McClane crashed barefoot through Nakatomi Plaza, action heroes tended to be larger-than-life muscle men. Willis brought something different: vulnerability, wit, frustration and sheer determination. McClane wasn’t a superhero. He was a guy having a very bad day. Audiences loved him for it.",
    "The success of Die Hard transformed Willis from television favorite to global movie star and launched one of Hollywood’s most successful action franchises. Yet his career was far broader than explosions and one-liners. He delivered memorable performances in Pulp Fiction, 12 Monkeys, Armageddon, The Fifth Element, Unbreakable and The Sixth Sense, along the way becoming one of the world’s most bankable stars.",
    "PULL:Willis brought something different: vulnerability, wit, frustration and sheer determination.",
    "Over four decades, films featuring Willis generated billions of dollars at the global box office, making him one of the most commercially successful actors of his generation. His appeal combined a winning mix of toughness and humor that crossed borders, languages and genres. Whether playing a time-travelling convict, a reluctant hero, a boxer or a ghost-haunted child psychologist, he possessed an unmistakable screen presence.",
    "Even in the later years of his career, Willis remained a familiar face to audiences, appearing in projects such as the vigilante thriller Death Wish and the wartime epic Air Strike. While these films did not match the cultural impact of his greatest hits, they demonstrated his enduring work ethic and commitment to entertaining audiences.",
    "In 2022, Willis retired from acting after being diagnosed with aphasia, a condition affecting communication and language abilities. His family later revealed that his condition had progressed to frontotemporal dementia, a degenerative neurological disease.",
    "For millions of film fans, he remains the gold standard against which every reluctant hero is measured.",
   ]),
 "godfather": dict(file="story-godfather.html", kicker="Latest News", title="Godfather 4: The Godmother?",
   dek="A new Godfather movie could be on the way, and this time the story takes a new direction.", byline="", pages="Page 8",
   lead="i31-godfather.jpg", lead_alt="Film stills from the Godfather movies beside the headline Godfather 4: The Godmother?",
   thumb="i31-godfather.jpg", spreads=[("pr-godfather.jpg", "Pages 8–9 as printed", "Spread from the printed magazine: the Godfather 4 story beside a full-page magazine promotion")],
   body=[
    "A new Godfather movie could be on the way. Paramount, the studio behind the three previous movies in the Mafia saga, has the film rights to an upcoming book which takes the story in a new direction.",
    "Connie, to be published in 2027 and written by bestselling author Adriana Trigani, tells the Corleone family story from the perspective of Don Corleone’s only daughter.",
    "Now the studio must decide whether to move ahead with a female focused continuation of one of the most iconic film franchises ever.",
    "Talia Shire played Connie Corleone in the Godfather trilogy and is the sister of Francis Ford Coppola who directed all three movies. Neither she nor her brother has yet been signed up to the new project.",
   ]),
 "willsmith": dict(file="story-willsmith.html", kicker="Latest News", title="Will Smith Launches a Comeback",
   dek="After four years largely out of the spotlight, Will Smith is poised for a comeback.", byline="", pages="Page 10",
   lead="i31-willsmith.jpg", lead_alt="Will Smith holding an Oscar statuette",
   thumb="i31-willsmith.jpg", spreads=[("pr-willsmith.jpg", "Pages 10–11 as printed", "Spread from the printed magazine: the Will Smith story beside a Big Film Fund advertisement")],
   body=[
    "After largely being out of the spotlight in the four years since slapping Chris Rock at the Oscars, Will Smith is poised for a comeback.",
    "He is set to star as an FBI agent in big budget action thriller Supermax for Amazon MGM. Meanwhile Paramount has signed a first-look deal with the star’s entertainment company, Westbrook.",
    "But while Hollywood appears ready to forgive and forget the slap heard around the world, it remains to be seen if audiences are ready to embrace Smith again.",
   ]),
 "taylor": dict(file="story-taylor.html", kicker="Awards", title="And the Oscar Goes to… Taylor Swift?",
   dek="Music icon Taylor Swift has dominated the Grammy Awards in recent years, but soon she could win her first Oscar.", byline="", pages="Page 16",
   lead="i31-taylor.jpg", lead_alt="Taylor Swift beside Jessie from Toy Story 5",
   thumb="i31-taylor.jpg", spreads=[("pr-taylor.jpg", "Pages 16–17 as printed", "Spread from the printed magazine: the Taylor Swift Oscar story beside a story on Javier Bardem at the TCL Chinese Theatre")],
   body=[
    "Music icon Taylor Swift has dominated the Grammy Awards in recent years but soon she could win her first Oscar.",
    "That’s because the superstar’s track from Toy Story 5 – inspired by the cowgirl doll character Jessie – is an early favourite for the next Academy Award for best motion picture song.",
    "Country-pop tune If I Knew It, I Knew You could put the world’s most popular entertainer on the Oscars stage, which would surely send ratings through the roof.",
    "But nothing is guaranteed because the Academy’s music branch is not always in awe of celebrity or chart hits and no country song has ever won an Oscar.",
    "If there are some Swifties among the voters, however, that could all change and Taylor might achieve yet another career milestone.",
   ]),
 "farrell": dict(file="story-farrell.html", kicker="Interviews", title="5 Questions for Colin Farrell",
   dek="While promoting the second season of his Apple TV series Sugar, Colin Farrell answers five questions.", byline="", pages="Pages 18–19",
   lead="car-farrell.jpg", lead_alt="Colin Farrell in a white shirt and braces, wearing sunglasses",
   thumb="i31-farrell.jpg", spreads=[("pr-farrell.jpg", "Pages 18–19 as printed", "Spread from the printed magazine: 5 Questions for Colin Farrell")],
   body=[
    "While promoting the second season of his Apple TV series Sugar, movie star Colin Farrell caught up with our own Sandro Monetti, with whom he co-produced Oscar shortlisted short film Room Taken, and answered these five questions.",
    "Q:Your character in Sugar loves Hollywood movies but what film is your favorite?",
    "I’ll go with L.A. Confidential. Love that film. Everything about that is just perfect. Curtis Hanson’s directing, every single musical cue, the cinematography, how L.A. looks, how it feels. David Strathairn. All the actors. You know, Spacey, Pearce. Russel Crowe. James Cromwell who was in the first season and features a little bit in the second season of Sugar. It’s just a masterclass of filmmaking and performance and mood.",
    "Q:In Sugar, you play an extraterrestrial disguised as human private investigator. Do you think aliens really could be living among us?",
    "So interesting, isn’t it? My God, I’d love to know. Maybe when I was a kid I didn’t think so. But for as long as I can remember now, I’ve always thought there’s probably, of course, many other worlds, many other civilizations, sentient beings, you know? I would imagine there’s a good chance that we’ve been watched for a long, long time.",
    "Q:What scares you?",
    "I’m so afraid of flying. I’ve got envy of anyone who is calm about getting on a plane. I just put one foot in front of the other to do it. I just have a very rapid, nervous, anxious response when we hit turbulence, especially if we’re over the water. My head is a disaster sometimes, you know. Runs away from me from time to time, and hitting turbulence is one of the cases when it does.",
    "Q:It’s more than 20 years since you made the film Alexander, directed by Oliver Stone, what’s he like?",
    "I’ve met a lot of bright people in my time. More bright people than it looked like I was going to meet, because I didn’t even finish high school. But I have, through my work as an actor, been fortunate to encounter some really, really brilliant men and women. And I don’t know that I’ve ever met anyone more brilliant than Oliver Stone. Like, truly. He is a voracious reader. A consummate thinker. Particularly in relation to world politics and the global stage. And our responsibility to each other as human beings. He’s an extraordinary patriot. I’m not saying everything he’s done is right, but I believe the man just cares deeply about human beings. He really does. Oliver is amazing.",
    "Q:Congratulations on recently turning 50. How do you reflect on that landmark birthday?",
    "I did find myself being surprisingly reflective. It caught me, just the number. I just, you know, reflected on my life for a bit. And not much of it was in relation to career. Truly it was more in relation to the obvious things, you know, where I came from, where I am, kind of family and friends, and loss and this and that and the other, you know, that kind of thing. And also, I was thinking of mortality and it’s like, whoa. So when the road gets shorter ahead of you than it was behind you, it becomes a very real thing and an intriguing thing, you know, the existence of that one great certainty that we all share. We don’t think about it of course when we’re young and then it becomes more apparent.",
   ]),
 "rudd": dict(file="story-rudd.html", kicker="Interviews", title="5 Questions for Paul Rudd",
   dek="From Clueless to latest film Power Ballad, Paul Rudd has been entertaining audiences for 30 years.", byline="Sandro Monetti", pages="Pages 20–21",
   lead="car-rudd.jpg", lead_alt="Paul Rudd playing an acoustic guitar",
   thumb="i31-rudd.jpg", spreads=[("pr-rudd.jpg", "Pages 20–21 as printed", "Spread from the printed magazine: 5 Questions for Paul Rudd")],
   body=[
    "From Clueless to latest film Power Ballad, Paul Rudd has been entertaining audiences for 30 years – along the way scoring big hits like Anchorman and Ant-Man. Here he talks about his long time at the top.",
    "Q:How do you reflect on your enduring career and the turning points in it?",
    "Having a long career kind of sneaks up on you, honestly. It’s a little bit like doing yard work, you know, or mowing a lawn. You’re just kind of focusing on that patch of grass in front of you, and you’re just pushing this thing and pushing this thing. And finally, you kind of stop after a while, look back, and realize you’ve mowed just a giant lawn. So, in looking back on the mowed lawn that is my IMDB page, there are certain things that do stick out as being seminal experiences and ones that I think probably thrust me into a different category. When Anchorman happened, all of a sudden, I was working with Judd Apatow and a lot of the same comedic actors. That was a really amazing time in my life and in my career. Then, certainly, the Marvel stuff. It was the first thing I ever did that kids had seen. So, my life changed drastically. ’Cause I’d be out, and a little kid would go, “How’s Iron Man?” That was a new thing. And in other countries, it was so visible.",
    "Q:Has being so visible complicated your life?",
    "Yeah, sure. There are certain things that become more complicated just in life because I’ve had some success in this career. And while there are so many benefits and things that are nice, there are other things that become a little trickier. I’ve really noticed the difference since the Marvel stuff, obviously just ’cause of the level of visibility. Certain things become a little tricker to just kind of be in big, large crowds or whatever it is. But I tend not to focus or talk too much about what’s difficult about being famous, ’cause it’s a ridiculous thing to talk about, and you sound like a real jerk.",
    "Q:How do you pick projects?",
    "It’s never really changed. It’s would I wanna see it? That’s the first thing. Second, is there something about it that really resonates with me, that I’m drawn to? And it’s like, oh, I think this would be fun to play. Usually, you can tell when you’re reading it, like, you’re imagining doing it. You’re imagining how you would kind of tackle a role. Like, I think about that. How they turn out is a completely different thing. I go into just about every single thing I’ve ever done, and I’ve gone in with, “Like, this could be great.” Like, I really have an optimistic point of view about it. And they don’t always turn out, and that can be a little demoralizing or a lot demoralizing. But I don’t think of the success really in box office. I think of it in terms of what I gained from it personally. Experiences themselves, they do count for a lot. I’ve had some really, really great experiences working on things. But the thing that really is the North Star for me is, would I wanna see it? And is there something within me that is drawing me to trying to tackle the role?",
    "Q:You’ve described your latest role, as a musician in Power Ballad, as your dream part. Why?",
    # PRINT ERROR, kept as printed: the first two sentences below were pasted from the Farrell interview.
    "I did find myself being surprisingly reflective. It caught I like to play music. I like to sing in the way that everyone kinda does and I’ve played guitar for many years, but I tend to play on my own. Here I was around real musicians and I would like to think that just being around that ups your game. This is not my lane, really, but they were certainly nice and welcoming and made me feel as if I, you know, could hang in the room. It was also a dream role because it was set in Ireland and I’m such a fan of Irish music, Guiness, pubs and the literature that comes out of Ireland. I love it all.",
    "Q:You’re from New Jersey so where does your love of Ireland come from?",
    "I know Ireland pretty well. I’ve been there many times. It’s one of my favorite places. My dad was a Titanic historian and spent a lot of time in Ireland. That was how he made his living, actually. He used to take lots of people through Ireland, and in particular, Cobh which was the last port of call for Titanic before she sailed to New York on the fateful voyage. So, I’d spent a lot of time there with my dad. I feel very comfortable and at home in Ireland and that’s due in large part because a lot of Irish people make you feel that way. So, it was great to film there. A dream role.",
   ]),
 "curtis": dict(file="story-curtis.html", kicker="Interviews", title="Curtis Calls the Shots",
   dek="Movie icon Jamie Lee Curtis is finding her greatest happiness in charge of a new TV sitcom.", byline="", pages="Pages 22–23",
   lead="car-curtis.jpg", lead_alt="Jamie Lee Curtis seated in a director’s chair, with the Newlyweds logo",
   thumb="i31-curtis.jpg", spreads=[("pr-curtis.jpg", "Pages 22–23 as printed", "Spread from the printed magazine: Curtis Calls the Shots, with Jamie Lee Curtis film stills")],
   body=[
    "Movie icon Jamie Lee Curtis has had a glittering career in films but is now finding her greatest happiness being in charge of a new TV sitcom.",
    "After starring in hits like True Lies, Trading Places, Halloween, A Fish Called Wanda and Everything Everywhere All at Once, she’s currently executive producing and appearing in NBC comedy series Newlyweds, which the actress co-created.",
    "“It’s my favorite job, I love the whole part of it, every aspect of it, the dance with the cameras, the idea that you actually get to rehearse something and work it and learn a joke and play it,” she said.",
    "“I’m 68 years old, and every single year, all I’ve ever said to my agents is ‘I want to do a sitcom, all I want to do is a sitcom.’ I just never got to do it, and so I just decided to basically kind of create my own job.”",
    "Newlyweds is a later-in-life love story and Jamie Lee loves her recurring guest star role as the sharp-tongued ex-wife of a buttoned-up college professor but also adores getting to call the shots on set as executive producer.",
    "“I’ve wanted to be a boss my whole life. I like to refer to myself as the HBIC, head bitch in charge,” she laughed.",
    "While streaming dominates the television landscape, Jamie Lee is thrilled to be making a sitcom for network television.",
    "“It’s must-see free TV,” she added. “You have to remember, a lot of people don’t have any money anymore, people are really struggling, and cable and all of the things you have to spend money on. This is network television, and I actually think this whole nostalgia of what sitcoms bring you into your house, things do come around.",
    "“I just think people want to have a good time in the comfort of their own home, and they want to turn on a network show and have laughs and have feelings. That’s what sitcoms do, and that’s why we love them.”",
   ]),
 "backcover": dict(file="story-backcover.html", kicker="Back Cover Story", title="Hollywood’s $10 Billion Comeback",
   dek="Industry fears that moviegoing was finished have proved unfounded thanks to an astonishing box office bounce back in 2026.", byline="", pages="Pages 48–49",
   lead="i31-boxoffice.jpg", lead_alt="Hollywood’s $10 Billion Comeback title graphic: the Hollywood sign, red carpet and spotlights",
   thumb="i31-boxoffice.jpg", spreads=[("pr-boxoffice.jpg", "Pages 48–49 as printed", "Spread from the printed magazine: Hollywood’s $10 Billion Comeback")],
   body=[
    "Industry fears that moviegoing was finished have proved unfounded thanks to an astonishing box office bounce back in 2026.",
    "American theatrical ticket sales are on track to surpass $10 billion for the first time since before the pandemic, a milestone that many executives had questioned only a year ago.",
    "Powering the turnaround has been a consistent release calendar and stronger audience demand for theatrical experiences.",
    "A major contributor has been science-fiction film Project Hail Mary, which has become one of the year’s defining theatrical successes. The Ryan Gosling-led film surpassed $300 million globally, providing evidence that audiences will still turn out for original, non-franchise movies with broad appeal.",
    "Talking of broad appeal, other unexpected hits included low budget horror movies Obsession and Backrooms and music biopic Michael, which showed that cinemas need not rely solely on sequels and superhero releases.",
    "Then in the summer came major titles like Christopher Nolan’s The Odyssey and Spider-Man: Brand New Day while still to come at the end of the year are Avengers: Doomsday and Dune which are expected to extend the box-office momentum through the remainder of 2026.",
    "Exhibitors say one of the biggest lessons from 2026 is that consistency matters more than individual blockbusters. This year, audiences have had a steady pipeline of family films, horror titles, prestige dramas and original event movies, helping maintain attendance over a longer period.",
    "Premium large-format screenings remain an important driver of revenue. Project Hail Mary and The Odyssey generated a significant share of their opening weekend takings from IMAX and other premium auditoriums, reflecting audiences’ willingness to pay higher ticket prices for event films that offer experiences difficult to replicate at home.",
    "The takeaway from all this is that exhibitors believe the industry’s recovery is no longer dependent on a handful of blockbusters. Instead, they argue that a balanced release slate featuring franchises, original films and mid-budget successes has restored confidence in the theatrical model.",
    "While challenges remain, executives increasingly view the 2026 numbers as the strongest indication yet that moviegoing has established a sustainable post-pandemic recovery rather than just experiencing a temporary rebound.",
   ]),
}

# Which stories fill which home-page slots (edit these lists each issue)
CAROUSEL = [
    ("farrell", "car-farrell.jpg", "Colin Farrell"),
    ("rudd",    "car-rudd.jpg",    "Paul Rudd"),
    ("curtis",  "car-curtis.jpg",  "Jamie Lee Curtis"),
]
SIDE = [("willis", "Cover Story"), ("godfather", "Latest News"), ("willsmith", "Latest News"), ("taylor", "Awards")]

ARCHIVE = [  # num, season, year, subject, cover file, alt
 (31, "Fall 2026", 2026, "Bruce Willis", "i31-cover.jpg", "Cover of Issue 31, Fall 2026: Bruce Willis"),
 (30, "Spring 2026", 2026, "Sylvester Stallone", "i30-cover.jpg", "Cover of Issue 30, Spring 2026: Sylvester Stallone"),
 (12, "Winter 2018", 2018, "China’s Filmmaking Couple", "cover-012.jpg", "Cover of the Winter 2018 issue: Qiankuan Li and Guiyun Xiao, China’s Filmmaking Couple"),
 (11, "Fall 2018", 2018, "Mel Gibson", "cover-011.jpg", "Cover of the Fall 2018 issue: Mel Gibson"),
 (9,  "Fall 2017", 2017, "Buting Yang", "cover-009.jpg", "Cover of the Fall 2017 issue: Buting Yang"),
]
STRIP = [30, 12, 11, 9]   # covers shown under "From the Archive" on the home page

# ------------------------------------------------------------------ shared chrome
def head(title, desc):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><!-- DEMO: remove before launch -->
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%2310244f'/%3E%3Cpath d='M32 10l6.2 13.4 14.6 1.7-10.8 10 2.9 14.5L32 42.4 19.1 49.6 22 35.1 11.2 25.1l14.6-1.7z' fill='%23c9a24a'/%3E%3C/svg%3E">
<link rel="preload" href="assets/fonts/playfair-display-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/site.css">
<script src="assets/js/site-info.js"></script>
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
'''

def nav(home=False, active=""):
    p = "" if home else "index.html"
    items = [("Latest Issue", f"{p}#latest-issue", "latest"), ("Back Cover", f"{p}#back-cover", "back"),
             ("Archive", "archive.html", "archive"), ("Advertise with Us", f"{p}#advertise", "advertise"),
             ("Contact", "#contact", "contact")]
    li = "".join(f'<li><a href="{h}"{" aria-current=\"page\"" if k == active else ""}>{l}</a></li>' for l, h, k in items)
    return f'''<nav class="nav" aria-label="Primary"><div class="wrap">
  <button class="nav-toggle" aria-expanded="false" aria-controls="nav-links">Menu</button>
  <ul class="nav-links" id="nav-links">{li}</ul>
</div></nav>
'''

def leaderboard():
    return f'''<div class="leader-wrap"><div class="wrap ad-zone">
  <span class="ad-label">Advertisement</span>
  <a class="ad ad--leader" href="mailto:{AD_EMAIL}?subject=Advertising%20in%20Hollywood%20International%20Filmmaker">
    <b>Your ad here</b><small>Leaderboard &middot; 970 &times; 90 &middot; Advertise in print and online</small>
  </a>
</div></div>
'''

def chrome_top(home=False, active=""):
    # Order, top to bottom: header banner, ad, logo, navigation
    return f'''<div class="topbar"><div class="wrap">
  <span><strong data-info="issue-line">Issue {CUR_ISSUE} &middot; {CUR_SEASON}</strong></span>
  <span class="catch" data-info="catchphrase">{esc(CATCH)}</span>
</div></div>
{leaderboard()}<header class="masthead"><div class="wrap">
  <a class="logo" href="index.html" aria-label="Hollywood International Filmmaker — home">{img("hi-logo.png", "Hollywood International Filmmaker", eager=True)}</a>
</div></header>
{nav(home, active)}'''

def ad_diamond():
    w, h = dims("ad-diamond.jpg")
    return f'''<div class="ad-zone"><span class="ad-label">Advertisement</span>
  <a class="ad ad--creative ad--page" href="https://diamondsofa.com" rel="sponsored noopener" target="_blank">
    <img src="assets/img/ad-diamond.jpg" width="{w}" height="{h}" alt="Diamond Sofa — gold and black velvet dining chairs around a marble table. diamondsofa.com" loading="lazy" decoding="async">
  </a></div>'''

def footer():
    return f'''<footer class="foot" id="contact"><div class="wrap">
  <div class="foot-grid">
    <div>
      <span class="fbrand">Hollywood International Filmmaker</span>
      <p>A quarterly magazine for filmmakers and film lovers, published by Hollywood International Film Exchange.</p>
      <address>6565 East Washington Blvd.<br>Los Angeles, CA 90040, USA<br><a href="mailto:{AD_EMAIL}">{AD_EMAIL}</a></address>
    </div>
    <div><h2>Magazine</h2><ul>
      <li><a href="index.html#latest-issue">Latest Issue</a></li><li><a href="index.html#back-cover">Back Cover</a></li>
      <li><a href="archive.html">Archive</a></li><li><a href="index.html#advertise">Advertise with Us</a></li></ul></div>
    <div><h2>Company</h2><ul>
      <li><a href="#about">About Us</a></li><li><a href="#team">Meet the Team</a></li>
      <li><a href="#submit">Submit a Story</a></li><li><a href="mailto:{AD_EMAIL}">Contact Us</a></li></ul></div>
    <div><h2>Follow</h2><ul>
      <li><a href="#facebook">Facebook &middot; Hollywood International Express</a></li>
      <li><a href="#x">X &middot; @HiFilmExpress</a></li></ul>
      <h2 style="margin-top:20px">Legal</h2><ul>
      <li><a href="#privacy">Privacy Policy</a></li><li><a href="#terms">Terms of Use</a></li><li><a href="#faq">F.A.Q.</a></li></ul></div>
  </div>
  <div class="sponsors"><strong>Sponsors</strong>Big Screen Entertainment &middot; Big Screen Holdings &middot; Hollywood International Film Exchange &middot; Hollywood International Film Festival &middot; Hollywood International Express &middot; Diamond Sofa &middot; Fairfax Entertainment &middot; Chinese Creative Culture Organization</div>
  <p class="copyright">&copy; 2026 Hollywood International Filmmaker Magazine. All rights reserved. Demo build &mdash; layout and copy are placeholders for review.</p>
</div></footer>
<script src="assets/js/site.js"></script>
</body>
</html>
'''

def back_bar(end=False):
    cls = "back-bar back-bar--end" if end else "back-bar"
    return f'<div class="{cls}"><div class="wrap"><a class="btn-back" href="index.html" data-back>Back</a></div></div>'

def write(name, content):
    with open(f"{SITE}/{name}", "w", encoding="utf-8") as f:
        f.write(content)

# ------------------------------------------------------------------ HOME
def home():
    h = head("Hollywood International Filmmaker — Fall 2026 Issue",
             "Hollywood International Filmmaker: the quarterly magazine for filmmakers and film lovers. Read the latest issue and browse the archive.")
    h += chrome_top(home=True)
    # carousel
    slides = ""
    for key, f, name in CAROUSEL:
        s = STORIES[key]
        w, hh = dims(f)
        slides += f'''<a class="slide" href="{s["file"]}"><img src="assets/img/{f}" width="{w}" height="{hh}" alt="{esc(name)}" {'fetchpriority="high"' if key == CAROUSEL[0][0] else 'loading="lazy" decoding="async"'}><span class="slide-name">{esc(name)}</span></a>'''
    carousel = f'''<section class="carousel" aria-roledescription="carousel" aria-label="Interviews">
  <span class="carousel-chip">Interviews</span>
  {slides}
  <div class="carousel-ctl"><button type="button" class="pause" aria-label="Pause the rotation">Pause</button></div>
</section>'''
    minis = ""
    for key, kick in SIDE:
        s = STORIES[key]
        mt = f"mini-{key}.jpg"
        w, hh = dims(mt)
        minis += f'''<article class="mini"><a class="thumb" href="{s["file"]}" tabindex="-1" aria-hidden="true"><img src="assets/img/{mt}" width="{w}" height="{hh}" alt="" loading="lazy" decoding="async"></a>
  <div class="txt"><span class="kicker">{kick}</span><h3><a href="{s["file"]}">{esc(s["title"])}</a></h3></div></article>'''
    h += f'''<main id="main">
<div class="wrap top-grid">{carousel}<div class="minis">{minis}</div></div>
'''
    # latest issue band
    cov = [a for a in ARCHIVE if a[0] == CUR_ISSUE][0]
    h += f'''<section class="issue-band" id="latest-issue" aria-label="The latest issue"><div class="wrap">
  <a href="{pdf_href(CUR_ISSUE)}" data-info="pdf" aria-label="Open the latest issue (PDF)">{img(cov[4], cov[5], "cover")}</a>
  <div><span class="kicker">The latest issue</span><h2>Issue {CUR_ISSUE} &middot; {CUR_SEASON}</h2>
    <ul class="coverlines"><li>AI Films</li><li>Colin Farrell</li><li>Dream of Love</li><li>Taylor Swift</li></ul>
    <p style="color:#cfd5e6;max-width:52ch;margin:12px 0 0">Everything in the printed magazine, online.</p></div>
  <div class="issue-actions"><a class="btn btn-gold" href="{pdf_href(CUR_ISSUE)}" data-info="pdf">Read this Issue</a><a class="btn btn-line" href="archive.html">Browse the archive</a></div>
</div></section>
'''
    # back cover + Diamond Sofa ad
    b = STORIES["backcover"]
    h += f'''<section class="back-cover" id="back-cover" aria-label="Back cover"><div class="wrap"><div class="cols bc-cols">
  <div class="bc-card">
    <div><span class="kicker">Back Cover Story</span><h2>{b["title"]}</h2>
    <p>{esc(b["dek"])}</p>
    <p><a class="btn btn-gold" href="{b["file"]}">Read the story</a></p>
    <p class="credit">Cover illustration by Todd Tuttle</p></div>
    {img("i31-illus.jpg", "Caricature illustration: Hollywood’s $10 Billion Box Office Year, with Spider-Man and film stars among stacks of cash")}
  </div>
  <aside class="sidebar">{ad_diamond()}</aside>
</div></div></section>
'''
    # from the archive
    cards = ""
    for num, season, yr, subj, cf, alt in ARCHIVE:
        if num not in STRIP: continue
        cards += f'''<div class="issue-card"><a class="cvlink" href="archive.html#issue-{num}"><div class="cv">{img(cf, alt)}</div>
  <h3>{esc(subj)}</h3><span class="meta">Issue {num} &middot; {season}</span></a></div>'''
    h += f'''<section class="strip" id="from-the-archive" aria-label="From the archive"><div class="wrap">
  <div class="sec-head"><h2>From the Archive</h2><a href="archive.html">See all issues</a></div>
  <div class="issues">{cards}</div>
</div></section>
'''
    # advertise
    w, hh = dims("ad-bestmag.jpg")
    h += f'''<section class="advertise" id="advertise"><div class="wrap">
  <div><h2>Advertise with Us</h2>
  <p>Reach film fans and industry readers in the printed magazine and on this site. Email us to be featured in the next issue.</p>
  <a class="btn btn-dark" href="mailto:{AD_EMAIL}?subject=Advertising%20in%20Hollywood%20International%20Filmmaker">Email us about advertising</a></div>
  <img src="assets/img/ad-bestmag.jpg" width="{w}" height="{hh}" alt="Magazine promotional image: Hollywood International Filmmaker covers displayed with industry awards" loading="lazy" decoding="async">
</div></section>
</main>
'''
    h += footer().replace('<script src="assets/js/site.js"></script>', '<script src="assets/js/site.js"></script>\n<script src="assets/js/carousel.js"></script>')
    write("index.html", h)

# ------------------------------------------------------------------ ARCHIVE
def archive():
    h = head("Archive — Hollywood International Filmmaker", "Browse and read past issues of Hollywood International Filmmaker magazine.")
    h += chrome_top(active="archive")
    def icard(num, season, yr, subj, cf, alt):
        href = pdf_href(num)
        return f'''<div class="issue-card" id="issue-{num}"><a class="cvlink" href="{href}"><div class="cv">{img(cf, alt)}</div>
  <h3>{esc(subj)}</h3><span class="meta">Issue {num} &middot; {season}</span></a>
  <a class="dl" href="{href}" download>Download PDF</a></div>'''
    years = sorted({a[2] for a in ARCHIVE}, reverse=True)
    body = ""
    for y in years:
        cards = "".join(icard(*a) for a in ARCHIVE if a[2] == y)
        if y == 2025:
            cards += ""
        body += f'<h2 class="year">{y}</h2><div class="issues">{cards}</div>'
        if y == 2026:
            body += '<h2 class="year">2025</h2><div class="issues"><div class="issue-card"><div class="cv pending"><b>29</b><span>Cover image to come</span></div><h3>Quentin Tarantino</h3><span class="meta">Issue 29 &middot; Fall 2025</span></div></div>'
    h += f'''<main id="main">
{back_bar()}
<div class="wrap">
<div class="page-head"><h1>The Archive</h1><p>Every printed issue, online. Click a cover to read the issue in your browser, or download the PDF.</p></div>
{body}
<p class="note"><strong>Demo note:</strong> Issues 31, 30, 12, 11 and 9 are built from the PDFs provided. Issue numbers for the older issues are provisional. Issue 29 is a placeholder until its files arrive. Older issues would appear below in the same grid, newest first.</p>
</div>
{back_bar(end=True)}
</main>'''
    h += footer()
    write("archive.html", h)

# ------------------------------------------------------------------ STORY PAGES
def story(key):
    a = STORIES[key]
    body = ""
    for p in a["body"]:
        if p.startswith("PULL:"):
            body += f'<blockquote class="pull">“{esc(p[5:])}”</blockquote>'
        elif p.startswith("Q:"):
            body += f'<h2 class="q">{esc(p[2:])}</h2>'
        else:
            body += f"<p>{esc(p)}</p>"
    printed = "".join(f'<figure><a href="assets/img/{n}">{img(n, alt)}</a><figcaption class="caption">{cap}</figcaption></figure>' for n, cap, alt in a["spreads"])
    by = f'<p class="byline"><span>By</span> {esc(a["byline"])} <span>&middot; {a["pages"]}</span></p>' if a["byline"] else f'<p class="byline"><span>{a["pages"]}</span></p>'
    h = head(f"{a['title']} — Hollywood International Filmmaker", a["dek"])
    h += chrome_top()
    h += f'''<main id="main">
{back_bar()}
<div class="wrap">
<header class="article-head"><span class="kicker">{a["kicker"]} &middot; Issue {CUR_ISSUE} &middot; {CUR_SEASON}</span>
  <h1>{esc(a["title"])}</h1><p class="dek">{esc(a["dek"])}</p>{by}</header>
<figure class="lede-img">{img(a["lead"], a["lead_alt"], eager=True)}</figure>
<div class="article-cols"><article class="body">{body}
<p class="end-note">This story first appeared in Issue {CUR_ISSUE} ({CUR_SEASON}) of Hollywood International Filmmaker.</p>
<section class="printed" aria-label="As it appeared in print"><div class="sec-head"><h2>As it appeared in print</h2></div>{printed}</section>
</article>
<aside class="sidebar">{ad_diamond()}</aside></div>
</div>
{back_bar(end=True)}
</main>'''
    h += footer()
    write(a["file"], h)

if __name__ == "__main__":
    home(); archive()
    for k in STORIES: story(k)
    print("built", 2 + len(STORIES), "pages")
