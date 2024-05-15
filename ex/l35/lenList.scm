(define (length s)
  (if (null? s) 0
      (+ 1 (length (cdr s)))))

(define (length-tail s)
  (define (length-iter s n)
    (if (null? s) n
        (length-iter (cdr s) (+ 1 n))))
  (length-iter s 0))
