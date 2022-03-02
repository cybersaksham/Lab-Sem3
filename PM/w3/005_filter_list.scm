;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 005_filter_list) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (filter_list prd ls) ; prd is given predicate & ls is list, We have to filter predicate on ls
  (cond
    ((null? ls) ls) ; If list is null return null
    ((prd (car ls)) (cons (car ls) (filter_list prd (cdr ls)))) ; Apply prd on first element if satisfies then consider it with remaining list
    (else (filter_list prd (cdr ls))) ; Else don't consider it and apply on remaining list
    )
  )
