
------------------------------------------------------------------------------------
1. SCIENTIFIC POSTER
------------------------------------------------------------------------------------
- **CTDP_Assignment_StudentID_6962175.pdf**  
  A self-contained A3 poster

------------------------------------------------------------------------------------
2. PYTHON CODE
------------------------------------------------------------------------------------

**Assignment Part I:**
- **Payoff structure.ipynb**  
  Illustrates the express certificate’s payoff profile, step-down thresholds and early redemption logic.

**Assignment Part II:**

1. **Svensson Method**  
   - **params_clean.ipynb**  
     Cleans and merges raw Bundesbank CSVs (beta0–3, tau1–2) into a single dataset.  
   - **Svenssons_method.ipynb**  
     Fits the Svensson yield curve and computes the 6-year spot rate.  
   - **beta0.csv**, **beta1.csv**, **beta2.csv**, **beta3.csv**, **tau1.csv**, **tau2.csv**  
     Raw Svensson parameter exports from Bundesbank.  
   - **svensson_parameters_cleaned.xlsx**  
     Final cleaned and combined Svensson parameters used for rate calculations.

2. **Task V – Valuation**  
   - **TaskV_01. Valuation_fixed_volat.ipynb**  
     Values the certificate using a fixed historical volatility.  
   - **TaskV_02. Valuation_rolling_volat.ipynb**  
     Values the certificate with a rolling (252-day) volatility window.  
   - **TaskV_03. Valuation_both.ipynb**  
     Compares fixed vs. rolling volatility valuation results side by side.  
   - **TaskV_Volatility.ipynb**  
     Computes and visualizes historical volatility estimates for Siemens Stock data
   - **module.py**  
     Shared functions 
   - **certificate_price_data.csv**  
     Daily market prices for ISIN DE000DK1BKQ3 over the last year.  
   - **fixed_volatility_simulations.csv**  
     Simulated certificate prices under fixed volatility assumptions.  
   - **rolling_volatility_simulations.csv**  
     Simulated certificate prices under rolling volatility assumptions.  
   - **siemens_stock_data.csv**  
     Historical Siemens AG closing prices used in simulations.  


 - **VI. Sensitivity Analysis.ipynb**  
     Calculates and plots the Greeks (Delta, Vega, Theta) across price/time scenarios.  
 - **VII. Replication.ipynb**  
     Builds the daily replicating portfolio and analyzes the equity fraction.

**Assignment Part III:**
- **Task VIII.ipynb**  
  Monte-Carlo simulation of unhedged S&P 500 investment returns and risk metrics.  
- **Task IX.ipynb**  
  Performance analysis of portfolios hedged with put options at various strikes and weights.  
- **Task X.ipynb**  
  Stress scenario analysis


 	

