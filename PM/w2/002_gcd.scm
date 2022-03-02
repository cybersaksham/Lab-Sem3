;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 002_gcd) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (gcd_ x y)
  (cond
    ((= x 0) y) ; If x is zero return y
    ((= y 0) x) ; If y is zero return x
    ((< x y) (gcd_ (remainder y x) x)) ; If x < y take y % x and find gcd with x
    ((> x y) (gcd_ (remainder x y) y)) ; If y < x take x % y and find gcd with y
    (else x) ; If equal then return any
    )
  )
