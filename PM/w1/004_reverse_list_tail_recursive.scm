;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 004_reverse_list_tail_recursive) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (reverseHelp ls acc)
  (if (null? ls)
      acc ; If list is null return acc
      (reverseHelp (cdr ls) (cons (car ls) acc)) ; Else call recursion on remaining list with first element stored in acc
   )
  )

(define (reverse2 ls) (reverseHelp ls '()))
