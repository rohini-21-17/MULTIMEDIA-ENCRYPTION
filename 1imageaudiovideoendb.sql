-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 04, 2025 at 04:37 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `1imageaudiovideoendb`
--

-- --------------------------------------------------------

--
-- Table structure for table `msgtb`
--

CREATE TABLE `msgtb` (
  `id` bigint(10) NOT NULL auto_increment,
  `SenderName` varchar(250) NOT NULL,
  `ReceiverName` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `FileName` varchar(250) NOT NULL,
  `PriKey` varchar(250) NOT NULL,
  `Type` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `msgtb`
--

INSERT INTO `msgtb` (`id`, `SenderName`, `ReceiverName`, `Email`, `FileName`, `PriKey`, `Type`) VALUES
(1, 'san', 'san', 'sangeeth5535@gmail.com', '2204a019a3d775d9247ac1af8644631ccea.jpg', '03b48b0964527d00d9788d61ca0fe1a5b03283f12ac6761192d9bb8dfa1b09c349', 'image'),
(2, 'san', 'san', 'sangeeth5535@gmail.com', '5401.jpg', '02999e9e43385d72d17ea7b7ed244059cf2d479d10a3ddf7c4178e7c402963cf7f', 'image');

-- --------------------------------------------------------


--
-- Table structure for table `recivertb`
--

CREATE TABLE `recivertb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `EmailId` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `recivertb`
--

INSERT INTO `recivertb` (`id`, `Name`, `Mobile`, `EmailId`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');

-- --------------------------------------------------------

--
-- Table structure for table `sendertb`
--

CREATE TABLE `sendertb` (
  `id` bigint(10) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `EmailId` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=2 ;

--
-- Dumping data for table `sendertb`
--

INSERT INTO `sendertb` (`id`, `Name`, `Mobile`, `EmailId`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san');
