; 4.1
; Write a function that returns the factorial of a number.
(define (factorial x)
  (if (= x 1)
      1
      (* x (factorial (- x 1)))))

; 4.2
; Write a function that returns the nth Fibonacci number.
(define (fib n)
  (if (or (= n 0) (= n 1))
      n
      (+ (fib (- n 1)) (fib (- n 2))))
)

; 5.1
(define (my-append a b)
  (if (eq? a nil)
      b
      (cons (car a) (my-append (cdr a) b)))
)

; 5.2
(define s '(5 4 (1 2) 3 7))

(define s-three (car (cdr (cdr (cdr s)))))

; 5.3
(define (duplicate lst)
        (if (eq? lst nil)
            nil
            (cons (car lst) (cons (car lst) (duplicate (cdr lst)))))
)

; 5.4
(define (insert element lst index)
        (cond ((eq? lst nil) (cons element nil))
              ((= index 0) (cons element lst))
              (else (cons (car lst) (insert element (cdr lst) (- index 1)))))
)