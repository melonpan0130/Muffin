CREATE TABLE `muffin`.`users` (
  `userid` VARCHAR(255) NOT NULL,
  `pw` VARCHAR(255) NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`userid`),
  UNIQUE INDEX `userid_UNIQUE` (`userid` ASC) VISIBLE);


insert into users values('melonpan', '1234', 'melon');
insert into users values('m', '1234', 'mm');

select * from users;