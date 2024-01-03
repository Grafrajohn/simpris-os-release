create table account
(
	accountID int not null auto_increment
		primary key,
	accountName varchar(100) not null,
	authenticationID varchar(45) null,
	authenticationID2 varchar(45) null,
	authenticationID3 varchar(45) null,
	membershipTypeID int not null,
	membershipRenewalDate datetime null,
	firstname varchar(50) null,
	lastname varchar(50) null,
	phone varchar(50) null,
	email varchar(75) null,
	createdDate datetime not null,
	createdBy int not null,
	updateDate datetime null,
	updatedBy int null,
	deletedDate datetime null,
	deletedBy int null,
	constraint ix_account
		unique (accountName, email)
)
comment 'Account is what is registered as the paying account. There is a one to one relationship between account and client.'
;