/* By Aleksey */

CREATE PROCEDURE projectsTeam()
BEGIN
	/* Write your SQL here. Terminate each statement with a semicolon. */
    SELECT DISTINCT name FROM projectLog ORDER BY name ASC;
END
