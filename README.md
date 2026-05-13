# 🔐 Windows Security Log Dashboard

A security monitoring dashboard for analyzing Windows Event Logs.

This project analyzes Windows Security Event Logs and visualizes:

- Successful logon events (Event ID 4624)
- Failed logon events (Event ID 4625)
- Logon type distribution
- Time-series event analysis
- Basic anomaly detection

The dashboard is built with Streamlit and allows users to upload Windows Event Log CSV files for analysis.

---

# 📌 Features

- Upload Windows Event Log CSV files
- Analyze successful and failed logon events
- Event count aggregation
- Time-series visualization
- Logon type analysis
- Failed login detection (4625)
- Interactive dashboard with Streamlit

---

# 🛠 Tech Stack

- Python
- pandas
- matplotlib
- Streamlit
- Windows Event Viewer

---

# 📂 Project Structure

```txt
windows-security-log-dashboard/
├── app.py
├── requirements.txt
├── README.md
├── sample_data/
│   ├── login_success.csv
│   └── login_failed.csv
└── images/
    └── dashboard.png
```

---

# 🚀 How to Run

## 1. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Launch Streamlit

```bash
streamlit run app.py
```

---

# 📊 Analyzed Event IDs

| Event ID | Description |
|---|---|
| 4624 | Successful Logon |
| 4625 | Failed Logon |

---

# 🔎 Logon Type Analysis

This project extracts and analyzes Windows logon types from Security Event Logs.

Example logon types:

| Type | Meaning |
|---|---|
| 2 | Interactive Logon |
| 5 | Service Logon |
| 7 | Unlock |
| 10 | Remote Desktop |
| 11 | Cached Logon |

---

# 🚨 Failed Login Detection

For testing purposes, failed authentication events were intentionally generated to verify Event ID 4625 detection.

The dashboard visualizes failed logon events and demonstrates a basic anomaly detection workflow.

---

# 📈 Example Dashboard

## Login Event Analysis

- Visualize event counts over time
- Display logon type distribution
- Detect failed login events

---

# 💡 Background

Security operations and SOC environments require:

- Log monitoring
- Event analysis
- Anomaly detection
- Visualization

This project demonstrates a basic Windows Security Log monitoring workflow using Python and Streamlit.

---

# 🔮 Future Improvements

- Night-time access detection
- IP address analysis
- Remote login detection
- Real-time monitoring
- SIEM integration
- Alert notification system

---

# 📷 Screenshot

(Add dashboard screenshot here)

---

# 👤 Author

Marina

ーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーーー

# 🔐 Windows Security Log Dashboard

Windowsイベントログを分析し、  
ログオン成功・失敗イベントを可視化する  
セキュリティ監視ダッシュボードです。

本プロジェクトでは、Windows Security Event Log を対象に、

- ログオン成功イベント（Event ID 4624）
- ログオン失敗イベント（Event ID 4625）
- ログオンタイプ分析
- 時系列分析
- 異常ログ検知

を実施しました。

Streamlit を用いてダッシュボード化し、  
CSVアップロードによるログ分析を可能にしています。

---

# 📌 Features

- WindowsイベントログCSVのアップロード
- ログオン成功/失敗イベント分析
- イベント件数の集計
- 時系列グラフ表示
- ログオンタイプ分析
- 異常ログ検知（4625）
- Streamlitによる可視化

---

# 🛠 Tech Stack

- Python
- pandas
- matplotlib
- Streamlit
- Windows Event Viewer

---

# 📂 Project Structure

```txt
windows-security-log-dashboard/
├── app.py
├── requirements.txt
├── README.md
├── sample_data/
│   ├── login_success.csv
│   └── login_failed.csv
└── images/
    └── dashboard.png
```

---

# 🚀 How to Run

## 1. Install Libraries

```bash
pip install -r requirements.txt
```

---

## 2. Run Streamlit

```bash
streamlit run app.py
```

---

# 📊 Analyzed Event IDs

| Event ID | Description |
|---|---|
| 4624 | Successful Logon |
| 4625 | Failed Logon |

---

# 🔎 Logon Type Analysis

本プロジェクトでは、  
Windows Security Log 内の「ログオン タイプ」を抽出し、  
ログオン種別の分布分析を実施しました。

代表的なログオンタイプ：

| Type | Meaning |
|---|---|
| 2 | Interactive Logon |
| 5 | Service Logon |
| 7 | Unlock |
| 10 | Remote Desktop |
| 11 | Cached Logon |

---

# 🚨 Failed Login Detection

テスト用に意図的な認証失敗を発生させ、  
Event ID 4625 を検知する検証を実施しました。

ログオン失敗イベントを可視化し、  
異常ログ検知の基本的な仕組みを確認しました。

---

# 📈 Example Dashboard

## Login Event Analysis

- 時間ごとのイベント件数を可視化
- ログオンタイプ分布を表示
- 異常イベントを検知

---

# 💡 Background

セキュリティ運用・SOC業務では、

- ログ監視
- 異常検知
- イベント分析
- 可視化

が重要となります。

本プロジェクトでは、  
Windowsイベントログを活用し、  
基本的なログ分析および監視ダッシュボードを実装しました。

---

# 🔮 Future Improvements

- 深夜アクセス検知
- IPアドレス分析
- リモートログイン検知
- リアルタイム監視
- SIEM連携
- アラート通知機能

---

# 📷 Screenshot

（ここに dashboard.png を貼り付け）

---

# 👤 Author

Marina
