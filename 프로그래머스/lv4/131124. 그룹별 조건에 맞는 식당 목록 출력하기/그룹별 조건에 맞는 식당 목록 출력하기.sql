SELECT P.MEMBER_NAME, R.REVIEW_TEXT, DATE_FORMAT(R.REVIEW_DATE, '%Y-%m-%d') as "REVIEW_DATE"
FROM MEMBER_PROFILE P
RIGHT JOIN REST_REVIEW R ON P.MEMBER_ID = R.MEMBER_ID
WHERE P.MEMBER_ID = (SELECT RR.MEMBER_ID
    FROM REST_REVIEW RR
    GROUP BY RR.MEMBER_ID
    ORDER BY COUNT(*) DESC
    LIMIT 1)
ORDER BY R.REVIEW_DATE, R.REVIEW_TEXT

-- 최다 리뷰 작성자 겹치는 경우 ...? 조건은 왜 없지..?