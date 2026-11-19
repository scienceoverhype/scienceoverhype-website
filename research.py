"""Research articles for scienceoverhype.com/research/.
One dict per article. build.py renders each into a page with a short-answer box, question headings,
sources, a visible FAQ, an author box and JSON-LD (Article + FAQPage + BreadcrumbList)."""

PM = "https://pubmed.ncbi.nlm.nih.gov/"

AUTHOR = {
    "name": "Nitish Vaibhav",
    "url": "/about/",
    "bio": ("Founder of Science Over Hype. Prediabetic with high cholesterol at 25, he got his reports back to "
            "the normal range by testing habits against the research. Not a doctor: every claim here links to "
            "its study, and this page is education, not medical advice."),
}

ARTICLES = [
# ------------------------------------------------------------------ #01
dict(
 slug="walking-after-meals-blood-sugar",
 num="01", series="Explainer",
 title="Does walking after a meal lower blood sugar?",
 desc="Yes. Studies show a light walk after eating lowers the post-meal blood sugar spike, even 2–5 minutes. Here is what the research found, how long to walk, and when.",
 published="2026-11-13", reviewed="2026-11-19",
 verdict="SCIENCE",
 verdict_text=("Yes. A light walk after eating lowers the rise in blood sugar that follows a meal. A review of 7 studies "
               "found that even 2–5 minutes of light walking beat sitting. In people with type 2 diabetes, a 10-minute "
               "walk after each meal worked better than one 30-minute walk at another time, most of all after dinner."),
 keywords=["walk after meal", "post-meal blood sugar", "glucose spike", "walking after dinner", "type 2 diabetes"],
 sections=[
  ("What happens to blood sugar after you eat?",
   "<p>Carbohydrates in a meal are broken down into glucose, which enters the blood over the next hour or two. "
   "That rise is normal. What matters for long-term metabolic health is how high and how often it spikes, and many of us "
   "eat our largest, most carb-heavy meal at night and then sit down.</p>"),
  ("Why does walking help?",
   "<p>Working muscles pull glucose out of the blood. When a muscle contracts, it moves glucose transporters (GLUT4) to its "
   "surface, so it can take in sugar without needing extra insulin. Walking uses the biggest muscles in the body, which is "
   "why even a slow walk makes a difference.</p>"),
  ("What do the studies show?",
   "<ul>"
   "<li><strong>Even 2–5 minutes helps.</strong> A meta-analysis of 7 studies found that breaking up sitting with light walking "
   "lowered post-meal glucose more than sitting. Standing helped a little; walking helped more. "
   "<span class='cite'>Buffey et al., Sports Medicine, 2022</span></li>"
   "<li><strong>10 minutes after each meal beat 30 minutes at once.</strong> In 41 adults with type 2 diabetes, a 10-minute walk "
   "after every meal lowered post-meal blood sugar by about 12% more than a single 30-minute daily walk. After dinner, the "
   "difference was about 22%. <span class='cite'>Reynolds et al., Diabetologia, 2016</span></li>"
   "<li><strong>Three short walks matched one long one.</strong> In 10 older adults at risk of impaired glucose tolerance, three "
   "15-minute walks after meals improved 24-hour blood sugar as well as one 45-minute walk, and the walk after dinner did the "
   "most. A small study. <span class='cite'>DiPietro et al., Diabetes Care, 2013</span></li>"
   "</ul>"),
  ("How long, and when, should you walk?",
   "<ul>"
   "<li><strong>When:</strong> soon after eating, ideally starting within 30 minutes and certainly within the first hour, while blood sugar is rising.</li>"
   "<li><strong>How long:</strong> 2 minutes helps; 10–15 minutes is the sweet spot in the studies.</li>"
   "<li><strong>How fast:</strong> an easy pace. You should be able to talk. This isn't a workout.</li>"
   "<li><strong>Which meal:</strong> if you only do one, do dinner.</li>"
   "</ul>"
   "<p>No space to walk? Walking around the house, climbing stairs or doing chores counts. Standing is better than sitting, "
   "but moving is better than standing.</p>"),
  ("What are the limits of the evidence?",
   "<p>Most studies are short and small, and they measure blood sugar for hours or a day, not years. They show a reliable, "
   "modest effect on post-meal glucose, not a cure for diabetes. If you take insulin or medicines that can cause low blood "
   "sugar, talk to your doctor before changing your routine.</p>"),
 ],
 faq=[
  ("Is it OK to walk right after eating?", "Yes, at an easy pace. Studies used light walking starting soon after the meal. Avoid hard exercise on a very full stomach if it makes you uncomfortable."),
  ("Is 10 minutes of walking after dinner enough?", "In a study of adults with type 2 diabetes, a 10-minute walk after each meal lowered post-meal blood sugar more than one 30-minute walk at another time, with the biggest effect after dinner."),
  ("Does standing after a meal help?", "A little. A meta-analysis found standing lowered post-meal glucose slightly compared with sitting, but light walking had a clearly larger effect."),
  ("Can walking after meals replace diabetes medication?", "No. It is a helpful habit with a modest effect. Never change medication without your doctor."),
 ],
 sources=[
  ("Buffey AJ et al. The acute effects of interrupting prolonged sitting time in adults with standing and light-intensity walking on biomarkers of cardiometabolic health: a systematic review and meta-analysis. Sports Medicine, 2022.",
   PM + "?term=Buffey+interrupting+prolonged+sitting+standing+light-intensity+walking+Sports+Med+2022"),
  ("Reynolds AN et al. Advice to walk after meals is more effective for lowering postprandial glycaemia in type 2 diabetes mellitus than advice that does not specify timing. Diabetologia, 2016.", PM + "27747394/"),
  ("DiPietro L et al. Three 15-min bouts of moderate postmeal walking significantly improves 24-h glycemic control in older people at risk for impaired glucose tolerance. Diabetes Care, 2013.", PM + "23761134/"),
 ],
 related=["7-day-sleep-reset"],
),
# ------------------------------------------------------------------ #02
dict(
 slug="does-it-take-21-days-to-form-a-habit",
 num="02", series="Explainer",
 title="Does it take 21 days to form a habit?",
 desc="No. The 21-day rule comes from a 1960 self-help book. In a UCL study of 96 people, habits took 66 days on average to become automatic, from 18 to about 254 days.",
 published="2026-11-16", reviewed="2026-11-19",
 verdict="HYPE",
 verdict_text=("No. The \"21 days\" idea comes from a 1960 self-help book, not a habit study. When UCL researchers tracked 96 "
               "people building a new daily habit, it took 66 days on average to feel automatic, ranging from 18 to an "
               "estimated 254 days. Missing a single day didn't undo progress."),
 keywords=["21 day habit", "how long to form a habit", "66 days habit", "habit formation", "Lally study"],
 sections=[
  ("Where does the 21-day rule come from?",
   "<p>It traces back to <em>Psycho-Cybernetics</em> (1960), a self-help book by plastic surgeon Maxwell Maltz. He observed that "
   "patients seemed to need \"a minimum of about 21 days\" to get used to a change, such as a new face after surgery. That was "
   "an observation about adjusting to change, not a measurement of habit formation, and over the decades \"a minimum of about "
   "21 days\" became \"21 days\".</p>"),
  ("What did the actual habit study find?",
   "<p>In 2010, researchers at University College London asked 96 volunteers to pick one new daily behaviour tied to a cue, "
   "such as drinking a glass of water after breakfast or going for a run before dinner, and to rate how automatic it felt each day for 12 weeks.</p>"
   "<ul>"
   "<li><strong>Average time to automatic: 66 days</strong> (the median).</li>"
   "<li><strong>Range: 18 to about 254 days.</strong> The longest times were estimated from each person's curve, because the study ended at 84 days.</li>"
   "<li><strong>Harder behaviours took longer.</strong> Drinking water became automatic faster than doing 50 sit-ups.</li>"
   "<li><strong>Missing one day didn't reset progress.</strong></li>"
   "</ul>"
   "<p class='cite'>Lally P et al., European Journal of Social Psychology, 2010</p>"),
  ("Why does the myth matter?",
   "<p>If you expect a habit to stick in three weeks, day 22 can feel like failure. Most people are only partway up the curve "
   "at that point. Planning for about two months is closer to what the research shows, and knowing a missed day is fine "
   "removes the \"I broke the streak, so I quit\" trap.</p>"),
  ("How do you build a habit faster?",
   "<ul>"
   "<li><strong>Tie it to a cue you already have:</strong> \"after I brush my teeth\", \"after I park the car\".</li>"
   "<li><strong>Start small.</strong> Simpler behaviours become automatic sooner. Two minutes daily beats an hour now and then.</li>"
   "<li><strong>Same time, same place.</strong> Consistent context is what turns a behaviour automatic.</li>"
   "<li><strong>Miss a day? Just continue.</strong> One miss didn't affect the curve in the study; quitting does.</li>"
   "</ul>"),
 ],
 faq=[
  ("How many days does it take to form a habit?", "In the best-known study, 66 days on average, with a range from 18 to about 254 days depending on the person and the behaviour."),
  ("Is the 21-day rule true?", "No. It comes from a 1960 self-help book's observation about adjusting to change, not from a study measuring habits."),
  ("Does missing a day ruin a habit?", "No. In the UCL study, missing one opportunity didn't materially affect how the habit formed."),
 ],
 sources=[
  ("Lally P, van Jaarsveld CHM, Potts HWW, Wardle J. How are habits formed: modelling habit formation in the real world. European Journal of Social Psychology, 2010.", "https://doi.org/10.1002/ejsp.674"),
  ("Maltz M. Psycho-Cybernetics. Prentice-Hall, 1960 (origin of the 21-day idea; not a study).", ""),
 ],
 related=["walking-after-meals-blood-sugar"],
),
# ------------------------------------------------------------------ #03
dict(
 slug="how-to-sleep-better-science",
 num="03", series="Guide",
 title="How can you sleep better? What the research supports",
 desc="What 6 hours of sleep does to hunger, immunity and focus, and the simple habits with real evidence: a fixed wake time, morning light, a caffeine cutoff and a cool, dark room.",
 published="2026-11-18", reviewed="2026-11-19",
 verdict="WHAT HELPS",
 verdict_text=("Most adults need 7 or more hours. Studies link short sleep to more hunger, a higher chance of catching a cold and "
               "slower thinking, often without feeling very tired. The habits with real evidence are simple: wake up at the "
               "same time daily, get morning daylight, stop caffeine 6 hours before bed and keep the bedroom cool and dark."),
 keywords=["how to sleep better", "sleep tips", "6 hours sleep enough", "caffeine before bed", "sleep hygiene"],
 sections=[
  ("Is 6 hours of sleep enough?",
   "<p>For most adults, no. Sleep experts recommend 7 or more hours a night. The tricky part is that short sleep doesn't always feel bad:</p>"
   "<ul>"
   "<li><strong>Hunger goes up.</strong> After two nights of 4 hours in bed, healthy young men had lower leptin (the fullness hormone), "
   "higher ghrelin (the hunger hormone) and reported more hunger. <span class='cite'>Spiegel et al., Annals of Internal Medicine, 2004</span></li>"
   "<li><strong>You catch colds more easily.</strong> When 164 adults were given a cold virus, those who had slept under 6 hours a night "
   "were about 4 times more likely to get sick than those who slept over 7. <span class='cite'>Prather et al., Sleep, 2015</span></li>"
   "<li><strong>Focus drops, but you don't notice.</strong> After two weeks of 6 hours a night, people's attention fell to the level seen "
   "after a full night without sleep, while they rated themselves only slightly sleepy. <span class='cite'>Van Dongen et al., Sleep, 2003</span></li>"
   "</ul>"),
  ("Which sleep habits have real evidence?",
   "<ol>"
   "<li><strong>Wake up at the same time every day,</strong> including weekends. Your body clock runs on routine, and a fixed wake time anchors it.</li>"
   "<li><strong>Get daylight in the morning.</strong> Morning light is the strongest signal that sets the body clock; evening light pushes it later.</li>"
   "<li><strong>No caffeine in the 6 hours before bed.</strong> In a sleep study, caffeine taken 6 hours before bedtime still cut sleep by more "
   "than an hour. The dose was 400 mg, about 3–4 cups of coffee. If you sleep at 11 pm, make 5 pm your last chai or coffee. "
   "<span class='cite'>Drake et al., Journal of Clinical Sleep Medicine, 2013</span></li>"
   "<li><strong>Keep the room cool, dark and quiet,</strong> and the phone away from the bed.</li>"
   "</ol>"),
  ("What helps with a racing mind at night?",
   "<p>Write tomorrow's to-do list. In a sleep-lab study, people who spent 5 minutes writing a specific to-do list before bed fell asleep "
   "about 9 minutes faster than people who wrote about tasks they had already finished. <span class='cite'>Scullin et al., "
   "Journal of Experimental Psychology: General, 2018</span></p>"),
  ("When should you see a doctor?",
   "<p>If you snore loudly, stop breathing in your sleep, wake up gasping, or feel very sleepy in the day despite enough time in bed, "
   "talk to a doctor. Conditions such as sleep apnoea need treatment, not tips.</p>"),
 ],
 faq=[
  ("How many hours of sleep do adults need?", "Sleep experts recommend 7 or more hours a night for adults."),
  ("How late can I drink coffee or chai?", "Aim for no caffeine in the 6 hours before bed. In one study, caffeine 6 hours before bedtime still cut sleep by more than an hour."),
  ("Does writing a to-do list help you fall asleep?", "In one sleep-lab study, people who wrote a specific to-do list for 5 minutes before bed fell asleep about 9 minutes faster."),
  ("Can you catch up on sleep at the weekend?", "Sleeping in shifts your body clock. A fixed wake time every day is one of the most reliable ways to sleep better."),
 ],
 sources=[
  ("Spiegel K et al. Sleep curtailment in healthy young men is associated with decreased leptin levels, elevated ghrelin levels, and increased hunger and appetite. Annals of Internal Medicine, 2004.", PM + "15583226/"),
  ("Prather AA et al. Behaviorally assessed sleep and susceptibility to the common cold. Sleep, 2015.", PM + "26118561/"),
  ("Van Dongen HPA et al. The cumulative cost of additional wakefulness: dose-response effects on neurobehavioral functions and sleep physiology from chronic sleep restriction and total sleep deprivation. Sleep, 2003.", "https://doi.org/10.1093/sleep/26.2.117"),
  ("Drake C et al. Caffeine effects on sleep taken 0, 3, or 6 hours before going to bed. Journal of Clinical Sleep Medicine, 2013.", PM + "24235903/"),
  ("Scullin MK et al. The effects of bedtime writing on difficulty falling asleep: a polysomnographic study comparing to-do lists and completed activity lists. Journal of Experimental Psychology: General, 2018.", PM + "29058942/"),
  ("Watson NF et al. Recommended amount of sleep for a healthy adult: a joint consensus statement of the American Academy of Sleep Medicine and Sleep Research Society. Sleep, 2015.", PM + "?term=Watson+recommended+amount+of+sleep+healthy+adult+consensus+2015"),
 ],
 related=["7-day-sleep-reset"],
),
# ------------------------------------------------------------------ #04
dict(
 slug="should-you-take-vitamin-d-supplement",
 num="04", series="The File",
 title="Should you take a vitamin D supplement?",
 desc="Low vitamin D is common in India, but in the 5-year VITAL trial, 2,000 IU a day didn't meaningfully cut cancer or heart disease in mostly healthy adults. Test, fix a real deficiency, don't megadose.",
 published="2026-11-20", reviewed="2026-11-19",
 verdict="PARTLY",
 verdict_text=("Partly. Vitamin D supplements make sense for a real deficiency, and low levels are common in India, where a review "
               "found about two-thirds of adults below 20 ng/mL. But in VITAL, a 5-year trial of 25,871 adults, 2,000 IU a day "
               "didn't meaningfully cut cancer or heart disease in mostly healthy people. Test if your doctor advises, and never megadose."),
 keywords=["vitamin D supplement", "vitamin D deficiency India", "should I take vitamin D", "VITAL trial", "vitamin D dose"],
 sections=[
  ("Why are so many Indians low in vitamin D?",
   "<p>India gets plenty of sun, yet a systematic review of South Asian studies found about 67% of Indian adults below 20 ng/mL, a common "
   "cut-off for deficiency. <span class='cite'>Siddiqee et al., BMC Public Health, 2021</span> Likely reasons:</p>"
   "<ul><li>Indoor work and avoiding midday sun.</li><li>Darker skin (more melanin) needs more sun to make the same amount.</li>"
   "<li>Air pollution blocks some of the UVB light the skin needs.</li><li>Few foods naturally contain much vitamin D.</li></ul>"
   "<p>How many people count as deficient depends heavily on which cut-off is used, so headlines like \"everyone is deficient\" overstate it.</p>"),
  ("What does vitamin D actually do?",
   "<p>Its clearest job is helping the gut absorb calcium for healthy bones. A true deficiency can weaken bones (rickets in children, "
   "osteomalacia in adults). Claims that extra vitamin D prevents most diseases have not held up in large trials.</p>"),
  ("Does taking vitamin D prevent cancer or heart disease?",
   "<p>The largest trial, VITAL, gave 25,871 adults (men 50+, women 55+) either 2,000 IU of vitamin D a day or a placebo, for a median of "
   "5.3 years. Vitamin D did not meaningfully lower the rate of invasive cancer or major heart and stroke events. Most participants were "
   "not deficient at the start, so the result applies to mostly healthy people, not to fixing a deficiency. "
   "<span class='cite'>Manson et al., New England Journal of Medicine, 2019</span></p>"
   "<p>The Endocrine Society's 2024 guideline also advises against routine vitamin D testing for healthy adults under 75, while suggesting "
   "supplements for specific groups such as older adults and pregnant women. Indian guidance and your doctor's judgement may differ, "
   "especially where deficiency is common. <span class='cite'>Demay et al., Journal of Clinical Endocrinology &amp; Metabolism, 2024</span></p>"),
  ("Who should consider a supplement?",
   "<ul>"
   "<li>People with a deficiency confirmed by the <strong>25-hydroxy vitamin D blood test</strong>.</li>"
   "<li>People with little sun exposure, darker skin, older age or conditions that affect absorption, if their doctor advises it.</li>"
   "<li>Pregnant women and older adults, under medical guidance.</li>"
   "</ul>"),
  ("Can you take too much vitamin D?",
   "<p>Yes. Vitamin D is stored in the body, so very high doses build up. Excess raises blood calcium, which can cause nausea, confusion and "
   "kidney damage; case reports from India describe this after repeated high-dose injections. Take the dose your doctor prescribes, and "
   "don't self-prescribe large weekly doses or injections.</p>"),
 ],
 faq=[
  ("Should everyone in India take vitamin D?", "No. Deficiency is common, but the right step is to test if your doctor advises it and treat a real deficiency, not to supplement blindly."),
  ("What did the VITAL trial find?", "In 25,871 adults followed for about 5 years, 2,000 IU of vitamin D a day did not meaningfully reduce invasive cancer or major cardiovascular events compared with placebo."),
  ("What vitamin D level counts as deficient?", "Below 20 ng/mL is a commonly used cut-off for deficiency, though guidelines differ."),
  ("Can vitamin D be toxic?", "Yes, at very high doses over time. It raises blood calcium and can damage the kidneys. Follow your doctor's dose."),
 ],
 sources=[
  ("Siddiqee MH et al. High prevalence of vitamin D deficiency among the South Asian adults: a systematic review and meta-analysis. BMC Public Health, 2021.", PM + "34627207/"),
  ("Manson JE et al. Vitamin D supplements and prevention of cancer and cardiovascular disease (VITAL). New England Journal of Medicine, 2019.", PM + "30415629/"),
  ("Demay MB et al. Vitamin D for the prevention of disease: an Endocrine Society clinical practice guideline. Journal of Clinical Endocrinology & Metabolism, 2024.", "https://doi.org/10.1210/clinem/dgae290"),
 ],
 related=["7-day-sleep-reset"],
),
]
