CREATE DATABASE IF NOT EXISTS `hotel_management` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hotel_management`;
CREATE TABLE IF NOT EXISTS `register` (
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `contact` varchar(45) DEFAULT NULL,
  `email` varchar(45) NOT NULL,
  `securityQ` varchar(45) DEFAULT NULL,
  `securityA` varchar(45) NOT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE IF NOT EXISTS `customer` (
  `Ref` int NOT NULL,
  `Name` varchar(45) NOT NULL,
  `Father` varchar(45) NOT NULL,
  `Gender` varchar(45) NOT NULL,
  `PostCode` varchar(45) NOT NULL,
  `Mobile` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Nationality` varchar(45) NOT NULL,
  `IDProof` varchar(45) NOT NULL,
  `IDNumber` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  PRIMARY KEY (`Ref`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE IF NOT EXISTS `room` (
  `contact` varchar(45) NOT NULL,
  `checkin` varchar(45) NOT NULL,
  `checkout` varchar(45) NOT NULL,
  `roomtype` varchar(45) NOT NULL,
  `roomavailable` varchar(45) NOT NULL,
  `meal` varchar(45) NOT NULL,
  `noOfdays` varchar(45) NOT NULL,
  PRIMARY KEY (`roomavailable`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE IF NOT EXISTS `details` (
  `floor` int NOT NULL,
  `RoomNo` varchar(45) NOT NULL,
  `RoomType` varchar(45) NOT NULL,
  PRIMARY KEY (`RoomNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


