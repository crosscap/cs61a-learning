; (define (map procedure s)
;   (if (null? s)
;       nil
;       (cons (procedure (car s))
;             (map procedure (cdr s)))))

(define (map procedure s)
  (define (map-reverse s m)
    (if (null? s)
        m
        (map-reverse (cdr s) (cons (procedure (car s)) m))))
  (reverse (map-reverse s nil)))

(define (reverse s)
  (define (reverse-iter s r)
    (if (null? s)
        r
        (reverse-iter (cdr s) (cons (car s) r))))
  (reverse-iter s nil))

(map (lambda (x) (- 5 x)) (list 1 2))
