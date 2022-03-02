;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 003_mean) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (mean ls) (mean2 (extractNo ls))) ; extracting numbers and finding mean

(define (mean2 ls)
  (if (null? ls)
      (error "No Number found") ; If no number then error
      (/ (Sum ls) (length ls)) ; Else return sum / length
      )
  )

(define (Sum ls) ; Helper funciton to calculate sum
  (if (null? ls)
      0 ; If list is null return 0
      (+ (car ls) (Sum (cdr ls))) ; Else return first element + sum of remaining list
      )
  )

(define (extractNo ls) ; Helper function to extract numbers
  (cond
    ((null? ls) '()) ; If list is null return null
    ((number? (car ls)) (cons (car ls) (extractNo (cdr ls)))) ; If first element is number then consider it and add in remaining list
    (else (extractNo (cdr ls))) ; Else call on remaining list
    )
  )
