select picpoints.*, scores.score, scores.email
FROM picpoints
INNER JOIN scores ON (picpoints.imgname = scores.imagename and scores.email = 'tommyT@gm.com')
ORDER BY scores.id desc
LIMIT 50
