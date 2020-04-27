
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

--
-- Database: `ReliabilityMeasures_DB`
--

-- --------------------------------------------------------

--
-- Table structure for table `questions`
--

CREATE TABLE `questions` (
  `id` int(10) NOT NULL,
  `text` varchar(500) NOT NULL,
  `subject` varchar(50) NOT NULL,
  `subject_id` tinyint(4) DEFAULT NULL,
  `topic` varchar(50) DEFAULT NULL,
  `topic_id` tinyint(5) DEFAULT NULL,
  `sub_topics` varchar(250) DEFAULT NULL,
  `sub_topics_id` mediumtext,
  `type` tinyint(3) DEFAULT NULL,
  `metadata` mediumtext COMMENT 'in json',
  `choices` text,
  `answer` text
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `quizzes`
--

CREATE TABLE `quizzes` (
  `id` int(11) NOT NULL,
  `provider_id` varchar(256) DEFAULT NULL,
  `tilte` varchar(100) NOT NULL,
  `desciption` varchar(500) DEFAULT NULL,
  `metadata` mediumtext COMMENT 'in json',
  `type` tinyint(4) DEFAULT NULL,
  `no_of_questions` tinyint(4) NOT NULL DEFAULT '1',
  `total_marks` decimal(10,0) DEFAULT '100',
  `questions` mediumtext COMMENT 'in json'
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(8) NOT NULL,
  `family_id` int(8) NOT NULL DEFAULT '1',
  `name` varchar(100) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `creation_date` datetime NOT NULL,
  `update_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `address` varchar(200) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT 'TX',
  `zip` varchar(20) DEFAULT NULL,
  `contact_person` varchar(50) DEFAULT NULL,
  `contact_person2` varchar(50) DEFAULT NULL,
  `phone` varchar(25) DEFAULT NULL,
  `phone2` varchar(25) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `teacher` varchar(200) DEFAULT NULL,
  `status` tinyint(2) NOT NULL DEFAULT '1',
  `school` tinyint(2) NOT NULL DEFAULT '1'
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='Student Info';

--
-- Indexes for dumped tables
--

--
-- Indexes for table `questions`
--
ALTER TABLE `questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `text` (`text`(333)),
  ADD KEY `subject` (`subject`,`topic`),
  ADD KEY `type` (`type`);

--
-- Indexes for table `quizzes`
--
ALTER TABLE `quizzes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT;
