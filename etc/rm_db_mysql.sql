-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: May 16, 2020 at 10:57 AM
-- Server version: 5.6.47-cll-lve
-- PHP Version: 7.2.7

SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

--
-- Database: `ReliabilityMeasures_DB`
--

-- --------------------------------------------------------

--
-- Table structure for table `items`
--

CREATE TABLE `items` (
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
  `answer` text,
  `user_id` varchar(256) DEFAULT NULL,
  `user_profile` text,
  `private` tinyint(1) DEFAULT '0',
  `approved` tinyint(1) DEFAULT '1',
  `timestamp_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `timestamp_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

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
  `topic_id` mediumtext,
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
  `name` varchar(100) NOT NULL,
  `desciption` varchar(500) DEFAULT NULL,
  `metadata` mediumtext COMMENT 'in json',
  `type` tinyint(4) DEFAULT NULL,
  `no_of_questions` tinyint(4) NOT NULL DEFAULT '1',
  `total_marks` decimal(10,0) DEFAULT '100',
  `questions` mediumtext COMMENT 'in json',
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `responses` smallint(6) NOT NULL DEFAULT '0',
  `external_link` varchar(500) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `quiz_questions`
--

CREATE TABLE `quiz_questions` (
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
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(8) NOT NULL,
  `provider_id` varchar(256) DEFAULT NULL,
  `name` varchar(100) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `creation_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `update_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `address` varchar(200) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT 'TX',
  `zip` varchar(20) DEFAULT NULL,
  `contact_person` varchar(50) DEFAULT NULL,
  `contact_person2` varchar(50) DEFAULT NULL,
  `phone` varchar(25) DEFAULT NULL,
  `phone2` varchar(25) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `age` int(3) DEFAULT NULL,
  `status` tinyint(2) NOT NULL DEFAULT '1',
  `school` varchar(50) DEFAULT NULL,
  `responses` text,
  `marks` varchar(15) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8 COMMENT='Student Info';

--
-- Indexes for dumped tables
--

--
-- Indexes for table `items`
--
ALTER TABLE `items`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `quiz_questions`
--
ALTER TABLE `quiz_questions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `text` (`text`(333)),
  ADD KEY `subject` (`subject`,`topic`),
  ADD KEY `type` (`type`);

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
-- AUTO_INCREMENT for table `items`
--
ALTER TABLE `items`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `questions`
--
ALTER TABLE `questions`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `quiz_questions`
--
ALTER TABLE `quiz_questions`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(8) NOT NULL AUTO_INCREMENT;
COMMIT;
