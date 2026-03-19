# sharetask-website

这是一个用于把 `sharetask` 静态站点部署到 **GitHub Pages** 的仓库模板。

## 自动部署

仓库内已包含 GitHub Actions 工作流：`.github/workflows/pages.yml`  
每次你向 `main` 分支 `push` 时，Actions 会把仓库内容部署到 GitHub Pages。

## 后续接入你的站点

当你拿到真正的 `sharetask` 静态站点文件后，把它们放到仓库根目录（包括 `index.html` 及相关资源文件）。然后重新 `push`，就会自动更新线上页面。

