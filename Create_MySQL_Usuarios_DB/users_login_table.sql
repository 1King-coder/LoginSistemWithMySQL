-- Run this archieve in your DB manager

CREATE TABLE `users`.`users_login` (
	`id` INT UNSIGNED auto_increment NOT NULL,
	`username` varchar(150) NOT NULL,
	`password_hash` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	CONSTRAINT users_login_PK PRIMARY KEY (id),
	CONSTRAINT users_login_UN_email UNIQUE KEY (email),
	CONSTRAINT users_login_UN_username UNIQUE KEY (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE = utf8mb4_unicode_ci;


