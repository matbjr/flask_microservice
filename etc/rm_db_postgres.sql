CREATE DATABASE "RM_DB"
    WITH
    OWNER = cloudsqlsuperuser
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF8'
    LC_CTYPE = 'en_US.UTF8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;


--
-- Table structure for table items
--

-- Table: public.items

-- DROP TABLE public.items;

CREATE TABLE public.items
(
    id serial NOT NULL,
    user_id character varying(256),
    text character varying(512) COLLATE pg_catalog."default" NOT NULL,
    subject character varying(50) COLLATE pg_catalog."default" NOT NULL,
    subject_id smallint,
    topic character varying(50) COLLATE pg_catalog."default" DEFAULT NULL::character varying,
    topic_id smallint,
    sub_topics character varying(250) COLLATE pg_catalog."default" DEFAULT NULL::character varying,
    sub_topics_id text COLLATE pg_catalog."default",
    type smallint,
    metadata json,
    choices json COLLATE pg_catalog."default",
    answer json COLLATE pg_catalog."default",
    private boolean,
    approved boolean,
    timestamp_created timestamp,
    timestamp_updated timestamp
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.items
    OWNER to "rm-2020";

-- --------------------------------------------------------

--
-- Table structure for table quizzes
--

CREATE TABLE public.quizzes (
  id integer NOT NULL,
  provider_id varchar(256) DEFAULT NULL,
  name varchar(100) NOT NULL,
  desciption varchar(500) DEFAULT NULL,
  metadata json,
  type smallint DEFAULT NULL,
  no_of_items smallint NOT NULL DEFAULT 1,
  total_marks decimal(10,0) DEFAULT 100,
  questions json,
  timestamp timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  responses smallint NOT NULL DEFAULT 0,
  external_link varchar(500) DEFAULT NULL
) WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.quizzes
    OWNER to "rm-2020";

-- --------------------------------------------------------

--
-- Table structure for table students
--

CREATE TABLE public.students (
  id int(8) NOT NULL,
  provider_id varchar(256) DEFAULT NULL,
  name varchar(100) NOT NULL,
  description varchar(500) DEFAULT NULL,
  creation_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  update_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  address varchar(200) DEFAULT NULL,
  city varchar(50) DEFAULT NULL,
  state varchar(50) DEFAULT 'TX',
  zip varchar(20) DEFAULT NULL,
  contact_person varchar(50) DEFAULT NULL,
  contact_person2 varchar(50) DEFAULT NULL,
  phone varchar(25) DEFAULT NULL,
  phone2 varchar(25) DEFAULT NULL,
  email varchar(100) DEFAULT NULL,
  age int(3) DEFAULT NULL,
  status tinyint(2) NOT NULL DEFAULT '1',
  school varchar(50) DEFAULT NULL,
  responses json,
  marks varchar(15) DEFAULT NULL
) WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;

ALTER TABLE public.students
    OWNER to "rm-2020";

COMMIT;
