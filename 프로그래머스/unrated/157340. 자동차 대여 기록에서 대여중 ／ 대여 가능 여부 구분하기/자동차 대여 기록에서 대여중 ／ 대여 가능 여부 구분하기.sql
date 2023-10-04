# SELECT distinct CAR_ID, CASE WHEN (DATE_FORMAT(START_DATE,'%Y-%m-%d') < '2022-10-16' AND DATE_FORMAT(END_DATE,'%Y-%m-%d')  <'2022-10-16') OR (DATE_FORMAT(START_DATE,'%Y-%m-%d') >'2022-10-17') THEN "대여 가능" ELSE  "대여중" END as "AVAILABILITY", start_date, end_date
# FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where '2022-10-16'  between (DATE_FORMAT(START_DATE,'%Y-%m-%d')) and (DATE_FORMAT(END_DATE,'%Y-%m-%d'))
# ORDER BY CAR_ID DESC

SELECT car.CAR_ID, case when sum(car.AVA) > 0 then "대여중" else "대여 가능" end as "AVAILABILITY"
FROM (SELECT CAR_ID, CASE WHEN '2022-10-16'  between (DATE_FORMAT(START_DATE,'%Y-%m-%d')) and (DATE_FORMAT(END_DATE,'%Y-%m-%d')) then "1" else "0" end as "AVA"
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) car
GROUP BY car.CAR_ID
ORDER BY car.CAR_ID DESC


