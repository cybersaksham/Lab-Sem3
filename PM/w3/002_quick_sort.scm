;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 002_quick_sort) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
(define (quickSort ls)
  (cond
    ((or (null? ls) (null? (cdr ls))) ls) ; If length of list is 0 or 1 return list
    (else (let ((pivot (car ls)) ; Let pivot at first element
                (left (cdr ls)) ; Let left as remaining list
                )
            (append (quickSort (filter (lambda (x) (< x pivot)) left)) ; Sort list having elements smaller than pivot
                    (list pivot) ; Add pivot in middle
                    (quickSort (filter (lambda (x) (>= x pivot)) left)) ; Sort list having elements greater than pivot
                    ) ; Concatenate them in order & pivot is at correct place
            )
          )
    )
  )
