def calculate_market_cap(price_per_share, total_shares):
    """Calculate market capitalization given price per share and total shares."""
    try:
        price = float(price_per_share)
        shares = int(total_shares)
        if price < 0 or shares < 0:
            raise ValueError("Price per share and total shares must be non-negative.")
        return price * shares
    except (ValueError, TypeError) as e:
        print(f"Error calculating market cap: {e}")
        return None

if __name__ == "__main__":
    # Market Cap = Price per Share * Total Number of Shares
    price_per_share = 56.7  # Example price per share
    total_shares = 1000000  # Example total number of shares

    market_cap = calculate_market_cap(price_per_share, total_shares)
    print(f"Market Capitalization: ${market_cap}")

    
