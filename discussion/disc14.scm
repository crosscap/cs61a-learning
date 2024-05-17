; 7.1
(define (deep-map fn lst)
  (cond ((eq? lst nil) nil)
        ((list? (car lst)) (cons (deep-map fn (car lst)) (deep-map fn (cdr lst))))
        (else (cons (fn (car lst)) (deep-map fn (cdr lst))))))

; (deep-map (lambda (x) (* x x)) '(1 2 3))
; (1 4 9)
; (deep-map (lambda (x) (* x x)) '(1 ((4) 5) 9))
; (1 ((16) 25) 81)
