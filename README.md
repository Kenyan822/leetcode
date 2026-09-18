# leetcode

[arai60](https://1kohei1.com/leetcode/) を[一般社団法人ソフトウェアエンジニアリング協会](https://www.swe.or.jp/)の
コーディング練習会の進め方で解いた記録。

## 進捗

arai60: 0 / 60

---

## 目指していること

**問題を通すことが目的ではない。**

ソフトウェアエンジニアは専門家集団であり、専門家集団には共通基盤となる「常識」がある。
その常識 — 知識だけでなく、反応・行動・感覚・判断 — を専門家に合わせることが目的。

到達点の目安:

- **初見の LeetCode medium を10分前後で書き上げる**
- 入出力と計算量が合っているだけでは足りない
- 同じコードを見たときに、専門家と同じ反応ができる
- 「専門家のブレの範囲はこれくらいで、自分はその選択肢の中からこれを選ぶ」という感覚を持つ

判断の基準として置いていること:

- **可読性とは、説明的な変数名を付けることではない。**
読む側のワーキングメモリを早く解放するコードが読みやすい
- **よく管理されたコードとは、現在と未来のチームメイトの邪魔をしないコード**
- 計算量は計算時間を見積もる手段にすぎない。
問題になるのは実際に何秒かかるかであって、漸近的な振る舞いそのものではない

## なぜ三段階なのか

「できていない」状態から逆算して段階を切っている。


| 詰まり方        | 診断                             |
| ----------- | ------------------------------ |
| 方法を思いつかない   | 一度見れば分かる。ここは重くない               |
| 文法ミスで通らない   | 回数を書けば直る                       |
| 覚えられない      | 理屈どおり書けば頭に入るはず。入らないなら書き方が素直でない |
| 10分で書き終わらない | 写すだけなら終わる。余計なことをしている           |


### step1 — 通す

- 答えを見ずに考える。**5分**で分からなければ答えを見る
- 理解したら答えを隠して書く。筆が進まず5分迷ったら、また見る
- **見たら全部消してやり直す**
- AC したら step1 完了

`memo.md` に書く:

- **最初に考えたこと** — 答えを見る前に何を思いついたか
- **詰まった点** — どこで筆が止まったか

### step2 — 整える

- 読みやすくできるだけ整える
- **過去に同じ問題を解いた人の解答を Discord で探して読む**

step2 の本体は整形ではなく **コメントの予測**。
通ったか通っていないかだけに注目すると、学習の効率がとても悪い。
自分のコードにレビュアーが何を言うかを予測し、実際のレビューとの差を取る。そこが学習の信号になる。

`memo.md` に書く:

- **何を変えたか / なぜ**
- **レビューで何を言われそうか** — 予測を先に書いておくと、実際のコメントとの差がそのまま学習点になる
- **他人の解答を読んで気づいたこと** — 自分と何が違い、その良し悪しは何か

### step3 — 定着させる

- **全部消す。**時間を測って書き直す。AC したらまた消して書く
- **10分以内・ノーエラーで3回連続**できたら済

測るのは **所要時間 / エラーの有無 / 連続回数** の3つだけ。
提出でエラーが出たらその回は失敗。連続が途切れたら数え直し。
10分は絶対ではなく、回答がとても長くなる問題では超えることもある。理念に従って調整する。

`memo.md` に試行を記録する:

```
## step3
1. 8:32 / エラー1（IndexError: 右端の境界）
2. 7:10 / ノーエラー
3. 6:48 / ノーエラー
4. 6:20 / ノーエラー → 済
```

この例では 2・3・4 が連続3回。1回目はエラーが出ているので数に入らない。

**「エラー1回」より「どこで間違えたか」を書く方が大事。**
繰り返すのは暗記のためではない。
**何回も繰り返し間違う箇所は、なんらかの不自然さを反映していることが多い。**
同じ箇所を2回以上間違えたら、記憶の問題ではなくコードが素直でないサインなので、step2 に戻って書き方を変える。

目標は「覚える」ではなく、**勝手に覚えてしまうくらい洗練させる**こと。
何回書いてもだいたい同じコードになる状態が、収束した状態。

## 一問の流れ

1. 着手した瞬間に Discord の自分のチャンネルに書き込む
2. step1 → step2 → step3
3. 呼んでいる標準ライブラリのドキュメントに目を通す。
 自分の実装とほぼ同じ機能が標準ライブラリにあれば、ソースを読む
4. GitHub に上げる
5. `#レビュー依頼` に投稿し、**同じ問題を直近で解いた人を5人メンション**する
6. あわせて **次に解く問題を予告**する
7. レビューを受けて書き直す

詰まったときは黙らない。応答が途切れるより、細かく刻んで投稿する方がよい。


| 状況              | どうするか                    |
| --------------- | ------------------------ |
| 5分考えて分からない      | 答えを見る（粘らない）              |
| 答えを見た           | 全部消してやり直す                |
| **15分考えて分からない** | **そこまで何を考えたのかを言語化して投げる** |
| 動かないコードが直せない    | そのまま投げる                  |


## レビュー — ここが本番

**自分が書いてコメントをもらうところは前座に過ぎず、他人のコードを読んでレビューするところが本番。**

エンジニアは読む方が多い仕事で、コメントを付ける側に回ることが最も学習になる。

- 内容の質は問わない。「読めない」「読める」「気に入った」「気に食わない」で十分
- 5分読んで読めなかった、でも十分に意味のあるコメント
- 机に向かえない日でも、5〜15分あれば回せる

コードがアクセプトされること自体は、大したことではない。

## ディレクトリ構成

各問題に `step1.py` / `step2.py` / `step3.py` / `memo.md` を置く。

段階ごとにファイルを分けるのは、
**step1 → step2 の差分がそのまま step2 の成果物**であり、
**step3 が step2 に収束しているかどうかが診断になる**ため。1ファイルに上書きするとこれが消える。

1問1ブランチ・1PR。段階ごとに commit を積み、レビュー対応が終わったらマージする。

## 出典

- 一般社団法人ソフトウェアエンジニアリング協会「コーディング練習会参加マニュアル」（2024年12月13日）
- 新井康平「[コーディング面接対策のために解きたいLeetCode 60問](https://1kohei1.com/leetcode/)」

---

## 一覧


| カテゴリ                  | #    | 問題                                                                                                                             | LeetCode                                                                                      | 済   | 日付  |
| --------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- | --- | --- |
| LinkedList            | 141  | [Linked List Cycle](./0141-linked-list-cycle/)                                                                                 | [↗](https://leetcode.com/problems/linked-list-cycle/)                                         |     |     |
| LinkedList            | 142  | [Linked List Cycle II](./0142-linked-list-cycle-ii/)                                                                           | [↗](https://leetcode.com/problems/linked-list-cycle-ii/)                                      |     |     |
| LinkedList            | 83   | [Remove Duplicates from Sorted List](./0083-remove-duplicates-from-sorted-list/)                                               | [↗](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)                        |     |     |
| LinkedList            | 82   | [Remove Duplicates from Sorted List II](./0082-remove-duplicates-from-sorted-list-ii/)                                         | [↗](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)                     |     |     |
| LinkedList            | 2    | [Add Two Numbers](./0002-add-two-numbers/)                                                                                     | [↗](https://leetcode.com/problems/add-two-numbers/)                                           |     |     |
| Stack                 | 20   | [Valid Parentheses](./0020-valid-parentheses/)                                                                                 | [↗](https://leetcode.com/problems/valid-parentheses/)                                         |     |     |
| Stack                 | 206  | [Reverse Linked List](./0206-reverse-linked-list/)                                                                             | [↗](https://leetcode.com/problems/reverse-linked-list/)                                       |     |     |
| Heap, PriorityQueue   | 703  | [Kth Largest Element in a Stream](./0703-kth-largest-element-in-a-stream/)                                                     | [↗](https://leetcode.com/problems/kth-largest-element-in-a-stream/)                           |     |     |
| Heap, PriorityQueue   | 347  | [Top K Frequent Elements](./0347-top-k-frequent-elements/)                                                                     | [↗](https://leetcode.com/problems/top-k-frequent-elements/)                                   |     |     |
| Heap, PriorityQueue   | 373  | [Find K Pairs with Smallest Sums](./0373-find-k-pairs-with-smallest-sums/)                                                     | [↗](https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)                           |     |     |
| HashMap               | 1    | [Two Sum](./0001-two-sum/)                                                                                                     | [↗](https://leetcode.com/problems/two-sum/)                                                   |     |     |
| HashMap               | 49   | [Group Anagrams](./0049-group-anagrams/)                                                                                       | [↗](https://leetcode.com/problems/group-anagrams/)                                            |     |     |
| HashMap               | 349  | [Intersection of Two Arrays](./0349-intersection-of-two-arrays/)                                                               | [↗](https://leetcode.com/problems/intersection-of-two-arrays/)                                |     |     |
| HashMap               | 929  | [Unique Email Addresses](./0929-unique-email-addresses/)                                                                       | [↗](https://leetcode.com/problems/unique-email-addresses/)                                    |     |     |
| HashMap               | 387  | [First Unique Character in a String](./0387-first-unique-character-in-a-string/)                                               | [↗](https://leetcode.com/problems/first-unique-character-in-a-string/)                        |     |     |
| HashMap               | 560  | [Subarray Sum Equals K](./0560-subarray-sum-equals-k/)                                                                         | [↗](https://leetcode.com/problems/subarray-sum-equals-k/)                                     |     |     |
| Graph, BFS, DFS       | 200  | [Number of Islands](./0200-number-of-islands/)                                                                                 | [↗](https://leetcode.com/problems/number-of-islands/)                                         |     |     |
| Graph, BFS, DFS       | 695  | [Max Area of Island](./0695-max-area-of-island/)                                                                               | [↗](https://leetcode.com/problems/max-area-of-island/)                                        |     |     |
| Graph, BFS, DFS       | 323  | [Number of Connected Components in an Undirected Graph](./0323-number-of-connected-components-in-an-undirected-graph/)         | [↗](https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/)     |     |     |
| Graph, BFS, DFS       | 127  | [Word Ladder](./0127-word-ladder/)                                                                                             | [↗](https://leetcode.com/problems/word-ladder/)                                               |     |     |
| Tree, BT, BST         | 104  | [Maximum Depth of Binary Tree](./0104-maximum-depth-of-binary-tree/)                                                           | [↗](https://leetcode.com/problems/maximum-depth-of-binary-tree/)                              |     |     |
| Tree, BT, BST         | 111  | [Minimum Depth of Binary Tree](./0111-minimum-depth-of-binary-tree/)                                                           | [↗](https://leetcode.com/problems/minimum-depth-of-binary-tree/)                              |     |     |
| Tree, BT, BST         | 617  | [Merge Two Binary Trees](./0617-merge-two-binary-trees/)                                                                       | [↗](https://leetcode.com/problems/merge-two-binary-trees/)                                    |     |     |
| Tree, BT, BST         | 108  | [Convert Sorted Array to Binary Search Tree](./0108-convert-sorted-array-to-binary-search-tree/)                               | [↗](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)                |     |     |
| Tree, BT, BST         | 112  | [Path Sum](./0112-path-sum/)                                                                                                   | [↗](https://leetcode.com/problems/path-sum/)                                                  |     |     |
| Tree, BT, BST         | 102  | [Binary Tree Level Order Traversal](./0102-binary-tree-level-order-traversal/)                                                 | [↗](https://leetcode.com/problems/binary-tree-level-order-traversal/)                         |     |     |
| Tree, BT, BST         | 103  | [Binary Tree Zigzag Level Order Traversal](./0103-binary-tree-zigzag-level-order-traversal/)                                   | [↗](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)                  |     |     |
| Tree, BT, BST         | 98   | [Validate Binary Search Tree](./0098-validate-binary-search-tree/)                                                             | [↗](https://leetcode.com/problems/validate-binary-search-tree/)                               |     |     |
| Tree, BT, BST         | 105  | [Construct Binary Tree from Preorder and Inorder Traversal](./0105-construct-binary-tree-from-preorder-and-inorder-traversal/) | [↗](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) |     |     |
| Dynamic Programming   | 276  | [Paint Fence](./0276-paint-fence/)                                                                                             | [↗](https://leetcode.com/problems/paint-fence/)                                               |     |     |
| Dynamic Programming   | 300  | [Longest Increasing Subsequence](./0300-longest-increasing-subsequence/)                                                       | [↗](https://leetcode.com/problems/longest-increasing-subsequence/)                            |     |     |
| Dynamic Programming   | 53   | [Maximum Subarray](./0053-maximum-subarray/)                                                                                   | [↗](https://leetcode.com/problems/maximum-subarray/)                                          |     |     |
| Dynamic Programming   | 62   | [Unique Paths](./0062-unique-paths/)                                                                                           | [↗](https://leetcode.com/problems/unique-paths/)                                              |     |     |
| Dynamic Programming   | 63   | [Unique Paths II](./0063-unique-paths-ii/)                                                                                     | [↗](https://leetcode.com/problems/unique-paths-ii/)                                           |     |     |
| Dynamic Programming   | 198  | [House Robber](./0198-house-robber/)                                                                                           | [↗](https://leetcode.com/problems/house-robber/)                                              |     |     |
| Dynamic Programming   | 213  | [House Robber II](./0213-house-robber-ii/)                                                                                     | [↗](https://leetcode.com/problems/house-robber-ii/)                                           |     |     |
| Dynamic Programming   | 121  | [Best Time to Buy and Sell Stock](./0121-best-time-to-buy-and-sell-stock/)                                                     | [↗](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)                           |     |     |
| Dynamic Programming   | 122  | [Best Time to Buy and Sell Stock II](./0122-best-time-to-buy-and-sell-stock-ii/)                                               | [↗](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)                        |     |     |
| Dynamic Programming   | 139  | [Word Break](./0139-word-break/)                                                                                               | [↗](https://leetcode.com/problems/word-break/)                                                |     |     |
| Dynamic Programming   | 322  | [Coin Change](./0322-coin-change/)                                                                                             | [↗](https://leetcode.com/problems/coin-change/)                                               |     |     |
| Binary Search         | 35   | [Search Insert Position](./0035-search-insert-position/)                                                                       | [↗](https://leetcode.com/problems/search-insert-position/)                                    |     |     |
| Binary Search         | 153  | [Find Minimum in Rotated Sorted Array](./0153-find-minimum-in-rotated-sorted-array/)                                           | [↗](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)                      |     |     |
| Binary Search         | 33   | [Search in Rotated Sorted Array](./0033-search-in-rotated-sorted-array/)                                                       | [↗](https://leetcode.com/problems/search-in-rotated-sorted-array/)                            |     |     |
| Binary Search         | 1011 | [Capacity To Ship Packages Within D Days](./1011-capacity-to-ship-packages-within-d-days/)                                     | [↗](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)                   |     |     |
| Recursion             | 50   | [Pow(x, n)](./0050-powx-n/)                                                                                                    | [↗](https://leetcode.com/problems/powx-n/)                                                    |     |     |
| Recursion             | 779  | [K-th Symbol in Grammar](./0779-k-th-symbol-in-grammar/)                                                                       | [↗](https://leetcode.com/problems/k-th-symbol-in-grammar/)                                    |     |     |
| Recursion             | 776  | [Split BST](./0776-split-bst/)                                                                                                 | [↗](https://leetcode.com/problems/split-bst/)                                                 |     |     |
| Sliding Window        | 3    | [Longest Substring Without Repeating Characters](./0003-longest-substring-without-repeating-characters/)                       | [↗](https://leetcode.com/problems/longest-substring-without-repeating-characters/)            |     |     |
| Sliding Window        | 209  | [Minimum Size Subarray Sum](./0209-minimum-size-subarray-sum/)                                                                 | [↗](https://leetcode.com/problems/minimum-size-subarray-sum/)                                 |     |     |
| Greedy + Backtracking | 46   | [Permutations](./0046-permutations/)                                                                                           | [↗](https://leetcode.com/problems/permutations/)                                              |     |     |
| Greedy + Backtracking | 78   | [Subsets](./0078-subsets/)                                                                                                     | [↗](https://leetcode.com/problems/subsets/)                                                   |     |     |
| Greedy + Backtracking | 39   | [Combination Sum](./0039-combination-sum/)                                                                                     | [↗](https://leetcode.com/problems/combination-sum/)                                           |     |     |
| Greedy + Backtracking | 22   | [Generate Parentheses](./0022-generate-parentheses/)                                                                           | [↗](https://leetcode.com/problems/generate-parentheses/)                                      |     |     |
| その他                   | 283  | [Move Zeroes](./0283-move-zeroes/)                                                                                             | [↗](https://leetcode.com/problems/move-zeroes/)                                               |     |     |
| その他                   | 252  | [Meeting Rooms](./0252-meeting-rooms/)                                                                                         | [↗](https://leetcode.com/problems/meeting-rooms/)                                             |     |     |
| その他                   | 253  | [Meeting Rooms II](./0253-meeting-rooms-ii/)                                                                                   | [↗](https://leetcode.com/problems/meeting-rooms-ii/)                                          |     |     |
| その他                   | 392  | [Is Subsequence](./0392-is-subsequence/)                                                                                       | [↗](https://leetcode.com/problems/is-subsequence/)                                            |     |     |
| その他                   | 31   | [Next Permutation](./0031-next-permutation/)                                                                                   | [↗](https://leetcode.com/problems/next-permutation/)                                          |     |     |
| その他                   | 8    | [String to Integer (atoi)](./0008-string-to-integer-atoi/)                                                                     | [↗](https://leetcode.com/problems/string-to-integer-atoi/)                                    |     |     |
| その他                   | 6    | [ZigZag Conversion](./0006-zigzag-conversion/)                                                                                 | [↗](https://leetcode.com/problems/zigzag-conversion/)                                         |     |     |


