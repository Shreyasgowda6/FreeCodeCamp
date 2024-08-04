from demographic_data_analyzer import analyze_demographic_data

if __name__ == '__main__':
    results = analyze_demographic_data()
    print("Demographic Analysis Results:")
    for key, value in results.items():
        print(f"{key}: {value}")

