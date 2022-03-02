;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 008_member_of_list) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (ismember atm ls)
  (cond
    ((null? ls) #f) ; If list is null return false
    ((eq? atm (car ls)) #t) ; If first element is equal return true
    (else (ismember atm (cdr ls))) ; Else call recursion on remaining list
    )
  )
