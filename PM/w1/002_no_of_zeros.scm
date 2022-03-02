;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 002_no_of_zeros) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (zeros ls) (zerosHelp ls 0))

(define (zerosHelp ls count)
  (cond
    ((null? ls) count) ; List is null so no zero
    ((zero? (car ls)) (zerosHelp (cdr ls) (+ count 1))) ; First element is zero so increase count
    (else (zerosHelp (cdr ls) count))) ; Else call on remaining list
  )
