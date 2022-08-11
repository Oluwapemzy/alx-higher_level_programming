-- Lists all shows in the database hbtn_0d_tvshows without a genre linked.
-- Records are ordered by ascending tv_shows.title and tv_show_genres.genre_id.
SELECT x.`title`, y.`genre_id`
  FROM `tv_shows` AS x
       LEFT JOIN `tv_show_genres` AS y
       ON x.`id` = y.`show_id`
       WHERE y.`genre_id` IS NULL
 ORDER BY x.`title`, y.`genre_id`;
