-- temtsture
SELECT state, max(value) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY max_temp DESC;
