;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 007_factorial) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (factorial n)
  (if (<= n 1)
      1 ; If n <= 1 return 1
      (* n (factorial (- n 1))) ; Else return n * factorial(n - 1)
      )
  )