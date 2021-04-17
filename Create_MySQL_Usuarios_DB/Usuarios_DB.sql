CREATE SCHEMA `usuarios` DEFAULT CHARACTER SET =utf8mb4 COLLATE =utf8mb4_bin;
USE usuarios;

CREATE TABLE `usuarios`.`login_usuarios` (
	`id` INT UNSIGNED auto_increment NOT NULL,
	`username` varchar(150) NOT NULL,
	`password_hash` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	CONSTRAINT login_usuarios_PK PRIMARY KEY (id),
	CONSTRAINT login_usuarios_UN_email UNIQUE KEY (email),
	CONSTRAINT login_usuarios_UN_username UNIQUE KEY (username)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE = utf8mb4_unicode_ci;



