SELECT count(distinct_college) AS distinct_college_number FROM
(SELECT DISTINCT college FROM player_bios) AS distinct_college;