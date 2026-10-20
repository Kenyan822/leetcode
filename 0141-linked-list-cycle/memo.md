# 141. Linked List Cycle

https://leetcode.com/problems/linked-list-cycle/

## step1

最初に考えたこと:メモリどれくらい使いそうか/

詰まった点:setに格納していくという発想

※ step1.py は head が None（空リスト）だと AttributeError で落ちる。Submit は AC した。step2 で直す。

## step2

何を変えたか / なぜ:最初のheadの判定を別に処理していたが、空のリストの場合にエラーになる、もっと汎化した記法があったため

レビューで何を言われそうか:変数名(node)が適切か、もっと計算量の早い解放はないか

## step3

<!-- 1. 8:32 / エラー1（どこで間違えたか） -->

1. 1:19 / ノーエラー
2. 1:15 / ノーエラー
3. 1:12 / ノーエラー → 済

## memo
