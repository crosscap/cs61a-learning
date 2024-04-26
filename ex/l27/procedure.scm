(define (square x) (* x x))
(define (average x y) (/ (+ x y) 2))
(define (sqrt x)
  (define (update guess)
    (if (= (square guess) x)
      guess
      (update (average guess (/ x guess)))))
  (update 1))
