-- phpMyAdmin SQL Dump
-- version 5.0.4deb2+deb11u1
-- https://www.phpmyadmin.net/
--
-- Хост: localhost:3306
-- Время создания: Окт 21 2024 г., 11:49
-- Версия сервера: 10.5.21-MariaDB-0+deb11u1
-- Версия PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `kholikov22092`
--

-- --------------------------------------------------------

--
-- Структура таблицы `kholikov22092`
--

CREATE TABLE `kholikov22092` (
  `surname` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `password` varchar(40) NOT NULL,
  `email` varchar(255) NOT NULL,
  `regdate` int(10) UNSIGNED DEFAULT NULL,
  `photo` varchar(255) DEFAULT NULL,
  `position` tinyint(1) UNSIGNED DEFAULT NULL,
  `about` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
