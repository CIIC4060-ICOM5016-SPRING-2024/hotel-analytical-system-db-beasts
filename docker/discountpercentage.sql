create function discount_percentage(membership_years integer) returns numeric
    language plpgsql
as
$$
DECLARE
    membership_discount float;
BEGIN
    -- Calculate membership discount based on years
    IF membership_years >= 1 AND membership_years <= 4 THEN
        membership_discount := 0.02; -- 2% discount for 1-4 years
    ELSIF membership_years >= 5 AND membership_years <= 9 THEN
        membership_discount := 0.05; -- 5% discount for 5-9 years
    ELSIF membership_years >= 10 AND membership_years <= 14 THEN
        membership_discount := 0.08; -- 8% discount for 10-14 years
    ELSIF membership_years >= 15 THEN
        membership_discount := 0.12; -- 12% discount for over 15 years
    ELSE
        membership_discount := 0;
    END IF;
    RETURN membership_discount;
END;
$$;
--
-- alter function discount_percentage(integer) owner to mhcrlshjnkrhdy;
--