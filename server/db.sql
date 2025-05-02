--
-- PostgreSQL database dump
--

-- Dumped from database version 14.17 (Homebrew)
-- Dumped by pg_dump version 14.17 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: articles; Type: TABLE; Schema: public; Owner: steph
--

CREATE TABLE public.articles (
    id integer NOT NULL,
    title character varying(255) NOT NULL,
    category text NOT NULL,
    link character varying(255) NOT NULL,
    author character varying(255) NOT NULL
);


ALTER TABLE public.articles OWNER TO steph;

--
-- Name: articles_id_seq; Type: SEQUENCE; Schema: public; Owner: steph
--

CREATE SEQUENCE public.articles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.articles_id_seq OWNER TO steph;

--
-- Name: articles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: steph
--

ALTER SEQUENCE public.articles_id_seq OWNED BY public.articles.id;


--
-- Name: emojis; Type: TABLE; Schema: public; Owner: steph
--

CREATE TABLE public.emojis (
    id integer NOT NULL,
    emoji character varying(255) NOT NULL,
    label text NOT NULL
);


ALTER TABLE public.emojis OWNER TO steph;

--
-- Name: emojis_id_seq; Type: SEQUENCE; Schema: public; Owner: steph
--

CREATE SEQUENCE public.emojis_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.emojis_id_seq OWNER TO steph;

--
-- Name: emojis_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: steph
--

ALTER SEQUENCE public.emojis_id_seq OWNED BY public.emojis.id;


--
-- Name: mood_logs; Type: TABLE; Schema: public; Owner: steph
--

CREATE TABLE public.mood_logs (
    id integer NOT NULL,
    user_id integer,
    emoji_id integer NOT NULL,
    journal_entry text,
    sentiment_score double precision,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.mood_logs OWNER TO steph;

--
-- Name: mood_logs_id_seq; Type: SEQUENCE; Schema: public; Owner: steph
--

CREATE SEQUENCE public.mood_logs_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.mood_logs_id_seq OWNER TO steph;

--
-- Name: mood_logs_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: steph
--

ALTER SEQUENCE public.mood_logs_id_seq OWNED BY public.mood_logs.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: steph
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    oauth_id character varying(255) DEFAULT NULL::character varying,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP
);


ALTER TABLE public.users OWNER TO steph;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: steph
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO steph;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: steph
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: articles id; Type: DEFAULT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.articles ALTER COLUMN id SET DEFAULT nextval('public.articles_id_seq'::regclass);


--
-- Name: emojis id; Type: DEFAULT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.emojis ALTER COLUMN id SET DEFAULT nextval('public.emojis_id_seq'::regclass);


--
-- Name: mood_logs id; Type: DEFAULT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.mood_logs ALTER COLUMN id SET DEFAULT nextval('public.mood_logs_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: articles; Type: TABLE DATA; Schema: public; Owner: steph
--

COPY public.articles (id, title, category, link, author) FROM stdin;
1	Want to Boost Your Confidence? Give These 9 Tips a Try	Want to Boost Your Confidence? Give These 9 Tips a Try	https://www.verywellmind.com/how-to-boost-your-self-confidence-4163098	Reviewed by Rachel Goldman, PhD, FTOS
2	18 Highly Effective Stress Relievers	18 Highly Effective Stress Relievers	https://www.verywellmind.com/tips-to-reduce-stress-3145195	Medically reviewed by Rachel Goldman, PhD, FTOS
3	The Best Way to Boost Your Motivation When You Just Aren't Feeling It	The Best Way to Boost Your Motivation When You Just Aren't Feeling It	https://www.verywellmind.com/what-to-do-when-you-have-no-motivation-4796954	Reviewed by David Susman, PhD
4	7 Ways to Find More Meaning and Purpose in Your Life	7 Ways to Find More Meaning and Purpose in Your Life	https://www.verywellmind.com/tips-for-finding-your-purpose-in-life-4164689	Reviewed by Carly Snyder, MD
5	Best Meditation Apps of 2024	Best Meditation Apps of 2024	https://www.verywellmind.com/best-meditation-apps-4767322	Medically reviewed by Rachel Goldman, PhD, FTOS
6	We've Been Testing Online Therapy For Years—These Services Are Worth Using	We've Been Testing Online Therapy For Years—These Services Are Worth Using	https://www.verywellmind.com/best-online-therapy-4691206	Medically reviewed by Steven Gans, MD
7	We've Been Testing Online Therapy For Years—These Services Are Worth Using	We've Been Testing Online Therapy For Years—These Services Are Worth Using	https://www.verywellmind.com/best-online-therapy-4691206	Medically reviewed by Steven Gans, MD
8	5 Healthy Ways to Live a Longer, Happier Life, According to Blue Zone Communities	5 Healthy Ways to Live a Longer, Happier Life, According to Blue Zone Communities	https://www.verywellmind.com/blue-zone-secrets-11714202	Reviewed by Rachel Goldman, PhD, FTOS
9	8 Common Conversation Mistakes You Don't Know You're Making	8 Common Conversation Mistakes You Don't Know You're Making	https://www.verywellmind.com/common-conversation-mistakes-11699413	By Ariane Resnick, CNC
10	How I Found Meaning Outside of Caregiving My Loved One With Alzheimer's	How I Found Meaning Outside of Caregiving My Loved One With Alzheimer's	https://www.verywellmind.com/how-i-found-meaning-outside-of-caregiving-8789818	By Wendy Wisner
11	TikTok's 'October Theory' Can *Finally* Help You Get Your Life Together—Here's How	TikTok's 'October Theory' Can *Finally* Help You Get Your Life Together—Here's How	https://www.verywellmind.com/october-theory-8732152	By Hannah Owens, LMSW
12	Feeling Stuck in a Rut? Take This Quiz to Find Out If It’s a Midlife Crisis	Feeling Stuck in a Rut? Take This Quiz to Find Out If It’s a Midlife Crisis	https://www.verywellmind.com/midlife-crisis-quiz-8609543	Reviewed by Rachel Goldman, PhD, FTOS
13	How TikTok's 'Burnt Toast Theory' Can Help Us Navigate the Lows of Life	How TikTok's 'Burnt Toast Theory' Can Help Us Navigate the Lows of Life	https://www.verywellmind.com/how-tiktok-s-burnt-toast-theory-can-help-life-8594568	By Theodora Blanchfield, AMFT
14	How to Mentally Prepare for Fatherhood, According to a Parenting Coach	How to Mentally Prepare for Fatherhood, According to a Parenting Coach	https://www.verywellmind.com/how-to-mentally-prepare-for-fatherhood-according-to-a-parenting-coach-7565867	By Sanjana Gupta
15	6 De-Escalation Techniques to Diffuse Conflict	6 De-Escalation Techniques to Diffuse Conflict	https://www.verywellmind.com/deescalation-techniques-to-diffuse-conflict-7498049	By Amy Marschall, PsyD
16	Compassion vs. Empathy: What's the Difference?	Compassion vs. Empathy: What's the Difference?	https://www.verywellmind.com/compassion-vs-empathy-what-s-the-difference-7494906	Reviewed by Rachel Goldman, PhD, FTOS
17	The Importance of Mindful Communication for Mental Health	The Importance of Mindful Communication for Mental Health	https://www.verywellmind.com/mindful-communication-definition-principles-benefits-how-to-do-it-7489103	By Tiara Blain, MA
18	How to Deal With a Condescending Partner	How to Deal With a Condescending Partner	https://www.verywellmind.com/how-do-you-deal-with-a-partner-who-is-condescending-7484593	By LaKeisha Fleming
19	What to Know About Atelophobia (Fear of Imperfection)	What to Know About Atelophobia (Fear of Imperfection)	https://www.verywellmind.com/atelophobia-fear-of-imperfection-symptoms-causes-treatment-coping-7377192	Medically reviewed by Daniel B. Block, MD
20	What Is the Pomodoro Technique?	What Is the Pomodoro Technique?	https://www.verywellmind.com/pomodoro-technique-history-steps-benefits-and-drawbacks-6892111	Reviewed by Daniel B. Block, MD
21	'I Need Attention:' What This Means and How to Stop Needing It	'I Need Attention:' What This Means and How to Stop Needing It	https://www.verywellmind.com/how-to-stop-attention-seeking-6823772	By Toketemu Ohwovoriole
22	How to Set Boundaries With Your Partner	How to Set Boundaries With Your Partner	https://www.verywellmind.com/how-to-set-boundaries-with-your-partner-6834034	By Sanjana Gupta
23	Option Paralysis in Online Dating	Option Paralysis in Online Dating	https://www.verywellmind.com/option-paralysis-in-online-dating-6829732	By Arlin Cuncic, MA
24	Does Stress Affect Blood Sugar?	Does Stress Affect Blood Sugar?	https://www.verywellmind.com/does-stress-effect-blood-sugar-6827694	Medically reviewed by Shaheen Lakhan, MD, PhD, FAAN
25	6 Ways to Become a Nicer Person	6 Ways to Become a Nicer Person	https://www.verywellmind.com/6-ways-to-become-a-nicer-person-5194074	Reviewed by Steven Gans, MD
26	Body Positivity vs. Body Neutrality	Body Positivity vs. Body Neutrality	https://www.verywellmind.com/body-positivity-vs-body-neutrality-5184565	Reviewed by Carly Snyder, MD
27	Why Alone Time Could Be Key to Improving Your Mental Health	Why Alone Time Could Be Key to Improving Your Mental Health	https://www.verywellmind.com/how-important-is-alone-time-for-mental-health-5184607	Medically reviewed by Steven Gans, MD
28	How Gratitude Makes You Happier	How Gratitude Makes You Happier	https://www.verywellmind.com/how-gratitude-makes-you-happier-5114446	Reviewed by Rachel Goldman, PhD, FTOS
29	Why It's Important to Have High Self-Esteem	Why It's Important to Have High Self-Esteem	https://www.verywellmind.com/why-it-s-important-to-have-high-self-esteem-5094127	Reviewed by Rachel Goldman, PhD, FTOS
30	How Storytelling Is Good for Your Mental Health	How Storytelling Is Good for Your Mental Health	https://www.verywellmind.com/how-storytelling-is-good-for-your-mental-health-5199744	Reviewed by Daniel B. Block, MD
31	Why Can’t I Make Friends?	Why Can’t I Make Friends?	https://www.verywellmind.com/why-can-t-i-make-friends-5199203	Medically reviewed by Rachel Goldman, PhD, FTOS
32	How To Deal With the Fact That People Are Trying To Scam You Every Day	How To Deal With the Fact That People Are Trying To Scam You Every Day	https://www.verywellmind.com/how-to-cope-when-people-are-trying-to-scam-you-11710898	By John Loeppky
33	I Replaced My Afternoon Coffee With Yerba Mate for a Month—Here’s What Changed	I Replaced My Afternoon Coffee With Yerba Mate for a Month—Here’s What Changed	https://www.verywellmind.com/i-tried-yerba-mate-every-day-for-a-month-11718006	Reviewed by Rachel Goldman, PhD, FTOS
34	7 Reasons to Try Maca Powder for Enhanced Mood and Energy	7 Reasons to Try Maca Powder for Enhanced Mood and Energy	https://www.verywellmind.com/can-maca-powder-boost-mood-and-energy-11716658	Reviewed by Alicia Bigelow, ND
35	Short on Time and Motivation? Try 'Task Snacking' Your To-Do List	Short on Time and Motivation? Try 'Task Snacking' Your To-Do List	https://www.verywellmind.com/task-snacking-11713065	By Sanjana Gupta
36	33 Reddit-Approved Tips for Self-Improvement and Better Mental Health	33 Reddit-Approved Tips for Self-Improvement and Better Mental Health	https://www.verywellmind.com/33-reddit-tips-for-better-mental-health-11708495	By Team Verywell Mind
37	I Drank Apple Cider Vinegar Every Day for a Week—Here's How I Felt	I Drank Apple Cider Vinegar Every Day for a Week—Here's How I Felt	https://www.verywellmind.com/i-tried-apple-cider-vinegar-for-energy-11708849	Medically reviewed by Alicia Bigelow, ND
38	How the 5-Second Rule Can Help You Break Free From Procrastination	How the 5-Second Rule Can Help You Break Free From Procrastination	https://www.verywellmind.com/5-second-rule-for-procrastination-11706675	By Adam England
39	You Are Enough Just as You Are—but It's OK To Seek Self-Improvement Too	You Are Enough Just as You Are—but It's OK To Seek Self-Improvement Too	https://www.verywellmind.com/you-are-enough-self-improvement-finding-balance-7093355	Fact checked by Zerah Isaacs
40	This Therapist-Approved Motivation Hack Will Help You Get Your Goals Back on Track	This Therapist-Approved Motivation Hack Will Help You Get Your Goals Back on Track	https://www.verywellmind.com/what-is-the-punch-card-trend-11703375	Fact checked by Andria Park Huynh
41	I Switched From Coffee to Matcha and Here's How It Affected My Energy	I Switched From Coffee to Matcha and Here's How It Affected My Energy	https://www.verywellmind.com/what-are-the-benefits-of-drinking-matcha-for-energy-11698395	By Kate Nelson
42	I Drank Lemon Water Every Morning for a Week —Here's What It Did for My Energy	I Drank Lemon Water Every Morning for a Week —Here's What It Did for My Energy	https://www.verywellmind.com/i-drank-lemon-water-for-a-week-11690668	Reviewed by Rachel Goldman, PhD, FTOS
43	I Tried Turmeric Lattes to Boost My Energy—Here's What Happened	I Tried Turmeric Lattes to Boost My Energy—Here's What Happened	https://www.verywellmind.com/can-turmeric-lattes-boost-your-energy-11695285	Medically reviewed by Alicia Bigelow, ND
44	I Tried Lion's Mane for a Month—Here’s What It Did for My Mental Health	I Tried Lion's Mane for a Month—Here’s What It Did for My Mental Health	https://www.verywellmind.com/i-tried-lions-mane-11694264	Medically reviewed by Alicia Bigelow, ND
45	7 Ways You Can Use ChatGPT for Your Mental Health and Wellness	7 Ways You Can Use ChatGPT for Your Mental Health and Wellness	https://www.verywellmind.com/using-chatgpt-for-mental-health-and-wellness-11695183	Medically reviewed by Daniel B. Block, MD
46	7 Ways to Get Through Your Midday Slump	7 Ways to Get Through Your Midday Slump	https://www.verywellmind.com/ways-to-get-through-a-midday-slump-11692553	By Cathy Cassata
47	7 Ways Your Makeup Routine Is Actually Helpful for Depression	7 Ways Your Makeup Routine Is Actually Helpful for Depression	https://www.verywellmind.com/makeup-routine-for-depression-11692002	Fact checked by Andria Park Huynh
48	7 Body Language Mistakes You Don't Know You're Making	7 Body Language Mistakes You Don't Know You're Making	https://www.verywellmind.com/7-body-language-mistakes-you-may-be-making-11690066	By Wendy Rose Gould
49	5 Surprising Ways TikTok's "Floor Time" Enhances Mental Health	5 Surprising Ways TikTok's "Floor Time" Enhances Mental Health	https://www.verywellmind.com/how-tiktok-s-floor-time-trend-can-benefit-your-mental-health-11683674	Reviewed by Rachel Goldman, PhD, FTOS
50	I Cut Out Sugar for a Month—Here’s What It Did for My Mental Health	I Cut Out Sugar for a Month—Here’s What It Did for My Mental Health	https://www.verywellmind.com/does-sugar-affect-mental-health-11683665	Medically reviewed by Rachel Goldman, PhD, FTOS
51	I Tried Junk Journaling For a Month—Here’s What Happened	I Tried Junk Journaling For a Month—Here’s What Happened	https://www.verywellmind.com/i-tried-junk-journaling-for-a-month-11679873	By Noma Nazish
52	I Swapped My Morning Coffee for Black Tea—Here’s How My Energy Shifted	I Swapped My Morning Coffee for Black Tea—Here’s How My Energy Shifted	https://www.verywellmind.com/can-black-tea-boost-your-energy-benefits-and-risks-11678690	Medically reviewed by Rachel Goldman, PhD, FTOS
53	How the Serenity Prayer Can Support Your Mental Health Journey	How the Serenity Prayer Can Support Your Mental Health Journey	https://www.verywellmind.com/serenity-prayer-and-mental-health-8781123	By Brina Patel
54	How to Cancel Plans Last Minute, According to Etiquette Experts	How to Cancel Plans Last Minute, According to Etiquette Experts	https://www.verywellmind.com/how-to-cancel-plans-last-minute-8789202	By Sanjana Gupta
55	I've Been a Victim of Fraud Twice—Here's What It Feels Like	I've Been a Victim of Fraud Twice—Here's What It Feels Like	https://www.verywellmind.com/what-it-feels-like-to-be-a-victim-of-fraud-8776106	By Nick Ingalls, MA
56	Are Mushroom Supplements the Key to Boosting Your Brain Health?	Are Mushroom Supplements the Key to Boosting Your Brain Health?	https://www.verywellmind.com/mushroom-supplements-for-brain-health-8784675	Medically reviewed by Steven Gans, MD
57	7 Effective Ways to Handle The Fear of Being Left Out	7 Effective Ways to Handle The Fear of Being Left Out	https://www.verywellmind.com/how-to-cope-with-the-fear-of-being-left-out-8769855	By Brina Patel
58	How the Eisenhower Matrix Can Be Your Secret to a Stress-Free Life	How the Eisenhower Matrix Can Be Your Secret to a Stress-Free Life	https://www.verywellmind.com/eisenhower-matrix-benefits-and-application-8779812	By Sanjana Gupta
59	How to Succeed at Work as an Introvert	How to Succeed at Work as an Introvert	https://www.verywellmind.com/how-to-thrive-at-work-as-an-introvert-8772247	By LaKeisha Fleming
60	6 Common Eye Contact Mistakes You Might Be Making	6 Common Eye Contact Mistakes You Might Be Making	https://www.verywellmind.com/eye-contact-mistakes-8770892	By Wendy Rose Gould
61	I'm a Therapist and I Didn't Set Goals This Year—Here's Why	I'm a Therapist and I Didn't Set Goals This Year—Here's Why	https://www.verywellmind.com/why-i-didnt-set-goals-this-year-8773029	By Julia Childs Heyl, MSW
62	Here's How to Optimize Your Daily Walk and Get Those Mental Health Benefits	Here's How to Optimize Your Daily Walk and Get Those Mental Health Benefits	https://www.verywellmind.com/optimize-your-daily-walk-for-mental-health-benefits-8771394	Medically reviewed by Steven Gans, MD
63	Unlock the Power of the 2-Minute Rule to Conquer Procrastination and Get It Done	Unlock the Power of the 2-Minute Rule to Conquer Procrastination and Get It Done	https://www.verywellmind.com/use-the-2-minute-rule-to-beat-procrastination-8720928	By John Loeppky
64	Dinner Parties Are In for 2025, And They’re Essential to Easing Our Crisis of Connection	Dinner Parties Are In for 2025, And They’re Essential to Easing Our Crisis of Connection	https://www.verywellmind.com/dinner-parties-are-in-for-2025-8764579	By Team Verywell Mind
65	Is the TikTok-Viral 75 Hard Challenge Right for You? Experts Explain	Is the TikTok-Viral 75 Hard Challenge Right for You? Experts Explain	https://www.verywellmind.com/75-hard-challenge-8750715	By Noma Nazish
66	Your (Mostly) Stress-Free Guide to Hosting an Unforgettable Dinner Party	Your (Mostly) Stress-Free Guide to Hosting an Unforgettable Dinner Party	https://www.verywellmind.com/your-stress-free-dinner-party-guide-8759244	By Kate Nelson
67	6 Types of Hobbies You Can Pick Up and Maintain as an Adult	6 Types of Hobbies You Can Pick Up and Maintain as an Adult	https://www.verywellmind.com/fun-hobbies-for-adults-8743814	By Brina Patel
68	25 Questions to Help You Discover Your True Passions	25 Questions to Help You Discover Your True Passions	https://www.verywellmind.com/25-questions-to-discover-your-passions-8754230	By Ariane Resnick, CNC
69	How to Be Kind Without Compromising Your Boundaries	How to Be Kind Without Compromising Your Boundaries	https://www.verywellmind.com/how-to-be-kind-without-being-a-pushover-8744349	By Julia Childs Heyl, MSW
70	I’m a People Pleaser Who Tried Saying "No" to Everything for a Week—Here’s What Happened	I’m a People Pleaser Who Tried Saying "No" to Everything for a Week—Here’s What Happened	https://www.verywellmind.com/i-tried-saying-no-to-everything-8752484	By Sian Ferguson
\.


--
-- Data for Name: emojis; Type: TABLE DATA; Schema: public; Owner: steph
--

COPY public.emojis (id, emoji, label) FROM stdin;
1	😀	happy
2	😐	neutral
3	☹️	unhappy
\.


--
-- Data for Name: mood_logs; Type: TABLE DATA; Schema: public; Owner: steph
--

COPY public.mood_logs (id, user_id, emoji_id, journal_entry, sentiment_score, created_at) FROM stdin;
1	1	1	today was a good day! i had a lot of fun building this app!	0.8	2025-04-28 11:02:29.993013
\.

--
-- Name: articles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: steph
--

SELECT pg_catalog.setval('public.articles_id_seq', 70, true);


--
-- Name: emojis_id_seq; Type: SEQUENCE SET; Schema: public; Owner: steph
--

SELECT pg_catalog.setval('public.emojis_id_seq', 3, true);


--
-- Name: mood_logs_id_seq; Type: SEQUENCE SET; Schema: public; Owner: steph
--

SELECT pg_catalog.setval('public.mood_logs_id_seq', 1, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: steph
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: articles articles_pkey; Type: CONSTRAINT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.articles
    ADD CONSTRAINT articles_pkey PRIMARY KEY (id);


--
-- Name: emojis emojis_pkey; Type: CONSTRAINT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.emojis
    ADD CONSTRAINT emojis_pkey PRIMARY KEY (id);


--
-- Name: mood_logs mood_logs_pkey; Type: CONSTRAINT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.mood_logs
    ADD CONSTRAINT mood_logs_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: mood_logs mood_logs_emoji_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.mood_logs
    ADD CONSTRAINT mood_logs_emoji_id_fkey FOREIGN KEY (emoji_id) REFERENCES public.emojis(id);


--
-- Name: mood_logs mood_logs_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: steph
--

ALTER TABLE ONLY public.mood_logs
    ADD CONSTRAINT mood_logs_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

