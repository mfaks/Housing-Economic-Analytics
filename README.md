<div align="center">
  
# 🏡 Housing-Economic-Analytics 📊

## ✨ Exploring Housing, Demographics, and Economics Trends Over Time ✨

</div>

## 🔗 Project Link  

[View Project Here](https://housing-economic-analytics.vercel.app)  


## Introduction 🚀
Housing-Economic-Analytics is a data-driven platform for exploring housing affordability and socioeconomic dynamics across the United States. By combining housing market data with economic and demographic indicators, the project enables analysis of regional affordability, market trends, and economic shifts. Designed as a full-stack data engineering pipeline, it ingests raw data from multiple APIs, transforms it into clean analytical datasets, and powers interactive dashboards for insights.

## Features ✨
- **Real-Time Data Ingestion**: Automated pipelines pulling housing and economic data from APIs like Zillow, U.S. Census, and Federal Reserve FRED
- **Clean Data Layers**: Bronze → Silver → Gold transformations for consistent and reliable analysis
- **Analytics Dashboards**: Interactive visualizations built with Looker Studio to explore affordability, demographics, and economic factors
- **Scalable Infrastructure**: Modular setup with Terraform and CI/CD on GitHub Actions for reproducible deployments
- **Cloud-Native Warehouse**: Centralized storage and querying with BigQuery datasets (raw, staging, analytics)
- **Extensible Design**: Easy integration of new indicators, APIs, or visualization tools

## Tech Stack 🛠️

### Data Engineering
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=database&logoColor=white)
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![US Census](https://img.shields.io/badge/US_Census-003366?style=for-the-badge&logo=us-census&logoColor=white)
![FRED](https://img.shields.io/badge/FRED-2E6DB4?style=for-the-badge&logo=federal-reserve&logoColor=white)

### Infrastructure
![Google Cloud](https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-669DF6?style=for-the-badge&logo=google-bigquery&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=for-the-badge&logo=terraform&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions&logoColor=white)

### Frontend
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![ShadCN](https://img.shields.io/badge/ShadCN_UI-000000?style=for-the-badge&logo=shadcnui&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)

## Architecture Overview 🏗️

Housing-Economic-Analytics follows a medallion data architecture with modular components:

- **Data Ingestion**: Cloud Functions extract data from the Census and FRED APIs and land it in GCP Storage
- **Data Warehousing**: Raw data is ingested into BigQuery (`raw` datasets)
- **Transformations**: dbt models transform raw → staging → analytics (Bronze → Silver → Gold)
- **Visualization**: Looker Studio dashboards visualize affordability, demographic trends, and economic indicators
- **Frontend**: React + Vite app embeds dashboards and provides a polished UI

## Contributing 🤝

To contribute:

1. Fork the repository  
2. Create a feature branch: `git checkout -b feature/your-feature-name`  
3. Commit changes: `git commit -m 'Add feature XYZ'`  
4. Push to your fork: `git push origin feature/your-feature-name`  
5. Open a pull request  

## What's Next? 🚀

- **Enhanced Dashboards**: More granular metrics like price-to-income ratio and rent affordability  
- **Expanded Data Sources**: Integration of World Bank or regional planning data  
- **Predictive Analytics**: ML models for housing market forecasting and affordability scoring  
- **User Accounts**: Save custom dashboard views and filters  
- **API Access**: Expose curated datasets for external analysis  

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact 📧

For questions or support, please reach out to the project maintainer:
- Muhammad Faks - [muhammad.faks@gmail.com](mailto:muhammad.faks@gmail.com)
