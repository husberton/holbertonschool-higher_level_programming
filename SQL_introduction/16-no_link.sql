-- select non-empty scores from second_table
SELECT score, name FROM second_table WHERE score is NOT NULL ORDER BY score DESC;