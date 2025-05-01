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
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: steph
--

COPY public.users (id, email, password, oauth_id, created_at) FROM stdin;
1	test@test.com	password123	\N	2025-04-28 11:02:29.993013
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

