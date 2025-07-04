# Git 常用命令详解：Merge、Rebase、Squash 与 Stash

## 📌 1. `git merge`

### ✅ 作用：

将一个分支的变更合并到当前分支，生成一个新的合并提交（merge commit）。

### 🧠 场景：

用于保留多个分支的提交历史，比如合并开发分支到主分支。

### 🛠️ 使用示例：

```bash
# 切换到主分支
git checkout main

# 合并 feature 分支到 main
git merge feature
```

### 🔍 特点：

* 保留两条分支的历史
* 会生成一个合并提交
* 若两个分支有冲突，需要手动解决冲突后再提交

---

## 🔁 2. `git rebase`

### ✅ 作用：

将当前分支的基底变基到另一个分支的最新提交之上。

### 🧠 场景：

用于生成更“线性”的提交历史，常用于代码提交前的整理。

### 🛠️ 使用示例：

```bash
# 将当前分支变基到 main 分支之上
git checkout feature
git rebase main
```

### 🔍 特点：

* 提交历史更清晰、线性
* 有修改历史的风险，不建议对共享分支使用

---

## 🧩 3. `git squash`（结合 `rebase` 使用）

### ✅ 作用：

将多个提交压缩成一个提交，常用于合并开发过程中的零碎提交。

### 🧠 场景：

在合并 PR 或准备提交前整理 commit 历史。

### 🛠️ 使用示例：

```bash
# 交互式变基
git rebase -i HEAD~3
```

在编辑界面中，将要压缩的 commit 前的 `pick` 改为 `squash` 或 `s`：

```
pick 1234567 初始提交
squash 89abcde 添加功能A
squash 456def0 修复bug
```

### 🔍 特点：

* 代码更整洁
* 可自定义提交信息
* 改写历史，请小心使用

---

## 📦 4. `git stash`

### ✅ 作用：

临时保存当前工作区的更改，切换分支后可恢复。

### 🧠 场景：

需要切换分支但当前更改未完成、不希望提交。

### 🛠️ 使用示例：

```bash
# 保存当前更改
git stash

# 查看 stash 列表
git stash list

# 恢复最近的 stash
git stash apply

# 删除最近的 stash
git stash drop

# 保存并自定义描述
git stash save "WIP: 修改登录页面"
```

### 🔍 特点：

* 保存工作区未提交内容
* 不污染分支历史
* 可多次 stash 并逐一管理

---

## 🧭 总结对比表

| 功能       | 作用           | 是否改写历史 | 场景           |
| -------- | ------------ | ------ | ------------ |
| `merge`  | 合并两个分支       | 否      | 保留完整历史       |
| `rebase` | 将提交重新应用到新的基底 | 是      | 清晰线性历史       |
| `squash` | 多个提交压缩为一个    | 是      | 精简 commit 历史 |
| `stash`  | 临时保存未提交的更改   | 否      | 切换分支、临时保存工作  |

git branch -d <feature>
git branch --all

