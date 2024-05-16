(define (split-at lst n)
  (define (helper new old n)
    (cond ((eq? old nil) (cons new nil))
          ((= n 0) (cons new old))
          (else (helper (append new (car old)) (cdr old) (- n 1)))))
  (helper nil lst n)
)


(define (compose-all funcs)
  (lambda (x)
    (if (eq? funcs nil)
        x
        ((compose-all (cdr funcs)) ((car funcs) x))))
)

(define (append lst item)
      (if (eq? lst nil)
          (cons item nil)
          (cons (car lst) (append (cdr lst) item))))