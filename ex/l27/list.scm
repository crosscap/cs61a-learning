(define s (cons 1 (cons 2 nil)))
(cons 3 s)
(cons (cons 4 (cons 3 nil)) s)
(cons s (cons s nil))

(list? s)
(null? s)
(list 1 2 3 4)
