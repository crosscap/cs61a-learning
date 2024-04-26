(define (fact n)
  (if (= n 0) 1 (* n (fact (- n 1)))))
(define (fact-exp n)
  (if (= n 0) 1 (list '* n (fact-exp (- n 1)))))

(define (fib n)
  (if (<= n 1) n (+ (fib (- n 2)) (fib (- n 1)))))

(define (fib-exp n)
  (if (<= n 1) n (list '+ (fib-exp (- n 2)) (fib-exp (- n 1)))))
