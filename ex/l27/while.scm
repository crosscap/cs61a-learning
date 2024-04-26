(begin
  (define (f x total)
    (if (< x 10) 
      (f (+ x 2) (+ total (* x x)))
      total))
  (f 2 0))

(define (sum-while initial-x condition       add-to-total update-x)
  ;	(sum-while 1	     '(< (* x x) 50) 'x           '(+ x 1))
  `(begin
    (define (f x total)
      (if ,condition
	(f ,update-x (+ total ,add-to-total))
	total))
    (f ,initial-x 0)))
(define  result (sum-while 1 '(< (* x x) 50) 'x '(+ x 1)))
(eval result)
(eval (sum-while 2 '(< x 10) '(* x x) '(+ x 2)))
