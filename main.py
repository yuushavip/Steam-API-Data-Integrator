from services import task

def main():
    all_steam_data = task.fetch_all_steam_data_and_save_to_csv()
            
if __name__ == "__main__":
    main()