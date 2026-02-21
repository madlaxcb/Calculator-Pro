# Calculator-Pro（Windows 独立程序）

你要求的是 **Windows 独立可执行程序**，不是网页版本。当前仓库为桌面应用实现：

- 标准计算器
- 科学计算器
- 程序员计算器（多进制 + 位运算）
- 单位换算
- 货币换算（实时汇率，失败时回退本地汇率）

## 本地运行（开发环境）

```bash
# basic command-line usage (arguments are operation and two numbers):
# add, sub, mul, div, pow
python app.py add 2 3
python app.py div 5 2
```

## 在 GitHub 上自动打包 Windows EXE（推荐）

仓库已提供 GitHub Actions 工作流：`.github/workflows/build-windows-exe.yml`。

### 使用方法

1. 把代码推送到 GitHub 仓库。
2. 打开仓库 `Actions` 页面。
3. 选择 **Build Windows EXE** 工作流并点击 **Run workflow**（也可在 PR / push 时自动触发）。
4. 构建完成后，在本次工作流的 **Artifacts** 下载：
   - `CalculatorPro-windows-exe`
   - 其中包含 `CalculatorPro.exe`

## 在 Windows 本地手动打包（备选）

```powershell
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed --name CalculatorPro app.py
```

生成文件：

- `dist\\CalculatorPro.exe`
