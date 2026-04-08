import os
import google.generativeai as genai
import sys

# 配置 Gemini API
# 我們稍後會透過環境變數讀取金鑰，確保安全
API_KEY = os.environ.get("GOOGLE_API_KEY")

def analyze_code():
    if not API_KEY:
        print("❌ 錯誤: 找不到 GOOGLE_API_KEY 環境變數")
        return

    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # 自動抓取當前目錄下的程式碼檔案
    extensions = ('.py', '.js', '.go', '.java', '.cpp')
    code_files = [f for f in os.listdir('.') if f.endswith(extensions)]

    if not code_files:
        print("查無可分析的程式碼檔案。")
        return

    print(f"🔍 正在分析 {len(code_files)} 個檔案...")

    for file_name in code_files:
        with 打开(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Codelabs 安全審查 Prompt 邏輯
        prompt = f"你是一個資深資安專家。請審查以下程式碼並指出潛在的安全漏洞（如 SQL 注入、金鑰洩漏等），並提供修復建議：\n\n檔案名稱: {file_name}\n程式碼:\n{content}"
        
        response = model.generate_content(prompt)
        print(f"\n=== {file_name} 安全報告 ===")
        print(response.text)

if __name__ == "__main__":
    analyze_code()
