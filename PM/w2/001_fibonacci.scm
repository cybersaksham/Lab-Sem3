;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 001_fibonacci) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (fibonacci atm)
  (cond
    ((< atm 1) '()) ; Fibonacci not defined for atm < 1 so return null
    ((= 1 atm) (cons 1 '())) ; Fibonacci of 1 is '(1)
    ((= 2 atm) (cons 1 (cons 1 '()))) ; Fibonacci of 2 is '(1 1)
    (else (append
           (fibonacci (- atm 1)) ; Find fibonacci of atm - 1
           (cons (+
                  (last_elem (fibonacci (- atm 1))) ; Last element of fibonacci atm - 1
                  (last_elem (fibonacci (- atm 2))) ; Last element of fibonacci atm - 2
                  ) ; Getting current fibonacci by adding them
                 '()
                 )
           ) ; Append current fibonacci in series of atm - 1
          )
    )
  )

(define (last_elem ls) ; Helper function to calculate last element
  (cond
    ((null? ls) #F) ; If list is null return null
    ((null? (cdr ls)) (car ls)) ; If list has only one element return that
    (else (last_elem (cdr ls))) ; ELse return last element of list excluding first element
    )
  )
