SELECT * FROM produto p WHERE p.categoria_id = 1;
SELECT * FROM produto p WHERE p.categoria_id = 2;
SELECT * FROM produto p WHERE p.categoria_id = 3;
SELECT * FROM produto p WHERE p.categoria_id = 4;

SELECT *
  FROM produto p
 WHERE p.categoria_id IN (1, 2, 3, 4);


