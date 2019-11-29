###  GIT Commit 规范

[规范配置校验参考地址](https://blog.csdn.net/zhaileilei1/article/details/83186047)

#### Message 格式

```
<type>(<scope>): <subject>
// 空一行
<body>
// 空一行
<footer>
```

#### Header

###### Header部分应只包含一行，包括三个字段：type、scope和subject

* type type用于说明Commit的类型，包含一下7种类型
```
feat：新功能（feature）
fix：修补bug
docs：文档（documentation）
style： 格式（不影响代码运行的变动）
refactor：重构（即不是新增功能，也不是修改bug的代码变动）
test：增加测试
chore：构建过程或辅助工具的变动
```


| type | desc | desc |
| --- | --- | --- |
| feat | A new feature | 新功能 |
| docs | Documentation only changes | 文档修改 |
| style | Changes that do not affect the meaning of the code (white-space, formatting, missing semicolons, etc) | 格式（不影响代码运行的变动） |
| refactor | A code change that neither fixes a bug nor adds a feature | 重构 |
| perf | A code change that improves performance | 提高性能 |
| test | Adding missing tests or correcting existing tests | 添加缺失测试或更正现有测试 |
| build | Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm) | 依赖的外部资源变化 |
| chore | Other changes that don't modify src or test files | 构建过程或辅助工具的变动 |
| revert | Reverts a previous commit | 恢复先前的提交 |

* scope
```
scope用于说明本次Commit所影响的范围，比如controller、user或者README，视项目的不同而不同
```
* subject是本次Commit目的的简短描述，一般不要超过50个字符
```
以动词开头，使用第一人称现在时，比如change，而不是changed或changes
第一个字母小写
结尾不加句号（.）
```
#### Body
```
    Body是对本地提交的一个详细描述，下面是一个示例
```
#### Footer 
```
    Footer只用于两种情况

    不兼容改动
    如果当前代码与上一个版本不兼容，则 Footer 部分以BREAKING CHANGE开头，后面是对变动的描述、以及变动理由和迁移方法。
    
    关闭Issue
    如果当前Commit是针对某个Issue的提交，那么久可以在Footer中关闭这个Issue：Closes #234