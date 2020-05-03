
-- Generation Time: April 23, 2020 at 07:47 PM


SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";



--
-- Database: `test`
--

-- --------------------------------------------------------

--
-- Table structure for table `librarian`
--

CREATE TABLE IF NOT EXISTS `librarian` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL,
  `city` varchar(100) NOT NULL,
  `contact` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=7 ;

--
-- Dumy data for table `librarian`
--

INSERT INTO `librarian` (`id`, `name`, `password`, `email`, `address`, `city`, `contact`) VALUES
(1, 'Angel', '123456', 'vladimirpet91@gmail.com', 'Boris27', 'Stara Zagora', '0894345591'),
(4, 'Atanas', '123456', 'vladimirpet91@gmail.com', 'Boris27', 'Stara Zagora', '0894345591'),
(6, 'Alexander', '123456', 'vladimirpet91@gmail.com', 'Boris27', 'Stara Zagora', '0894345591');


