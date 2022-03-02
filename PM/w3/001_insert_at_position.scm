;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 001_insert_at_position) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (insert_at a ls i) ; insert element a in list ls at index i starting from 0
  (cond
    ((< i 0) (insert_at a ls (+ (+ 1 (length ls)) i))) ; i is negative then insert at index length + 1 + i
    ((= i 0) (cons a ls)) ; i = 0 then insert at front
    ((null? ls) ls) ; If list is null then return null
    (else (cons (car ls) (insert_at a (cdr ls) (- i 1)))) ; Else insert in list excluding first element with i = i - 1 and add first element to it
    )
  )
