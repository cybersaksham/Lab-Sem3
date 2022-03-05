;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 002_merge_sort) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
;; Merge Sort
(define (mergesort L)
  (if (null? L) L ; If null return null
      (if (not (list? L)) "mergesort requires a list argument" ; If L is not a list
          (if (null? (cdr L)) L ; If length is 1 return list
              (if (and (number? (car L)) (number? (cadr L))) (merge_h (mergesort (car (split L))) (mergesort (cadr (split L)))) ; Merge even and odd split after sorting
                  (mergesort (cdr L)) ; Else drop first element
              )
          )
      )
  )
  )


; Sorts a list using odd_copy and even_copy
(define (merge_h L M)
  (if (null? L) M ; If L is null return M
      (if (null? M) L ; If M is null return L
          (if (number? (car L))
              (if (number? (car M))
                  (if (< (car L) (car M)) (cons (car L) (merge_h (cdr L) M)) ; Insert smaller element at front and run for remaining
                      (cons (car M) (merge_h L (cdr M))))
                  (merge_h L (cdr L)))
              (merge_h M (cdr M))
              )
          )
      )
  )

;; Split function
(define (split L)
  (cons (odd_copy L) (cons (even_copy L) '())) ; Combine odd & even copy
  )

;; Find odd copy
(define (odd_copy L)
  (if (null? L) '() ; If list is null return null
      (if (null? (cdr L)) (list (car L)) ; If length is 1 return first element
          (cons (car L) (odd_copy (cddr L))) ; Else insert first element at front & drop first 2 elements
          )
      )
  )

;; Find even copy
(define (even_copy L)
  (if (null? L) '() ; If list is null return null
      (if (null? (cdr L)) '() ; If length is 1 return null
          (cons (cadr L) (even_copy (cddr L))) ; Else insert second element at front & drop first 2 elements
          )
      )
  )
