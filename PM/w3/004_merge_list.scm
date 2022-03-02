;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 004_merge_list) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (merge_list ls1 ls2) ; ls1 and ls2 are two sorted lists, We have to merge them into one sorted list
  (cond
    ((null? ls1) ls2) ; If ls1 became empty return ls2
    ((null? ls2) ls1) ; If ls2 became empty return ls1
    ; Compare first elements of ls1 & ls2
    ((> (car ls1) (car ls2)) (cons (car ls2) (merge_list ls1 (cdr ls2)))) ; If ls1 is greater call on ls1 & (ls2 excluding first element) and add first element at index 0
    ((< (car ls1) (car ls2)) (cons (car ls1) (merge_list (cdr ls1) ls2))) ; If ls2 is greater call on (ls1 excluding first element) & ls2 and add first element at index 0
    (else (cons (car ls1) (cons (car ls2) (merge_list (cdr ls1) (cdr ls2))))) ; Else call on both reduced lists and add first elements at index 0 & 1
    )
  )
