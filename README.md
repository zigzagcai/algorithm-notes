
# LeetCode 热题分类题解

## 说明
repo仅作为个人算法学习的记录，README模板主要参考[LeetCode_Hot100_Python](https://github.com/realnghon/LeetCode_Hot100_Python)，算法题解主要学习自[0x3f大佬](https://github.com/EndlessCheng)，插件使用的是[vscode-leetcode](https://marketplace.visualstudio.com/items?itemName=ccagml.vscode-leetcode-problem-rating)

### 目录
1. [哈希](#哈希)
2. [双指针](#双指针)
3. [滑动窗口](#滑动窗口)
4. [子串](#子串)
5. [普通数组](#普通数组)
6. [矩阵](#矩阵)
7. [链表](#链表)
8. [二叉树](#二叉树)
9. [二分查找](#二分查找)
10. [栈](#栈)
11. [堆](#堆)
12. [贪心算法](#贪心算法)
13. [动态规划](#动态规划)
14. [技巧](#技巧)

## 哈希

| 难度  | 题号  | 题目名称    | 题解链接                                |
| --- | --- | ------- | ----------------------------------- |
| 简单  | 1   | [两数之和](https://leetcode.cn/problems/two-sum/description/)    | [题解](./1.two-sum.py)       |
| 中等  | 49  | [字母异位词分组](https://leetcode.cn/problems/group-anagrams/description/) | [题解](./49.group-anagrams.py) |
| 中等  | 128 | [最长连续序列](https://leetcode.cn/problems/longest-consecutive-sequence/description/)  | [题解](./128.longest-consecutive-sequence.py) |

## 双指针

| 难度   | 题号 | 题目名称            | 题解链接                                        |
|--------|------|---------------------|-------------------------------------------------|
| 简单   | 283  | [移动零](https://leetcode.cn/problems/move-zeroes/description/)               | [题解](./283.move-zeroes.py)            |
| 中等   | 11   | [盛最多水的容器](https://leetcode.cn/problems/container-with-most-water/description/)       | [题解](./11.container-with-most-water.py)     |
| 中等   | 15   | [三数之和](https://leetcode.cn/problems/3sum/description/)             | [题解](./15.3-sum.py)           |

## 滑动窗口

| 难度   | 题号 | 题目名称                | 题解链接                                            |
|--------|------|-------------------------|-----------------------------------------------------|
| 中等   | 3    | [无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/)      | [题解](./3.longest-substring-without-repeating-characters.py)    |
| 中等   | 438  | [找到字符串中所有字母异位词](https://leetcode.cn/problems/find-all-anagrams-in-a-string/description/) | [题解](./438.find-all-anagrams-in-a-string.py) |

## 子串

| 难度   | 题号 | 题目名称          | 题解链接                                        |
|--------|------|-------------------|-------------------------------------------------|
| 中等   | 560  | [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/description/)    | [题解](./560.subarray-sum-equals-k.py)     |

## 普通数组

| 难度   | 题号 | 题目名称                | 题解链接                    |
|--------|------|-------------------------|-----------------------------|
| 中等   | 53   | [最大子数组和](https://leetcode.cn/problems/maximum-subarray/description/)            | [题解](./53.maximum-subarray.py) |
| 中等   | 56   | [合并区间](https://leetcode.cn/problems/merge-intervals/description/)                | [题解](./56.merge-intervals.py) |
| 中等   | 189  | [轮转数组](https://leetcode.cn/problems/rotate-array/description/)                | [题解](./189.rotate-array.py) |
| 中等   | 238  | [除自身以外数组的乘积](https://leetcode.cn/problems/product-of-array-except-self/description)     | [题解](./238.product-of-array-except-self.py) |

## 矩阵

| 难度  | 题号  | 题目名称      | 题解链接                                    |
| --- | --- | --------- | --------------------------------------- |
| 中等  | 73  | [矩阵置零](https://leetcode.cn/problems/set-matrix-zeroes/description/)      | [题解](./73.set-matrix-zeroes.py)      |
| 中等  | 54  | [螺旋矩阵](https://leetcode.cn/problems/spiral-matrix/description/)      | [题解](./54.spiral-matrix.py)        |
| 中等  | 48  | [旋转图像](https://leetcode.cn/problems/rotate-image/description/)      | [题解](./48.rotate-image.py)       |
| 中等  | 240 | [搜索二维矩阵 II](https://leetcode.cn/problems/search-a-2d-matrix-ii/description/) | [题解](./240.search-a-2-d-matrix-ii.py) |

## 链表

| 难度  | 题号  | 题目名称           | 题解链接                                       |
| --- | --- | -------------- | ------------------------------------------ |
| 简单  | 160 | [相交链表](https://leetcode.cn/problems/intersection-of-two-linked-lists/description/)           | [题解](./160.intersection-of-two-linked-lists.py)            |
| 简单  | 206 | [反转链表](https://leetcode.cn/problems/reverse-linked-list/description/)           | [题解](./206.reverse-linked-list.py)            |
| 简单  | 234 | [回文链表](https://leetcode.cn/problems/palindrome-linked-list/description/)           | [题解](./234.palindrome-linked-list.py)            |
| 简单  | 141 | [环形链表](https://leetcode.cn/problems/linked-list-cycle/description/)           | [题解](./141.linked-list-cycle.py)            |
| 简单  | 21  | [合并两个有序链表](https://leetcode.cn/problems/merge-two-sorted-lists/description/)       | [题解](./21.merge-two-sorted-lists.py)         |
| 中等  | 142 | [环形链表 II](https://leetcode.cn/problems/linked-list-cycle-ii/description/)        | [题解](./142.linked-list-cycle-ii.py)       |
| 中等  | 2   | [两数相加](https://leetcode.cn/problems/add-two-numbers/description/)           | [题解](./Hot100_Medium.md#2-两数相加)            |
| 中等  | 19  | [删除链表的倒数第 N 个节点](https://leetcode.cn/problems/remove-nth-node-from-end-of-list/description/) | [题解](./19.remove-nth-node-from-end-of-list.py) |
| 中等  | 24  | [两两交换链表的节点](https://leetcode.cn/problems/swap-nodes-in-pairs/description/)      | [题解](./Hot100_Medium.md#24-两两交换链表的节点)      |
| 中等  | 148 | [排序链表](https://leetcode.cn/problems/sort-list/description/)           | [题解](./148.sort-list.py)          |
| 中等  | 146 | [LRU 缓存](https://leetcode.cn/problems/lru-cache/description/)         | [题解](./146.lru-cache.py)        |

## 二叉树

| 难度  | 题号  | 题目名称            | 题解链接                                         |
| --- | --- | --------------- | -------------------------------------------- |
| 简单  | 94  | [二叉树的中序遍历](https://leetcode.cn/problems/binary-tree-inorder-traversal/description/)        | [题解](./94.binary-tree-inorder-traversal.py)           |
| 简单  | 104 | [二叉树的最大深度](https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/)        | [题解](./104.maximum-depth-of-binary-tree.py)          |
| 简单  | 226 | [翻转二叉树](https://leetcode.cn/problems/invert-binary-tree/description/)           | [题解](./226.invert-binary-tree.py)             |
| 简单  | 543 | [二叉树的直径](https://leetcode.cn/problems/diameter-of-binary-tree/description/)          | [题解](./Hot100_Easy.md#543-二叉树的直径)            |
| 简单  | 108 | [将有序数组转换为二叉搜索树](https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/)   | [题解](./108.convert-sorted-array-to-binary-search-tree.py)     |
| 中等  | 102 | [二叉树的层序遍历](https://leetcode.cn/problems/binary-tree-level-order-traversal/description/)        | [题解](./102.binary-tree-level-order-traversal.py)        |
| 中等  | 98  | [验证二叉搜索树](https://leetcode.cn/problems/validate-binary-search-tree/description/)         | [题解](./98.validate-binary-search-tree.py)          |
| 中等  | 230 | [二叉搜索树中第 K 小的元素](https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/)  | [题解](./230.kth-smallest-element-in-a-bst.py)  |
| 中等  | 199 | [二叉树的右视图](https://leetcode.cn/problems/binary-tree-right-side-view/description/)         | [题解](./199.binary-tree-right-side-view.py)         |
| 中等  | 114 | [二叉树展开为链表](https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/description/)        | [题解](./114.flatten-binary-tree-to-linked-list.py)        |
| 中等  | 105 | [从前序与中序遍历序列构造二叉树](https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/) | [题解](./105.construct-binary-tree-from-preorder-and-inorder-traversal.py) |
| 中等  | 437 | [路径总和 III](https://leetcode.cn/problems/path-sum-iii/description/)        | [题解](./437.path-sum-iii.py)        |
| 中等  | 236 | [二叉树的最近公共祖先](https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree/description/)      | [题解](./236.lowest-common-ancestor-of-a-binary-tree.py)      |

## 图论
| 难度  | 题号  | 题目名称          | 题解链接                                     |
| --- | --- | ------------- | ---------------------------------------- |
| 中等  | 200 | [岛屿数量](https://leetcode.cn/problems/number-of-islands/description/)          | [题解](./200.number-of-islands.py)        |
| 中等  | 994 | [腐烂的橘子](https://leetcode.cn/problems/rotting-oranges/description/)         | [题解](./994.rotting-oranges.py)       |
| 中等  | 207 | [课程表](https://leetcode.cn/problems/course-schedule/description/)           | [题解](./207.course-schedule.py)         |
| 中等  | 208 | [实现 Trie (前缀树)](https://leetcode.cn/problems/implement-trie-prefix-tree/description/) | [题解](./208.implement-trie-prefix-tree.py) |

## 回溯法
| 难度  | 题号  | 题目名称               | 题解链接                                     |
| --- | --- | ------------------ | ---------------------------------------- |
| 中等  | 46  | [全排列](https://leetcode.cn/problems/permutations/description/)                | [题解](./46.permutations.py)           |
| 中等  | 78  | [子集](https://leetcode.cn/problems/subsets/description/)                 | [题解](./78.subsets.py)             |
| 中等  | 17  | [电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/)         | [题解](./17.letter-combinations-of-a-phone-number.py)   |
| 中等  | 39  | [组合总和](https://leetcode.cn/problems/combination-sum/description/)              | [题解](./39.combination-sum.py)           |
| 中等  | 22  | [括号生成](https://leetcode.cn/problems/generate-parentheses/description/)               | [题解](./22.generate-parentheses.py)           |
| 中等  | 79  | [单词搜索](https://leetcode.cn/problems/word-search/description/)               | [题解](./79.word-search.py)           |
| 中等  | 131 | [分割回文串](https://leetcode.cn/problems/palindrome-partitioning/description/)             | [题解](./131.palindrome-partitioning.py)         |


## 二分查找

| 难度  | 题号  | 题目名称                  | 题解链接                                              |
| --- | --- | --------------------- | ------------------------------------------------- |
| 简单  | 35  | [搜索插入位置](https://leetcode.cn/problems/search-insert-position/description/)                | [题解](./35.search-insert-position.py)                  |
| 中等  | 74  | [搜索二维矩阵](https://leetcode.cn/problems/search-a-2d-matrix/description/)                | [题解](./74.search-a-2-d-matrix.py)                |
| 中等  | 34  | [在排序数组中查找元素的第一个和最后一个位置](https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/) | [题解](./34.find-first-and-last-position-of-element-in-sorted-array.py) |
| 中等  | 33  | [搜索旋转排序数组](https://leetcode.cn/problems/search-in-rotated-sorted-array/description/)              | [题解](./33.search-in-rotated-sorted-array.py)              |
| 中等  | 153 | [寻找旋转排序数组中的最小值](https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/)         | [题解](./153.find-minimum-in-rotated-sorted-array.py)        |

## 栈

| 难度  | 题号  | 题目名称  | 题解链接                               |
| --- | --- | ----- | ---------------------------------- |
| 简单  | 20  | [有效的括号](https://leetcode.cn/problems/valid-parentheses/description/) | [题解](./20.valid-parentheses.py)    |
| 中等  | 155 | [最小栈](https://leetcode.cn/problems/min-stack/description/)   | [题解](./155.min-stack.py)   |
| 中等  | 394 | [字符串解码](https://leetcode.cn/problems/decode-string/description/) | [题解](./394.decode-string.py) |
| 中等  | 739 | [每日温度](https://leetcode.cn/problems/daily-temperatures/description/)  | [题解](./739.daily-temperatures.py)  |

## 堆

| 难度  | 题号  | 题目名称       | 题解链接                                    |
| --- | --- | ---------- | --------------------------------------- |
| 中等  | 215 | [数组中第K个最大元素](https://leetcode.cn/problems/kth-largest-element-in-an-array/description/) | [题解](./215.kth-largest-element-in-an-array.py) |
| 中等  | 347 | [前 K 个高频元素](https://leetcode.cn/problems/top-k-frequent-elements/description/)  | [题解](./347.top-k-frequent-elements.py)  |

## 贪心算法

| 难度  | 题号  | 题目名称      | 题解链接                                 |
| --- | --- | --------- | ------------------------------------ |
| 简单  | 121 | [买卖股票的最佳时机](https://leetcode.cn/problems/best-time-to-buy-and-sell-stock/description/) | [题解](./121.best-time-to-buy-and-sell-stock.py) |
| 中等  | 55  | [跳跃游戏](https://leetcode.cn/problems/jump-game/description/)      | [题解](./55.jump-game.py)     |
| 中等  | 45  | [跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/description/)   | [题解](./45.jump-game-ii.py)  |
| 中等  | 763 | [划分字母区间](https://leetcode.cn/problems/partition-labels/description/)    | [题解](./763.partition-labels.py)  |

## 动态规划

| 难度  | 题号  | 题目名称    | 题解链接                                 |
| --- | --- | ------- | ------------------------------------ |
| 简单  | 70  | [爬楼梯](https://leetcode.cn/problems/climbing-stairs/description/)     | [题解](./70.climbing-stairs.py)        |
| 简单  | 118 | [杨辉三角](https://leetcode.cn/problems/pascals-triangle/description/)    | [题解](./118.pascals-triangle.py)      |
| 中等  | 198 | [打家劫舍](https://leetcode.cn/problems/house-robber/description/)    | [题解](./198.house-robber.py)    |
| 中等  | 279 | [完全平方数](https://leetcode.cn/problems/perfect-squares/description/)   | [题解](./279.perfect-squares.py)   |
| 中等  | 322 | [零钱兑换](https://leetcode.cn/problems/coin-change/description/)    | [题解](./322.coin-change.py)    |
| 中等  | 139 | [单词拆分](https://leetcode.cn/problems/word-break/description/)    | [题解](./139.word-break.py)    |
| 中等  | 300 | [最长递增子序列](https://leetcode.cn/problems/longest-increasing-subsequence/description/) | [题解](./300.longest-increasing-subsequence.py) |
| 中等  | 152 | [乘积最大子数组](https://leetcode.cn/problems/maximum-product-subarray/description/) | [题解](./152.maximum-product-subarray.py) |
| 中等  | 416 | [分割等和子集](https://leetcode.cn/problems/partition-equal-subset-sum/description/)  | [题解](./416.partition-equal-subset-sum.py)  |
| 困难  | 32  | [最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/description/)  | [题解](./32.longest-valid-parentheses.py)     |

## 多维动态规划

| 难度  | 题号   | 题目名称    | 题解链接                                                                                          |
| --- | ---- | ------- | --------------------------------------------------------------------------------------------- |
| 中等  | 62   | [不同路径](https://leetcode.cn/problems/unique-paths/description/)    | [题解](./62.unique-paths.py)                              |
| 中等  | 64   | [最小路径和](https://leetcode.cn/problems/minimum-path-sum/description/)   | [题解](./64.minimum-path-sum.py)                     |
| 中等  | 5    | [最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/description/)  | [题解](./5.longest-palindromic-substring.py)             |
| 中等  | 1143 | [最长公共子序列](https://leetcode.cn/problems/longest-common-subsequence/description/) | [题解](./1143.longest-common-subsequence.py) |
| 中等  | 72   | [编辑距离](https://leetcode.cn/problems/edit-distance/description/)    | [题解](./72.edit-distance.py)                              |

## 技巧

| 难度  | 题号  | 题目名称     | 题解链接                                |
| --- | --- | -------- | ----------------------------------- |
| 简单  | 136 | [只出现一次的数字](https://leetcode.cn/problems/single-number/description/) | [题解](./136.single-number.py) |
| 简单  | 169 | [多数元素](https://leetcode.cn/problems/majority-element/description/)     | [题解](./169.majority-element.py)     |
| 中等  | 75  | [颜色分类](https://leetcode.cn/problems/sort-colors/description/)     | [题解](./75.sort-colors.py)    |
| 中等  | 31  | [下一个排列](https://leetcode.cn/problems/next-permutation/description/)    | [题解](./31.next-permutation.py)   |
| 中等  | 287 | [寻找重复数](https://leetcode.cn/problems/find-the-duplicate-number/description/)    | [题解](./287.find-the-duplicate-number.py)  |