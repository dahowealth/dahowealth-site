import yfinance as yf

tickers = [
    "USDXOF=X",
    "USDXAF=X",
    "USDNGN=X",
    "USDGHS=X",
    "USDKES=X",
    "USDZAR=X"
]

for t in tickers:

    try:
        ticker = yf.Ticker(t)

        rate = ticker.fast_info["last_price"]

        print(f"{t}: {rate}")

    except Exception as e:

        print(f"{t}: FAILED")
        print(e)

ticker = "USDXOF=X"

df = yf.download(
    ticker,
    period="1y",
    interval="1d",
    progress=False
)

print(df.head())
print("\n")
print(df.tail())
print("\n")
print(df.columns)
print("\nRows:", len(df))

ticker = "USDXOF=X"

df = yf.download(
    ticker,
    period="1y",
    interval="1d",
    progress=False
)

print(df.reset_index().to_dict("records")[:5])
print(df.columns)
print(df.tail())
