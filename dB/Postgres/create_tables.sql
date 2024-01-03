create table simpris.account
(
	accountID int generated always as identity,
	accountName varchar(100) not null,
	authenticationID varchar(45) null,
	authenticationID2 varchar(45) null,
	authenticationID3 varchar(45) null,
	membershipTypeID int not null,
	membershipRenewalDate timestamp null,
	firstname varchar(50) null,
	lastname varchar(50) null,
	phone varchar(50) null,
	email varchar(75) null,
	createdDate timestamp not null,
	createdBy int not null,
	updateDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (accountID),
	constraint ix_account
		unique (accountName, email)
)

;

create table simpris.answer
(
	answerID int generated always as identity,
	questionID int not null,
	answer varchar(5000) not null,
	createdDate timestamp null,
	createdBy int null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (answerID)
)
;

create table simpris.auth_group
(
	id int generated always as identity,
	name varchar(80) not null,
	
		primary key (id),
	constraint name
		unique (name)
)
;

create table simpris.auth_user
(
	id int generated always as identity,
	password varchar(128) not null,
	last_login timestamp null,
	is_superuser smallint not null,
	username varchar(30) not null,
	first_name varchar(30) not null,
	last_name varchar(30) not null,
	email varchar(75) not null,
	is_staff smallint not null,
	is_active smallint not null,
	date_joined timestamp not null,
	
		primary key (id),
	constraint username
		unique (username)
)
;

create table simpris.auth_user_groups
(
	id int generated always as identity,
	user_id int not null,
	group_id int not null,
	
		primary key (id),
	constraint user_id
		unique (user_id, group_id),
	constraint auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id
		foreign key (group_id) references auth_group (id),
	constraint auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id
		foreign key (user_id) references auth_user (id)
)
;

create index auth_user_groups_0e939a4f
	on auth_user_groups (group_id)
;

create index auth_user_groups_e8701ad4
	on auth_user_groups (user_id)
;

create table simpris.board
(
	id int generated always as identity,
	userID int not null,
	itemID int not null,
	itemType int not null,
	columnNo int not null,
	itemOrder int not null,
	
		primary key (id)
)

;

create table simpris.client
(
	clientID int generated always as identity,
	accountID int not null,
	userID mediumint(11) not null,
	clientName varchar(100) not null,
	address1 varchar(45) not null,
	address2 varchar(45) not null,
	address3 varchar(45) not null,
	city varchar(45) not null,
	region varchar(45) not null,
	country varchar(50) not null,
	postcode varchar(45) not null,
	createdDate timestamp not null,
	createdBy int not null,
	updateDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (clientID),
	constraint FK_client_account
		foreign key (accountID) references account (accountID)
)

;

create index ix_client
	on client (clientName)
;

create table simpris.comment
(
	commentID int generated always as identity,
	parentID int not null,
	parentTypeID int not null,
	commentTypeID int not null,
	commentText varchar(5000) not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (commentID)
)
;

create table simpris.country
(
	countryID int not null,
	countryName varchar(100) not null,
	
		primary key (countryID),
	constraint ix_country
		unique (countryName)
)
;

create table simpris.django_content_type
(
	id int generated always as identity,
	app_label varchar(100) not null,
	model varchar(100) not null,
	
		primary key (id),
	constraint django_content_type_app_label_45f3b1d93ec8c61c_uniq
		unique (app_label, model)
)
;

create table simpris.auth_permission
(
	id int generated always as identity,
	name varchar(50) not null,
	content_type_id int not null,
	codename varchar(100) not null,
	
		primary key (id),
	constraint content_type_id
		unique (content_type_id, codename),
	constraint auth__content_type_id_508cf46651277a81_fk_django_content_type_id
		foreign key (content_type_id) references django_content_type (id)
)
;

create table simpris.auth_group_permissions
(
	id int generated always as identity,
	group_id int not null,
	permission_id int not null,
	
		primary key (id),
	constraint group_id
		unique (group_id, permission_id),
	constraint auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id
		foreign key (permission_id) references auth_permission (id),
	constraint auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id
		foreign key (group_id) references auth_group (id)
)
;

create index auth_group_permissions_0e939a4f
	on auth_group_permissions (group_id)
;

create index auth_group_permissions_8373b171
	on auth_group_permissions (permission_id)
;

create index auth_permission_417f1b1c
	on auth_permission (content_type_id)
;

create table simpris.auth_user_user_permissions
(
	id int generated always as identity,
	user_id int not null,
	permission_id int not null,
	
		primary key (id),
	constraint user_id
		unique (user_id, permission_id),
	constraint auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id
		foreign key (permission_id) references auth_permission (id),
	constraint auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id
		foreign key (user_id) references auth_user (id)
)
;

create index auth_user_user_permissions_8373b171
	on auth_user_user_permissions (permission_id)
;

create index auth_user_user_permissions_e8701ad4
	on auth_user_user_permissions (user_id)
;

create table simpris.django_admin_log
(
	id int generated always as identity,
	action_time timestamp not null,
	object_id longtext null,
	object_repr varchar(200) not null,
	action_flag smallint  not null,
	change_message longtext not null,
	content_type_id int null,
	user_id int not null,
	
		primary key (id),
	constraint djang_content_type_id_58fcbaa5a9e45863_fk_django_content_type_id
		foreign key (content_type_id) references django_content_type (id),
	constraint django_admin_log_user_id_2cbcf755a38a186b_fk_auth_user_id
		foreign key (user_id) references auth_user (id)
)
;

create index django_admin_log_417f1b1c
	on django_admin_log (content_type_id)
;

create index django_admin_log_e8701ad4
	on django_admin_log (user_id)
;

create table simpris.django_migrations
(
	id int generated always as identity,
	app varchar(255) not null,
	name varchar(255) not null,
	applied timestamp not null,
	
		primary key (id)
)
;

create table simpris.django_session
(
	session_key varchar(40) not null,
	session_data longtext not null,
	expire_date timestamp not null,
	
		primary key (session_key)
)
;

create index django_session_de54fa62
	on django_session (expire_date)
;

create table simpris.django_site
(
	id int generated always as identity,
	domain varchar(100) not null,
	name varchar(50) not null,
	
		primary key (id),
	constraint django_site_domain_a2e37b91_uniq
		unique (domain)
)
;

create table simpris.document
(
	documentID int generated always as identity,
	documentTypeID int default '0' not null,
	documentParentID int default '0' not null,
	documentName varchar(100) not null,
	documentFileName varchar(100) not null,
	documentTitle varchar(100) null,
	createdDate timestamp not null,
	createdBy int not null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (documentID)
)
;

create table simpris.groups
(
	id mediumint  generated always as identity,
	name varchar(20) not null,
	description varchar(100) not null,
	
		primary key (id)
)
;

create table simpris.invoice
(
	invoiceID int generated always as identity,
	clientID int not null,
	userID mediumint(10) not null,
	statusID int default '1' not null ,
	supersededBy int null ,
	description varchar(50) not null ,
	comments varchar(500) not null ,
	createdDate timestamp not null,
	createdBy mediumint(8) not null,
	deletedDate timestamp null,
	deletedBy mediumint(8) null,
	invoicecol varchar(45) null,
	
		primary key (invoiceID)
)
;

create index ix_invoice_client
	on invoice (clientID)
;

create table simpris.invoiceline
(
	invoiceID int not null,
	lineNo int not null,
	taskID int not null,
	timeID int not null,
	itemDescription varchar(150) not null,
	tax1Rate decimal(10,2)  not null,
	tax2Rate decimal(10,2)  not null,
	tax3Rate decimal(10,2)  not null,
	hourlyRate decimal(10,2)  not null,
	noHours decimal(10,1)  not null,
	agreedRate decimal(10,1)  not null ,
	tax1 decimal(10,2)  not null,
	tax2 decimal(10,2)  not null,
	tax3 decimal(10,2)  not null,
	grossTotal decimal(10,2)  not null,
	netTotal decimal(10,2)  not null,
	
		primary key (invoiceID, lineNo)
)
;

create table simpris.login_attempts
(
	id mediumint  generated always as identity,
	ip_address varbinary(16) not null,
	login varchar(100) not null,
	time int  null,
	
		primary key (id)
)
;

create table simpris.lookup
(
	clientID int default '0' not null,
	lookupTypeID int not null,
	lookupSubTypeID int not null,
	lookupOrder int not null,
	lookupValueNum int null,
	lookupValueChar varchar(50) null,
	lookupDescription varchar(200) not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (clientID, lookupTypeID, lookupSubTypeID)
)
;

create index ix_lookup_subtypeid
	on lookup (lookupSubTypeID)
;

create index ix_lookup_typeid
	on lookup (lookupTypeID)
;

create table simpris.meta
(
	id mediumint  generated always as identity,
	user_id mediumint  null,
	first_name varchar(50) null,
	last_name varchar(50) null,
	mainOrganisationID int null ,
	phone varchar(20) null,
	
		primary key (id)
)
;

create table simpris.opinion
(
	opinionID int generated always as identity,
	userID int not null,
	itemType int not null ,
	itemID int not null,
	opinionType int null,
	opinion varchar(250) null,
	createdDate timestamp null,
	createdBy int null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (opinionID),
	constraint ix_opinion
		unique (userID, itemType, itemID)
)

;

create table simpris.organisation
(
	organisationID int generated always as identity,
	clientID int not null,
	organisationName varchar(100) not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (organisationID),
	constraint FK_organisation_client
		foreign key (clientID) references client (clientID)
)
;

create index fk_org_project
	on organisation (organisationID)
;

create index ix_organisation
	on organisation (organisationName, clientID)
;

create table simpris.organisation_archive
(
	organisationID int not null,
	clientID int not null,
	organisationName varchar(100) not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null
)
;

create table simpris.payrate
(
	payrateID int generated always as identity,
	payrateDescription varchar(20) not null,
	rate decimal(10,2) not null,
	rateper int not null,
	taskType int null,
	effectiveDate timestamp not null,
	createdDate timestamp default CURRENT_TIMESTAMP not null,
	createdBy int not null,
	updateDate timestamp null,
	updateBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (payrateID)
)
;

create table simpris.phase
(
	phaseID int generated always as identity,
	clientID int not null,
	phaseName varchar(50) not null,
	phaseDescription varchar(500) null,
	startDate timestamp null,
	endDate timestamp null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (phaseID)
)

;

create table simpris.problem
(
	problemID int generated always as identity,
	clientID int not null,
	organisationID int not null,
	problemTypeID int not null,
	problemSubTypeID int null,
	problemHeader varchar(50) not null,
	problemDescription varchar(2000) not null,
	noOfPeopleAffected int not null,
	scope int not null,
	problemStatusID int null,
	problemPriorityID int null,
	assignedTo int null,
	completedDate timestamp null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (problemID),
	constraint ix_problem
		unique (organisationID, problemHeader),
	constraint FK_problem_organisation
		foreign key (organisationID) references organisation (organisationID)
)
;

create index ix_problem_client
	on problem (clientID)
;

create index ix_problem_type
	on problem (problemTypeID)
;

create table simpris.problem_archive
(
	problemID int not null,
	clientID int not null,
	organisationID int not null,
	problemTypeID int not null,
	problemSubTypeID int null,
	problemHeader varchar(50) not null,
	problemDescription varchar(2000) not null,
	noOfPeopleAffected int not null,
	scope int not null,
	problemStatusID int null,
	problemPriorityID int null,
	assignedTo int null,
	completedDate timestamp null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null
)
;

create table simpris.problemlink
(
	id int generated always as identity,
	problemID int not null,
	problemLinkID int not null,
	problemLinkType int not null,
	createdDate timestamp not null,
	createdBy int not null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (id),
	constraint ix_tasklink_unique
		unique (problemID, problemLinkID)
)

;

create table simpris.programme
(
	programmeID int generated always as identity,
	clientID int default '0' not null,
	programmeName varchar(50) not null,
	programmeDescription varchar(500) null,
	manager int null,
	createdBy int not null,
	createdDate timestamp not null,
	updatedBy int null,
	updatedDate timestamp null,
	deletedBy int null,
	deletedDate timestamp null,
	
		primary key (programmeID),
	constraint ix_program
		unique (clientID, programmeName)
)

;

create table simpris.project
(
	projectID int generated always as identity,
	organisationID int not null,
	programmeID int null,
	clientID int not null,
	projectName varchar(50) not null,
	projectDescription varchar(500) null,
	stakeholderID int null,
	projectManagerID int null,
	deliverables varchar(1500) null,
	budget decimal null,
	importance int null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (projectID),
	constraint FK_project_organisation
		foreign key (organisationID) references organisation (organisationID)
)

;

create index ix_project_client
	on project (clientID)
;

create table simpris.project_archive
(
	projectID int not null,
	organisationID int not null,
	programmeID int null,
	clientID int not null,
	projectName varchar(50) not null,
	projectDescription varchar(500) null,
	stakeholderID int null,
	projectManagerID int null,
	deliverables varchar(1500) null,
	budget decimal null,
	importance int null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null
)
;

create table simpris.question
(
	questionID int generated always as identity,
	questionName varchar(45) null,
	questionText varchar(5000) null,
	createdDate timestamp null,
	createdBy int null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedBy int null,
	deletedDate timestamp null,
	
		primary key (questionID)
)
;

create table simpris.questionnaire
(
	questionnaireID int generated always as identity,
	questionnaireName varchar(45) not null,
	contactUserID int not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (questionnaireID)
)

;

create table simpris.questionnaire_question
(
	questionnaireID int not null,
	questionID int not null,
	createdDate timestamp null,
	createdBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (questionnaireID, questionID)
)
;

create table simpris.queue
(
	queueID int generated always as identity,
	queueName varchar(45) not null,
	queueDescription varchar(450) null,
	createdBy int not null,
	createdDate timestamp not null,
	updatedBy int null,
	updatedDate timestamp null,
	deletedBy int null,
	deletedDate timestamp null,
	
		primary key (queueID)
)

;

create table simpris.queue_user
(
	id int generated always as identity,
	queueID int not null,
	queueUserID int null,
	queueTeamID int null,
	createdBy int null,
	createdDate timestamp null,
	updatedBy int null,
	updatedDate timestamp null,
	deletedBy int null,
	deletedDate timestamp null,
	
		primary key (id),
	constraint queueID
		foreign key (queueID) references queue (queueID)
)

;

create index queueID_idx
	on queue_user (queueID)
;

create table simpris.status
(
	statusID int not null,
	userID mediumint null,
	itemID int null,
	itemType int null,
	status int null,
	statuscol varchar(45) null,
	
		primary key (statusID),
	constraint ix_status
		unique (userID, itemID, itemType)
)

;

create table simpris.step
(
	stepID int generated always as identity,
	clientID int not null,
	taskID int not null,
	description varchar(100) not null,
	status int default '1' not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (stepID)
)

;

create table simpris.task
(
	taskID int generated always as identity,
	taskListID int not null,
	clientID int not null,
	taskTypeID int not null,
	taskName varchar(50) not null,
	taskDescription varchar(10000) not null,
	taskStatusID int null,
	taskPriorityID int null,
	assignedTo int null,
	taskStartDate timestamp null,
	taskTimeEstimate decimal(10,1) null,
	taskPercentComplete int null,
	completionDate timestamp null,
	phaseID int null,
	taskLinkID int null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (taskID)
)
;

create index fk_task_tasklist
	on task (taskListID)
;

create index fk_tasklist
	on task (taskListID)
;

create index ix_task_client
	on task (clientID)
;

create table simpris.task_archive
(
	taskID int not null,
	taskListID int not null,
	clientID int not null,
	taskTypeID int not null,
	taskName varchar(50) not null,
	taskDescription varchar(500) not null,
	taskStatusID int null,
	taskPriorityID int null,
	assignedTo int null,
	taskStartDate timestamp null,
	taskTimeEstimate decimal(10,1) null,
	taskPercentComplete int null,
	completionDate timestamp null,
	phaseID int null,
	taskLinkID int null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null
)
;

create table simpris.task_template
(
	tasktemplateID int generated always as identity,
	clientID int null,
	tasktemplateName varchar(100) null,
	createdDate timestamp null,
	createdBy int null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (tasktemplateID),
	constraint ix_tasktemplate
		unique (tasktemplateName, clientID)
)

;

create table simpris.tasklist
(
	taskListID int generated always as identity,
	projectID int not null,
	clientID int not null,
	taskListName varchar(50) not null,
	taskListDescription varchar(500) null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (taskListID),
	constraint ix_tasklist
		unique (taskListName, projectID),
	constraint projectID_taskListName
		unique (projectID, taskListName),
	constraint FK_tasklist_project
		foreign key (projectID) references project (projectID)
)
;

create index fk_tasklist_project
	on tasklist (projectID)
;

create index ix_tasklist_client
	on tasklist (clientID)
;

create table simpris.tasklist_archive
(
	taskListID int not null,
	projectID int not null,
	clientID int null,
	taskListName varchar(50) not null,
	taskListDescription varchar(500) null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedID int null,
	deletedDate timestamp null,
	deletedBy int null
)
;

create table simpris.taskstep
(
	taskstepID int generated always as identity,
	taskID int null,
	steporder int null,
	
		primary key (taskstepID),
	constraint ix_taskstep
		unique (taskID, steporder)
)

;

create table simpris.taxrate
(
	taxrateID int generated always as identity,
	clientID int not null,
	taxrateDescription varchar(100) not null,
	taxrate decimal(10,2) not null,
	effectiveDate timestamp default '0000-00-00 00:00:00' not null,
	createdDate timestamp default CURRENT_TIMESTAMP not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	
		primary key (taxrateID)
)

;

create table simpris.team
(
	teamID int generated always as identity,
	clientID int not null,
	teamName varchar(100) not null,
	teamDescription varchar(1000) null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (teamID)
)
;

create table simpris.team_user
(
	id int generated always as identity,
	teamID int not null,
	userID int not null,
	clientID int not null,
	createdBy int not null,
	createdDate timestamp not null,
	updatedBy int null,
	updatedDate timestamp null,
	deletedBy int null,
	deletedDate timestamp null,
	
		primary key (id)
)

;

create table simpris.test_table
(
	testint int not null
)
;

create table simpris.time
(
	timeID int generated always as identity,
	clientID int not null,
	timeDay timestamp not null,
	hours float not null,
	taskID int not null,
	timeTypeID int not null,
	userID mediumint(11) not null,
	comments varchar(50) null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (timeID),
	constraint FK1_time_task
		foreign key (taskID) references task (taskID)
)

;

create index ix_time_client
	on time (clientID)
;

create table simpris.user_attributes
(
	userID int not null,
	vip char default 'n' not null,
	countryID int null,
	mobilePhoneNo varchar(20) null,
	faxNo varchar(20) null,
	photo varchar(100) null,
	
		primary key (userID)
)

;

create table simpris.user_configuration
(
	userID mediumint not null,
	lookupTypeID int  not null,
	configurationData varchar(50) not null,
	configurationDataNum float not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp not null,
	updatedBy int not null,
	deletedDate timestamp not null,
	deletedBy int not null,
	
		primary key (userID, lookupTypeID)
)

;

create table simpris.user_cookie
(
	id int generated always as identity,
	userID bigint not null,
	uuID varchar(128) not null,
	username varchar(100) not null,
	password varchar(40) not null,
	created_on timestamp default CURRENT_TIMESTAMP not null,
	
		primary key (id)
)
;

create table simpris.user_payrate
(
	userID int not null,
	payrateID int not null,
	effectiveDate timestamp not null,
	defaultRate decimal(10,2) null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	
		primary key (userID)
)

;

create table simpris.user_status
(
	statusID int not null,
	userID mediumint null,
	itemID int null,
	itemType int null,
	status int null,
	statuscol varchar(45) null,
	
		primary key (statusID),
	constraint ix_unique
		unique (userID, itemID, itemType)
)

;

create table simpris.user_taxrate
(
	userID int not null,
	taxrateID decimal(10,2) not null,
	effectiveDate timestamp null,
	defaultRate decimal(10,2) null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	
		primary key (userID)
)

;

create table simpris.useractivity
(
	activityID int generated always as identity,
	userID mediumint(11) not null,
	activityTypeID mediumint(11) not null,
	activityData varchar(100) null,
	activity_module_id int null,
	client_id int null,
	activityDate timestamp not null,
	
		primary key (activityID)
)
;

create table simpris.userorganisation
(
	id int generated always as identity,
	userID mediumint(11) not null,
	organisationID int not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (id),
	constraint FK_userorganisation_organisation
		foreign key (organisationID) references organisation (organisationID)
)
;

create index fk_user_org
	on userorganisation (organisationID)
;

create table simpris.userproject
(
	id int generated always as identity,
	userID mediumint(11) not null,
	projectID int not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null,
	
		primary key (id),
	constraint fk_user_project
		foreign key (projectID) references project (projectID)
)
;

create table simpris.userreport
(
	userID int not null,
	reportID int not null,
	createdDate timestamp not null,
	createdBy int not null,
	updatedDate timestamp null,
	updatedBy int null,
	deletedDate timestamp null,
	deletedBy int null
)
;

create table simpris.users
(
	id mediumint  not null,
	clientID int not null,
	ip_address varbinary(16) not null,
	username varchar(100) not null,
	password varchar(40) not null,
	salt varchar(40) null,
	email varchar(100) not null,
	activation_code varchar(40) null,
	forgotten_password_code varchar(40) null,
	forgotten_password_time int  null,
	remember_code varchar(40) null,
	created_on int  not null,
	last_login int  null,
	active smallint  null,
	first_name varchar(50) null,
	last_name varchar(50) null,
	company int  null,
	phone varchar(20) null,
	
		primary key (id),
	constraint email
		unique (email),
	constraint username
		unique (username)
)
;

create table simpris.users_archive
(
	id mediumint  not null,
	clientID int not null,
	ip_address varbinary(16) not null,
	username varchar(100) not null,
	password varchar(40) not null,
	salt varchar(40) null,
	email varchar(100) not null,
	activation_code varchar(40) null,
	forgotten_password_code varchar(40) null,
	forgotten_password_time int  null,
	remember_code varchar(40) null,
	created_on int  not null,
	last_login int  null,
	active smallint  null,
	first_name varchar(50) null,
	last_name varchar(50) null,
	company int  null,
	phone varchar(20) null
)
;

create table simpris.users_groups
(
	id mediumint  generated always as identity,
	user_id mediumint  not null,
	group_id mediumint  not null,
	
		primary key (id)
)
;

create table simpris.usertask
(
	userID mediumint(11) not null,
	taskID int not null,
	
		primary key (userID, taskID),
	constraint FK_usertask_task
		foreign key (taskID) references task (taskID)
)
;
