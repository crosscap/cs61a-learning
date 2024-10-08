(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement

;; zip a series of pairs to tow list
;; Return the list of tow list
;; (zip '((1 2) (3 4) (5 6)))
;; ((1 3 5) (2 4 6))
;; Notice: Each pair should just have tow element (PAIR!)
;; otherwise the following element will be packed together
;; (zip '((1 2 3) (3 4) (5 6 7)))
;; ((1 3 5) (2 3 4 6 7))
(define (zip pairs)
  (define (helper pairs first second)
    (if (eq? pairs nil)
        (list first second)
        (helper (cdr pairs)
                (append first (list (caar pairs)))
                (append second (cdar pairs)))))
  (helper pairs nil nil))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (helper s index)
    (if (eq? s nil)
        nil
        (cons (cons index (cons (car s) nil))
              (helper (cdr s) (+ index 1)))))
  (helper s 0)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to COMP and return
;; the merged lists.
(define (merge comp list1 list2)
  ; BEGIN PROBLEM 16
  (cond ((eq? list1 nil) list2)
        ((eq? list2 nil) list1)
        (else (if (comp (car list1) (car list2))
                  (cons (car list1) (merge comp (cdr list1) list2))
                  (cons (car list2) (merge comp (cdr list2) list1)))))
  )
  ; END PROBLEM 16


(merge < '(1 5 7 9) '(4 8 10))
; expect (1 4 5 7 8 9 10)
(merge > '(9 7 5 1) '(10 8 4 3))
; expect (10 9 8 7 5 4 3 1)

;; Problem 17

(define (nondecreaselist s)
    ; BEGIN PROBLEM 17
    (define (helper s res lst last)
      (cond ((eq? s nil) (append res (list lst)))
            ((>= (car s) last) (helper (cdr s)
                                       res
                                       (append lst (list (car s)))
                                       (car s)))
            (else (helper (cdr s)
                          (append res (list lst))
                          (cons (car s) nil)
                          (car s)))))
    (helper s nil nil -1)
    )
    ; END PROBLEM 17

;; Problem EC
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((quoted? expr)
         ; BEGIN PROBLEM EC
         expr
         ; END PROBLEM EC
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM EC
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM EC
           (let ((forms (car (zip values)))
                 (vals (cadr (zip values))))
             (cons (cons 'lambda (cons forms (map let-to-lambda body)))
                   (map let-to-lambda vals)))
           ; END PROBLEM EC
           ))
        (else
         ; BEGIN PROBLEM EC
         (map let-to-lambda expr)
         ; END PROBLEM EC
         )))
