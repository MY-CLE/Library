
CREATE OR REPLACE FUNCTION public.login(giv_username text, giv_password text)
 RETURNS integer
 LANGUAGE plpgsql
AS $function$


DECLARE
	v_username VARCHAR(30);
BEGIN
	SELECT email
	INTO v_username
	FROM public.credentials  
	WHERE password = giv_password;

	IF v_username = giv_username THEN
		return userID from public.credentials where v_username = giv_username;
	ELSE
		RETURN 0;
	END IF;
END;
$function$
;

