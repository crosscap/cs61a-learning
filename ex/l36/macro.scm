(print 2)
(begin (print 2) (print 2))
(define (twice expr) (list 'begin expr expr))
(twice (print 2))
(twice '(print 2))
(eval (twice '(print 2)))

(define-macro (twice expr) (list 'begin expr expr))

(define x -2)
(define (check val) (if val 'Passed 'Failed))
(check (> x 0))
(define-macro (check expr) (list 'if expr ''Passed ''Failed))
(check (> x 0))
(define-macro (check expr) (list 'if expr ''Passed (list 'quote (list 'Failed:  expr))))
