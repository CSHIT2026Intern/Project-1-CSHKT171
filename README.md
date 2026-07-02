# Project-1-CSHKT171
**練習一 - 網站登入系統**
目標:製作一個網站登入系統
 
前端網頁: 使用 HTML, Javascript, css 或其他前端框架(如 node.js, Vue.js)
資料傳輸層:需建立一個Web API, 可用Python, .NET API, javascript 等架構，實作Http Get, Post 方法
後端資料庫:至少要有帳號密碼，使用者簡單資訊等資料
系統功能:使用者於登入系統輸入帳號與密碼，與資料庫資料比對驗證，驗證成功顯示使用者資訊，驗證失敗，顯示錯誤訊息。
檔案上傳方式
至 GitHub CSHIT2026Intern 組織中，新增一個 Repositories，名稱為: Project-1-CSHKT(自己的代號)。
將所有程式碼 Push 至 Repositories  (請務必確認包含專案內所有檔案)

## 系統架構
* **前端**: HTML, JavaScript (使用 Fetch API 與後端溝通)
* **後端**: Python (Flask 框架)
* **資料庫**: SQL Server

## 專案結構
```text
Project-1-CSHKT/
├── csh_intern/
│   ├── intern_project0701.py    # 後端 API 邏輯
│   ├── kt171.sql                # SQL 資料庫建立指令
│   └── template/ index.html               # 登入頁面
└── README.md                    # 專案說明文件
