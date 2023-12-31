SELECT INFO.HISTORY_ID, ROUND((INFO.DAILY_FEE * ((100-IFNULL(PP.DISCOUNT_RATE, 0))/100) * INFO.DAYS),0) AS "FEE"
FROM (
    SELECT H.HISTORY_ID, START_DATE, END_DATE ,DATEDIFF(H.END_DATE, H.START_DATE)+1 as "DAYS",
    CASE WHEN DATEDIFF(H.END_DATE, H.START_DATE) BETWEEN 7 AND 29 THEN '7일 이상'
    WHEN DATEDIFF(H.END_DATE, H.START_DATE) BETWEEN 30 AND 89 THEN '30일 이상'
    WHEN DATEDIFF(H.END_DATE, H.START_DATE) >= 90 THEN '90일 이상'
    ELSE '미대상' END AS "DURATION"
    , C.DAILY_FEE
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
JOIN CAR_RENTAL_COMPANY_CAR C ON C.CAR_ID = H.CAR_ID
WHERE C.CAR_TYPE = '트럭'
) INFO
LEFT JOIN (
    SELECT P.DURATION_TYPE, P.DISCOUNT_RATE
    FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    WHERE P.CAR_TYPE = '트럭'
) PP ON PP.DURATION_TYPE = INFO.DURATION
ORDER BY FEE DESC, INFO.HISTORY_ID DESC

-- 검증
# SELECT *
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# WHERE START_DATE=END_DATE

    # SELECT P.DURATION_TYPE, P.DISCOUNT_RATE
    # FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN P
    # WHERE P.CAR_TYPE = '트럭'

-- 724	6182400	40	2022-10-31 00:00:00	2022-12-10 00:00:00	168000
# SELECT *, DATEDIFF(H.END_DATE, H.START_DATE)
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY H
# JOIN CAR_RENTAL_COMPANY_CAR C ON C.CAR_ID = H.CAR_ID
# WHERE C.CAR_TYPE = '트럭' AND H.HISTORY_ID = 724
-- 724	20	2022-10-31 00:00:00	2022-12-10 00:00:00	20	트럭	168000	주차감지센서,통풍시트	40 624960


