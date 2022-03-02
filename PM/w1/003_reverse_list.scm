;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 003_reverse_list) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (reverse1 ls)
  (if (null? ls)
      '() ; If list is null return null
      (append (reverse1 (cdr ls)) (list (car ls))) ; Else append first element at last of reversed remaining list
     )
  )
