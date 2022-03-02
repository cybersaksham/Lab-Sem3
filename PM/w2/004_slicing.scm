;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 004_slicing) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (sliceList ls i j)
  (cond
    ((null? ls) '()) ; If list is null return null
    ((< i 1) '()) ; If i < 1 return null
    ((> j (length ls)) '()) ; If j > length of list return null
    ((< j i) '()) ; If j < i return null
    ((= j 1) (cons (car ls) '())) ; If lst index is 1 return first element
    ((= i 1) (cons (car ls) (sliceList (cdr ls) i (- j 1)))) ; If first index is 1 add first element in remaining slicing with i & j - 1
    (else (sliceList (cdr ls) (- i 1) (- j 1))) ; Else slice on remaining list with  i - 1 & j - 1
    )
  )
