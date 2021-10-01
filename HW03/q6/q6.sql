ALTER TABLE player_bios
ADD COLUMN height_inch numeric;


UPDATE player_bios
set height_inch = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

ALTER TABLE player_bios
DROP COLUMN height;

ALTER TABLE player_bios
RENAME COLUMN height_inch TO height;


SELECT firstname, lastname, height FROM player_bios limit 5;