(cond ((> x 10) (print 'big))
      ((> x 5)  (print 'medium))
      (else     (print 'small)))
(print
  (cond ((> x 10) 'big)
  ((> x 5)  'medium)
  (else     'small)))
(cond ((> x 10) (begin (print 'big)   (print 'guy)))
      (else     (begin (print 'small) (print 'fry))))
(if (> x 10) (begin
                (print 'big)
	              (print 'guy))
             (begin
                (print 'small)
                (print 'fry)))
(define c (let ((a 3)
  	            (b (+ 2 2)))
            (sqrt (+ (* a a) (* b b)))))
