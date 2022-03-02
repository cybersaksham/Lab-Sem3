;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 009_sum_of_elems) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (sumofelems ls)
  (if
   (null? ls) 0 ; If list is null return 0
   (+ (car ls) (sumofelems (cdr ls))) ; Else return first element + sum of remaining list
   )
  )
