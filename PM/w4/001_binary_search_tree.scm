;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-advanced-reader.ss" "lang")((modname 001_binary_search_tree) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #t #t none #f () #f)))
;; Creating a new node
(define create_newnode (λ (node_value left_subtree right_subtree)
(list node_value left_subtree right_subtree)
))

;; Getting node value
(define node_value (λ (tree) (car tree)))

;; Getting left subtree
(define left_subtree (λ (tree) (cadr tree)))

;; Getting right subtree
(define right_subtree (λ (tree) (caddr tree)))

;; Getting height difference (balance factor)
(define height_difference (λ (left_subtree right_subtree)
                            (let ((lh (height left_subtree))
                                  (rh (height right_subtree)))
                              (if (< lh rh) (- rh lh) (- lh rh))
                              )
                            )
  )

;; Initializing a new tree
(define initialize (λ () '()))

;; Inserting a value
(define insert (λ (tree value)
                 (cond
                   ((isempty? tree) (create_newnode value (initialize) (initialize)))
                   ((< value (node_value tree))
                    (create_newnode (node_value tree)
                                    (insert (left_subtree tree) value)
                                    (right_subtree tree)))
                   ((> value (node_value tree))
                    (create_newnode (node_value tree)
                                    (left_subtree tree)
                                    (insert (right_subtree tree) value)))
                   (else tree)
                   )
                 )
  )

;; Checking for empty
(define isempty? (λ (tree) (null? tree)))

;; Getting height
(define height (λ (tree)
                 (cond
                   ((isempty? tree) -1)
                   (else (cond
                           ((> (height (left_subtree tree)) (height (right_subtree tree)))
                            (+ 1 (height (left_subtree tree))))
                           (else (+ 1 (height (right_subtree tree))))
                           )
                         )
                   )
                 )
  )

;; Input
(define sa (initialize))
(define sa1 (insert sa 100))
(format "Insert 100 -> ~s" sa1)
(define sa2 (insert sa1 80))
(format "Insert 80 -> ~s" sa2)
(define sa3 (insert sa2 70))
(format "Insert 70 -> ~s" sa3)
(define sa4 (insert sa3 120))
(format"Insert 120 -> ~s" sa4)
(define sa5 (insert sa4 110))
(format "Insert 110 -> ~s" sa5)
(define bst (insert sa5 130))
(format "Insert 130 -> ~s" bst)
(format "Is BST Empty -> ~s" (isempty? bst))
(format "Height of BST -> ~s" (height bst))
