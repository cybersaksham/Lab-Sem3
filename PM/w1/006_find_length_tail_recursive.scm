;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 006_find_length_tail_recursive) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (findlenHelp ls acc)
  (if (null? ls)
      acc ; If list is null return acc
      (findlenHelp (cdr ls) (+ acc 1)) ; Else call recursion on remaining list and increase acc
      )
  )

(define (findlen ls) (findlenHelp ls 0))
