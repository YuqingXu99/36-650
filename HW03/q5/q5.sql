ALTER TABLE player_bios
ADD COLUMN position text;



UPDATE player_bios
SET position = (SELECT position 
				FROM new_table 
				WHERE new_table.player = player_bios.id);



SELECT firstname, lastname, position FROM player_bios limit 5;