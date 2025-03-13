create database chessClubDB;

use chessClubDB;

create table schools(
	school_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
	school_name varchar(60) not null unique,
	number_of_students int not null
);

INSERT INTO schools (school_name, number_of_students) VALUES 
('Von Neumann Polytechnic School', 1200),
('Ayn Rand Psychology School', 850),
('Edmund Hillary Mountaineering School', 500),
('Alan Turing Computer Science Institute', 1500),
('Nikola Tesla Engineering Academy', 1800),
('Marie Curie Research Institute', 1400),
('Carl Sagan Astronomical School', 950),
('Ada Lovelace Coding Academy', 1300),
('Richard Feynman Physics School', 1100),
('Leonardo da Vinci Art & Science School', 1700);

select * from schools;

CREATE TABLE members (
    member_id INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(20),
    surname VARCHAR(20),
    school_id INT UNSIGNED NOT NULL,  -- Chave estrangeira para associar à escola
    FOREIGN KEY (school_id) REFERENCES schools(school_id) ON DELETE CASCADE
);

INSERT INTO members (name, surname, school_id) VALUES 
('Howard', 'Roark', 1), 
('Dagny', 'Taggart', 1), 
('John', 'Galt', 1),
('Francisco', 'd’Anconia', 2),
('Hank', 'Rearden', 2),
('Ayn', 'Rand', 2),
('Phileas', 'Fogg', 3),
('Jonathan', 'Harker', 3),
('Edmund', 'Hillary', 3),
('Sherlock', 'Holmes', 4),
('Arthur', 'Conan Doyle', 4),
('Alan', 'Turing', 4),
('Victor', 'Frankenstein', 5),
('Nikola', 'Tesla', 5),
('Prometheus', 'Unbound', 5),
('Marie', 'Curie', 6),
('Ludwig', 'von Mises', 6),
('Frédéric', 'Bastiat', 6),
('Carl', 'Sagan', 7),
('Isaac', 'Asimov', 7),
('Arthur', 'C. Clarke', 7),
('Ada', 'Lovelace', 8),
('Margaret', 'Hamilton', 8),
('Alan', 'Kay', 8),
('Richard', 'Feynman', 9),
('Murray', 'Rothbard', 9),
('Thomas', 'Sowell', 9),
('Leonardo', 'da Vinci', 10),
('Johann', 'Goethe', 10),
('Oscar', 'Wilde', 10);

select m.member_id, m.name, m.surname, s.school_name from members as m join schools as s 
on m.school_id = s.school_id
order by m.member_id;