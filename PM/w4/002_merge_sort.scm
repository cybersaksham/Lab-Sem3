;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 002_merge_sort) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
;; Merge Sort
(define (mergesort L)
  (if (null? L) L
      (if (not (list? L)) "mergesort requires a list argument"
          (if (null? (cdr L)) L
              (if (and (number? (car L)) (number? (cadr L))) (merge_h (mergesort (car (split L))) (mergesort (cadr (split L))))
                  (mergesort (cdr L))
              )
          )
      )
  )
  )


;sorts a list using odd_copy and even_copy
(define (merge_h L M)
  (if (null? L) M
      (if (null? M) L
          (if (number? (car L))
              (if (number? (car M))
                  (if (< (car L) (car M)) (cons (car L) (merge_h (cdr L) M))
                      (cons (car M) (merge_h L (cdr M))))
                  (merge_h L (cdr L)))
              (merge_h M (cdr M))
              )
          )
      )
  )

;; Split function
(define (split L)
  (cons (odd_copy L) (cons (even_copy L) '()))
  )

;; Find odd copy
(define (odd_copy L)
  (if (null? L) '()
      (if (null? (cdr L)) (list (car L))
          (cons (car L) (odd_copy (cddr L)))
          )
      )
  )

;; Find even copy
(define (even_copy L)
  (if (null? L) '()
      (if (null? (cdr L)) '()
          (cons (cadr L) (even_copy (cddr L)))
          )
      )
  )
