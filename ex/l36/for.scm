(define (map fn vals)
  (if (null? vals)
      ()
      (cons (fn (car vals)) (map fn (cdr vals)))))

(map (lambda (x) (* x x)) '(2 3 4 5))

(define-macro (for sym vals expr)
  (list 'map (list 'lambda (list sym) expr) vals))

(for x '(2 3 4 5) (* x x))
