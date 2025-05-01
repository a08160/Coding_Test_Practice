-- 문제1. 강원도에 위치한 생산공장 목록 출력하기
/*
LIKE: 와일드카드 문자 사용하여 패턴 검색
%: 0개 이상의 문자와 일치치
*/
SELECT FACTORY_ID, FACTORY_NAME, ADDRESS FROM FOOD_FACTORY WHERE ADDRESS LIKE '강원도%'