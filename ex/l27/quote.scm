(define a 1)
(define b 2)

(list a b)
(list 'a 'b)
(list 'a b)
(list (quote a) (quote b))
'(list a b)

(list 'quotient 10 2)
(eval (list 'quotient 10 2)) 
