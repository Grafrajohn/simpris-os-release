CREATE
VIEW `vw_select_problem_detail_sidebar` AS
    SELECT
        'Created:' AS `description`,
        DATE_FORMAT(`prob`.`createdDate`, '%d %b %Y') AS `column2`,
        prob.createdBy AS `id`,
        0 AS `column4`,
        `prob`.`problemID` AS `problemID`,
        usr.first_name,
        usr.last_name
    FROM
        `problem` `prob` join auth_user usr on prob.createdBy = usr.id
    UNION SELECT
        'Changed:' AS `description`,
        DATE_FORMAT(`probar`.`updatedDate`, '%d %b %Y') AS `column2`,
        probar.updatedBy AS `id`,
        3 AS `column4`,
        `probar`.`problemID` AS `problemID`,
        usr.first_name,
        usr.last_name
    FROM
        `problem_archive` `probar` join auth_user usr on probar.updatedBy = usr.id
	where updatedDate is not null
    ORDER BY `column4`