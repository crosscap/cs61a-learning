(define (reduce procedure s start)
  (if (null? s) start
    (reduce procedure
            (cdr s)
            (procedure start (car s)))))

(reduce * '(3 4 5) 2)
(reduce (lambda (x y) (cons y x)) '(3 4 5) '(2))
