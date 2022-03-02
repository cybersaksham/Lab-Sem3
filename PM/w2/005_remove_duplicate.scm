;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 005_remove_duplicate) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (removeDuplicates ls) (removeDuplicatesHelp ls '()))

(define (removeDuplicatesHelp ls ls2) ; Helper function to remove duplicates - ls2 is for record of previous elements
  (cond
    ((null? ls) '()) ; If list is null return null
    ((member (car ls) ls2) (removeDuplicatesHelp (cdr ls) (cons (car ls) ls2))) ; If first element of list is present in ls2 then remove duplicates from further lsit without adding first element
    (else (cons (car ls) (removeDuplicatesHelp (cdr ls) (cons (car ls) ls2)))) ; Else remove duplicates from further list but also add first element
    )
  )
