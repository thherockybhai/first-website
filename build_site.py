import os

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>RSM Security Services | Precision. Protection. Performance.</title>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Barlow+Condensed:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--r-red:#b91c1c;--r-redd:#7f1d1d;--r-blk:#080a07;--r-char:#141610;--r-oli:#1a2208;--r-gld:#c9a84c;--r-ow:#e8e4d8;--r-mut:#8a8a7a;--r-grn:#00ff88;--r-tr:transparent}
*{margin:0;padding:0;box-sizing:border-box;cursor:none}
html{scroll-behavior:smooth;scrollbar-width:none}
::-webkit-scrollbar{display:none}
body{background:var(--r-blk);color:var(--r-ow);font-family:'Barlow Condensed',sans-serif;overflow-x:hidden}
#scan{position:fixed;inset:0;pointer-events:none;z-index:997;background:repeating-linear-gradient(to bottom,var(--r-tr) 0,var(--r-tr) 2px,rgba(185,28,28,.04) 2px,rgba(185,28,28,.04) 3px)}
#curs{position:fixed;width:28px;height:28px;pointer-events:none;z-index:999;transform:translate(-50%,-50%);background:url('data:image/svg+xml;utf8,<svg width="28" height="28" xmlns="http://www.w3.org/2000/svg"><circle cx="14" cy="14" r="13" fill="none" stroke="%23b91c1c"/><path d="M14 0v4M14 24v4M0 14h4M24 14h4" stroke="%23b91c1c"/><circle cx="14" cy="14" r="1.5" fill="%23b91c1c"/></svg>') center no-repeat;transition:transform .15s}
.hov:hover~#curs,a:hover~#curs,button:hover~#curs{transform:translate(-50%,-50%) scale(1.6);filter:hue-rotate(45deg)}
.tk{position:fixed;top:0;width:100%;height:32px;background:var(--r-blk);border-bottom:.5px solid rgba(185,28,28,.4);z-index:996;display:flex;align-items:center;overflow:hidden}
.tk-i{display:inline-block;white-space:nowrap;animation:mq 40s linear infinite;font-family:'IBM Plex Mono',monospace;font-size:11px;letter-spacing:.1em;color:var(--r-mut)}
.tk-i span{color:var(--r-gld)}
@keyframes mq{0%{transform:translateX(0)}100%{transform:translateX(-50%)}}
nav{position:fixed;top:32px;width:100%;height:64px;background:rgba(8,10,7,.85);backdrop-filter:blur(16px);border-bottom:.5px solid rgba(185,28,28,.3);z-index:995;display:flex;justify-content:space-between;align-items:center;padding:0 40px}
.nl{display:flex;gap:32px}
.nl a{font-weight:600;font-size:13px;text-transform:uppercase;letter-spacing:.12em;color:var(--r-ow);text-decoration:none;border-bottom:1px solid transparent;transition:.2s}
.nl a:hover{color:var(--r-red);border-bottom-color:var(--r-red)}
#hero{height:100vh;position:relative;background:var(--r-blk);overflow:hidden}
#cnv{position:absolute;inset:0;z-index:1}
#so{position:absolute;inset:0;background:rgba(0,255,136,.06);opacity:0;z-index:2;pointer-events:none}
#hud{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);text-align:center;z-index:3;opacity:0}
.brk{position:absolute;width:30px;height:30px;border:2px solid var(--r-grn);opacity:0;z-index:3}
.btl{top:40px;left:40px;border-right:0;border-bottom:0} .btr{top:40px;right:40px;border-left:0;border-bottom:0}
.bbl{bottom:40px;left:40px;border-right:0;border-top:0} .bbr{bottom:40px;right:40px;border-left:0;border-top:0}
.hl{position:absolute;bottom:80px;left:80px;z-index:10;padding:48px}
.hr{position:absolute;bottom:80px;right:80px;z-index:10;background:rgba(8,10,7,.75);backdrop-filter:blur(20px);border:.5px solid rgba(185,28,28,.4);border-radius:12px;padding:28px 32px;display:grid;grid-template-columns:1fr 1fr;gap:24px}
.btn{background:var(--r-red);color:var(--r-ow);padding:14px 32px;font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:14px;letter-spacing:.15em;text-decoration:none;text-transform:uppercase;transition:.3s;display:inline-block;border-radius:2px}
.btn-s{background:0 0;border:1.5px solid var(--r-gld);color:var(--r-gld)}
.btn:hover{transform:scale(1.04)}
.btn-p:hover{box-shadow:0 0 20px rgba(185,28,28,.5)}
.f-ant{font-family:'Anton',sans-serif} .f-mon{font-family:'IBM Plex Mono',monospace}
.c-red{color:var(--r-red)} .c-gld{color:var(--r-gld)} .c-mut{color:var(--r-mut)} .c-ow{color:var(--r-ow)}

.s-wrap{display:flex;gap:48px;padding:48px 80px 80px;max-width:1400px;margin:0 auto}
.s-col{flex:1}
.scard{background:var(--r-char);border-left:3px solid;border-radius:6px;padding:18px 22px;margin-bottom:10px;display:flex;align-items:center;gap:16px;transition:all .15s}
.scr{border-left-color:rgba(185,28,28,.5)} .scg{border-left-color:rgba(201,168,76,.5)}
.scard:hover{background:#1a1c17;transform:translateY(-3px)}
.scr:hover{border-left-color:var(--r-red)} .scg:hover{border-left-color:var(--r-gld)}
.sci{width:36px;height:36px;display:flex;justify-content:center;align-items:center}
.sc-ti{font-weight:600;font-size:16px;color:var(--r-ow)} .sc-de{font-weight:400;font-size:13px;color:var(--r-mut);margin-top:2px}

.wgrd{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;padding:40px 80px;max-width:1400px;margin:0 auto}
.wcd{background:var(--r-char);border-top:2px solid var(--r-red);border-radius:8px;padding:28px;transition:all .3s}
.wcd:hover{background:rgba(185,28,28,.08);border-top-color:#ff3333;box-shadow:0 4px 24px rgba(185,28,28,.2)}

.tcon{display:flex;overflow-x:auto;scroll-snap-type:x mandatory;padding:40px 80px;gap:20px;scrollbar-width:none}
.tcd{flex:0 0 380px;scroll-snap-align:start;background:rgba(20,22,16,.9);border:.5px solid rgba(185,28,28,.25);border-radius:16px;padding:32px;position:relative}

.sec-ov{font-size:11px;letter-spacing:.2em;text-transform:uppercase}
.sec-ti{font-size:72px;line-height:1;margin-top:8px}
.sec-hl{width:64px;height:2px;background:var(--r-red);margin:16px auto}

section{position:relative;z-index:5;opacity:0}
.he{opacity:0}

@media(max-width:1024px){.s-wrap,.wgrd,#abt .w{flex-direction:column;grid-template-columns:1fr}.wgrd{grid-template-columns:repeat(2,1fr)}.cr{padding:40px 80px}}
@media(max-width:768px){*{cursor:auto!important}#curs{display:none!important}.hl{padding:40px 24px;bottom:80px;left:0}.hr{position:relative;bottom:auto;right:auto;padding:0 24px;margin-top:100vh;transform:translateY(-70px)}.s-wrap,.wgrd,.tcon,#cnt .w{padding:40px 24px}.wgrd{grid-template-columns:1fr}nav .nl{display:none}nav .hb{display:flex}}
</style>
</head>
<body>
<div id="scan"></div><div id="curs"></div>

<div class="tk"><div class="tk-i">""" + ("RSM SECURITY SERVICES <span>&middot;</span> EST. 2011 <span>&middot;</span> HASSAN & BENGALURU <span>&middot;</span> INDUSTRIAL SECURITY <span>&middot;</span> HOUSING SOCIETY PROTECTION <span>&middot;</span> WATCHMAN SERVICES <span>&middot;</span> GUNMAN <span>&middot;</span> BODY GUARD <span>&middot;</span> FACILITY MANAGEMENT <span>&middot;</span> LABOUR SUPPLY <span>&middot;</span> PEST CONTROL <span>&middot;</span> HOUSEKEEPING <span>&middot;</span> VEHICLE MANAGEMENT <span>&middot;</span> CALL: +91 97317 90907 <span>&middot;</span> PRECISION. PROTECTION. PERFORMANCE. <span>&middot;</span> " * 4) + """</div></div>

<nav>
<div class="hov"><img src="x" onerror="this.outerHTML='<div style=\\'display:flex;flex-direction:column\\'><div class=\\'f-ant c-red\\' style=\\'font-size:30px;line-height:1\\'>RSM</div><div style=\\'font-size:11px;font-weight:600;letter-spacing:.15em;color:var(--r-ow)\\'>SECURITY SERVICES</div></div>'"></div>
<div class="nl"><a href="#hero">Home</a><a href="#srv">Services</a><a href="#abt">About</a><a href="#why">Why Us</a><a href="#tst">Clients</a><a href="#cnt">Contact</a></div>
<div class="hb" style="display:none;flex-direction:column;gap:5px;padding:10px" onclick="tm()"><div style="width:20px;height:2px;background:#e8e4d8"></div><div style="width:20px;height:2px;background:#e8e4d8"></div></div>
</nav>

<div id="mm" style="position:fixed;inset:0;background:var(--r-blk);z-index:994;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:32px;opacity:0;pointer-events:none;transition:.4s">
""" + "".join([f'<a href="#{l.lower()[:3]}" class="ml f-ant c-ow" style="font-size:48px;text-decoration:none" onclick="tm()">{l.upper()}</a>' for l in ["Home","Services","About","Why Us","Clients","Contact"]]) + """
</div>

<div id="hero">
  <div id="cnv"></div>
  <div id="so"></div>
  <div id="hud" class="f-mon"><div style="color:var(--r-grn);font-weight:700;font-size:14px;letter-spacing:.3em">AREA SECURED</div><div class="c-gld" style="font-size:11px;margin-top:8px">PROTECTED BY RSM SECURITY SERVICES</div></div>
  <div class="brk btl"></div><div class="brk btr"></div><div class="brk bbl"></div><div class="brk bbr"></div>
  
  <div class="hl">
    <div class="he" style="display:flex;align-items:center;gap:8px;margin-bottom:16px"><div style="width:8px;height:8px;background:var(--r-red);border-radius:50%;animation:pls 1.5s infinite"></div><div class="f-mon c-mut" style="font-size:11px">OPERATIONAL SINCE 2011 &middot; HASSAN & BENGALURU</div></div>
    <div class="he f-ant c-ow" style="font-size:120px;line-height:.85">RSM</div>
    <div class="he f-ant" style="font-size:120px;line-height:.85;color:transparent;-webkit-text-stroke:2px var(--r-red)">SECURITY</div>
    <div class="he f-ant c-gld" style="font-size:80px;line-height:1">SERVICES</div>
    <div class="he c-ow" style="font-weight:600;font-size:20px;letter-spacing:.25em;margin-top:16px;text-transform:uppercase">Precision. Protection. Performance.</div>
    <div class="he f-mon c-mut" style="font-size:12px;margin-top:8px">Industrial Security &middot; Facility Management &middot; Labour Supply</div>
    <div class="he" style="display:flex;gap:16px;margin-top:28px"><a href="#srv" class="btn btn-p">EXPLORE SERVICES</a><a href="#cnt" class="btn btn-s">CONTACT US</a></div>
  </div>
  
  <div class="hr he">
""" + "".join([f'<div><div class="f-ant c-gld" style="font-size:56px;line-height:1">{nu}</div><div class="f-mon c-mut" style="font-size:10px;margin-top:4px">{la}</div></div>' for nu,la in [("13+","YEARS ACTIVE"),("500+","CLIENTS"),("12","SERVICE TYPES"),("2011","EST.")]]) + """
  </div>
</div>

<div class="tk" style="position:relative;top:auto;border-top:.5px solid rgba(185,28,28,.3);z-index:5;"><div class="tk-i" style="animation-duration:35s;font-size:12px">""" + ("".join([f'<span>◆</span> {x} ' for x in ["INDUSTRIAL SECURITY", "HOUSING SOCIETY PROTECTION", "WATCHMAN", "GUNMAN", "BODY GUARD", "FACILITY MANAGEMENT", "HOUSEKEEPING", "PEST CONTROL", "GARDENING", "PANTRY SERVICES", "COOKS", "STORE MANAGEMENT", "VEHICLE MANAGEMENT", "FOOD SERVICES", "TOUR MANAGEMENT", "RENTING"]]) * 2) + """</div></div>

<section id="srv" style="background:var(--r-blk);padding:80px 0;min-height:100vh">
  <div style="text-align:center"><div class="f-mon c-mut sec-ov">WHAT WE DELIVER</div><div class="f-ant c-ow sec-ti">Our Services</div><div class="sec-hl"></div></div>
  <div class="s-wrap">
    <div class="s-col">
      <div class="c-red" style="font-weight:700;font-size:22px;margin-bottom:24px;text-transform:uppercase">Security & Facility</div>
      """ + "".join([f'<div class="scard scr he"><div class="sci"><div style="width:24px;height:24px;border:2px solid var(--r-red);border-radius:4px 4px 12px 12px"></div></div><div><div class="sc-ti">{t}</div><div class="sc-de">{d}</div></div></div>' for t,d in [("Industrial Security","Comprehensive protection for manufacturing"),("Housing Society Protection","24/7 guarded security for complexes"),("Gunman & Body Guard","Armed personnel & VIP protection"),("Facility Management","Repair, Restore, Maintain & Represent"),("Housekeeping & Pest Control","Sanitation and pest management"),("Vehicle & Tour Management","Logistics and parking control"),("Gardening, Pantry & Cooks","Landscaping & culinary staff"),("Store Management","Inventory and store oversight")]]) + """
    </div>
    <div class="s-col">
      <div class="c-gld" style="font-weight:700;font-size:22px;margin-bottom:24px;text-transform:uppercase">Labour Management</div>
      """ + "".join([f'<div class="scard scg he"><div class="sci"><div class="c-gld" style="width:28px;height:28px;border:2px solid currentColor;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:12px;font-weight:700">LD</div></div><div><div class="sc-ti">{t}</div><div class="sc-de">{d}</div></div></div>' for t,d in [("Qualified & Experienced Staff","Vetted professional personnel"),("Skilled Operators","Professionally trained operational staff"),("Skill Matrix Maintained","Continuous competency evaluation"),("Performance Measured","Metrics-driven service standards"),("Service Reliable","Consistent deliverables"),("Flexible Deployment","Engagement models suited to you"),("Minimum Turnaround Time","Rapid employment capability")]]) + """
      <div class="he" style="border:1px solid rgba(201,168,76,.3);background:rgba(201,168,76,.05);border-radius:8px;padding:20px;margin-top:24px;font-size:14px;line-height:1.6;color:var(--r-ow)"><strong>Technical & Office Management</strong> — We supply trained, certified labour for both technical operations and office support roles across Karnataka.</div>
    </div>
  </div>
</section>

<section id="abt" style="background:var(--r-oli);padding:80px;min-height:80vh">
  <div class="w" style="display:flex;max-width:1400px;margin:0 auto;gap:60px">
    <div style="flex:0 0 55%;position:relative;padding-left:20px">
      <div style="position:absolute;left:24px;top:10px;bottom:10px;width:1px;background:rgba(185,28,28,.3)"></div>
      """ + "".join([f'<div class="he" style="position:relative;padding-left:40px;margin-bottom:40px"><div style="position:absolute;left:-3px;top:12px;width:8px;height:8px;background:var(--r-red);border-radius:50%;box-shadow:0 0 10px rgba(185,28,28,.6)"></div><div class="f-ant c-red" style="font-size:36px;line-height:1">{y}</div><div class="c-ow" style="font-weight:500;font-size:15px;margin-top:4px">{e}</div></div>' for y,e in [("2011","RSM Security Founded, Hassan"),("2013","Industrial & Housing Security Launched"),("2015","Facility Management Services Added"),("2017","Labour Supply Division established"),("2019","200+ Active Clients Across Karnataka"),("2022","12 Full Service Categories Operational"),("2025","500+ Clients &middot; Hassan & Bengaluru")]]) + """
    </div>
    <div style="flex:0 0 45%" class="art">
      <div class="f-mon c-mut sec-ov he">EST. 2011 &middot; HASSAN, KARNATAKA</div>
      <h3 class="f-ant c-ow he" style="font-size:52px;line-height:1.1;margin:12px 0 24px">Built on Trust.<br>Deployed with Precision.</h3>
      <p class="c-ow he" style="font-size:15px;line-height:1.8;margin-bottom:16px">RSM Security Services was founded in 2011 with a singular mission — to deliver professional, reliable, and disciplined security and facility management solutions to clients across Karnataka. From industrial premises to residential societies, we guard what matters most.</p>
      <p class="c-ow he" style="font-size:15px;line-height:1.8;margin-bottom:16px">Our labour management division provides qualified, certified, and performance-tracked personnel for both technical and office operations. Every individual we deploy is assessed through our proprietary skill matrix, ensuring you always get the right professional.</p>
      <div class="he f-mon c-ow" style="background:rgba(185,28,28,.08);border:.5px solid rgba(185,28,28,.3);border-radius:8px;padding:16px;margin-top:24px;font-size:12px;display:grid;grid-template-columns:100px 1fr;gap:8px">
        """ + "".join([f'<div class="c-mut">{k}</div><div>{v}</div>' for k,v in [("SP MAHESH","+91 97317 90907"),("MITHUN","+91 63611 60346"),("CHIRAG","+91 90199 47419"),("OFFICE","+91 90148 59090"),("ADDRESS","Sampige Road, 1st Floor, Near Women Police Station, Hassan")]]) + """
      </div>
    </div>
  </div>
</section>

<section id="why" style="background:var(--r-blk);padding:80px 0;min-height:80vh">
  <div style="text-align:center"><div class="f-mon c-red sec-ov">OPERATIONAL ADVANTAGE</div><div class="f-ant c-ow sec-ti">Why RSM?</div><div class="sec-hl"></div></div>
  <div class="wgrd">
    """ + "".join([f'<div class="wcd he"><div style="width:36px;height:42px;border:3px solid var(--r-red);border-radius:4px 4px 20px 20px;margin:0 auto 20px"></div><div class="c-ow" style="font-weight:700;font-size:18px;margin-bottom:8px">{t}</div><div class="c-mut" style="font-size:13px;line-height:1.5">{d}</div></div>' for t,d in [("13+ Years Experience","Over a decade of trusted service excellence."),("Trained & Certified Staff","Rigorous selection and continuous evaluation."),("End-to-End Solutions","Single point for all facility management needs."),("Flexible Engagement","Customized models designed for your business."),("Rapid Response","Low turnaround time for emergent requests."),("Serving 500+ Clients","A vast network of satisfied partners.")]]) + """
  </div>
  <div class="he" style="display:flex;justify-content:center;align-items:center;gap:40px;padding:20px 80px 80px;flex-wrap:wrap">
    """ + "".join([f'<div style="text-align:center"><div class="f-ant c-gld" style="font-size:64px;line-height:1">{n}</div><div class="f-mon c-mut" style="font-size:11px;margin-top:8px">{l}</div></div><div style="width:1px;height:60px;background:rgba(185,28,28,.2)"></div>' for n,l in [("13+","YEARS"),("500+","CLIENTS"),("12","SERVICES")]] + [f'<div style="text-align:center"><div class="f-ant c-gld" style="font-size:64px;line-height:1">100+</div><div class="f-mon c-mut" style="font-size:11px;margin-top:8px">STAFF</div></div>']) + """
  </div>
</section>

<section id="tst" style="background:var(--r-char);padding:80px 0;min-height:60vh;overflow:hidden">
  <div style="text-align:center"><div class="f-mon c-red sec-ov">VOICES FROM THE FIELD</div><div class="f-ant c-ow sec-ti">Client Trust</div><div class="sec-hl"></div></div>
  <div class="tcon he">
    """ + "".join([f'<div class="tcd"><div class="f-ant c-red" style="position:absolute;top:10px;left:20px;font-size:96px;opacity:.15;line-height:1">"</div><div class="f-mon c-gld" style="font-size:14px;margin-bottom:20px">★★★★★</div><div class="c-ow" style="font-size:15px;font-style:italic;line-height:1.75;margin-bottom:24px;position:relative;z-index:2">{q}</div><div class="f-mon c-red" style="font-weight:700;font-size:12px">{n}</div><div class="f-mon c-mut" style="font-size:11px;margin-top:2px">{r}</div></div>' for q,n,r in [("RSM completely transformed our housing society\\'s security. Their watchmen are disciplined, alert, and professionally trained. Night or day, we feel protected.","Rajesh Kumar","Secretary, Greenwood Residency"),("We have relied on RSM for facility management and pest control for over four years. Response time is exceptional and service quality never drops.","Anita Sharma","Admin Manager, Prestige Tech Towers"),("Their labour deployment process is unlike anything we\\'ve seen. The skill matrix approach means every technician they send is exactly right for the job.","Venkat Rao","Operations Head, Mantri Infrastructure"),("From pantry to vehicle management — RSM handles our entire facility. Hiring them was the best operational decision we\\'ve made in five years.","Deepa Nair","HR Director, Sobha Developers"),("RSM\\'s body guard service gave our executive team complete confidence during a high-profile industry event. Absolute professionals.","Suresh Patil","CEO, Summit Hospitality Group")]]) + """
  </div>
</section>

<section id="cnt" style="background:var(--r-blk);display:flex;align-items:center;min-height:60vh">
  <div class="w" style="display:flex;width:100%;max-width:1400px;margin:0 auto">
    <div class="he" style="flex:1;padding:80px"><h2 class="f-ant c-ow" style="font-size:80px;line-height:1;margin:0">READY TO SECURE<br><span class="c-red">YOUR FACILITY?</span></h2><div class="c-ow" style="font-size:16px;line-height:1.7;margin-top:24px;max-width:400px">From security personnel to complete facility management — RSM delivers precision-trained professionals to your doorstep.</div><a href="tel:+919014859090" class="btn btn-p" style="margin-top:32px">GET IN TOUCH</a><span class="f-mon c-mut" style="font-size:11px;margin-top:16px;display:block">Response within 24 hours &middot; Active in Hassan & Bengaluru</span></div>
    <div class="he cr" style="flex:1;display:flex;flex-direction:column;gap:12px;justify-content:center">
      """ + "".join([f'<div style="background:var(--r-char);border-left:3px solid var(--{c});border-radius:0 8px 8px 0;padding:16px 20px;display:flex;align-items:{"center" if "red" in c else "flex-start"};gap:20px"><div class="c-gld" style="font-weight:600;font-size:14px;text-transform:uppercase;width:80px">{n}</div><div class="f-mon c-ow" style="font-size:{"15px" if "red" in c else "12px"};line-height:1.5;text-decoration:none">{v}</div></div>' for c,n,v in [("r-red","SP MAHESH","+91 97317 90907"),("r-red","MITHUN","+91 63611 60346"),("r-red","CHIRAG","+91 90199 47419"),("r-red","OFFICE","+91 90148 59090"),("r-gld","ADDRESS","Sampige Road, 1st Floor, 1st Cross<br>Near Women Police Station, Hassan<br>Karnataka, India")]]) + """
    </div>
  </div>
</section>

<footer style="width:100%;height:56px;background:#050705;border-top:.5px solid rgba(185,28,28,.2);display:flex;justify-content:space-between;align-items:center;padding:0 40px;font-family:'IBM Plex Mono',monospace;font-size:11px;color:var(--r-mut)">
  <div>RSM SECURITY SERVICES &copy; 2025</div><div class="c-red" style="font-size:10px">◆ ◆ ◆</div><div>EST. 2011 &middot; HASSAN, KARNATAKA</div>
</footer>

<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script>
// Mobile toggle
function tm(){ const m=document.getElementById('mm'); if(m.style.opacity=='0'){ m.style.opacity='1'; m.style.pointerEvents='all'; gsap.to('.ml',{y:0,opacity:1,stagger:0.1,ease:'back.out'});} else { m.style.opacity='0'; m.style.pointerEvents='none'; gsap.set('.ml',{y:20,opacity:0}); } }

// Cursor
const cur = document.getElementById('curs');
let cx=0, cy=0, tx=0, ty=0;
document.addEventListener('mousemove',e=>{ tx=e.clientX; ty=e.clientY; });
function raf(){ cx+=(tx-cx)*0.12; cy+=(ty-cy)*0.12; cur.style.left=cx+'px'; cur.style.top=cy+'px'; requestAnimationFrame(raf); } raf();
if(('ontouchstart' in window) || (navigator.maxTouchPoints > 0)) cur.style.display='none';

// Reveal
const obs = new IntersectionObserver((es)=>{ es.forEach(e=>{ if(e.isIntersecting){ gsap.fromTo(e.target,{opacity:0,y:50},{opacity:1,y:0,duration:0.9,ease:'power3.out',stagger:0.1}); obs.unobserve(e.target); } }); },{threshold:0.12});
document.querySelectorAll('.he').forEach(e=>obs.observe(e));
document.addEventListener('DOMContentLoaded', ()=> gsap.set('.he',{opacity:0}) );

// Three.js Build
const scene = new THREE.Scene(); scene.fog = new THREE.FogExp2(0x080a07, 0.012);
const W=window.innerWidth, H=window.innerHeight;
const camera = new THREE.PerspectiveCamera(45, W/H, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({alpha:true, antialias:true});
renderer.setSize(W, H); renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
document.getElementById('cnv').appendChild(renderer.domElement);

const city = new THREE.Group(); scene.add(city);
const mat = new THREE.MeshStandardMaterial({color:0x1a1c14});
const gBox = new THREE.BoxGeometry(1,1,1);
for(let i=0;i<100;i++){
  let h = 2 + Math.random()*16, w = 1 + Math.random()*2, d = 1 + Math.random()*2;
  const b = new THREE.Mesh(gBox, mat); b.scale.set(w,h,d); b.position.set((Math.random()-0.5)*120, h/2, (Math.random()-0.5)*120);
  const edges = new THREE.LineSegments(new THREE.EdgesGeometry(gBox), new THREE.LineBasicMaterial({color:0xb91c1c, transparent:true, opacity:0.5}));
  b.add(edges); city.add(b);
}
const plane = new THREE.Mesh(new THREE.PlaneGeometry(200,200), new THREE.MeshStandardMaterial({color:0x0d0f0b}));
plane.rotation.x = -Math.PI/2; scene.add(plane);
scene.add(new THREE.GridHelper(200, 40, 0xb91c1c, 0x1a1c14));
scene.add(new THREE.AmbientLight(0x1a0808, 0.4));
const dl = new THREE.DirectionalLight(0xb91c1c, 0.8); dl.position.set(10,20,10); scene.add(dl);
const pl = new THREE.PointLight(0xc9a84c, 0.6); pl.position.set(0,30,0); scene.add(pl);

const pGeo = new THREE.BufferGeometry(); const pPos = new Float32Array(1500*3);
for(let i=0;i<1500;i++){ pPos[i*3]=(Math.random()-0.5)*150; pPos[i*3+1]=Math.random()*40; pPos[i*3+2]=(Math.random()-0.5)*150; }
pGeo.setAttribute('position', new THREE.BufferAttribute(pPos,3));
const particles = new THREE.Points(pGeo, new THREE.PointsMaterial({color:0xc9a84c, size:0.15, transparent:true, opacity:0.6}));
scene.add(particles);

const camGrp = new THREE.Group();
const cMat = new THREE.MeshStandardMaterial({color:0x2a2d26, roughness:0.3, metalness:0.8});
const body = new THREE.Mesh(new THREE.CylinderGeometry(1.2,1.5,3,8), cMat); body.rotation.z=Math.PI/2;
const lensC = new THREE.Mesh(new THREE.CylinderGeometry(0.6,0.8,1.2,12), cMat); lensC.position.x=-2; lensC.rotation.z=Math.PI/2;
const arm = new THREE.Mesh(new THREE.BoxGeometry(0.3,2.5,0.3), cMat); arm.position.set(0,2,0);
const mnt = new THREE.Mesh(new THREE.BoxGeometry(1.5,0.3,1.5), cMat); mnt.position.set(0,3.2,0);
const lMat = new THREE.MeshStandardMaterial({color:0xb91c1c, emissive:0xb91c1c, emissiveIntensity:0.8, transparent:true, opacity:0.9});
const lensG = new THREE.Mesh(new THREE.CylinderGeometry(0.5,0.5,1.21,12), lMat); lensG.position.x=-2; lensG.rotation.z=Math.PI/2;
camGrp.add(body,lensC,arm,mnt,lensG);

const cvs = document.createElement('canvas'); cvs.width=256; cvs.height=64; const ctx=cvs.getContext('2d');
ctx.fillStyle='#1a1c14'; ctx.fillRect(0,0,256,64); ctx.fillStyle='#b91c1c'; ctx.font='32px Anton,sans-serif'; ctx.fillText('RSM', 10, 32); ctx.fillStyle='#c9a84c'; ctx.font='11px sans-serif'; ctx.fillText('SECURITY SERVICES', 10, 50);
const lbl = new THREE.Mesh(new THREE.PlaneGeometry(2.5,0.7), new THREE.MeshBasicMaterial({map:new THREE.CanvasTexture(cvs)}));
lbl.position.set(0,0,1.51); camGrp.add(lbl);

camGrp.position.set(0,80,20); scene.add(camGrp);
if(W<768) camGrp.scale.set(0.6,0.6,0.6);

const scP = new THREE.Mesh(new THREE.PlaneGeometry(200,0.3), new THREE.MeshBasicMaterial({color:0xff0000, transparent:true, opacity:0.35}));
scP.rotation.x = -Math.PI/2; scP.position.y=0.2; scP.position.z=-100; scene.add(scP);

camera.position.set(0,60,80); camera.lookAt(0,0,0);
const tl = gsap.timeline();
tl.to(camera.position, {y:25, z:50, duration:2, ease:'power2.inOut'}, 0)
  .to(camGrp.position, {y:35, duration:2, ease:'back.out(1.2)'}, 2)
  .to(lMat, {emissiveIntensity:2.0, duration:0.4, yoyo:true, repeat:3}, 4)
  .to(scP.position, {z:100, duration:2.5, ease:'none'}, 4)
  .to('#so', {opacity:0.3, duration:0.3, yoyo:true, repeat:1}, 6.5)
  .to('#so', {opacity:0.03, duration:0.1}, 7.1)
  .to('.brk', {opacity:1, duration:0.3}, 7)
  .to('#hud', {opacity:1, duration:0.4}, 7)
  .to('#hud', {opacity:0.7, duration:0.1, yoyo:true, repeat:4}, 7.4)
  .to('.hl > *, .hr', {opacity:1, y:0, stagger:0.12, duration:0.8, ease:'power3.out'}, 8);

function render(){
  const pA = pGeo.attributes.position.array;
  for(let i=0;i<1500;i++){ pA[i*3+1]+=0.02; if(pA[i*3+1]>20) pA[i*3+1]=0; }
  pGeo.attributes.position.needsUpdate=true;
  if(tl.time()>8){
    camGrp.rotation.y += 0.003;
    camGrp.position.y = 35 + Math.sin(Date.now()*.0015)*0.5;
    city.rotation.y += 0.0005;
  }
  renderer.render(scene, camera);
  requestAnimationFrame(render);
}
render();
window.addEventListener('resize',()=>{ camera.aspect=window.innerWidth/window.innerHeight; camera.updateProjectionMatrix(); renderer.setSize(window.innerWidth, window.innerHeight); });
</script>
</body>
</html>"""

with open('c:/Users/user/.gemini/antigravity/playground/vector-viking/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
