# Gemini

Gemini — 輕量的 Python CLI 與可重用 GitHub Action（已中文化，並附簡易桌面 GUI）。

快速說明
- CLI: 支援類似 slash 的指令（例如 `/gemini summary`）。
- GUI: 提供簡單的 tkinter 視窗，可用於本地互動式操作。
- Action: 已封裝為可重用的 GitHub Action（Docker runner），可在 workflow 中直接使用。

可用指令（CLI）

- `/init`：初始化（範例 stub，會顯示狀態）。
- `/gemini`：顯示基本狀態。
- `/gemini summary`：列印 repository 摘要。
- `/gemini help`：顯示說明文字。

執行方式

1) 命令列模式（中文化輸出）：

```bash
python gemini.py /gemini help
```

2) 啟動 GUI（本機）：

```bash
python gemini.py --gui
# 或
python gemini.py -g
```

GUI 會顯示一個簡單視窗，可輸入指令（例如 `/gemini summary`），並在視窗中顯示輸出。

在 CI 中使用（作為 GitHub Action）

此專案包含可重用的 Action，示例 workflow：

```yaml
jobs:
	run-gemini:
		runs-on: ubuntu-latest
		steps:
			- uses: actions/checkout@v4
			- name: Run Gemini Action
				uses: m2106337/Gemini/.github/actions/gemini@v1.0.0
				with:
					command: '/gemini summary'
```

或在同一 repo 內引用本地 action：

```yaml
uses: ./.github/actions/gemini
with:
	command: '/gemini help'
```

Marketplace 與發佈說明

本 repo 已包含 `action.yml`、`LICENSE` 與 release 資源，可用於發佈到 GitHub Marketplace。發佈步驟（摘要）：

1. 建立 release tag（例如 `v1.0.0`）並推送。
2. 在 GitHub 上建立 Release（或使用 `gh` CLI 建立 draft）。
3. 在 Release 中上傳截圖（建議尺寸可參考 Marketplace 文件），並填寫中英文說明。
4. 在 repository 的 Marketplace 發佈流程中提交上架申請（需填寫類別與 Metadata）。

我們已在 release draft 中上傳占位截圖，並填寫初步發佈說明；如需替換為實際截圖，請將圖片提供到 `.github/release-assets/`，我可以幫你上傳到 Release。

如何貢獻與測試

- 本地測試（使用 pytest）：

```bash
python -m pytest -q
```

- 專案結構與相關檔案：
	- [README.md](README.md)
	- [gemini.py](gemini.py)
	- [tests/test_gemini.py](tests/test_gemini.py)
	- [.github/actions/gemini](.github/actions/gemini)
	- [.github/workflows/ci.yml](.github/workflows/ci.yml)

需要我替你：
- 把實際截圖上傳到 release（你提供圖片）
- 將 Release draft 正式發佈到 GitHub（publish）
- 增加更完整的 Marketplace metadata（圖示、分類、範例）

歡迎告訴我你想先做哪一項，我會接著幫你執行。
