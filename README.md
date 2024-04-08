# Steam API 資料整合

**Steam 官方說明文件:**
[https://partner.steamgames.com/doc/api](https://partner.steamgames.com/doc/api)

使用 python 編寫，透過 Steam 官方提供的 Web API 抓取資料，並轉成 csv 檔案保存至 `/data` 資料夾，執行的操作設定都可以從 `/config` 資料夾透過 `config.yaml` 決定，`config`、`data` 資料夾路徑可以設定環境變數，預設是根據專案根目錄的相對路徑。

### config.yaml

執行時會抓取 `settings` 中的 `target_appids` 該列表包含的 steam appid。而其他的設定項目會對應 `/models` 的模組，`columns` 表示要保存的資料欄位，`params` 則是連線請求的參數 (值為空的情況則不會使用)。

---

# Steam API Data Integration

**Official Steam Documentation:**
[https://partner.steamgames.com/doc/api](https://partner.steamgames.com/doc/api)

This project is written in Python and utilizes the official Steam Web API to fetch data, which is then saved as CSV files in the `/data` folder. Execution settings can be adjusted in the `/config` folder through `config.yaml`. Both the `config` and `data` directory paths can be set via environment variables, with default relative paths based on the project's root directory.

### config.yaml

During execution, the `settings` section's `target_appids` list is used to fetch data for the specified Steam app IDs. Other configuration settings correspond to the modules in the `/models` directory, where `columns` define the data fields to be saved, and `params` specify the request parameters for the API calls (parameters with empty values will not be used).
