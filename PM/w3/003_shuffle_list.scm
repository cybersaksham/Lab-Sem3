;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 003_shuffle_list) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (shuffle_list ls1 ls2) ; ls1 is first list, ls2 is second list, We have to shuffle them
  (cond
    ((null? ls1) ls2) ; If ls1 became empty return ls2
    ((null? ls2) ls1) ; If ls2 became empty return ls1
    (else (append
           (list (car ls1)) ; Add first element of ls1 on index 0
           (list (car ls2)) ; Add first element of ls2 on index 1
           (shuffle_list (cdr ls1) (cdr ls2)) ; Shuffle ls1 & ls2 excluding first elements
           )
          )
    )
  )
