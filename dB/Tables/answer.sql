create table answer
(
	answerID int not null auto_increment
		primary key,
	questionID int not null,
	answer varchar(5000) not null,
	createdDate datetime null,
	createdBy int null,
	updatedDate datetime null,
	updatedBy int null,
	deletedDate datetime null,
	deletedBy int null
)
;