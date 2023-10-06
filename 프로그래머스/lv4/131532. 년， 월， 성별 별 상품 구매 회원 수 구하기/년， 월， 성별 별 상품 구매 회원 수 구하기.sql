SELECT YEAR(S.SALES_DATE) AS YEAR, MONTH(S.SALES_DATE) AS MONTH, U.GENDER, COUNT(distinct  U.USER_ID) AS USERS
FROM ONLINE_SALE S
LEFT JOIN USER_INFO U ON U.USER_ID = S.USER_ID
WHERE U.GENDER IS NOT NULL
GROUP BY YEAR, MONTH,  U.GENDER
ORDER BY YEAR, MONTH, GENDER


-- 검증
# select *
# FROM ONLINE_SALE S
# LEFT JOIN USER_INFO U ON U.USER_ID = S.USER_ID
# WHERE U.GENDER IS NOT NULL
# order by s.sales_date, u.user_id, u.gender